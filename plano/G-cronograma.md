<!-- Arquivo gerado por scripts/gerar.py — não edite à mão. -->

# G) Cronograma em formato de planilha

## Arquivos

| Aba pedida | CSV (colar no Sheets/Excel) | Linhas |
|---|---|---|
| Diagnóstico | [`01-diagnostico.csv`](../planilhas/01-diagnostico.csv) | 17 |
| Cronograma diário | [`02-cronograma-diario.csv`](../planilhas/02-cronograma-diario.csv) | 481 |
| Resumo semanal | [`03-resumo-semanal.csv`](../planilhas/03-resumo-semanal.csv) | 24 |
| Recursos | [`04-recursos.csv`](../planilhas/04-recursos.csv) | 146 |
| Matriz de cobertura | [`05-matriz-de-cobertura.csv`](../planilhas/05-matriz-de-cobertura.csv) | 238 |
| Candidatura | [`06-candidatura.csv`](../planilhas/06-candidatura.csv) | 22 |
| (extra) Horas por trilha | [`07-horas-por-trilha.csv`](../planilhas/07-horas-por-trilha.csv) | 20 |

Tudo junto, com abas, filtros, listas suspensas de Status/Nível e links clicáveis: [`planilhas/plano-de-estudos.xlsx`](../planilhas/plano-de-estudos.xlsx) (abre no Excel e no Google Sheets: Arquivo → Importar → Fazer upload).

**Para colar um CSV no Google Sheets:** Arquivo → Importar → Fazer upload → escolha o CSV → "Substituir planilha atual" ou "Inserir nova(s) página(s)"; separador: vírgula. No Excel: Dados → De Texto/CSV → codificação UTF-8. Os CSVs usam UTF-8 com BOM, então acentos abrem corretamente.

A coluna **Modo** (extra, no fim do cronograma) separa Estudo, Lab/exercício, Projeto, Escrita, Revisão de agente e Reforço flex; é ela que prova a regra de ≥50% de prática.

## Números do plano

- 24 semanas × 6 dias = 144 dias; 576 h técnicas + 144 h de inglês.
- Prática no tempo técnico: **84%** (laboratórios, projeto, escrita de artefatos e revisão de agentes; o reforço flex conta como 0%). Nenhuma semana fica abaixo de 50%.
- Liderança e comunicação (T15): 69 h = 12,0% do tempo técnico (alvo do pedido: ~10%; 10,8% nas semanas 3-22; as semanas 1, 2, 23 e 24 concentram diagnóstico, planejamento e avaliação de lacunas).
- Tópicos na matriz: 238, todos com pelo menos uma semana.
- **Horas por trilha contam a trilha principal de cada bloco.** Padrões de T02-T04 (SQL, idempotência, outbox, retries) também são praticados dentro de blocos de T05, T08, T09 e T10; a coluna 'Nº de blocos' da matriz mostra quantas vezes cada tópico aparece.

## Horas por trilha

| Trilha | Prioridade | Nível-alvo | Horas no plano | % do tempo técnico | Horas de prática | % prática na trilha |
|---|---|---|---|---|---|---|
| T00 Diagnóstico e setup | Essencial | — | 18 | 3,1% | 18 | 100% |
| T01 Linguagens e ferramentas (Go, Python, TypeScript, Git/GitHub) | Essencial (TypeScript: recomendado) | Go e Python: intermediário-avançado; TypeScript: intermediário; Git/GitHub: avançado | 30 | 5,2% | 27 | 90% |
| T02 Bancos de dados, SQL e modelagem (PostgreSQL) | Essencial | Intermediário-avançado | 15,5 | 2,7% | 14 | 90% |
| T03 APIs, webhooks e integrações (HTTP, idempotência, retries, rate limits) | Essencial | Avançado | 15,5 | 2,7% | 12 | 77% |
| T04 Sistemas distribuídos e arquitetura event-driven (Pub/Sub, outbox) | Essencial | Intermediário-avançado | 15,5 | 2,7% | 8,5 | 55% |
| T05 Orquestração de workflows (Temporal, sagas) | Essencial | Intermediário-avançado | 31 | 5,4% | 28,5 | 92% |
| T06 Arquitetura de domínio (DDD, Clean Architecture, CQRS, projeções, migração lado a lado) | Essencial | Intermediário-avançado (capaz de revisar) | 45,5 | 7,9% | 33,5 | 74% |
| T07 Cloud GCP e DevOps (Cloud Run, Cloud SQL, Cloud Build, CI/CD) | Essencial | Intermediário | 27 | 4,7% | 26 | 96% |
| T08 Confiabilidade, testes e observabilidade (SRE, incidentes, RCA) | Essencial | Intermediário-avançado | 65,5 | 11,4% | 58 | 89% |
| T09 Dados, analytics e qualidade (BigQuery, dbt, reconciliação, BI) | Essencial (BI e Snowflake: recomendado/baixa) | Intermediário | 36,5 | 6,3% | 35,5 | 97% |
| T10 Integrações do domínio (Stripe, Airtable; Healthie, PandaDoc, Cognito) | Essencial (Healthie, PandaDoc, Cognito: opcional) | Avançado em Stripe e Airtable; familiaridade nas demais | 53 | 9,2% | 43,5 | 82% |
| T11 IA aplicada (Document AI, Gemini, human-in-the-loop, evals) | Essencial (é o produto que o cargo lidera) | Intermediário | 27 | 4,7% | 24 | 89% |
| T12 Growth engineering e frontend (Next.js, A/B, tracking, anúncios) | Recomendado | Intermediário | 34 | 5,9% | 29 | 85% |
| T13 Segurança e compliance (estilo HIPAA, PHI, acesso, auditoria) | Essencial | Intermediário | 19,5 | 3,4% | 13 | 67% |
| T14 Engenharia AI-native (Claude Code, Codex, guardrails, testes de arquitetura, multiagente) | Essencial | Avançado | 29 | 5,0% | 29 | 100% |
| T15 Liderança, gestão de projetos e comunicação (~10% do tempo técnico) | Essencial | Intermediário (simulado) com evidência escrita | 69 | 12,0% | 67 | 97% |
| T16 Produto, operações e negócio (processos, automação de Ops, startup) | Recomendado | Intermediário | 4 | 0,7% | 1 | 25% |
| T17 Inglês técnico e entrevistas (1h/dia, fora das 4h técnicas) | Essencial | C1 funcional para entrevistas (meta a calibrar no diagnóstico) | 144 | fora das 4h | — | — |
| T18 Carreira e candidatura (semanas 23-24) | Essencial | Pronto para processos de vagas intermediárias | 17,5 | 3,0% | 16,5 | 94% |
| Reforço flex (alocado pelo diagnóstico) | — | — | 23 | 4,0% | — | — |

## Resumo semanal

| Semana | Tema | Marco do projeto | Critério de pronto | Artefatos de liderança | Checkpoint de revisão | % prática (técnico) |
|---|---|---|---|---|---|---|
| 1 | Diagnóstico I + setup do ambiente | Repositório 'leaveflow' criado (monorepo vazio com docs/), projeto GCP com alertas de orçamento. | 17 exercícios de diagnóstico feitos e registrados na aba Diagnóstico; plano ajustado v1 escrito. | Revisão de PR (D13), design doc de 1 página (D14), plano ajustado v1. | — | 92% |
| 2 | Diagnóstico complementar + fundamentos personalizados | Design doc #1 do LeaveFlow, glossário e context map preliminar. | Badge de Cloud Run iniciado/concluído, design doc #1 revisado, registro de riscos v0. | Design doc #1, registro de riscos, plano de comunicação. | — | 83% |
| 3 | Serviço 'legado' em Python + modelagem v1 + dados fictícios | intake-legacy (FastAPI + Postgres) com testes, rodando em Docker. | POST/GET de casos, migrações, seeds fictícios, cobertura ≥70%, logs sem PHI, docker compose up funcionando. | Design doc #2 (por que o legado é assim), retro + update semanal. | — | 77% |
| 4 | Go essencial + endpoint idempotente persistido + Checkpoint 1 | case-service v0 (Go) com POST idempotente persistido e GET paginado. | go test -race verde com 50 requisições concorrentes; ADR-001; demo de 3 min gravada. | ADR-001, checkpoint 1 (matriz + replanejamento). | Sim: Matriz + horas reais + replanejamento | 83% |
| 5 | CI/CD, Cloud Run, Cloud SQL, staging e produção | Pipeline Cloud Build: lint → testes → build → deploy staging; prd por tag com aprovação. | Release v0.1.0 em prd; rollback testado; ADR-002 (topologia); custo diário anotado. | ADR-002, runbook de release, update + registro de riscos. | — | 83% |
| 6 | APIs, webhooks e kit de integração + TypeScript | Kit de integração (Go e Python) + receptor de webhooks genérico + cliente TS gerado do OpenAPI. | Teste de caos com provedor fake (30% erros/429) sem efeitos duplicados; PR do júnior revisado. | Design doc #3 (padrão de integração), revisão de PR do júnior #1. | — | 77% |
| 7 | DDD estratégico/tático + Clean Architecture + testes de arquitetura | case-service reorganizado (domain/app/adapters) com agregado Case e eventos de domínio. | Context map + Bounded Context Canvas; testes de arquitetura quebrando o build em violação. | ADR-003 (limites e o que NÃO separar), 1:1 simulado com o júnior. | — | 73% |
| 8 | Transactional outbox + Pub/Sub + consumidores idempotentes + Checkpoint 2 | Outbox + relay (SKIP LOCKED) → Pub/Sub; consumidor idempotente; DLQ com CLI de reprocessamento. | Teste prova atomicidade (rollback não publica); poison message vai para DLQ; checkpoint 2 feito. | Postmortem simulado #1, checkpoint 2 com comunicação de risco. | Sim: Matriz + horas reais + replanejamento | 75% |
| 9 | Temporal: fundamentos e workflow CaseLifecycle v1 | orchestrator (Go) com CaseLifecycle v1 + ponte Pub/Sub → sinal; worker Python esqueleto. | Temporal 101/102 concluídos; testes de workflow e replay passando. | Design doc #4 (CaseLifecycle), plano quinzenal com trade-offs. | — | 88% |
| 10 | Sagas, CQRS e projeções; versionamento de workflows | Saga com compensações; projeções case_summary e ops_queue_view com rebuild; versionamento aplicado. | Teste de falha em cada passo da saga; rebuild = estado incremental; replay antes/depois do patch. | ADR-004 (CQRS onde paga), mensagem de desbloqueio ao júnior. | — | 81% |
| 11 | Migração do modelo legado para o novo, lado a lado | Legado emitindo eventos; backfill idempotente; comparador de paridade; roteamento por feature flag. | 100% em staging e 10% em prd com paridade ≥99% nos campos críticos; runbook de cutover/rollback ensaiado. | Plano de iniciativa grande (formato 60 dias), premortem, status report para stakeholders. | — | 85% |
| 12 | Stripe I: checkout, webhooks e PaymentConfirmed + Checkpoint 3 | billing (Go): Checkout Session, webhook assinado com inbox, PaymentConfirmed → saga. | Webhook duplicado não duplica efeito; evento fora de ordem tratado; estorno de teste na saga; checkpoint 3. | Design doc #5 (pagamentos e modos de falha), checkpoint 3. | Sim: Matriz + horas reais + replanejamento | 77% |
| 13 | Stripe II: assinaturas, dunning, portal, upsell e reconciliação | Ciclo de assinatura com test clocks, portal do cliente, add-on de upsell, job de reconciliação. | 3 discrepâncias plantadas detectadas e corrigidas; release v0.4 com pagamentos/assinaturas. | Runbook de discrepância, resposta ao pedido do Head of Growth. | — | 88% |
| 14 | Airtable I: observar Ops, Single Queue e projeção de saída | Base Single Queue + ops-sync (Python) projetando eventos com rate limit, validação e anexos. | Caso aparece na Single Queue com anexo em <1 min; burst de 200 casos respeita 5 req/s; mapeamento validado no CI. | Mapa as-is + job stories, ADR-005, mensagem de alinhamento com Ops. | — | 79% |
| 15 | Airtable II: mudanças de Ops, replays seguros e recuperação | Entrada via automação → endpoint assinado; propriedade por campo; CLI de replay; reconciliação diária. | Teste de edição concorrente passa; game day recuperado; release v0.5 com métrica antes/depois. | Runbook de recuperação, postmortem do game day com 3 correções sistêmicas. | — | 88% |
| 16 | AI Form Filler I: extração, evals e privacidade + Checkpoint 4 | form-filler (Python): extração A (Document AI) e B (Gemini) + harness de evals + activity no workflow. | Métricas por campo publicadas; fallback para revisão humana abaixo do limiar; checkpoint 4. | ADR-006, brief de delegação do Form Filler ao júnior, checkpoint 4. | Sim: Matriz + horas reais + replanejamento | 83% |
| 17 | AI Form Filler II: human-in-the-loop e melhoria contínua | Fila de revisão (workflow + console Next.js), análise de erros, PDF preenchido, trilha de auditoria. | Métrica do eval melhora após ajustes (antes/depois documentado); e2e completo verde; release v0.6. | Doc 'onde falhou, o que aprendi', revisão de PR do júnior #3. | — | 88% |
| 18 | Observabilidade de ponta a ponta e SLOs | Tracing distribuído (HTTP + Pub/Sub + Temporal), SLOs com alertas de burn rate, dashboards, teste de carga. | Trace de um caso em 5 serviços; bug sutil achado só com logs/traces; relatório de capacidade. | Runbooks por alerta, relatório de confiabilidade. | — | 81% |
| 19 | Dados: BigQuery, dbt, qualidade e BI | Pub/Sub → BigQuery; dbt (staging → marts) com testes; dashboard Looker Studio; memo de decisão. | Testes de qualidade verdes no CI; incidente de dados plantado detectado e corrigido. | Contrato de dados, relatório para stakeholders. | — | 92% |
| 20 | Segurança e compliance estilo HIPAA + game day geral + Checkpoint 5 | Threat model, IAM mínimo, RBAC, trilha de auditoria, pseudonimização, guardrails de agentes para dados sensíveis. | Auditoria de acesso demonstrada; game day resolvido com postmortem; checkpoint 5. | Política de tratamento de dados, checklist de PR de dados sensíveis, postmortem. | Sim: Matriz + horas reais + replanejamento | 85% |
| 21 | Growth I: funil Next.js, experimento A/B e tracking | web/: intake multi-etapas, página de preço com A/B, dataLayer → GTM → GA4, conversões server-side. | Eventos no GA4 DebugView; purchase server-side deduplicado; variantes estáveis. | Brief do experimento com Growth, alinhamento sobre limites de atribuição. | — | 83% |
| 22 | Growth II: análise do experimento, upsell e full stack | Análise do experimento (SRM, IC), experimento de upsell, e2e Playwright, adapter Healthie/Cognito. | Memo de decisão publicado; release v0.8 de Growth. | Relatório do experimento, priorização de pedidos conflitantes Growth × Ops. | — | 88% |
| 23 | Avaliação de lacunas, correções sistêmicas e narrativa do sistema | Avaliação de lacunas + 3 correções sistêmicas + doc/vídeo 'como um caso flui' + portfólio. | Avaliação publicada; 3 correções em prd; walkthrough de 5 min; README de portfólio. | Avaliação de lacunas, onboarding doc, retrospectiva. | — | 92% |
| 24 | Prontidão para candidatura + Checkpoint 6 | LeaveFlow v1.0 com tag, custos desligados, portfólio publicado. | 7 respostas finais, vídeo Q5 ≤3 min, 3+ mocks feitos, 3-5 candidaturas piloto enviadas, checkpoint 6. | Plano 30-60-90 pessoal, checkpoint 6, análise de distância atualizada. | Sim: Matriz + horas reais + replanejamento | 96% |
