# Diagnóstico (semana 1; semana 2 para refazer ou complementar)

Objetivo: medir o seu nível real em cada grupo de tópicos **antes** de distribuir as horas das semanas 3 a 24.
Ignore qualquer autoavaliação: o nível vem do exercício, com critério objetivo.

- Enunciados e critérios de nível: [`exercicios.md`](exercicios.md) (gerado a partir de `scripts/plano/diagnostico.py`).
- Onde registrar: [`planilhas/01-diagnostico.csv`](../planilhas/01-diagnostico.csv) ou a aba **Diagnóstico** do XLSX
  (colunas *Resultado* e *Nível*). Depois, copie o nível para a coluna *Nível no diagnóstico* da Matriz.
- Como ajustar o plano com o resultado: [`plano/00-visao-geral-e-ajuste.md`](../plano/00-visao-geral-e-ajuste.md#3-ajuste-pós-diagnóstico).
- Gabaritos: [`gabaritos.md`](gabaritos.md). **Só abra depois de terminar o exercício.**

## Regras para o diagnóstico valer

1. Cronometre. Se estourar o tempo, pare e registre até onde chegou (isso é informação, não fracasso).
2. Sem IA nos exercícios D01-D14 e D16. A IA é permitida (e obrigatória) só no D15, que mede justamente o uso de agentes.
3. Documentação oficial pode ser consultada; tutoriais passo a passo, não (exceto quando o critério diz o contrário).
4. Registre evidência: link do commit, print do teste, tempo gasto. Na dúvida entre dois níveis, marque o menor.

## Materiais

| Exercício | Material |
|---|---|
| D04 SQL/PostgreSQL | [`d04-schema.sql`](d04-schema.sql) — schema, 200 mil casos fictícios e as 6 tarefas no final do arquivo |
| D10 Confiabilidade | [`d10-incidente/`](d10-incidente/) — `handler.py`, `fake_provider.py`, `test_handler.py`, `logs-incidente.jsonl` (só biblioteca padrão; rode `python -m unittest -v` dentro da pasta) |
| D13 Liderança | [`d13-pr-junior.diff`](d13-pr-junior.diff) — PR simulado com 6 problemas plantados |
| D06 Dados | Dataset público `bigquery-public-data.ga4_obfuscated_sample_ecommerce` no [BigQuery sandbox](https://cloud.google.com/blog/products/data-analytics/query-without-a-credit-card-introducing-bigquery-sandbox) |
| D08, D11, D12 | Abaixo, nesta página |
| D07, D14 | Rubricas abaixo |

Para subir um Postgres local para o D04: `docker run --name pg -e POSTGRES_PASSWORD=dev -p 5432:5432 -d postgres:16`
e depois `psql -h localhost -U postgres -f diagnostico/d04-schema.sql`.

---

## D08 — 8 cenários de sistemas distribuídos (45 min)

Para cada cenário, responda em 2-4 linhas: o que dá errado e qual padrão/técnica resolve.

1. O provedor de pagamento entrega o mesmo webhook `payment.succeeded` três vezes em 10 minutos.
2. O serviço grava o caso no Postgres, faz commit e em seguida publica `CaseOpened` no Pub/Sub. O publish falha (rede) depois do commit.
3. O consumidor recebe a mensagem, envia o e-mail de boas-vindas e o processo cai antes do *ack*.
4. Os eventos `payment.succeeded` e `payment.refunded` do mesmo pagamento chegam ao seu sistema em ordem invertida.
5. Uma saga faz: cobrar → agendar consulta → gerar documento. O passo 3 falha de forma definitiva.
6. Um cliente HTTP genérico faz retry automático de `POST /charges` após timeout de 5 s.
7. Um replay de eventos para o Airtable sobrescreveu uma anotação que Ops tinha feito à mão no registro.
8. Um job de backfill de 100 mil casos caiu no registro 60 mil.

---

## D11 — Classificação de 20 campos (30 min)

Categorias: **A** identificador direto (inclui as categorias do Safe Harbor: nomes, datas ligadas à pessoa exceto o ano,
contatos, números de registro/conta, IP, fotos...); **B** quasi-identificador (não está na lista, mas identifica em combinação);
**C** informação de saúde sensível; **D** não sensível/operacional.
Para cada campo diga também: pode ir para log? Pode ir para o BigQuery (e de que forma)? Quem precisa acessar?

| # | Campo do intake |
|---|---|
| 1 | Nome completo |
| 2 | E-mail |
| 3 | Telefone |
| 4 | Endereço (rua e número) |
| 5 | CEP/ZIP completo (5 dígitos) |
| 6 | Data de nascimento |
| 7 | Número do Social Security (SSN) |
| 8 | Número da carteirinha do plano de saúde |
| 9 | Endereço IP de quem preencheu o formulário |
| 10 | Foto do documento de identidade |
| 11 | Ano de nascimento (só o ano) |
| 12 | Estado de residência |
| 13 | Nome do empregador |
| 14 | Cargo/função |
| 15 | Diagnóstico em texto livre escrito pelo médico |
| 16 | Código CID-10 do diagnóstico |
| 17 | Medicamentos em uso |
| 18 | Duração estimada do afastamento (dias) |
| 19 | ID interno do caso (UUID aleatório, não derivado de dados pessoais) |
| 20 | Status do caso (opened, paid, scheduled...) |

---

## D12 — Processo manual de Ops (45 min)

Narrativa (números fictícios):

> Toda manhã, uma pessoa de Ops abre a caixa de e-mail compartilhada e o painel do provedor de pagamentos. Para cada
> pagamento novo, procura o formulário de intake correspondente (às vezes chegou por e-mail, às vezes por telefone), copia
> 14 campos para uma linha do Airtable, anexa o PDF que o paciente enviou e marca "pronto para agendar". Depois, liga ou
> manda SMS para o paciente marcar a consulta, registra o horário no sistema clínico e copia o horário de volta para o
> Airtable. Após a consulta, o médico preenche o formulário do empregador; Ops baixa o PDF, confere 8 campos contra o
> intake (nome, datas, empregador), corrige à mão quando há divergência, envia para assinatura eletrônica e, quando
> assinado, manda para o paciente por e-mail. Cerca de 15% dos casos têm algum dado divergente; 5% esperam mais de 48 h
> porque o pagamento não foi casado com o intake. Ops gasta em média 35 min por caso e o volume é de 40 casos por dia.

Entregue: (1) mapa *as-is* em raias (Paciente, Ops, Médico, Sistemas); (2) três candidatos a automação priorizados por
impacto × esforço × risco, com a métrica que cada um move; (3) o que você observaria/perguntaria a Ops antes de automatizar.

---

## Rubrica do D07 (arquitetura) — 6 itens × 0-2 pontos

| Item | 0 | 1 | 2 |
|---|---|---|---|
| Bounded contexts | Ausentes ou por tabela/tela | Contextos plausíveis sem responsabilidades claras | Contextos com responsabilidades e linguagem próprias e relações entre eles |
| Consistência e transações | Ignora | Cita, mas usa transação distribuída/dual-write | Consistência local + eventos (outbox/saga) e onde a consistência eventual é aceitável |
| Idempotência | Ausente | Só em um ponto | Em webhooks, consumidores e chamadas externas (chaves e dedupe) |
| Falhas e retries | Ausente | Retries genéricos | Timeouts, backoff, DLQ, compensações, comportamento fail-safe por etapa |
| Observabilidade | Ausente | Logs | Logs estruturados + métricas de negócio + tracing + alertas |
| Simplicidade e trade-offs | Over-engineering ou nenhum trade-off | Alguns trade-offs | Começa simples, justifica cada peça e diz o que **não** faria agora |

Iniciante 0-5 · Intermediário 6-9 · Avançado 10-12.

## Rubrica do D14 (comunicação) — 6 itens × 0-2 pontos

| Item | 0 | 1 | 2 |
|---|---|---|---|
| Problema | Confuso ou ausente | Descrito sem impacto | Problema + impacto no negócio + quem é afetado |
| Alternativas | Nenhuma | Uma alternativa sem trade-off | 2+ alternativas com trade-offs e a escolha justificada |
| Plano | Vago | Etapas sem marcos | Marcos verificáveis, critério de pronto, rollout/rollback |
| Riscos | Ausentes | Listados | Listados com mitigação e sinal de alerta precoce |
| Concisão | >1 página / prolixo | Algumas redundâncias | 1 página, frases curtas, sem jargão desnecessário |
| Mensagem de atraso | Sem formato | Falta um dos três elementos | O que aconteceu + o que muda + novo prazo (e o que você precisa de quem lê) |

Iniciante 0-5 · Intermediário 6-9 · Avançado 10-12.

## Rubrica do D17 (inglês) — autoavaliação do vídeo (repetida todo sábado)

| Item (0-2) | 0 | 1 | 2 |
|---|---|---|---|
| Fluência | Pausas longas e frequentes | Algumas pausas, recupera | Fluxo natural; pausas só para ênfase |
| Pronúncia | Erros que impedem entender | Erros perceptíveis, compreensível | Clara; acento não atrapalha |
| Estrutura | Sem começo/meio/fim | Estrutura parcial | Contexto → ação → resultado, com transições |
| Vocabulário técnico | Impreciso ou traduzido do português | Correto, repetitivo | Preciso e variado |
| Tempo | Fora de 1:30-3:30 | Fora por até 30 s | Dentro do alvo |

Anote também, a partir da transcrição: palavras por minuto e muletas ("é...", "uh", "like") por minuto.
