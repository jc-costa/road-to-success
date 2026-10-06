<!-- Arquivo gerado por scripts/gerar.py — edite scripts/plano/templates/D-fluxo-ai-native.md. -->

# D) Fluxo de trabalho AI-native

A vaga não quer alguém que "escreve prompts". Quer alguém que **planeja, delega, revisa e verifica de forma independente**
o trabalho de agentes, com regras, guardrails e testes versionados no repositório. O plano treina isso em três camadas:
o harness do repositório (montado nas semanas 1-7 e auditado na 23), o uso diário durante os blocos de projeto e um
**lab AI-native semanal** (sexta, 1 h) com um exercício específico. Total de labs: 24.

Ferramentas: [Claude Code](https://code.claude.com/docs/en/memory) como agente principal e
[Codex](https://developers.openai.com/codex/guides/agents-md) para tarefas paralelas/em segundo plano e para comparação.
Curso de base: [Claude Code in Action](https://anthropic.skilljar.com/claude-code-in-action) (semana 2).

## 1. Regras no nível do repositório

- **`AGENTS.md` é a fonte única** das convenções (lido pelo Codex e por outras ferramentas que seguem o formato
  [agents.md](https://agents.md/)).
- **`CLAUDE.md`** carrega o `AGENTS.md` e acrescenta só o que é específico do Claude Code (a doc de
  [memória](https://code.claude.com/docs/en/memory) explica como importar outros arquivos).
- Regra de manutenção: **toda vez que você pegar o mesmo erro do agente duas vezes, vira uma linha nas regras**, com a
  data e o link do PR. Isso gera o histórico que alimenta a resposta Q7 da candidatura.

Esqueleto de `AGENTS.md` (adapte ao projeto):

```markdown
# LeaveFlow — instruções para agentes

## Contexto
Sistema de casos de afastamento médico com DADOS FICTÍCIOS. Serviços em services/, eventos em schemas/events/.

## Comandos
- make test        # unit + integração (Testcontainers)
- make lint        # gofmt/go vet, ruff/mypy, eslint
- make arch        # testes de arquitetura (go-arch-lint / import-linter)
- make evals       # só form-filler: falha se a métrica cair

## Regras de arquitetura
- domain/ não importa adapters/ nem infra/. Casos de uso ficam em app/.
- Toda escrita externa usa chave de idempotência; todo consumidor deduplica por event_id.
- Migrações de banco: expand/contract; nunca DROP/RENAME na mesma release que a mudança de código.

## Nunca
- Logar payload de caso, nome, e-mail, diagnóstico ou qualquer dado pessoal: logue case_id.
- Editar infra/, .github/, migrações antigas ou arquivos .env.
- Usar dados reais. Desligar, pular ou apagar testes para "passar".

## Pronto significa
- make lint test arch verdes; docs/ADR atualizados se mudou arquitetura;
- PR pequeno (< ~300 linhas) com descrição: problema, mudança, como testar, riscos.
```

## 2. Guardrails

| Guardrail | Como | Semana |
|---|---|---|
| Permissões | `.claude/settings.json` com `deny` para segredos e infra e `allow` só para comandos seguros ([doc](https://code.claude.com/docs/en/permissions)) | 1, 5, 20 |
| Hooks | `PreToolUse` bloqueia edição de caminhos protegidos; `Stop` roda lint/testes antes de o agente encerrar ([doc](https://code.claude.com/docs/en/hooks)) | 2, 5 |
| Testes de arquitetura | go-arch-lint (Go), import-linter (Python), dependency-cruiser (TS) no CI | 7 |
| Evals como gate | Mudança de prompt/schema do Form Filler só entra se a métrica não cair | 16 |
| CI obrigatório + branch protection | Nada entra sem CI verde; agentes abrem PR, não fazem push na main | 5 |
| Guardrails de dados sensíveis | Deny de leitura de dumps/datasets reais, checagem de PHI em logs no CI | 20 |

Exemplo de configuração (confira os nomes exatos na documentação antes de usar):

```json
{
  "permissions": {
    "allow": ["Bash(make test)", "Bash(make lint)", "Bash(make arch)"],
    "deny": ["Read(./.env)", "Read(./.env.*)", "Edit(infra/**)", "Edit(services/*/migrations/**)"]
  },
  "hooks": {
    "PreToolUse": [
      { "matcher": "Edit|Write", "hooks": [{ "type": "command", "command": "python3 .claude/hooks/protect_paths.py" }] }
    ],
    "Stop": [
      { "hooks": [{ "type": "command", "command": "make lint test arch" }] }
    ]
  }
}
```

Sobre o hook `Stop`: o `make` sai com código 2 quando algo falha, e código 2 num hook `Stop` impede o agente de encerrar
(a saída de erro volta para ele corrigir). É o comportamento desejado, mas pode virar laço: leia na doc de hooks como
detectar que o hook já está ativo e limite as tentativas.

```python
# .claude/hooks/protect_paths.py — bloqueia edições em caminhos protegidos (exit 2 = bloquear e explicar ao agente)
import json, re, sys
data = json.load(sys.stdin)
path = data.get("tool_input", {}).get("file_path", "")
if re.search(r"(^|/)(infra|\.github)/|/migrations/|\.env", path):
    print(f"Caminho protegido: {path}. Peça aprovação humana e abra um ADR.", file=sys.stderr)
    sys.exit(2)
```

Teste de arquitetura em Go sem ferramenta extra (alternativa ao go-arch-lint):

```bash
# falha se algum pacote de domain depender (direta ou indiretamente) de adapters/infra
bad=$(go list -f '{{.ImportPath}}: {{join .Deps " "}}' ./internal/domain/... | grep -E 'internal/(adapters|infra)')
[ -z "$bad" ] || { echo "violação de camadas: $bad"; exit 1; }
```

Import-linter (Python), em `.importlinter`:

```ini
[importlinter]
root_package = ops_sync

[importlinter:contract:camadas]
name = Camadas do ops-sync
type = layers
layers =
    ops_sync.entrypoints
    ops_sync.service
    ops_sync.domain
```

## 3. Fluxos multiagente

| Fluxo | Como funciona | Quando usar |
|---|---|---|
| Planner → implementer → reviewer | Você aprova o plano (plan mode ou `PLANS.md`); um agente implementa; um subagente revisor com checklist e ferramentas só de leitura revisa; você arbitra | Features de 1-3 dias |
| Testes adversariais independentes | Sessão B escreve testes a partir da **especificação**, sem ver a implementação da sessão A | Idempotência, concorrência, sagas |
| Tarefas paralelas | Worktrees do git ou tarefas em segundo plano do Codex, cada uma com escopo e critério de pronto próprios | Itens independentes (cliente TS, adapters, docs) |
| Executor de runbook | Subagente só com leitura + dry-run segue o runbook e relata; humano executa a ação | Recuperação e incidentes |
| Revisão em duas lentes | Dois revisores com focos diferentes (segurança × idempotência) | Pagamentos e dados sensíveis |

Subagentes ficam em `.claude/agents/*.md` ([doc](https://code.claude.com/docs/en/sub-agents)), por exemplo:

```markdown
---
name: idempotency-reviewer
description: Revisa diffs procurando retries não idempotentes, falta de dedupe por event_id e dados pessoais em logs. Use depois de mudanças em handlers, consumidores ou clientes de API.
tools: Read, Grep, Glob
---
Você revisa código do LeaveFlow. Para cada achado, cite arquivo:linha, o risco concreto e a correção mínima.
Classifique como BLOQUEANTE, SUGESTÃO ou NIT. Não proponha refatorações fora do escopo do diff.
```

## 4. Protocolo de verificação independente (todo PR de agente)

1. Havia plano escrito **antes** do código? O diff faz só o que o plano dizia?
2. Leia o diff inteiro. Diff grande demais para ler → peça para quebrar em PRs menores.
3. Rode você mesmo: `make lint test arch` (e `go test -race` onde houver concorrência).
4. Quebre um teste de propósito (mude uma asserção ou o código) e confira que ele falha: teste que não falha não protege.
5. Procure os erros típicos de agente no projeto: não-determinismo em workflow, retry de operação não idempotente,
   dado pessoal em log, migração destrutiva, tratamento de erro que engole exceção, mocks que testam o próprio mock.
6. Casos de borda que **você** escreve (nulos, fuso horário, duplicatas, ordem invertida).
7. Mudou arquitetura ou contrato? Exija ADR/atualização do schema de eventos.
8. Registre em `docs/agent-reviews.md`: data, tarefa, ferramenta, havia plano?, tempo, defeitos pegos por você,
   pegos pelos testes, que escaparam, regra criada.

## 5. Métricas que você vai mostrar na entrevista

- % de tarefas com plano prévio · defeitos por PR de agente (pegos por você × pelos testes × escapados para staging) ·
  regras criadas por erro recorrente · tempo de ciclo de PRs com e sem agentes (estimativa honesta).

## 6. Anti-padrões

Aceitar diff grande sem ler; pedir ao mesmo agente para revisar o próprio código como única verificação; deixar o agente
mexer em infra/segredos; tarefa sem critério de pronto; avaliar feature de LLM "no olho" em vez de evals; esconder que usou
agente. A vaga é explícita: o trabalho é seu, inclusive o que o agente escreveu.

## 7. Labs semanais

| Semana | Dia | Atividade concreta | Entregável |
|---|---|---|---|
| 1 | 6 (Sáb) | CLAUDE.md e AGENTS.md v0 (comandos, convenções, 'nunca faça', definição de pronto) + permissões básicas | CLAUDE.md/AGENTS.md v0 commitados |
| 2 | 5 (Sex) | Claude Code in Action (módulos iniciais) + hook que roda testes ao final de cada tarefa | Hook commitado + nota |
| 3 | 5 (Sex) | AI-native lab: agente implementa export CSV; revisar o diff linha a linha, rodar testes, achar ≥1 problema (PHI em log? paginação?) | Entrada em docs/agent-reviews.md |
| 4 | 5 (Sex) | AI-native lab: subagente 'revisor' com checklist de idempotência; comparar a revisão dele com a sua (falsos positivos/negativos) | docs/agent-reviews.md atualizado |
| 5 | 5 (Sex) | AI-native lab: hook que bloqueia edição de infra/segredos e exige lint+testes antes de concluir; provar que barra uma ação proibida | .claude/settings.json + hook commitados |
| 6 | 5 (Sex) | AI-native lab: Codex com AGENTS.md gera o cliente Python; comparar com Claude Code; manter uma fonte única de regras | Nota comparativa + regras unificadas |
| 7 | 5 (Sex) | AI-native lab: pedir ao agente uma feature que viola camadas; ver o teste de arquitetura pegar; registrar a regra no CLAUDE.md/AGENTS.md | Regra nova + entrada em agent-reviews |
| 8 | 5 (Sex) | AI-native lab multiagente: agente A implementa o consumidor, agente B (sessão separada) escreve testes adversariais sem ver a implementação; você arbitra | Relatório: bugs achados por B |
| 9 | 5 (Sex) | AI-native lab: agente escreve código de workflow; caçar não-determinismo (time.Now, rand, goroutines) com replay test; regra no CLAUDE.md | Regra + agent-reviews |
| 10 | 5 (Sex) | AI-native lab: plan mode para compensações; avaliar o plano antes do código e recusar 2 sugestões complexas demais, justificando | Plano anotado + agent-reviews |
| 11 | 5 (Sex) | AI-native lab: agente gera o comparador; você escreve casos de borda (nulos, timezones, status desconhecidos) e mede quantos o agente perdeu | agent-reviews |
| 12 | 5 (Sex) | AI-native lab: 2 agentes revisam o handler (segurança × idempotência); consolidar e aplicar só o que se justifica | agent-reviews |
| 13 | 5 (Sex) | AI-native lab: agente (Codex com PLANS.md) escreve o job a partir do seu plano; verificar com dados plantados e teste de propriedade | agent-reviews |
| 14 | 5 (Sex) | AI-native lab: agente propõe o mapeamento a partir do schema; validar campo a campo contra a spec e medir a taxa de erro do agente | agent-reviews |
| 15 | 5 (Sex) | AI-native lab: subagente 'runbook-executor' só com leitura + dry-run executa o runbook; você valida as conclusões | agent-reviews |
| 16 | 5 (Sex) | AI-native lab: agente altera prompt/schema; mudança só entra se o eval melhora (eval como guardrail no CI) | Gate de eval no CI |
| 17 | 5 (Sex) | AI-native lab: 'júnior + agente' geram um PR grande; exigir quebra em PRs pequenos, revisar e verificar de forma independente | agent-reviews |
| 18 | 5 (Sex) | AI-native lab: agente analisa logs/traces exportados e propõe causa raiz; confirmar ou refutar com evidência | agent-reviews |
| 19 | 5 (Sex) | AI-native lab: agente escreve modelos dbt; testes dbt + sua revisão de SQL (joins errados, grão) | agent-reviews |
| 20 | 5 (Sex) | AI-native lab: guardrails dos agentes para dados sensíveis (deny de paths/comandos, sem dados reais, sem segredos); testar violação | settings + teste de violação |
| 21 | 5 (Sex) | AI-native lab: agente implementa componente do funil; checar acessibilidade, eventos (debug do GTM) e testes | agent-reviews |
| 22 | 5 (Sex) | AI-native lab: fluxo multiagente completo numa feature pequena (planner → implementer → reviewer → você aprova); medir tempo e defeitos | agent-reviews com métricas |
| 23 | 5 (Sex) | AI-native lab: auditoria do próprio harness (CLAUDE.md/AGENTS.md, hooks, subagentes, testes de arquitetura) — o que mudou e por quê | docs/ai-harness-changelog.md |
| 24 | 5 (Sex) | AI-native lab final cronometrado: feature nova planejada, delegada a agentes, verificada e entregue em 1h | Relatório do exercício |
