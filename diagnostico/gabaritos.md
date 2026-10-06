# Gabaritos do diagnóstico

> **Spoiler.** Só leia depois de fazer o exercício e registrar o tempo. Os números do D04 foram conferidos no
> PostgreSQL 16 com o `d04-schema.sql` deste repositório (o gerador de números aleatórios muda entre versões).

## D04 — SQL/PostgreSQL

Valores esperados: **T1** closed 115.891 · opened 30.113 · paid 23.959 · scheduled 13.859 · cancelled 9.997 · documented 6.181.
**T2** 1.011 casos. **T4** 3.196 casos com cobrança duplicada, 3.196 cobranças extras, US$ 316.404,00 cobrados a mais.

```sql
SET search_path TO d04;

-- T1
SELECT status, count(*) FROM cases GROUP BY status ORDER BY count(*) DESC;

-- T2 (anti-join com NOT EXISTS; LEFT JOIN ... IS NULL também vale)
SELECT p.case_id, p.at AS paid_at
FROM case_events p
WHERE p.type = 'paid' AND p.at >= timestamptz '2026-06-24 00:00+00'
  AND NOT EXISTS (SELECT 1 FROM case_events s WHERE s.case_id = p.case_id AND s.type = 'scheduled')
ORDER BY p.at;

-- T3 (LAG sobre os eventos do caso)
WITH ev AS (
  SELECT case_id, type, at,
         LAG(type) OVER w AS prev_type, LAG(at) OVER w AS prev_at
  FROM case_events
  WHERE type IN ('opened', 'paid')
  WINDOW w AS (PARTITION BY case_id ORDER BY at)
)
SELECT date_trunc('month', prev_at) AS mes,
       avg(at - prev_at) AS media,
       percentile_cont(0.9) WITHIN GROUP (ORDER BY extract(epoch FROM at - prev_at)) / 3600 AS p90_horas
FROM ev
WHERE type = 'paid' AND prev_type = 'opened'
GROUP BY 1 ORDER BY 1;

-- T4
WITH p AS (
  SELECT *, LAG(created_at) OVER (PARTITION BY case_id, amount_cents ORDER BY created_at) AS prev_at
  FROM payments
)
SELECT case_id, count(*) + 1 AS pagamentos, sum(amount_cents) AS cobrado_a_mais_cents
FROM p
WHERE prev_at IS NOT NULL AND created_at - prev_at < interval '5 minutes'
GROUP BY case_id ORDER BY case_id;

-- T5 (RANK mantém empates: um mês pode ter 4 linhas se houver empate no 3º lugar;
--     ROW_NUMBER corta empates de forma arbitrária; DENSE_RANK pode trazer mais de 3 grupos)
WITH m AS (
  SELECT date_trunc('month', opened_at) AS mes, reason, count(*) AS n FROM cases GROUP BY 1, 2
), r AS (
  SELECT *, RANK() OVER (PARTITION BY mes ORDER BY n DESC) AS rk FROM m
)
SELECT mes, reason, n, rk FROM r WHERE rk <= 3 ORDER BY mes, rk;

-- T6
CREATE INDEX case_events_type_at_idx   ON case_events (type, at);       -- filtro "paid desde X" + ordenação
CREATE INDEX case_events_case_type_idx ON case_events (case_id, type);  -- sonda do anti-join
ANALYZE case_events;
-- Antes: seq scans paralelos + hash anti join (lê os ~740 mil eventos).
-- Depois: bitmap index scan em (type, at) para ~6,7 mil eventos 'paid' recentes e nested loop anti join
-- com index-only scan em (case_id, type). Alternativa válida: índice parcial (case_id) WHERE type = 'scheduled'.
-- Sem filtro de data, a consulta devolve ~12% da tabela: seq scan + hash join é mais barato que milhares
-- de buscas por índice, e o planner está certo em ignorar o índice.

-- BÔNUS: garantir "um caso, um horário" no banco e reservar sem disputa
CREATE UNIQUE INDEX slots_one_per_case ON slots (case_id) WHERE case_id IS NOT NULL;
BEGIN;
WITH s AS (
  SELECT id FROM slots
  WHERE clinician = 'clinician_3' AND case_id IS NULL
  ORDER BY starts_at
  LIMIT 1
  FOR UPDATE SKIP LOCKED          -- a 2ª sessão pula o horário travado e pega o próximo
)
UPDATE slots SET case_id = 42 FROM s WHERE slots.id = s.id
RETURNING slots.id, slots.starts_at;
COMMIT;
-- Alternativa: UPDATE ... WHERE id = :id AND case_id IS NULL e checar rowcount (concorrência otimista).
```

## D08 — cenários

| # | O que dá errado | Resposta esperada (padrão) |
|---|---|---|
| 1 | Efeito repetido 3× (ex.: cobrar, enviar e-mail) | Entrega *at-least-once*: dedupe por `event.id` (tabela inbox com UNIQUE) na mesma transação do efeito; responder 2xx rápido e processar assíncrono |
| 2 | Banco e fila divergem (caso existe, evento nunca sai) — *dual write* | **Transactional outbox** (evento gravado na mesma transação; relay publica com retry) ou CDC |
| 3 | Mensagem reentregue → e-mail duplo | Consumidor idempotente: registro do processamento + chave de idempotência no envio; ack só depois do efeito |
| 4 | Estado final errado (pago depois de estornado) | Não confiar na ordem: versão/timestamp do objeto, buscar o estado atual na fonte (API do provedor), máquina de estados que rejeita transição inválida; ordering key por entidade quando a ordem importa |
| 5 | Cliente cobrado e agendado sem documento | Saga: compensações em ordem inversa (cancelar consulta, estornar), idempotentes; ou *forward recovery* (retry/fila humana) se for o certo para o negócio; estado durável (Temporal) |
| 6 | Cobrança duplicada | Retry só com **idempotency key** (servidor guarda o resultado por chave); sem chave, não fazer retry de operação não idempotente; backoff com jitter |
| 7 | Edição manual de Ops perdida | **Propriedade por campo** (projeção nunca escreve campos de Ops), detecção de conflito por versão/`lastModifiedTime`, replay com dry-run/diff |
| 8 | Recomeçar do zero duplica ou demora; parar no meio deixa estado misto | **Checkpoint** persistido (cursor), escrita idempotente (upsert), lotes pequenos, reexecução segura e métricas de progresso |

Conte como correta a resposta que identifica o problema **e** propõe o mecanismo (nomear o padrão vale o nível avançado).

## D10 — incidente de cobrança duplicada

- **Causa raiz:** o handler processa a entrega *at-least-once* de forma não idempotente: não deduplica por `event.id`
  e chama `create_charge` sem chave de idempotência. Qualquer reentrega gera nova cobrança.
- **Fator contribuinte (nos logs):** `notify_ops` síncrono levou 12,4 s no pico (campanha às 14h); o provedor desiste
  em 10 s e reenvia o mesmo evento (`attempt: 2`). A 1ª resposta 200 chega depois do retry. 37 duplicatas no dia.
- **Teste de regressão (falha no código atual):** entregar o mesmo payload duas vezes e afirmar
  `len(provider.charges) == 1` e uma única linha em `charges`.
- **Correção mínima:** UNIQUE em `charges.provider_event_id` + checagem antes de efeitos;
  `create_charge(..., idempotency_key=f"followup:{event['id']}")`; tirar `notify_ops` do caminho síncrono (fila/outbox).
- **Ações sistêmicas:** padrão de inbox para todos os webhooks (documentado e coberto por teste de contrato); alerta de
  latência do endpoint perto do timeout do provedor; reconciliação diária que alerta duplicatas em minutos, não no fim do dia;
  revisão de todas as chamadas externas com efeito financeiro exigindo idempotency key.
- **5 porquês (exemplo):** cliente cobrado 2× → handler rodou 2× → provedor reenviou → resposta demorou >10 s →
  chamada síncrona a Ops dentro do handler e nenhum mecanismo de dedupe porque o padrão de webhook nunca foi definido.

## D11 — classificação

| Categoria | Campos |
|---|---|
| A — identificador direto | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 |
| B — quasi-identificador | 11, 12, 13, 14 |
| C — saúde sensível | 15, 16, 17, 18 |
| D — não sensível / operacional | 19, 20 |

Regras esperadas: A e C **nunca** em log; no BigQuery, A só pseudonimizado (hash com sal/token) ou removido, C só em
dataset restrito ou agregado/de-identificado; B generalizado (faixas, só estado) e fora de logs; D pode ir para logs e
analytics (o UUID aleatório é o que deve circular nos logs). Acesso pelo **mínimo necessário**: Ops vê contato e status;
clínicos veem dados de saúde; engenharia trabalha com dados fictícios e pseudônimos; todo acesso a A/C fica em trilha de
auditoria. Nuance avançada: o CEP de 5 dígitos sai pelo Safe Harbor (só os 3 primeiros dígitos podem ficar, e com condição
de população); o ano de nascimento pode ficar, mas idades acima de 89 são agregadas.

## D12 — referência de resposta

- **Mapa as-is:** pagamento → busca manual do intake → digitação de 14 campos → anexo → contato para agendar → registro
  duplo do horário → formulário médico → conferência de 8 campos → correção → assinatura → envio ao paciente.
- **Priorização típica (justifique a sua):** (1) casar pagamento ↔ intake automaticamente e criar o registro na fila
  (alto impacto: remove a digitação e os 5% parados >48 h; esforço médio; risco baixo se houver fila de exceções);
  (2) pré-preencher e validar o formulário contra o intake (ataca os 15% divergentes; esforço alto; risco médio: exige
  revisão humana); (3) sincronizar o horário do sistema clínico (impacto médio, esforço baixo).
- **Antes de automatizar:** acompanhar 5-10 casos reais com Ops, medir tempo por etapa (baseline), listar exceções
  (pagamento sem intake, intake duplicado, nome divergente), perguntar quais campos eles corrigem e por quê, e combinar
  como eles vão reportar quando a automação errar.

## D13 — os 6 problemas do PR

| # | Problema | Por que é bloqueante |
|---|---|---|
| 1 | Token do Airtable fixo no código (`AIRTABLE_TOKEN = "pat..."`) | Segredo no repositório; deve vir do Secret Manager/variável de ambiente e o token exposto deve ser revogado |
| 2 | `log.info("... %s", case)` registra o caso inteiro | Vaza PHI (nome, diagnóstico) para os logs; logar só `case_id` e metadados |
| 3 | Trocou PATCH com `performUpsert` por `POST` de criação + retry | Não idempotente: cada retry ou replay cria um registro duplicado na Single Queue |
| 4 | Sempre envia `ops_status` e `ops_notes` | Campos de Ops são sobrescritos a cada sync/replay: perde edições manuais |
| 5 | `while True` com `sleep(0.1)` para qualquer status ≠ 200 | Sem limite de tentativas, sem backoff/jitter, ignora 429 (esperar 30 s) e repete erros 4xx para sempre: laço quente que piora o rate limit |
| 6 | `except Exception: ... return` | Engole o erro: a mensagem é confirmada e o caso some sem DLQ nem alerta (e erros de rede, que mereciam retry, não têm nenhum) |

Extras que também contam a favor: perda do `client` injetado (testabilidade, reuso de conexão, timeout explícito), PR sem
testes e sem evidência do "testei local", descrição sem o problema raiz. Um bom elogio: o júnior notou um problema real
(casos que não aparecem na fila) e explicou a motivação no PR.

## D02, D03, D15, D16 — pontos de checagem rápidos

- **D02:** a chave precisa ser reservada de forma atômica (mutex/`sync.Map` + estado "em processamento") para o teste
  concorrente criar 1 caso só; guarde o hash do corpo para devolver 422 quando a mesma chave vier com corpo diferente.
- **D03:** `switch (status.kind)` com `const _exhaustive: never = status` no `default` prova exaustividade.
- **D15:** o sinal de nível avançado é encontrar o que o agente errou **sem** pedir para o próprio agente revisar.
- **D16:** atribuir a variante no middleware (cookie definido no servidor) evita *flicker* e garante estabilidade.
