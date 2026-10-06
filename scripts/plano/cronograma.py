"""Cronograma de 24 semanas × 6 dias: 4h técnicas + 1h de inglês por dia.

Bloco técnico: (trilha, tópicos, atividade, recursos, horas, modo, entregável)
  modo: E = estudo (leitura/vídeo), L = laboratório/exercício guiado, P = projeto (construção),
        W = escrita de artefato, R = revisão/verificação de trabalho de agente, F = reforço flex.
  Prática = L + P + W + R. O reforço flex (F) entra no denominador, mas não no numerador
  (conta como 0% prática), para o percentual ser conservador.
Os blocos de inglês são gerados a partir dos parâmetros semanais em INGLES (semana 1 é explícita).
"""


def b(trilha, topicos, atividade, recursos, horas, modo, entregavel):
    return {
        "trilha": trilha,
        "topicos": topicos.split(),
        "atividade": atividade,
        "recursos": [r for r in recursos.split(",") if r],
        "horas": horas,
        "modo": modo,
        "entregavel": entregavel,
    }


def flex(sugestao):
    return b("FLEX", "", f"Reforço flex (regras no item 0): {sugestao}", "", 1, "F",
             "Nota de 3 linhas: o que reforçou e evidência")


SEMANAS = []


def semana(n, fase, tema, objetivos, marco, pronto, lideranca, checkpoint, dias):
    assert len(dias) == 6, n
    SEMANAS.append(dict(n=n, fase=fase, tema=tema, objetivos=objetivos, marco=marco, pronto=pronto,
                        lideranca=lideranca, checkpoint=checkpoint, dias=dias))


F0 = "Fase 0: diagnóstico e fundação"
F1 = "Fase 1: fundamentos e primeiro serviço"
F2 = "Fase 2: event-driven, domínio e workflows"
F3 = "Fase 3: integrações, pagamentos, Ops e IA"
F4 = "Fase 4: confiabilidade, dados e compliance"
F5 = "Fase 5: growth, consolidação e candidatura"

# ---------------------------------------------------------------- Semana 1
semana(1, F0, "Diagnóstico I + setup do ambiente",
       "Medir o nível em todos os grupos; montar ambiente com controle de custo; primeira visão do domínio.",
       "Repositório 'leaveflow' criado (monorepo vazio com docs/), projeto GCP com alertas de orçamento.",
       "17 exercícios de diagnóstico feitos e registrados na aba Diagnóstico; plano ajustado v1 escrito.",
       "Revisão de PR (D13), design doc de 1 página (D14), plano ajustado v1.",
       False, [
           [b("T00", "LT05 LT06 VS06 CD01", "Setup: conta GCP (créditos de teste) com alertas de orçamento (US$10/25/50), repositório GitHub 'leaveflow' (monorepo), Docker, Go, Python (uv), Node LTS, gcloud, Postgres local em Docker", "R706", 1.5, "P", "Ambiente pronto + print dos alertas de orçamento"),
            b("T00", "LT01 VS02", "D01 Python (ver aba Diagnóstico)", "", 1, "L", "Código + testes + nível D01"),
            b("T00", "LT02 VB15 VS01", "D02 Go: endpoint idempotente", "", 1, "L", "Código + testes + nível D02"),
            b("T00", "CQ12", "Registrar resultados de D01-D02 com evidências (tempo, testes, rubrica)", "", 0.5, "W", "Aba Diagnóstico preenchida (D01-D02)")],
           [b("T00", "LT03 VS04", "D03 TypeScript", "", 1, "L", "Código + testes + nível D03"),
            b("T00", "LT04 DA01 DA04", "D04 SQL/PostgreSQL (diagnostico/d04-schema.sql)", "", 1, "L", "Queries + EXPLAIN + nível D04"),
            b("T00", "LT05 LT06 LT07", "D05 Git/GitHub/Agile", "R104", 0.5, "L", "PR de treino + histórias + nível D05"),
            b("T16", "VB01 OP09", "Domínio: FMLA Fact Sheet #28G e formulário WH-380-E (o que é um caso de afastamento médico nos EUA)", "R1603,R1107", 1, "E", "Glossário inicial (15 termos)"),
            b("T00", "PC01", "Estrutura docs/ do repositório: design-docs/, adr/, updates/, postmortems/, runbooks/, agent-reviews.md", "", 0.5, "P", "Commit com a estrutura de docs")],
           [b("T00", "DA02 DA07 DA11", "D06 Dados no BigQuery sandbox (dataset GA4 de exemplo)", "R907,R905", 1, "L", "SQL + bytes processados + nível D06"),
            b("T00", "CD02 CD06 VS07", "D09 Cloud: deploy no Cloud Run sem tutorial", "", 1, "L", "URL do serviço + nível D09"),
            b("T15", "LI01 CQ02 LI10", "D13 Liderança: revisar o PR do júnior + roteiro de 1:1", "", 1, "W", "Comentários + roteiro + nível D13"),
            b("T15", "PC01 VL01 VL02 VL04", "D14 Comunicação: design doc de 1 página + update + mensagem de atraso", "", 1, "W", "3 textos + nível D14")],
           [b("T00", "EA04 EA09", "D07 Arquitetura e design de sistema", "", 1, "L", "1 página + diagrama + nível D07"),
            b("T00", "EA08 VB28 VB29", "D08 Sistemas distribuídos e workflows (8 cenários)", "", 1, "L", "Respostas corrigidas + nível D08"),
            b("T00", "CQ09 CQ10 VB20", "D10 Confiabilidade: incidente de cobrança duplicada", "", 1, "L", "Fix + teste + 5 porquês + nível D10"),
            b("T00", "CO01", "D11 Compliance: classificação de 20 campos", "", 0.5, "L", "Tabela corrigida + nível D11"),
            b("T00", "OP02 OP01", "D12 Operações e negócio: mapa do processo manual de Ops", "", 0.5, "L", "Mapa as-is + priorização + nível D12")],
           [b("T00", "VA06 VA01 VS28", "D15 AI-native: estender D02 com agente e verificar sozinho", "R1402", 1, "L", "Plano + lista de erros do agente + nível D15"),
            b("T00", "VG03 LT03 VS05 VS24", "D16 Growth/frontend: variantes estáveis + evento no dataLayer", "", 1, "L", "Código + teste + nível D16"),
            b("T00", "CQ12 PC08", "Consolidar aba Diagnóstico (nível por grupo) e coluna 'Nível no diagnóstico' da Matriz", "", 1, "W", "Planilha atualizada"),
            b("T15", "LT07 LI06 VQ06", "Shape Up: 'Principles of Shaping' e 'Set Boundaries' (appetite) — base para cortar escopo", "R1504", 1, "E", "Notas: 5 ideias aplicáveis ao plano")],
           [b("T15", "VK01 OP05 PC08", "Calibração: aplicar as regras de ajuste (item 0) e escrever 'Plano ajustado v1' (o que ganha/perde horas e por quê)", "", 1.5, "W", "docs/plano-ajustado-v1.md"),
            b("T06", "VB01 EA09 V302", "EventStorming big picture do LeaveFlow: eventos do caso de ponta a ponta (intake → pagamento → consulta → documentação → encerramento)", "R1605", 1.5, "P", "Foto/diagrama dos eventos + hotspots"),
            b("T14", "VA02 VS28 VS29 VS30", "CLAUDE.md e AGENTS.md v0 (comandos, convenções, 'nunca faça', definição de pronto) + permissões básicas", "R1401,R1403", 1, "R", "CLAUDE.md/AGENTS.md v0 commitados")],
       ])

# ---------------------------------------------------------------- Semana 2
semana(2, F0, "Diagnóstico complementar + fundamentos personalizados",
       "Refazer exercícios fracos/inconclusivos; reforçar fundamentos conforme o diagnóstico; modelar o domínio e o plano do projeto.",
       "Design doc #1 do LeaveFlow, glossário e context map preliminar.",
       "Badge de Cloud Run iniciado/concluído, design doc #1 revisado, registro de riscos v0.",
       "Design doc #1, registro de riscos, plano de comunicação.",
       False, [
           [b("T00", "LT02 LT04", "Refazer diagnósticos abaixo do esperado (padrão: D02 e D04 em variante nova); se todos ok, aprofundar o pior grupo", "", 2, "L", "Níveis revisados na aba Diagnóstico"),
            b("T01", "LT02 VS01", "Tour of Go: Basics + Methods/Interfaces (se D02 = avançado, trocar por reforço do pior grupo)", "R101", 2, "L", "Exercícios do tour resolvidos")],
           [b("T02", "LT04 DA04", "pgexercises: Basic, Joins, Aggregates", "R202", 2, "L", "Soluções em sql/pgexercises.md"),
            b("T06", "EA09 VB25", "DDD Reference (Evans): bounded context, ubiquitous language, context map", "R606", 1, "E", "Resumo de 1 página"),
            b("T01", "LT01 LT02 CQ04", "Templates de serviço: Python (uv, ruff, mypy, pytest) e Go (Makefile, go vet, testes)", "", 1, "P", "templates/ no monorepo")],
           [b("T06", "VB31 EA09 OP02", "EventStorming de processo + glossário (linguagem ubíqua) do caso de afastamento", "R1605,R607", 2, "P", "docs/glossario.md + mapa de processo"),
            b("T16", "OP09 VK03 VR03", "Mentalidade de startup: 'Do Things that Don't Scale'", "R1601", 1, "E", "3 implicações para o seu trabalho com Ops/Growth"),
            b("T15", "V302 PC01", "Doc 'Fluxo de um caso v0' (1 página, hipótese a validar nas próximas semanas)", "", 1, "W", "docs/fluxo-do-caso-v0.md")],
           [b("T07", "CD02 VS07 VS09", "Google Skills: Develop Serverless Applications on Cloud Run (labs iniciais)", "R701", 3, "L", "Labs concluídos"),
            b("T01", "LT03", "TypeScript Handbook: The Basics, Everyday Types, Narrowing", "R103", 1, "E", "Notas + 5 exercícios no playground")],
           [b("T07", "CD02 CD01", "Google Skills Cloud Run: concluir labs + challenge lab", "R701", 2, "L", "Badge (ou progresso registrado)"),
            b("T01", "LT05 LT06 CQ02", "GitHub Skills: revisar pull requests e resolver conflitos de merge", "R107", 1, "L", "Cursos concluídos"),
            b("T14", "VA01 VA03 VS28", "Claude Code in Action (módulos iniciais) + hook que roda testes ao final de cada tarefa", "R1404,R1405", 1, "R", "Hook commitado + nota")],
           [b("T15", "VL01 PC01 EA06 EA14", "Design doc #1: LeaveFlow — problema, escopo, não-objetivos, contextos, marcos das 24 semanas, riscos", "R1502", 1.5, "W", "docs/design-docs/001-leaveflow.md"),
            b("T15", "OP08 PC06 PC17", "Registro de riscos v0 + plano de comunicação (CEO, Growth, Ops, júnior: o quê, quando, por qual canal)", "R1508", 1.5, "W", "docs/riscos.md + docs/comunicacao.md"),
            flex("refazer o exercício de diagnóstico com pior nota")],
       ])

# ---------------------------------------------------------------- Semana 3
semana(3, F1, "Serviço 'legado' em Python + modelagem v1 + dados fictícios",
       "Construir o sistema legado de propósito simples (será migrado na semana 11); Python e Postgres na prática; classificação de dados desde o dia 1.",
       "intake-legacy (FastAPI + Postgres) com testes, rodando em Docker.",
       "POST/GET de casos, migrações, seeds fictícios, cobertura ≥70%, logs sem PHI, docker compose up funcionando.",
       "Design doc #2 (por que o legado é assim), retro + update semanal.",
       False, [
           [b("T02", "DA01 DA04 LT04 VS03", "PostgreSQL cap. 13 (MVCC, níveis de isolamento): anotar 5 armadilhas para o projeto", "R201", 1.5, "E", "notas/postgres.md"),
            b("T01", "LT01 VS02 EA02 VB01 VK05", "intake-legacy (FastAPI): esqueleto com uv/ruff/mypy/pytest; POST /intake sem idempotência (proposital: é o 'legado')", "R108", 2.5, "P", "Serviço rodando local + testes")],
           [b("T13", "CO01 VR07 VD04", "HHS: resumo da Security Rule + identificadores do Safe Harbor; classificar cada campo do intake", "R1301,R1302", 1, "E", "docs/data-classification.md"),
            b("T02", "DA05 DA01 LT04 VB13", "Modelo v1 'legado': tabela única cases (status texto livre, payload JSONB), migrações SQL, seeds com Faker (100% fictícios)", "R201", 3, "P", "migrations/ + gerador de dados")],
           [b("T01", "LT01 CQ01 EA03", "Fluxo legado: validação pydantic, listagem/filtro, transições de status ad hoc (anti-padrão consciente); testes de integração com Testcontainers", "R812", 3, "P", "Testes de integração verdes"),
            b("T15", "PC01 VL01 EA06", "Design doc #2 (1 página): 'Por que o legado é assim' — limites e dívidas conhecidas (base da migração)", "R1502", 1, "W", "docs/design-docs/002-legado.md")],
           [b("T06", "LT01 EA05 VB25", "Cosmic Python caps. 1-2 (domain model, repository): comparar com o legado", "R601", 1, "E", "Lista: 5 problemas do legado à luz do livro"),
            b("T02", "LT04 DA01 DA13 EA07", "Queries operacionais no legado: casos parados >48h, funil por status, duplicados por e-mail; índices + EXPLAIN ANALYZE", "R203", 3, "P", "sql/operacional.sql com planos antes/depois")],
           [b("T08", "CQ01 CO01 VB18 CQ07", "Logging estruturado JSON com redação de campos sensíveis, healthcheck, erros padronizados; cobertura ≥70%", "R809", 3, "P", "Logs sem PHI + relatório de cobertura"),
            b("T14", "VA01 VA06 VS28 CQ02", "AI-native lab: agente implementa export CSV; revisar o diff linha a linha, rodar testes, achar ≥1 problema (PHI em log? paginação?)", "R1402", 1, "R", "Entrada em docs/agent-reviews.md")],
           [b("T07", "CD07 LT06 EA12", "Dockerfile multi-stage + docker compose (api + postgres) + Makefile; tag v0.0.1", "", 1.5, "P", "docker compose up funcionando"),
            b("T15", "PC03 PC05 PC07 PC08 VL02 LT07", "Retro semanal + update semanal para o 'CEO' + atualizar Status no cronograma", "R1509", 1.5, "W", "docs/updates/semana-03.md"),
            flex("Python: typing avançado e pydantic")],
       ])

# ---------------------------------------------------------------- Semana 4
semana(4, F1, "Go essencial + endpoint idempotente persistido + Checkpoint 1",
       "Ganhar fluência em Go; implementar idempotência de verdade com Postgres; primeiro checkpoint.",
       "case-service v0 (Go) com POST idempotente persistido e GET paginado.",
       "go test -race verde com 50 requisições concorrentes; ADR-001; demo de 3 min gravada.",
       "ADR-001, checkpoint 1 (matriz + replanejamento).",
       True, [
           [b("T01", "LT02 VS01", "Tour of Go: genéricos e concorrência (goroutines, channels, select)", "R101", 2, "L", "Exercícios resolvidos"),
            b("T01", "LT02 CQ01", "Learn Go with Tests: HTTP server, concorrência, context", "R102", 2, "L", "Exercícios com testes")],
           [b("T03", "VB15 VB14 EA11 VB11", "Stripe (idempotência) + AWS (retries seguros): extrair regras para a API do LeaveFlow", "R301,R303", 1, "E", "docs/regras-de-api.md"),
            b("T03", "VB15 LT02 DA01 VB11 VS01", "case-service v0: POST /cases com Idempotency-Key persistida (unique + resposta armazenada), corpo divergente → 422; pgx + migrações", "R303", 3, "P", "Endpoint idempotente com testes")],
           [b("T08", "CQ01 VB15 EA08", "Testes: table-driven, httptest, go test -race com 50 requisições concorrentes na mesma chave; Testcontainers", "R807", 3, "P", "Testes de concorrência verdes"),
            b("T15", "OP07 PC01 VL03 EA13", "ADR-001: idempotência via tabela de chaves (alternativas: Redis, chave natural) com trade-offs", "R1505", 1, "W", "docs/adr/001-idempotencia.md")],
           [b("T01", "LT02", "Effective Go (erros, interfaces) + Go by Example (context, timeouts)", "R105,R106", 1, "E", "Checklist de estilo Go do projeto"),
            b("T01", "LT02 VB11 EA05", "GET /cases/{id} e listagem com paginação por cursor, erros problem+json, timeouts/context de ponta a ponta", "R106", 3, "P", "Endpoints + testes")],
           [b("T02", "DA01 DA04 VB13 EA08", "Concorrência no Postgres: simular lost update, corrigir com SELECT ... FOR UPDATE e comparar níveis de isolamento", "R204", 3, "P", "Teste que reproduz e prova a correção"),
            b("T14", "VA05 VA06 VS28 CQ02", "AI-native lab: subagente 'revisor' com checklist de idempotência; comparar a revisão dele com a sua (falsos positivos/negativos)", "R1406", 1, "R", "docs/agent-reviews.md atualizado")],
           [b("T01", "VC01 LT06", "Checkpoint 1: demo gravada (3 min) dos 2 serviços; tag v0.1.0-rc", "", 1.5, "P", "Vídeo + tag"),
            b("T15", "PC08 LI06 OP05 VL04 VK01 VR10", "Checkpoint 1: atualizar a Matriz (nível atual), horas reais × plano, replanejar 4 semanas e decidir cortes", "R1504", 1.5, "W", "docs/checkpoints/cp1.md"),
            flex("Go: concorrência e genéricos")],
       ])

# ---------------------------------------------------------------- Semana 5
semana(5, F1, "CI/CD, Cloud Run, Cloud SQL, staging e produção",
       "Colocar os 2 serviços em staging/produção com pipeline, segredos e custo sob controle.",
       "Pipeline Cloud Build: lint → testes → build → deploy staging; prd por tag com aprovação.",
       "Release v0.1.0 em prd; rollback testado; ADR-002 (topologia); custo diário anotado.",
       "ADR-002, runbook de release, update + registro de riscos.",
       False, [
           [b("T07", "CD02 CD01 VS07 VS06", "Google Skills Cloud Run: labs de Pub/Sub e API gateway (se badge já feito na semana 2, avance no lab de Terraform)", "R701", 2, "L", "Labs concluídos"),
            b("T07", "CD03 VB06 VB04 VS08 OP07", "Projeto GCP: Artifact Registry, contas de serviço por serviço; ADR-002 (1 instância Cloud SQL com bancos stg/prd × 2 instâncias como na vaga: custo × isolamento)", "R706", 2, "P", "docs/adr/002-topologia-gcp.md")],
           [b("T07", "CD05 CD04 VS11", "Cloud Build → Cloud Run (docs) + SWE at Google cap. 24 (entrega contínua)", "R702,R707", 1, "E", "Notas"),
            b("T07", "CD04 CD05 CD06 VB09 EA12 VS11", "cloudbuild.yaml para Go e Python: lint → testes → build → push → deploy staging; prd por tag com aprovação manual", "R702", 3, "P", "Pipeline verde")],
           [b("T07", "VS08 DA01 CD07 VB04 CO01", "Cloud SQL Postgres (menor tier; parar quando ocioso) + conexão do Cloud Run + Secret Manager; migrações no pipeline", "R703,R705", 3, "P", "Serviços em staging usando Cloud SQL"),
            b("T15", "CQ03 PC02 V304", "Runbook de release v1: checklist pré/pós deploy, rollback por revisão do Cloud Run, quem avisar", "", 1, "W", "docs/runbooks/release.md")],
           [b("T08", "VB09 CD06", "SRE book: 'Embracing Risk' e 'Release Engineering'", "R801", 1, "E", "Notas aplicadas ao pipeline"),
            b("T07", "VB06 CD06 CD07 VB08 VB02", "Staging × prd por serviço, config por ambiente, smoke test pós-deploy, rollback = mudança de tráfego entre revisões", "R702", 3, "P", "Rollback demonstrado")],
           [b("T08", "CD10 VB18 CQ06", "Cloud Logging (JSON com trace id), métricas de request, alerta de taxa de 5xx em staging", "R809,R811", 3, "P", "Alerta disparando num teste"),
            b("T14", "VA03 VA02 VS30", "AI-native lab: hook que bloqueia edição de infra/segredos e exige lint+testes antes de concluir; provar que barra uma ação proibida", "R1405,R1407", 1, "R", ".claude/settings.json + hook commitados")],
           [b("T07", "CD06 V304 VC01 VC04", "Release v0.1.0 em prd com release notes; verificar custo diário no billing", "", 1.5, "P", "Release notes + custo/dia"),
            b("T15", "OP08 PC03 PC15", "Update semanal + registro de riscos (custo GCP, trial do Temporal Cloud, cota do Airtable Free)", "R1508", 1.5, "W", "docs/updates/semana-05.md"),
            flex("Docker/Cloud Run (concorrência, timeouts, cold start)")],
       ])

# ---------------------------------------------------------------- Semana 6
semana(6, F1, "APIs, webhooks e kit de integração + TypeScript",
       "Criar a base reutilizável para as 20+ integrações; contratos tipados; primeira simulação de júnior.",
       "Kit de integração (Go e Python) + receptor de webhooks genérico + cliente TS gerado do OpenAPI.",
       "Teste de caos com provedor fake (30% erros/429) sem efeitos duplicados; PR do júnior revisado.",
       "Design doc #3 (padrão de integração), revisão de PR do júnior #1.",
       False, [
           [b("T03", "VB14 EA11 VB08", "AWS: timeouts, retries, backoff com jitter + especificação Standard Webhooks", "R302,R304", 1.5, "E", "Resumo de regras"),
            b("T03", "EA11 VB14 VB16 VB07 LT02 VC04", "Kit de integração em Go: cliente HTTP com timeout, retry exponencial + jitter (só idempotentes), circuit breaker simples, token bucket; testes com servidor fake", "R302", 2.5, "P", "pkg/integration com testes")],
           [b("T03", "EA11 VB11", "Webhooks: HMAC sobre corpo cru, tolerância de timestamp, proteção contra replay", "R304", 1, "E", "Checklist de webhook"),
            b("T03", "VB15 VB16 EA10 VR04 VB23", "Receptor de webhooks genérico (Go): verifica assinatura → grava evento cru (inbox) → 200 rápido → processamento assíncrono com dedupe por event id", "R304", 3, "P", "Receptor + testes de duplicata")],
           [b("T03", "LT01 EA11 VB14", "Kit equivalente em Python (httpx + tenacity) para ops-sync e form-filler; contrato comum de erros/retries", "R108", 3, "P", "libs/py-integration com testes"),
            b("T15", "PC01 VL01 LI11 VB32", "Design doc #3: 'Padrão de integração LeaveFlow' (inbox, retries, DLQ, idempotência) escrito para o júnior seguir", "R1502", 1, "W", "docs/design-docs/003-integracoes.md")],
           [b("T01", "LT03 VS04", "TypeScript Handbook: generics, unions discriminadas, utility types", "R103", 1, "E", "Exercícios"),
            b("T01", "LT03 VB11 EA11 CQ01", "OpenAPI do case-service + cliente TypeScript tipado gerado + validação zod; CLI TS que cria casos (prova de contrato)", "R103", 3, "P", "clients/ts + teste de contrato")],
           [b("T02", "LT04 DA07 DA01", "pgexercises (window functions, CTEs) + 3 queries de domínio (tempo em cada status, por coorte semanal)", "R202", 3, "L", "sql/analitico.sql"),
            b("T14", "VA01 VA02 VS29 VS30", "AI-native lab: Codex com AGENTS.md gera o cliente Python; comparar com Claude Code; manter uma fonte única de regras", "R1403,R1412", 1, "R", "Nota comparativa + regras unificadas")],
           [b("T03", "VB16 VB08 CQ08", "Caos leve: provedor fake com 30% de 500/429 e latência alta; provar que o kit não duplica efeitos", "", 1.5, "P", "Relatório do teste de caos"),
            b("T15", "CQ02 LI08 LI10 VC02 VA06", "Simulação júnior #1: revisar PR 'do júnior' gerado com 6 erros plantados (retry não idempotente, segredo em log...) usando a Feedback Equation", "R1503,R1507", 1.5, "W", "Revisão escrita + o que ensinar"),
            flex("SQL: índices e planos de execução")],
       ])

# ---------------------------------------------------------------- Semana 7
semana(7, F2, "DDD estratégico/tático + Clean Architecture + testes de arquitetura",
       "Definir bounded contexts e o modelo de domínio novo; impor camadas com testes de arquitetura no CI.",
       "case-service reorganizado (domain/app/adapters) com agregado Case e eventos de domínio.",
       "Context map + Bounded Context Canvas; testes de arquitetura quebrando o build em violação.",
       "ADR-003 (limites e o que NÃO separar), 1:1 simulado com o júnior.",
       False, [
           [b("T06", "EA09 VB25 VB31", "Learning DDD (partes I-II) ou DDD Reference: subdomínios, bounded contexts, context map", "R602,R606", 2, "E", "Notas"),
            b("T06", "VB31 EA09 VB01 EA04", "Context map do LeaveFlow (Intake, Case Management, Billing, Scheduling, Clinical Docs, Ops Queue, Growth/Analytics) + Bounded Context Canvas de Case Management", "R607", 2, "P", "docs/context-map.md + canvas")],
           [b("T06", "VB26 VB27 EA05", "Wild Workouts / Go With The Domain: camadas, ports & adapters, CQRS leve em Go", "R603,R608", 1.5, "E", "Notas + trechos de referência"),
            b("T06", "VB25 VB13 EA09 LT02", "Agregado Case: máquina de estados explícita, invariantes, value objects (CaseId, LeaveWindow), eventos de domínio; testes unitários puros", "R603", 2.5, "P", "internal/domain com testes")],
           [b("T06", "VB26 EA05 EA06", "Reorganizar case-service em domain/app/adapters/ports; casos de uso (commands) com Unit of Work", "R601", 3, "P", "Refatoração com testes verdes"),
            b("T15", "VB32 VC09 OP07 VL03 EA13", "ADR-003: limites dos bounded contexts e o que NÃO separar agora (monólito modular × serviços)", "R1505", 1, "W", "docs/adr/003-bounded-contexts.md")],
           [b("T06", "VB25 VB26 LT01", "Cosmic Python caps. 4-7 (service layer, Unit of Work, aggregates)", "R601", 1, "E", "Notas"),
            b("T14", "VA04 VB26 CQ04", "Testes de arquitetura: go-arch-lint (domain não importa adapters) + import-linter (camadas) no CI", "R1409,R1408", 3, "P", "Build falha em violação (prova)")],
           [b("T06", "VB25 VB23 PC01", "Linguagem ubíqua: glossário, nomes de eventos (CaseOpened, PaymentConfirmed, ConsultScheduled, CertificationDrafted, CaseClosed) e JSON Schemas versionados", "", 3, "P", "schemas/events/*.json + glossário"),
            b("T14", "VA04 VA03 VA06", "AI-native lab: pedir ao agente uma feature que viola camadas; ver o teste de arquitetura pegar; registrar a regra no CLAUDE.md/AGENTS.md", "R1402", 1, "R", "Regra nova + entrada em agent-reviews")],
           [b("T06", "EA04 VC01", "Demo: comando OpenCase ponta a ponta + diagrama C4 nível 2 atualizado", "", 1.5, "P", "Vídeo + diagrama"),
            b("T15", "LI08 LI03 LI10 VC02", "1:1 simulado com o 'júnior' (roteiro: objetivos, bloqueios, feedback, plano de crescimento)", "R1506", 1.5, "W", "docs/lideranca/1on1-01.md"),
            flex("DDD: releitura dirigida dos pontos que ficaram confusos")],
       ])

# ---------------------------------------------------------------- Semana 8
semana(8, F2, "Transactional outbox + Pub/Sub + consumidores idempotentes + Checkpoint 2",
       "Publicar eventos de domínio com garantia e consumir sem duplicar efeitos; DLQ e reprocessamento.",
       "Outbox + relay (SKIP LOCKED) → Pub/Sub; consumidor idempotente; DLQ com CLI de reprocessamento.",
       "Teste prova atomicidade (rollback não publica); poison message vai para DLQ; checkpoint 2 feito.",
       "Postmortem simulado #1, checkpoint 2 com comunicação de risco.",
       True, [
           [b("T04", "EA08 VB29 VB23", "DDIA 2ª ed.: codificação/evolução de esquemas e processamento de streams (seleção) + padrão outbox", "R401,R402", 2, "E", "Notas"),
            b("T04", "VB29 DA01 VB13", "Tabela outbox gravada na mesma transação do agregado; teste provando que rollback não publica", "R402", 2, "P", "Outbox + teste de atomicidade")],
           [b("T04", "VS09 VB03 EA08", "Pub/Sub: exactly-once (pull), ordering keys, dead-letter topics", "R403,R405,R406", 1, "E", "Tabela de garantias"),
            b("T04", "VB29 VS09 VB14 VB16", "Relay do outbox (Go): SELECT ... FOR UPDATE SKIP LOCKED, publish com ordering key = case_id, métrica de lag; emulador local", "R402", 3, "P", "Relay com testes")],
           [b("T04", "VB15 VB16 VS09 CQ09", "Consumidor idempotente (processed_messages), DLQ com max delivery attempts, CLI de reprocessamento da DLQ", "R405", 3, "P", "Consumidor + CLI"),
            b("T15", "CQ10 PC02 VB20 VB21 VK04", "Postmortem simulado #1 (blameless): 'mensagem duplicada gerou e-mail duplo' — timeline, causa raiz, correção sistêmica", "R806", 1, "W", "docs/postmortems/001.md")],
           [b("T04", "VB28 VB10 EA08", "microservices.io: Saga (coreografia × orquestração) — por que vamos orquestrar com Temporal", "R404", 1, "E", "Nota de decisão"),
            b("T07", "VS09 CD03 CD04 VB02", "Pub/Sub em staging (tópicos/assinaturas scriptados com gcloud ou Terraform), push × pull (ADR curta); relay como serviço Cloud Run", "R704", 3, "P", "infra/pubsub + ADR curta")],
           [b("T08", "CQ01 VB16 EA08", "Testes de integração outbox → Pub/Sub (emulador) + poison message indo para a DLQ", "R807", 3, "P", "Testes verdes no CI"),
            b("T14", "VA05 VA06 VS28", "AI-native lab multiagente: agente A implementa o consumidor, agente B (sessão separada) escreve testes adversariais sem ver a implementação; você arbitra", "R1406", 1, "R", "Relatório: bugs achados por B")],
           [b("T04", "VB23 VC01 VR02", "Checkpoint 2: demo OpenCase → evento no Pub/Sub → consumidor idempotente; mostrar a DLQ", "", 1.5, "P", "Vídeo"),
            b("T15", "VL04 PC18 PC08 V306", "Checkpoint 2: Matriz + horas; se houver atraso, mensagem de risco (o que aconteceu, o que muda, novo prazo)", "R1504", 1.5, "W", "docs/checkpoints/cp2.md"),
            flex("DDIA: capítulo de transações")],
       ])

# ---------------------------------------------------------------- Semana 9
semana(9, F2, "Temporal: fundamentos e workflow CaseLifecycle v1",
       "Dominar o modelo de execução durável; workflow com sinais, timers e activities idempotentes.",
       "orchestrator (Go) com CaseLifecycle v1 + ponte Pub/Sub → sinal; worker Python esqueleto.",
       "Temporal 101/102 concluídos; testes de workflow e replay passando.",
       "Design doc #4 (CaseLifecycle), plano quinzenal com trade-offs.",
       False, [
           [b("T05", "VS12 VB10 VD03", "Temporal 101 (Go) completo", "R501", 2, "L", "Curso concluído"),
            b("T05", "VB10 VB03 LT02", "orchestrator (Go): dev server local, worker, CaseLifecycle v1 (sem compensações) com activities chamando o case-service", "R505", 2, "P", "Workflow rodando local")],
           [b("T05", "VB10 CQ01 VS12", "Temporal 102 (Go): testes, debug, determinismo, deploy", "R502", 2, "L", "Curso concluído"),
            b("T05", "VB03 VB13 VB23", "Sinais (PaymentConfirmed), timer de SLA (48h), queries de estado; ponte Pub/Sub → signal com consumidor idempotente", "R505", 2, "P", "Ponte + testes")],
           [b("T05", "CQ01 VB10", "Testes de workflow (ambiente de teste com time skipping) + replay test com histórico salvo", "R502", 3, "P", "Testes verdes"),
            b("T15", "VL01 VB13 PC01", "Design doc #4: CaseLifecycle — estados, sinais, timeouts; o que fica no workflow × no agregado", "R1502", 1, "W", "docs/design-docs/004-caselifecycle.md")],
           [b("T05", "VB14 VB15 VS12", "Docs Temporal: activities idempotentes, retry policies, heartbeats; visão do Python SDK", "R505,R506", 1, "E", "Notas"),
            b("T05", "VB14 VB15 VB08", "Retry policy por activity (erros de negócio não-retryable), timeouts start-to-close/schedule-to-close, idempotency key = workflowId + activityId", "R505", 3, "P", "Políticas + testes de falha")],
           [b("T05", "LT01 VS12 VB02", "Worker Python (form-filler) registrando activity ExtractDocument (stub) numa task queue dedicada", "R506", 3, "P", "Worker Python rodando"),
            b("T14", "VA06 VA02 VA03", "AI-native lab: agente escreve código de workflow; caçar não-determinismo (time.Now, rand, goroutines) com replay test; regra no CLAUDE.md", "R1402", 1, "R", "Regra + agent-reviews")],
           [b("T05", "VC01 VB10", "Demo: caso percorre o workflow com sinal de pagamento simulado e timer", "", 1.5, "P", "Vídeo + histórico no Temporal UI"),
            b("T15", "VL03 PC03 LI06 VC03", "Update semanal + plano das próximas 2 semanas com trade-offs (velocidade × escopo × qualidade)", "R1504", 1.5, "W", "docs/updates/semana-09.md"),
            flex("Go/Temporal: exercícios extras do curso 102")],
       ])

# ---------------------------------------------------------------- Semana 10
semana(10, F2, "Sagas, CQRS e projeções; versionamento de workflows",
       "Compensações confiáveis, read models alimentados por eventos e evolução segura de workflows em execução.",
       "Saga com compensações; projeções case_summary e ops_queue_view com rebuild; versionamento aplicado.",
       "Teste de falha em cada passo da saga; rebuild = estado incremental; replay antes/depois do patch.",
       "ADR-004 (CQRS onde paga), mensagem de desbloqueio ao júnior.",
       False, [
           [b("T05", "VB28 VB16", "Temporal: Saga Pattern Made Easy (compensações LIFO)", "R504", 1.5, "E", "Notas"),
            b("T05", "VB28 VB16 VB12 VS16", "Saga no CaseLifecycle: pagamento → agendamento (adapter fake no estilo Healthie) → documentação; compensações (estorno, cancelar consulta) testadas por passo", "R504", 2.5, "P", "Saga + testes de falha")],
           [b("T06", "VB27 VB30", "CQRS e projeções: Cosmic Python (CQRS) + queries no Wild Workouts", "R601,R603", 1, "E", "Notas"),
            b("T06", "VB30 VB27 VB15 DA05", "Projeções case_summary e ops_queue_view alimentadas por eventos, idempotentes por event_id; endpoint de query separado", "R601", 3, "P", "Read models + testes")],
           [b("T06", "VB30 VB16 DA11", "Rebuild de projeção a partir do log de eventos com versão de projeção; teste: rebuild = estado incremental", "", 3, "P", "Comando de rebuild + teste"),
            b("T15", "VB32 VC09 OP07", "ADR-004: CQRS só onde paga (read models para Ops e analytics) e quando NÃO usar", "R1505", 1, "W", "docs/adr/004-cqrs.md")],
           [b("T05", "VS12 CD08", "Temporal: Versioning Workflows (Go)", "R503", 1, "L", "Curso concluído"),
            b("T05", "CD08 VB10 CQ05", "Aplicar versionamento numa mudança do CaseLifecycle com execuções em andamento; replay test antes/depois", "R503", 3, "P", "Patch versionado + replay verde")],
           [b("T07", "VS12 VB03 CD07 VS07", "Temporal em staging: Temporal Cloud (créditos de teste) ou dev server + gravação; worker no Cloud Run com credenciais no Secret Manager", "R507,R705", 3, "P", "Worker em staging (ou plano B documentado)"),
            b("T14", "VA06 VB32 VA01", "AI-native lab: plan mode para compensações; avaliar o plano antes do código e recusar 2 sugestões complexas demais, justificando", "R1402", 1, "R", "Plano anotado + agent-reviews")],
           [b("T05", "VC01 VB28", "Demo: falha no agendamento dispara estorno e cancelamento; histórico no Temporal UI", "", 1.5, "P", "Vídeo"),
            b("T15", "LI08 LI09 LI10 VC02 V307", "Simulação júnior #2: júnior travado em bug de não-determinismo — mensagem de desbloqueio com perguntas de coaching (sem dar a resposta)", "R1503", 1.5, "W", "docs/lideranca/desbloqueio-01.md"),
            flex("Temporal: testes de workflow")],
       ])

# ---------------------------------------------------------------- Semana 11
semana(11, F2, "Migração do modelo legado para o novo, lado a lado",
       "Executar uma migração real em estilo strangler fig: eventos do legado, backfill, shadow read, cutover por coorte e rollback.",
       "Legado emitindo eventos; backfill idempotente; comparador de paridade; roteamento por feature flag.",
       "100% em staging e 10% em prd com paridade ≥99% nos campos críticos; runbook de cutover/rollback ensaiado.",
       "Plano de iniciativa grande (formato 60 dias), premortem, status report para stakeholders.",
       False, [
           [b("T06", "VB24 CD08 VK05", "Fowler: Strangler Fig + Parallel Change (expand/contract)", "R604,R605", 1.5, "E", "Notas"),
            b("T06", "VB24 VB29 EA10 LT01", "intake-legacy passa a emitir eventos (outbox em Python) no Pub/Sub; case-service consome via camada anticorrupção (legado → domínio)", "R604", 2.5, "P", "Eventos do legado materializando o modelo novo")],
           [b("T06", "VB24 VB15 VB16 DA06 CD02", "Backfill idempotente dos casos legados → modelo novo (Cloud Run job) com checkpoints e reexecução segura", "R604", 4, "P", "Job de backfill + teste de reexecução")],
           [b("T09", "VB17 DA11 DA13 VB24", "Shadow read + comparador diário legado × novo (campos críticos), relatório de divergências e % de paridade", "", 3, "P", "Relatório de paridade"),
            b("T15", "V309 EA14 OP05 OP06 OP08 EA13", "Plano de iniciativa grande (formato 60 dias): objetivo de negócio, restrições, limites do sistema atual, alternativas (big-bang × strangler × dual-write), plano até produção, riscos", "R1502,R1508", 1, "W", "docs/design-docs/005-migracao.md")],
           [b("T15", "OP08 VL04", "Premortem da migração (HBR): 10 modos de falha e mitigação", "R1508", 1, "W", "Seção de riscos do plano"),
            b("T06", "VB24 VB08 VB32", "Roteamento de leituras para o modelo novo por feature flag (coorte/percentual) com rollback instantâneo; justificar por que evitar dual-write", "", 3, "P", "Flag + testes")],
           [b("T08", "VB24 V303 CD09 CQ08", "Runbook de cutover/rollback + ensaio em staging: 10% → 50% → 100% acompanhando paridade e erros", "R805", 3, "P", "docs/runbooks/cutover.md + log do ensaio"),
            b("T14", "VA06 DA11", "AI-native lab: agente gera o comparador; você escreve casos de borda (nulos, timezones, status desconhecidos) e mede quantos o agente perdeu", "R1402", 1, "R", "agent-reviews")],
           [b("T06", "VB24 CD06 V301 OP06", "Release: migração 100% em staging e 10% em prd (dados fictícios) + nota de release", "", 1.5, "P", "Release notes"),
            b("T15", "PC04 PC15 PC17 OP07", "Status report da iniciativa para stakeholders (1 página) com a decisão pedida (go/no-go para 50%)", "R1501", 1.5, "W", "docs/updates/status-migracao.md"),
            flex("SQL/migrações expand-contract")],
       ])

# ---------------------------------------------------------------- Semana 12
semana(12, F3, "Stripe I: checkout, webhooks e PaymentConfirmed + Checkpoint 3",
       "Pagamento integrado de ponta a ponta com idempotência, ordem de eventos tratada e estorno como compensação.",
       "billing (Go): Checkout Session, webhook assinado com inbox, PaymentConfirmed → saga.",
       "Webhook duplicado não duplica efeito; evento fora de ordem tratado; estorno de teste na saga; checkpoint 3.",
       "Design doc #5 (pagamentos e modos de falha), checkpoint 3.",
       True, [
           [b("T10", "VS15 VB12 VD02", "Stripe: assinaturas com Checkout + testes + idempotent requests", "R1001,R1006,R1015", 1.5, "E", "Notas"),
            b("T10", "VB12 VS15 VB15 LT02", "billing (Go): produtos/preços (avaliação avulsa + assinatura de acompanhamento), Checkout Session com idempotency key e metadata case_id", "R1001", 2.5, "P", "Checkout de teste funcionando")],
           [b("T10", "VB15 EA10", "Stripe webhooks: duplicados, ordem, assinatura, processamento assíncrono", "R1002", 1, "E", "Checklist"),
            b("T10", "VB15 VB16 VB12 EA10 VS15", "Webhook: assinatura no corpo cru, inbox, dedupe por event.id, buscar estado atual do objeto (não confiar na ordem); Stripe CLI", "R1002", 3, "P", "Handler + testes")],
           [b("T10", "VB28 VB12 VB29 VB03", "PaymentConfirmed → outbox → Pub/Sub → sinal no CaseLifecycle; estorno real (modo de teste) como compensação da saga", "R1002", 3, "P", "Fluxo integrado"),
            b("T15", "VL01 VB08 PC01", "Design doc #5: pagamentos — estados e falhas (recusa, webhook atrasado, duplicado) e o que acontece com o caso em cada uma", "R1502", 1, "W", "docs/design-docs/006-pagamentos.md")],
           [b("T13", "CO01 VR07", "Escopo PCI mínimo com Checkout hospedado + OWASP API Top 10 (BOLA, autenticação)", "R1304", 1, "E", "Checklist de segurança de pagamentos"),
            b("T08", "CQ01 VB12 VB16", "Testes: cartões de teste (sucesso, recusa, 3DS), reentrega de webhook, evento fora de ordem, contrato do payload", "R1006", 3, "P", "Suite de testes de pagamento")],
           [b("T08", "VB18 CD10 VB12", "Métricas e alertas: falhas de webhook, eventos não processados >15 min, divergência pagamento × caso", "R811", 3, "P", "Alertas configurados"),
            b("T14", "VA05 VA06 CQ02", "AI-native lab: 2 agentes revisam o handler (segurança × idempotência); consolidar e aplicar só o que se justifica", "R1406", 1, "R", "agent-reviews")],
           [b("T10", "VC01 V301 VD02", "Checkpoint 3: demo checkout de teste → caso avança; webhook duplicado sem efeito duplo", "", 1.5, "P", "Vídeo"),
            b("T15", "PC08 VL04 LI06 V306 VR10", "Checkpoint 3: Matriz, horas, replanejamento; decidir o que vira opcional (valor > perfeição)", "R1504", 1.5, "W", "docs/checkpoints/cp3.md"),
            flex("Stripe: cenários de teste adicionais")],
       ])

# ---------------------------------------------------------------- Semana 13
semana(13, F3, "Stripe II: assinaturas, dunning, portal, upsell e reconciliação",
       "Cobrir o ciclo de vida da assinatura e garantir que dinheiro e casos batem.",
       "Ciclo de assinatura com test clocks, portal do cliente, add-on de upsell, job de reconciliação.",
       "3 discrepâncias plantadas detectadas e corrigidas; release v0.4 com pagamentos/assinaturas.",
       "Runbook de discrepância, resposta ao pedido do Head of Growth.",
       False, [
           [b("T10", "VS15 VB12", "Stripe: webhooks de assinatura + test clocks", "R1008,R1005", 1, "E", "Notas"),
            b("T10", "VB12 VB13 VD02 VG02", "Ciclo de assinatura: trial, renovação, falha (past_due), cancelamento → estado de acompanhamento do caso; test clocks avançando 2 meses", "R1005", 3, "P", "Testes com test clocks")],
           [b("T10", "VG02 VB12 VS15 VC06", "Customer portal (hospedado pelo Stripe) + upsell: add-on 'revisão expressa' pós-pagamento atrás de feature flag", "R1016", 4, "P", "Portal + add-on")],
           [b("T10", "VB17 DA13", "Stripe: payout reconciliation e balance transactions", "R1007", 1, "E", "Notas"),
            b("T09", "VB17 DA11 DA12 CD02", "Ledger interno por caso + job de reconciliação (Cloud Run job + Cloud Scheduler): Stripe × ledger × casos → tabela de discrepâncias", "R1007", 2, "P", "Job de reconciliação"),
            b("T15", "DA13 CD09 PC02", "Runbook 'discrepância de pagamento' (investigação, quem avisar, correção caso a caso)", "", 1, "W", "docs/runbooks/discrepancia-pagamento.md")],
           [b("T09", "VB17 VB19 VB20 DA13 CQ09", "Alertas de reconciliação; corrigir 3 discrepâncias plantadas (webhook perdido, estorno manual no dashboard, preço errado)", "R1007", 4, "P", "RCA das 3 discrepâncias")],
           [b("T13", "CO01 VR07 VD04", "Dados de pagamento: guardar só IDs (nada de cartão), retenção, acesso por papel, logs sem PII", "R1304", 3, "P", "Revisão + correções"),
            b("T14", "VA06 VA01 VS29", "AI-native lab: agente (Codex com PLANS.md) escreve o job a partir do seu plano; verificar com dados plantados e teste de propriedade", "R1413", 1, "R", "agent-reviews")],
           [b("T10", "VD02 V301 CD06", "Release v0.4: pagamentos e assinaturas em prd (modo de teste) + release notes", "", 1.5, "P", "Release notes"),
            b("T15", "VC06 VG01 PC18 VL03 PC13 PC09 PC10 PC11 PC14", "Simulação: Head of Growth pede 'teste de preço amanhã' — responder com plano mínimo viável, riscos e prazo realista", "R1504", 1.5, "W", "Resposta escrita"),
            flex("Stripe: reconciliação")],
       ])

# ---------------------------------------------------------------- Semana 14
semana(14, F3, "Airtable I: observar Ops, Single Queue e projeção de saída",
       "Tratar Ops como cliente; projetar casos na Single Queue respeitando rate limits, cota e integridade de campos.",
       "Base Single Queue + ops-sync (Python) projetando eventos com rate limit, validação e anexos.",
       "Caso aparece na Single Queue com anexo em <1 min; burst de 200 casos respeita 5 req/s; mapeamento validado no CI.",
       "Mapa as-is + job stories, ADR-005, mensagem de alinhamento com Ops.",
       False, [
           [b("T16", "VR09 OP02 VK03", "Paul Graham + YC: falar com usuários antes de construir", "R1601,R1604", 1, "E", "Roteiro de entrevista com Ops"),
            b("T16", "OP01 OP02 OP03 VR09 VC07", "'Sombra' simulada de Ops: 5 job stories + mapa as-is (raias) do processo manual", "R1605", 1, "W", "docs/ops/as-is.md"),
            b("T10", "VO01 VO02 VO04 VS19", "Base Airtable 'Single Queue': tabelas, campos, views por fila/SLA, campos de Ops × campos do backend", "R1003", 2, "P", "Base + doc de propriedade de campos")],
           [b("T10", "VO05 VS19", "Airtable Web API: introdução, rate limits (5 req/s por base; 429 → 30 s) e cota por plano (Free: 1.000/mês)", "R1003,R1011", 1, "E", "Orçamento de chamadas"),
            b("T10", "VO02 VO05 VB14 LT01 VB07", "ops-sync (Python): Pub/Sub → upsert no Airtable por case_id, lotes de 10, token bucket 5 req/s, backoff em 429; adapter fake para dev/teste (poupa a cota)", "R1003", 3, "P", "ops-sync com testes")],
           [b("T10", "VO04 VO09 CQ04 DA12", "Spec de mapeamento (YAML) + validação estrita (tipos, enums, obrigatórios) + testes de contrato: campo errado quebra o build", "", 3, "P", "mapping.yaml + testes"),
            b("T15", "OP07 VO05 VB32", "ADR-005: projeção event-driven + reconciliação periódica; orçamento de chamadas de API", "R1505", 1, "W", "docs/adr/005-sync-airtable.md")],
           [b("T10", "VO06", "Airtable: upload de anexos (até 5 MB por bytes, ou por URL)", "R1009", 1, "E", "Notas"),
            b("T10", "VO06 VB15 VB14", "Anexos: PDF do caso enviado ao Airtable com idempotência (hash do arquivo em campo) e retry", "R1009", 3, "P", "Anexos idempotentes")],
           [b("T08", "VB18 VO05 CD10", "Observabilidade do ops-sync: lag, 429/min, falhas por campo, logs com case_id sem PHI, alerta de lag >10 min", "R811", 3, "P", "Painel + alerta"),
            b("T14", "VA06 VO09", "AI-native lab: agente propõe o mapeamento a partir do schema; validar campo a campo contra a spec e medir a taxa de erro do agente", "R1402", 1, "R", "agent-reviews")],
           [b("T10", "VO02 VO05 VC07", "Demo: caso na Single Queue com anexo em <1 min; burst de 200 casos dentro do rate limit", "", 1.5, "P", "Vídeo"),
            b("T15", "PC12 PC16 PC18 PC06 VC07", "Update semanal + mensagem de alinhamento para Ops (o que muda no dia a dia, o que não muda, como reportar problemas)", "R1509", 1.5, "W", "docs/updates/semana-14.md"),
            flex("Python: testes de contrato")],
       ])

# ---------------------------------------------------------------- Semana 15
semana(15, F3, "Airtable II: mudanças de Ops, replays seguros e recuperação",
       "Fechar o ciclo bidirecional sem nunca sobrescrever edições manuais; recuperar caso a caso.",
       "Entrada via automação → endpoint assinado; propriedade por campo; CLI de replay; reconciliação diária.",
       "Teste de edição concorrente passa; game day recuperado; release v0.5 com métrica antes/depois.",
       "Runbook de recuperação, postmortem do game day com 3 correções sistêmicas.",
       False, [
           [b("T10", "VO03 VS19", "Automations ('When record updated' → 'Run a script' com fetch) × Webhooks API (cursor/payloads): comparar", "R1004,R1010", 1, "E", "Tabela comparativa"),
            b("T10", "VO03 VB22 VB15 EA10", "Entrada: automação do Airtable chama o ops-sync (HMAC + timestamp); ops-sync valida e emite comando ao case-service", "R1004", 3, "P", "Fluxo Ops → backend")],
           [b("T10", "VO07 VO09 VB15 VB13", "Propriedade por campo + versionamento: projeção nunca sobrescreve campo de Ops; conflito detectado por lastModifiedTime/versão; testes de edição concorrente", "", 4, "P", "Testes de conflito verdes")],
           [b("T10", "VO07 VO08 VB16", "CLI de replay: 1 caso / intervalo / todos a partir do log de eventos, com dry-run e diff", "", 3, "P", "CLI + testes"),
            b("T15", "VO08 CD09 PC15", "Runbook de recuperação caso a caso (DLQ, diff, replay, verificação com Ops) + comunicação com Ops durante incidente", "R805", 1, "W", "docs/runbooks/recuperacao-airtable.md")],
           [b("T09", "VB17 VO09 DA11 DA13", "Reconciliação diária Airtable × banco (campos críticos); corrigir 3 divergências plantadas", "", 4, "P", "Relatório + correções")],
           [b("T08", "CQ08 V303 VB16 VO08", "Game day: tempestade de 429 + automação desligada por 1h + campo renomeado por Ops; detectar, mitigar, recuperar", "R805", 3, "P", "Timeline do game day"),
            b("T14", "VA03 VA05 VA06", "AI-native lab: subagente 'runbook-executor' só com leitura + dry-run executa o runbook; você valida as conclusões", "R1407,R1406", 1, "R", "agent-reviews")],
           [b("T10", "VB22 OP03 V312 OP04 VR02", "Release v0.5 (Ops) em prd + métrica antes/depois (tempo manual estimado por caso)", "", 1.5, "P", "Release notes com métrica"),
            b("T15", "CQ10 VB21 V310 PC02 VK04", "Postmortem do game day (blameless) + 3 correções sistêmicas priorizadas", "R806", 1.5, "W", "docs/postmortems/002.md"),
            flex("Airtable: cenários de conflito")],
       ])

# ---------------------------------------------------------------- Semana 16
semana(16, F3, "AI Form Filler I: extração, evals e privacidade + Checkpoint 4",
       "Extrair dados de documentos com qualidade medida; decidir Document AI × Gemini com dados.",
       "form-filler (Python): extração A (Document AI) e B (Gemini) + harness de evals + activity no workflow.",
       "Métricas por campo publicadas; fallback para revisão humana abaixo do limiar; checkpoint 4.",
       "ADR-006, brief de delegação do Form Filler ao júnior, checkpoint 4.",
       True, [
           [b("T11", "VS14 EA15", "Google Skills: Automate Data Capture at Scale with Document AI (labs)", "R1103", 2, "L", "Labs concluídos"),
            b("T11", "EA15 VC05 DA12", "Dataset: 30 documentos sintéticos (atestados/intake fictícios em PDF) + WH-380-E (público) como formulário-alvo + rótulos-padrão", "R1107", 2, "P", "datasets/form-filler + labels")],
           [b("T11", "VS13", "Vertex AI: structured output (response schema)", "R1101", 1, "E", "Notas"),
            b("T11", "VS13 VS14 EA15 LT01", "Extração A (Document AI Form Parser) e B (Gemini com schema pydantic); normalização e validação (datas, períodos)", "R1101,R1102", 3, "P", "Pipeline A e B")],
           [b("T11", "EA15 DA10 VD01", "Harness de evals: precisão/recall por campo, % de documentos 100% corretos, custo e latência; comparar A × B × híbrido", "R1104", 3, "P", "Relatório de evals"),
            b("T15", "OP07 VD04 VB32", "ADR-006: Document AI × Gemini × híbrido (precisão, custo, privacidade/BAA, latência)", "R1303", 1, "W", "docs/adr/006-extracao.md")],
           [b("T13", "VD04 CO01 VR07", "Google Cloud HIPAA (produtos cobertos pelo BAA) + Sensitive Data Protection", "R1303,R1305", 1, "E", "Notas"),
            b("T11", "CO01 VD04 VB08", "Privacidade no pipeline: sem PHI em logs/traces, redação de prompts registrados, documentos com acesso restrito e retenção", "R1305", 3, "P", "Checklist + testes de redação")],
           [b("T05", "VB10 VC05 VB08", "Activity ExtractDocument (worker Python) no CaseLifecycle; timeouts/retries; revisão humana quando confiança < limiar", "R506", 3, "P", "Integração no workflow"),
            b("T14", "VA03 VA06 EA15", "AI-native lab: agente altera prompt/schema; mudança só entra se o eval melhora (eval como guardrail no CI)", "R1104", 1, "R", "Gate de eval no CI")],
           [b("T11", "VC05 VD01", "Checkpoint 4: demo documento → campos extraídos + métricas", "", 1.5, "P", "Vídeo"),
            b("T15", "LI05 LI07 LI02 LI04 LI03 VC05 V307 PC08", "Checkpoint 4 + brief de delegação: 'o Form Filler é do júnior' — escopo, critérios de pronto, pontos de verificação", "R1504", 1.5, "W", "docs/checkpoints/cp4.md + docs/lideranca/delegacao-form-filler.md"),
            flex("evals e análise de erros")],
       ])

# ---------------------------------------------------------------- Semana 17
semana(17, F3, "AI Form Filler II: human-in-the-loop e melhoria contínua",
       "Revisão humana integrada ao workflow; ciclo de feedback que melhora métricas de forma comprovada.",
       "Fila de revisão (workflow + console Next.js), análise de erros, PDF preenchido, trilha de auditoria.",
       "Métrica do eval melhora após ajustes (antes/depois documentado); e2e completo verde; release v0.6.",
       "Doc 'onde falhou, o que aprendi', revisão de PR do júnior #3.",
       False, [
           [b("T11", "VD01 EA15", "Anthropic: checkpoints humanos em agentes + Hamel: análise de erros", "R1106,R1104", 1, "E", "Notas"),
            b("T11", "VD01 VB10 VO01 VC05", "Fila de revisão humana: workflow aguarda sinal ReviewApproved/Corrected; timeout escala para Ops (view no Airtable)", "R506", 3, "P", "HITL no workflow")],
           [b("T12", "VC08 VR05 VS05 VS18 CO01", "Console de revisão (Next.js): campo + trecho de origem + confiança; correções salvas como feedback; login de staff (Cognito ou alternativa) com RBAC", "R1201,R1014", 4, "P", "Console funcionando")],
           [b("T11", "VD01 CQ05 CQ11", "Análise de erros das correções (top 5 modos de falha) → ajustes (prompt, regras, pós-processamento) → reexecutar evals", "R1104", 3, "P", "Antes/depois das métricas"),
            b("T15", "VD01 PC02 VQ04", "Doc 'Onde o AI Form Filler falhou, o que aprendi, como melhorei' (vira evidência para a candidatura)", "", 1, "W", "docs/form-filler-licoes.md")],
           [b("T11", "VS17 VB01 CO01 VC05", "Preencher o PDF-alvo com campos aprovados; envio para assinatura via PandaDoc sandbox (opcional) ou adapter fake; auditoria de quem aprovou", "R1013", 4, "P", "PDF preenchido + log de auditoria")],
           [b("T08", "CQ01 CQ04 VB09", "Testes e2e: intake → pagamento → extração → revisão → documento final; evals de regressão no CI", "", 3, "P", "e2e verde no CI"),
            b("T14", "VA06 VC02 LI10 CQ02", "AI-native lab: 'júnior + agente' geram um PR grande; exigir quebra em PRs pequenos, revisar e verificar de forma independente", "R1511", 1, "R", "agent-reviews")],
           [b("T11", "VD01 V301 CD06", "Release v0.6: Form Filler com revisão humana em prd (dados fictícios)", "", 1.5, "P", "Release notes"),
            b("T15", "CQ02 LI08 LI10 V314 LI03", "Simulação júnior #3: PR do júnior no Form Filler com erros plantados (PHI em log, limiar fixo no código, sem teste) — revisão + coaching", "R1503", 1.5, "W", "Revisão escrita"),
            flex("Next.js: formulários e estados de erro")],
       ])

# ---------------------------------------------------------------- Semana 18
semana(18, F4, "Observabilidade de ponta a ponta e SLOs",
       "Enxergar um caso atravessando todos os serviços; alertar pelo que importa ao negócio; testar capacidade.",
       "Tracing distribuído (HTTP + Pub/Sub + Temporal), SLOs com alertas de burn rate, dashboards, teste de carga.",
       "Trace de um caso em 5 serviços; bug sutil achado só com logs/traces; relatório de capacidade.",
       "Runbooks por alerta, relatório de confiabilidade.",
       False, [
           [b("T08", "VB18 CD10", "OpenTelemetry Go (getting started) + Cloud Trace overview", "R803,R810", 1.5, "E", "Notas"),
            b("T08", "VB18 VB19 EA08", "Tracing distribuído: HTTP + contexto propagado em atributos do Pub/Sub + interceptors do Temporal → Cloud Trace", "R803", 2.5, "P", "Trace ponta a ponta")],
           [b("T08", "CD11 VB09", "SRE Workbook: Implementing SLOs + Alerting on SLOs", "R802", 1, "E", "Notas"),
            b("T08", "CD11 CD10 VB18", "SLIs/SLOs: disponibilidade do intake, latência do checkout, tempo caso → Single Queue, lag do outbox; alertas por burn rate; dashboards", "R811", 3, "P", "SLOs + alertas")],
           [b("T08", "CD10 CQ06 VB18", "Métricas custom: profundidade da DLQ, compensações/dia, 429 do Airtable, falhas de extração; uptime checks", "R804", 3, "P", "Métricas no dashboard"),
            b("T15", "CD09 PC02 LI11", "Runbooks por alerta (significado, impacto, primeiros 5 min, escalonamento) como padrão do repositório", "R805", 1, "W", "docs/runbooks/alertas.md")],
           [b("T08", "CD10 VS06", "Google Skills: Monitor and Log with Google Cloud Observability (lab)", "R804", 1, "L", "Lab concluído"),
            b("T08", "VB19 CQ07 CQ09 VB20", "Debug em produção (staging): injetar bug sutil de timezone e achar só com logs/traces; documentar o caminho", "R809", 3, "P", "Relato do debug")],
           [b("T08", "EA07 CD02 DA01", "Escalabilidade: teste de carga no intake e no checkout; ajustar concorrência do Cloud Run, pool de conexões e índices; relatório de capacidade", "R203", 3, "P", "docs/capacidade.md"),
            b("T14", "VA06 VB20", "AI-native lab: agente analisa logs/traces exportados e propõe causa raiz; confirmar ou refutar com evidência", "R1402", 1, "R", "agent-reviews")],
           [b("T08", "VB18 V302", "Demo: trace de um caso em 5 serviços + painel de SLO", "", 1.5, "P", "Vídeo"),
            b("T15", "PC02 PC03 V305", "Update semanal + relatório técnico de confiabilidade (SLOs atuais, lacunas, próximos passos)", "R1501", 1.5, "W", "docs/relatorios/confiabilidade.md"),
            flex("observabilidade: queries de logs")],
       ])

# ---------------------------------------------------------------- Semana 19
semana(19, F4, "Dados: BigQuery, dbt, qualidade e BI",
       "Camada analítica confiável: eventos no BigQuery, marts testados, reconciliação e decisões com dados.",
       "Pub/Sub → BigQuery; dbt (staging → marts) com testes; dashboard Looker Studio; memo de decisão.",
       "Testes de qualidade verdes no CI; incidente de dados plantado detectado e corrigido.",
       "Contrato de dados, relatório para stakeholders.",
       False, [
           [b("T09", "DA02 VS10 DA08", "Google Skills: Derive Insights from BigQuery Data (labs)", "R901", 2, "L", "Labs concluídos"),
            b("T09", "DA02 DA06 VB05 CO01", "Assinatura Pub/Sub → BigQuery (eventos crus); dataset raw particionado; IDs pseudonimizados (sem PHI)", "R906", 2, "P", "Dataset raw recebendo eventos")],
           [b("T09", "DA09 DA11", "dbt Fundamentals (modelos, sources, testes)", "R903", 2, "L", "Módulos concluídos"),
            b("T09", "DA05 DA07 DA09 LT04", "dbt Core + BigQuery: staging → marts (funil de intake, pagamentos, tempo de ciclo, fila de Ops)", "R903", 2, "P", "analytics/ (dbt)")],
           [b("T09", "DA11 DA12 VB17", "Testes: unique, not_null, relationships, accepted_values, freshness + testes custom de reconciliação (Stripe × ledger × casos)", "R904", 3, "P", "dbt test verde no CI"),
            b("T15", "DA12 DA06 PC01", "Contrato de dados (eventos → BigQuery): donos, SLAs de frescor, mudanças compatíveis", "", 1, "W", "docs/contrato-de-dados.md")],
           [b("T09", "DA02 DA05", "Google Skills: Build a Data Warehouse with BigQuery (partições, JSON, arrays)", "R902", 1, "L", "Lab concluído"),
            b("T09", "DA08 DA10 DA07 VK03", "Dashboard Looker Studio (SLA/backlog de Ops, funil, receita) + memo com 3 recomendações baseadas em dados", "R901", 3, "P", "Dashboard + memo")],
           [b("T09", "DA13 VB20 VB21", "Incidente de dados plantado (duplicatas por replay): detectar pelo teste, RCA e correção sistêmica", "", 2, "P", "RCA"),
            b("T09", "DA03", "Snowflake (prioridade baixa): 'Snowflake in 20 minutes' + nota comparando com BigQuery", "R908", 1, "L", "Nota comparativa"),
            b("T14", "VA06 DA11", "AI-native lab: agente escreve modelos dbt; testes dbt + sua revisão de SQL (joins errados, grão)", "R1402", 1, "R", "agent-reviews")],
           [b("T09", "DA08 DA11", "Demo: dashboard + testes de qualidade verdes no CI", "", 1.5, "P", "Vídeo"),
            b("T15", "PC03 PC13 DA10", "Relatório para Growth/Ops: o que os dados dizem e suas limitações", "R1501", 1.5, "W", "docs/relatorios/dados-semana-19.md"),
            flex("SQL analítico")],
       ])

# ---------------------------------------------------------------- Semana 20
semana(20, F4, "Segurança e compliance estilo HIPAA + game day geral + Checkpoint 5",
       "Controles de dados sensíveis por padrão e resposta a incidente sozinho, com correções sistêmicas.",
       "Threat model, IAM mínimo, RBAC, trilha de auditoria, pseudonimização, guardrails de agentes para dados sensíveis.",
       "Auditoria de acesso demonstrada; game day resolvido com postmortem; checkpoint 5.",
       "Política de tratamento de dados, checklist de PR de dados sensíveis, postmortem.",
       True, [
           [b("T13", "CO01 VD04 VR07", "HHS: salvaguardas administrativas/técnicas da Security Rule + de-identificação", "R1301,R1302", 1.5, "E", "Notas"),
            b("T13", "CO01 VD04 EA04", "Threat model leve (STRIDE) do LeaveFlow; inventário de dados sensíveis por serviço; matriz de acesso por papel", "R1304", 2.5, "P", "docs/seguranca/threat-model.md")],
           [b("T13", "CO01 VD04 VR07 CD03", "Controles: IAM mínimo por serviço, RBAC no console, trilha de auditoria imutável (quem acessou qual caso, quando), Cloud Audit Logs de data access", "R1306", 4, "P", "Auditoria funcionando")],
           [b("T13", "CO01 DA12 VD04", "Rotação de segredos, retenção/expurgo de documentos, pseudonimização no BigQuery (SDP ou hash com sal), revisão OWASP API Top 10 (BOLA)", "R1305,R1304", 3, "P", "Correções + checklist"),
            b("T15", "CO01 LI11 VA03", "Política de tratamento de dados (1 página) + checklist de PR 'dados sensíveis' para júnior e agentes", "", 1, "W", "docs/seguranca/politica-dados.md")],
           [b("T08", "V303 CQ08 CQ06 VK06 VB16", "Game day geral: deploy ruim + DLQ crescendo + webhook do Stripe fora; detectar pelos alertas, mitigar (rollback), comunicar", "R805", 4, "P", "Timeline do incidente")],
           [b("T08", "VB21 V310 CQ11 CQ12 CQ05", "Correções sistêmicas (ex.: rollback automático, alerta faltante, teste ausente) + registro de defeitos classificado", "R806", 3, "P", "PRs das correções"),
            b("T14", "VA03 CO01", "AI-native lab: guardrails dos agentes para dados sensíveis (deny de paths/comandos, sem dados reais, sem segredos); testar violação", "R1407", 1, "R", "settings + teste de violação")],
           [b("T13", "VD04 CO01", "Demo: auditoria de acesso + incidente resolvido", "", 1.5, "P", "Vídeo"),
            b("T15", "PC08 CQ10 PC02 V306", "Checkpoint 5: Matriz, horas; postmortem do game day publicado; replanejar as 4 semanas finais", "R806", 1.5, "W", "docs/checkpoints/cp5.md + docs/postmortems/003.md"),
            flex("segurança: OWASP API")],
       ])

# ---------------------------------------------------------------- Semana 21
semana(21, F5, "Growth I: funil Next.js, experimento A/B e tracking",
       "Construir o funil e um experimento confiável com eventos client e server-side.",
       "web/: intake multi-etapas, página de preço com A/B, dataLayer → GTM → GA4, conversões server-side.",
       "Eventos no GA4 DebugView; purchase server-side deduplicado; variantes estáveis.",
       "Brief do experimento com Growth, alinhamento sobre limites de atribuição.",
       False, [
           [b("T12", "VS05 LT03 VR05", "Next.js Learn (App Router: rotas, server actions, data fetching)", "R1201", 2, "L", "Capítulos concluídos"),
            b("T12", "VC08 VS05 VB15 VG02", "web/: landing + intake multi-etapas (Server Actions → API de intake com idempotência por submission id) + página de preço", "R1201", 2, "P", "Funil navegável")],
           [b("T12", "VG02 VG05 DA10", "Kohavi caps. 1-3 (OEC, métricas guardrail, armadilhas)", "R1203", 1, "E", "Notas"),
            b("T12", "VG02 VG05 VC06", "A/B de apresentação de preço/checkout: bucketing determinístico por cookie (ou GrowthBook), exposição registrada, flag de desligar", "R1204", 3, "P", "Experimento ativo")],
           [b("T12", "VG03 VS24 VS25", "Plano de tracking → dataLayer → GTM → GA4 (sign_up, begin_checkout, purchase); consentimento básico", "R1202,R1205", 3, "P", "docs/tracking-plan.md + container GTM"),
            b("T15", "VG01 PC09 PC10 PC14 VL03", "Brief do experimento com Growth: hipótese, métrica primária, guardrails, tamanho de amostra, duração, critério de decisão", "R1203", 1, "W", "docs/growth/brief-exp-01.md")],
           [b("T12", "VG04 VS26 VS27", "GA4 Measurement Protocol + Meta CAPI (event_id para dedupe) + enhanced conversions (conceito)", "R1206,R1207,R1208", 1, "E", "Notas"),
            b("T12", "VG03 VG04 VS26 VS27 VB23", "Conversão server-side: PaymentConfirmed → purchase no GA4 (Measurement Protocol) e CAPI em modo teste com event_id compartilhado; UTMs/gclid persistidos no caso", "R1206", 3, "P", "Eventos server-side")],
           [b("T12", "VS22 VS21 VS20 VB07", "Ciclo de vida: evento no Klaviyo (conta grátis) ou adapter fake; formulário externo (Heyflow/Webflow) → webhook de intake idempotente", "R1209,R1211", 3, "P", "Integrações de growth"),
            b("T14", "VA06 VC08", "AI-native lab: agente implementa componente do funil; checar acessibilidade, eventos (debug do GTM) e testes", "R1402", 1, "R", "agent-reviews")],
           [b("T12", "VG03 VC06", "Demo: funil completo com variantes e eventos no GA4 DebugView", "", 1.5, "P", "Vídeo"),
            b("T15", "PC13 PC18 PC06 PC16 VG01", "Update semanal + alinhamento com o 'Head of Growth' sobre o que é confiável medir (limites de atribuição)", "R1509", 1.5, "W", "docs/updates/semana-21.md"),
            flex("TypeScript/React")],
       ])

# ---------------------------------------------------------------- Semana 22
semana(22, F5, "Growth II: análise do experimento, upsell e full stack",
       "Analisar com rigor, decidir com dados, comprar × construir; polir o full stack.",
       "Análise do experimento (SRM, IC), experimento de upsell, e2e Playwright, adapter Healthie/Cognito.",
       "Memo de decisão publicado; release v0.8 de Growth.",
       "Relatório do experimento, priorização de pedidos conflitantes Growth × Ops.",
       False, [
           [b("T09", "DA07 VS25 VG03", "BigQuery: análise de funil no dataset de exemplo do GA4", "R905", 2, "L", "sql/ga4-funil.sql"),
            b("T12", "DA10 VG02 VG05", "Simular tráfego do experimento → conversão por variante, SRM check, intervalo de confiança; memo de decisão", "R1203", 2, "P", "Memo de decisão")],
           [b("T12", "VS23 VB32", "VWO × GrowthBook × solução própria: quando comprar e quando construir", "R1210", 1, "E", "Nota de decisão"),
            b("T12", "VG02 VD02 VS15", "Experimento de upsell no checkout (add-on via price do Stripe) com guardrail de reembolso", "R1001", 3, "P", "Experimento de upsell")],
           [b("T12", "VR05 CQ01 VC08", "Polimento full stack: estados de erro, retries no cliente, loading, e-mails transacionais (fake), testes Playwright do funil", "", 3, "P", "e2e do funil verde"),
            b("T15", "PC03 PC04 DA10 VG01", "Relatório do experimento para stakeholders (decisão, aprendizado, próximo teste)", "R1501", 1, "W", "docs/growth/relatorio-exp-01.md")],
           [b("T10", "VS16 VS18 VB07 EA10", "Integrações opcionais: adapter de agendamento a partir da doc GraphQL do Healthie (com fake) + verificação de JWT do Cognito no backend", "R1012,R1014", 4, "P", "Adapters + testes")],
           [b("T09", "DA11 VG05 VB17", "Qualidade de dados de marketing: duplicidade client × server, eventos perdidos, reconciliação GA4 × pagamentos", "", 3, "P", "Relatório de qualidade"),
            b("T14", "VA05 VA01 V313 LI04", "AI-native lab: fluxo multiagente completo numa feature pequena (planner → implementer → reviewer → você aprova); medir tempo e defeitos", "R1406", 1, "R", "agent-reviews com métricas")],
           [b("T12", "VC06 V312", "Release v0.8 de Growth em prd", "", 1.5, "P", "Release notes"),
            b("T15", "LI06 PC17 PC18 VL03 PC11 PC09 PC10 PC12 PC14", "Simulação: pedidos conflitantes de Growth e Ops na mesma semana — priorização escrita com trade-offs e comunicação para ambos", "R1504", 1.5, "W", "docs/lideranca/priorizacao-01.md"),
            flex("full stack")],
       ])

# ---------------------------------------------------------------- Semana 23
semana(23, F5, "Avaliação de lacunas, correções sistêmicas e narrativa do sistema",
       "Fazer com o próprio projeto o que a vaga pede em 30/60 dias: avaliar lacunas, corrigir o mais importante e explicar o sistema.",
       "Avaliação de lacunas + 3 correções sistêmicas + doc/vídeo 'como um caso flui' + portfólio.",
       "Avaliação publicada; 3 correções em prd; walkthrough de 5 min; README de portfólio.",
       "Avaliação de lacunas, onboarding doc, retrospectiva.",
       False, [
           [b("T15", "V305 OP05 PC02 V311 VC03 EA14", "Avaliação de lacunas (formato da vaga): arquitetura, confiabilidade, execução; o que corrigir primeiro e por quê (impacto × esforço × risco)", "R1502", 2, "W", "docs/avaliacao-de-lacunas.md"),
            b("T08", "V308 VB21 CQ05", "Correção sistêmica #1 da avaliação", "", 2, "P", "PR + métrica")],
           [b("T08", "V308 V310 V313 CQ05 OP04 OP06 VK05", "Correções sistêmicas #2 e #3 (ex.: contract tests entre serviços, alerta de reconciliação que abre issue, script de onboarding)", "", 4, "P", "PRs + métricas")],
           [b("T06", "V302 VB01 EA04", "Doc 'Como um caso flui de ponta a ponta' (diagrama de sequência) + walkthrough gravado de 5 min", "", 3, "P", "docs/fluxo-do-caso.md + vídeo"),
            b("T15", "LI11 LI09 V314 PC01", "Onboarding doc para um júnior (setup, arquitetura, como contribuir, padrões de revisão)", "R1501", 1, "W", "docs/onboarding.md")],
           [b("T18", "EA04", "Hello Interview: framework de entrega de system design", "R1707", 1, "E", "Notas"),
            b("T18", "EA04 EA07 VB32", "Mock de system design gravado: 'projetar o LeaveFlow do zero' e 'sync com Airtable em escala'", "R1707", 3, "P", "2 gravações + autoavaliação")],
           [b("T01", "VC01 LT05 PC01 EA01", "Portfólio: README principal, diagramas, índice de ADRs, métricas (cobertura, SLOs, custo/mês), vídeo demo de 3 min", "", 3, "P", "README de portfólio"),
            b("T14", "VA02 VA03 VS30 V313", "AI-native lab: auditoria do próprio harness (CLAUDE.md/AGENTS.md, hooks, subagentes, testes de arquitetura) — o que mudou e por quê", "R1401", 1, "R", "docs/ai-harness-changelog.md")],
           [b("T15", "V315 V311 VK03", "3 oportunidades de alto valor não pedidas, com estimativa de impacto", "", 1.5, "W", "docs/propostas.md"),
            b("T15", "V316 PC03 VK01", "Update semanal + retrospectiva das 23 semanas (ciclos, releases, comunicação, accountability)", "", 1.5, "W", "docs/retro-final.md"),
            flex("o tópico com pior nível na Matriz")],
       ])

# ---------------------------------------------------------------- Semana 24
semana(24, F5, "Prontidão para candidatura + Checkpoint 6",
       "Fechar o projeto, finalizar respostas e vídeo, simular entrevistas e começar a aplicar para vagas intermediárias.",
       "LeaveFlow v1.0 com tag, custos desligados, portfólio publicado.",
       "7 respostas finais, vídeo Q5 ≤3 min, 3+ mocks feitos, 3-5 candidaturas piloto enviadas, checkpoint 6.",
       "Plano 30-60-90 pessoal, checkpoint 6, análise de distância atualizada.",
       True, [
           [b("T18", "VQ01 VQ02 VQ03 VQ04 VQ06 VQ07 VK04", "Respostas finais das 7 perguntas (aba Candidatura) com métricas reais do projeto", "R1704", 2, "W", "Respostas finais"),
            b("T18", "VK08 VK06 VK02 OP09 VR03", "Mercado: 20 vagas-alvo intermediárias, plataformas (Revelo, Strider), modelos de contratação (PJ/contractor × EOR), faixa salarial, fit com ritmo 60h+", "R1801,R1802", 2, "P", "docs/carreira/vagas-alvo.md")],
           [b("T18", "VR04 VB32 VR02", "Mock técnico de deep dive do projeto (gravado): idempotência, outbox, sagas, replay do Airtable", "", 2, "P", "Gravação + autoavaliação"),
            b("T14", "VQ07 VA01 VR08", "Doc 'How I use AI in engineering' com exemplos reais do repositório (diffs, revisões, falhas de agentes pegas)", "", 2, "W", "docs/how-i-use-ai.md")],
           [b("T18", "VQ03 VQ04 VQ06 VR06", "Mock comportamental (STAR) com par ou gravado: Q3, Q4, Q6 + liderança/mentoria", "R1704,R1706", 3, "P", "Gravação + notas"),
            b("T15", "V304 V309 OP05", "Plano 30-60-90 pessoal para uma vaga como esta (2 primeiras semanas em detalhe)", "", 1, "W", "docs/carreira/plano-30-60-90.md")],
           [b("T01", "CD06 CD08 LT06 VC01", "Fechamento técnico: congelar LeaveFlow v1.0 (tag, release notes) e desligar recursos pagos do GCP", "", 4, "P", "Tag v1.0 + custo zerado")],
           [b("T18", "VR03 VK08", "Candidaturas piloto: 3-5 vagas intermediárias + registro do feedback", "", 3, "P", "Planilha de candidaturas"),
            b("T14", "VA06 VA01 V313", "AI-native lab final cronometrado: feature nova planejada, delegada a agentes, verificada e entregue em 1h", "", 1, "R", "Relatório do exercício")],
           [b("T15", "PC08 VK01 VR01 V316", "Checkpoint 6 final: Matriz (nível final), análise de distância atualizada, plano dos próximos 3 meses", "", 1.5, "W", "docs/checkpoints/cp6.md"),
            b("T18", "PC01 VC01", "Publicar post técnico (blog/LinkedIn) sobre o projeto", "", 1.5, "W", "Link do post"),
            flex("buffer final: o que ficou pendente")],
       ])


# ---------------------------------------------------------------- Leitura dirigida
# 1h de leitura às quartas (semanas 3-22, exceto a 13, que já tem estudo na quarta): sai 1h do
# bloco de projeto de 3h da quarta. Mantém a teoria em dia com o que está sendo construído.
LEITURAS = {
    3: ("T08", "CQ01", "Leitura dirigida: Software Engineering at Google, caps. 11-12 (testing overview, unit testing)", "R808", "5 práticas de teste adotadas no projeto"),
    4: ("T04", "DA04 EA08", "Leitura dirigida: DDIA 2ª ed., capítulo de transações (ACID, isolamento fraco, lost update, write skew)", "R401", "Notas ligadas ao teste de lost update"),
    5: ("T08", "CD10 CD11", "Leitura dirigida: SRE book, 'Monitoring Distributed Systems' (quatro sinais de ouro)", "R801", "Lista de sinais por serviço"),
    6: ("T13", "CO01 EA11", "Leitura dirigida: OWASP API Security Top 10, API1-API5 (autorização e autenticação)", "R1304", "Checklist de API do projeto"),
    7: ("T06", "EA09 VB25", "Leitura dirigida: Learning DDD, agregados, eventos de domínio e modelagem tática", "R602", "Notas aplicadas ao agregado Case"),
    8: ("T04", "EA08 VB15", "Leitura dirigida: DDIA 2ª ed., processamento de streams (idempotência, exactly-once na prática)", "R401", "Notas ligadas ao consumidor idempotente"),
    9: ("T04", "EA08", "Leitura dirigida: DDIA 2ª ed., problemas de sistemas distribuídos (timeouts, relógios, falhas parciais)", "R401", "3 riscos para o CaseLifecycle"),
    10: ("T06", "VB23 VB25", "Leitura dirigida: Cosmic Python, eventos e message bus", "R601", "Comparação com a ponte Pub/Sub → Temporal"),
    11: ("T06", "VB24 VB31", "Leitura dirigida: DDD Reference, context mapping e anticorruption layer", "R606", "Desenho da ACL legado → domínio"),
    12: ("T10", "VB12 VS15", "Leitura dirigida: Stripe, 'Using webhooks with subscriptions'", "R1008", "Mapa evento → ação para a semana 13"),
    14: ("T10", "VO03 VS19", "Leitura dirigida: Airtable Webhooks API overview (preparo da semana 15)", "R1010", "Prós e contras × automações"),
    15: ("T08", "CQ10 V303", "Leitura dirigida: SRE book, 'Managing Incidents' e 'Postmortem Culture'", "R801", "Papéis de incidente aplicados ao game day"),
    16: ("T11", "EA15 VD01", "Leitura dirigida: Hamel Husain, evals (níveis de avaliação, análise de erros)", "R1104", "Plano de evals do Form Filler"),
    17: ("T15", "CQ02 LI10", "Leitura dirigida: Google eng-practices, guia de code review (padrão de revisão e comentários)", "R1511", "Checklist de revisão para o júnior"),
    18: ("T08", "EA07 VB16", "Leitura dirigida: SRE book, 'Handling Overload' e 'Addressing Cascading Failures'", "R801", "Riscos de sobrecarga do LeaveFlow"),
    19: ("T09", "DA12 VB17", "Leitura dirigida: SRE Workbook, 'Data Processing Pipelines'", "R802", "Riscos do pipeline de dados"),
    20: ("T13", "CO01 VD04", "Leitura dirigida: HHS, proposta de atualização da Security Rule (fact sheet) — o que pode mudar", "R1307", "Notas: impacto em logs, MFA e criptografia"),
    21: ("T12", "VG05 DA10", "Leitura dirigida: Kohavi, métricas e confiabilidade de experimentos (seleção de capítulos)", "R1203", "Métricas do experimento 01"),
    22: ("T12", "VG05", "Leitura dirigida: Kohavi, sample ratio mismatch e armadilhas de análise", "R1203", "Checklist de análise"),
}

for _s in SEMANAS:
    if _s["n"] in LEITURAS:
        _qua = _s["dias"][2]
        _proj = next(bl for bl in _qua if bl["modo"] == "P" and bl["horas"] >= 3)
        _proj["horas"] -= 1
        _t, _top, _ativ, _rec, _ent = LEITURAS[_s["n"]]
        _qua.insert(0, b(_t, _top, _ativ, _rec, 1, "E", _ent))


# ---------------------------------------------------------------- Inglês
# Semana 1: diagnóstico explícito. (tópicos, atividade, recursos, entregável)
INGLES_S1 = [
    ("ID01 VK07", "D17 (parte 1): EF SET de 50 min (leitura + escuta) → nível CEFR", "R1701", "Score/certificado EF SET"),
    ("ID01 VQ05", "D17 (parte 2): gravar 2 min explicando um projeto real (acoplamento de simuladores em HPC) sem roteiro; transcrever; contar palavras/min e muletas", "", "Vídeo + transcrição + rubrica"),
    ("ID01 VL02 VL04 PC05", "D17 (parte 3): amostra escrita — update diário + e-mail avisando atraso; autoavaliar clareza, gramática e concisão", "", "2 textos + rubrica"),
    ("ID01", "Escuta: 5 min de um episódio técnico; transcrever 1 min e medir precisão (%)", "R1709", "Transcrição + % de acerto"),
    ("ID01 VQ01", "Resposta oral não preparada à Q1 ('What interested you in this role?'), 2 min, gravada", "", "Gravação + 3 erros recorrentes"),
    ("ID01 VK07", "Consolidar o nível de inglês (D17) e definir metas de 24 semanas (palavras/min, muletas/min, CEFR alvo)", "", "Metas na aba Diagnóstico"),
]

# Semanas 2-24: (vocabulário, pergunta STAR, documento da semana, conversa/mock, vídeo)
INGLES = {
    2: ("carreira e apresentação pessoal", "VQ01", "design doc #1 do LeaveFlow", "self-mock: self-introduction de 60 s + 3 perguntas de follow-up", "Quem sou eu: formação, o projeto de HPC e por que backend event-driven"),
    3: ("APIs e bancos (endpoint, payload, schema, migration, constraint)", "VQ02", "design doc #2 (o legado)", "self-mock: explicar o sistema legado a um entrevistador", "O 'sistema legado' do LeaveFlow e suas dívidas"),
    4: ("concorrência e idempotência (race condition, retry, duplicate, lock)", "VQ07", "ADR-001 (idempotência)", "self-mock: 'What is idempotency and how did you implement it?'", "Idempotência explicada com o case-service"),
    5: ("deploy e infraestrutura (pipeline, rollout, rollback, staging, secret)", "VQ04", "runbook de release", "self-mock: walk-through do pipeline de CI/CD", "Meu pipeline do commit à produção"),
    6: ("integrações (webhook, signature, backoff, jitter, throttling)", "VQ06", "design doc #3 (padrão de integração)", "self-mock: 'How do you handle third-party API failures?'", "Como recebo webhooks com segurança"),
    7: ("DDD (bounded context, aggregate, invariant, ubiquitous language)", "VQ03", "ADR-003 (bounded contexts)", "self-mock: explicar o context map em 3 min", "Os bounded contexts do LeaveFlow"),
    8: ("mensageria (at-least-once, ack, dead-letter, ordering key, backlog)", "VQ05", "postmortem simulado #1", "self-mock: 'Explain the transactional outbox pattern'", "Outbox pattern em 2 minutos"),
    9: ("workflows (durable execution, signal, timer, activity, determinism)", "VQ01", "design doc #4 (CaseLifecycle)", "peer mock comportamental (Exponent Practice) ou self-mock", "Por que usar Temporal (e quando não usar)"),
    10: ("sagas e CQRS (compensation, read model, projection, rebuild)", "VQ02", "ADR-004 (CQRS onde paga)", "self-mock: 'Walk me through a saga failure'", "Saga com compensações no CaseLifecycle"),
    11: ("migração (backfill, cutover, shadow traffic, rollback, parity)", "VQ06", "plano da iniciativa de migração", "peer mock: 'Tell me about a large initiative you led'", "Migração lado a lado sem big-bang"),
    12: ("pagamentos (checkout, charge, refund, dispute, reconciliation)", "VQ04", "design doc #5 (pagamentos)", "self-mock: system design de checkout com webhooks", "Webhooks do Stripe: duplicados, ordem e assinatura"),
    13: ("assinaturas e finanças (subscription, dunning, proration, ledger, payout)", "VQ07", "runbook de discrepância de pagamento", "peer mock técnico", "Como reconcilio pagamentos"),
    14: ("operações (queue, SLA, backlog, handoff, workaround)", "VQ03", "ADR-005 (sync com Airtable)", "self-mock: 'How do you work with non-technical teams?'", "Single Queue no Airtable e rate limits"),
    15: ("recuperação (replay, conflict, source of truth, drift)", "VQ05", "runbook de recuperação caso a caso", "peer mock: incidente e postmortem", "Replay sem sobrescrever edições de Ops"),
    16: ("IA aplicada (extraction, schema, confidence, eval, ground truth)", "VQ01", "ADR-006 (Document AI × Gemini)", "self-mock: 'How do you evaluate an LLM feature?'", "AI Form Filler: extração e evals"),
    17: ("human-in-the-loop (review, override, feedback loop, failure mode)", "VQ02", "doc 'onde falhou, o que aprendi'", "peer mock: projeto com LLM", "HITL: onde falhou e como melhorei"),
    18: ("observabilidade (SLO, SLI, error budget, trace, span, burn rate)", "VQ04", "relatório de confiabilidade", "self-mock: debugging em produção", "SLOs e tracing de um caso"),
    19: ("dados (grain, freshness, lineage, data contract, dashboard)", "VQ06", "contrato de dados", "peer mock: SQL/analytics", "Qualidade de dados no LeaveFlow"),
    20: ("segurança (least privilege, audit trail, PHI, encryption, retention)", "VQ07", "política de tratamento de dados", "self-mock: 'How do you handle sensitive data?'", "Incidente simulado e postmortem"),
    21: ("growth (funnel, conversion, variant, guardrail metric, attribution)", "VQ03", "brief do experimento", "peer mock comportamental (STAR)", "Experimento A/B no funil"),
    22: ("experimentação (sample size, significance, SRM, novelty effect)", "VQ05", "relatório do experimento", "mock de system design (Hello Interview) + comportamental", "Tracking server-side e deduplicação"),
    23: ("liderança (delegation, ownership, trade-off, stakeholder, escalation)", "VQ04", "avaliação de lacunas", "mock de deep dive técnico do projeto + comportamental", "Versão candidata do vídeo Q5 (most challenging thing)"),
    24: ("entrevistas e negociação (compensation, contractor, overlap, availability)", "VQ05", "respostas finais das 7 perguntas", "mock final completo (comportamental + técnico) com par", "Vídeo final Q5 + pitch de 60 s"),
}


def ingles_da_semana(n):
    if n == 1:
        return INGLES_S1
    vocab, q, doc, mock, video = INGLES[n]
    update = " + 10 min: update diário em inglês (progresso / o que funciona / o que não funciona / próximos passos)"
    terca = (
        f"Simulação de entrevista extra (gravada, 30 min) sobre {vocab.split(' (')[0]} + revisão dos erros{update}"
        if n >= 21 else
        f"Escuta → fala: 20 min de episódio/talk técnico sobre {vocab.split(' (')[0]}; resumir em voz alta 2 min (gravado); anotar 5 expressões{update}"
    )
    return [
        ("ID01 VK07 PC05 VL02", f"Pronúncia e fluência: shadowing 20 min (Rachel's English) + 10 termos da semana no YouGlish — {vocab}{update}", "R1703,R1702", "Lista de termos + áudio de shadowing"),
        ("ID01 VK07 PC05", terca, "R1709" if n < 21 else "R1706", "Gravação + 5 expressões"),
        (f"ID01 {q} VL02", f"STAR: escrever/refinar a resposta {q[1:].replace('Q0', 'Q')} (≤250 palavras) e falar 3× cronometrado (alvo: 2 min){update}", "R1704,R1705", "Resposta revisada + melhor gravação"),
        ("ID01 PC01 VL01", f"Escrita técnica em inglês: {doc}, revisado com os princípios do Technical Writing One (frases curtas, voz ativa, termos consistentes){update}", "R1501", "Documento em inglês"),
        ("ID01 VK07", f"Conversação: {mock}; registrar 3 erros recorrentes{update}", "R1706", "Notas de erros"),
        ("ID01 VQ05 VK07", f"Vídeo semanal (2-3 min): {video}; autoavaliação com a rubrica (fluência, pronúncia, estrutura, vocabulário, tempo) e comparação com a semana anterior", "", "Vídeo + rubrica preenchida"),
    ]
