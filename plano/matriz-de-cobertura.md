<!-- Arquivo gerado por scripts/gerar.py — não edite à mão. -->

# Matriz de cobertura

Todos os tópicos das seções 3 e 4 do pedido, um por linha: **98 itens da seção 4** (o pedido fala em 81, mas a lista colada tem 98; todos foram incluídos) e **140 da seção 3** (responsabilidades, padrões, Airtable, Growth, liderança, AI-native, 30-60-90, requisitos, diferenciais, cultura, stack e as 7 perguntas). As semanas são calculadas a partir do cronograma; o gerador falha se algum tópico ficar sem semana. Os níveis (diagnóstico, atual e por checkpoint) são preenchidos na planilha [`05-matriz-de-cobertura.csv`](../planilhas/05-matriz-de-cobertura.csv) ou na aba do XLSX.

| ID | Grupo | Tópico | Trilha | Prioridade | Diagnóstico | Semanas | Como será comprovado |
|---|---|---|---|---|---|---|---|
| LT01 | Linguagens e ferramentas | Python | T01 | Essencial | D01 | 1, 2, 3, 6, 7, 9, 11, 14, 16 | Serviços intake-legacy, ops-sync e form-filler no repositório + D01 refeito no CP |
| LT02 | Linguagens e ferramentas | Go | T01 | Essencial | D02 | 1, 2, 4, 6, 7, 8, 9, 10, 12 | case-service, billing e orchestrator no repositório + D02 refeito no CP |
| LT03 | Linguagens e ferramentas | TypeScript | T01 | Recomendado | D03 | 1, 2, 6, 17, 21 | App Next.js + cliente tipado gerado do OpenAPI |
| LT04 | Linguagens e ferramentas | SQL | T02 | Essencial | D04 | 1, 2, 3, 5, 6, 19 | Migrações, queries operacionais/analíticas e modelos dbt |
| LT05 | Linguagens e ferramentas | GitHub | T01 | Essencial | D05 | 1, 2, 6, 17, 20, 23 | PRs com template, checks obrigatórios, issues e board do projeto |
| LT06 | Linguagens e ferramentas | Controle de versão | T01 | Essencial | D05 | 1, 2, 3, 4, 24 | Histórico limpo, branches curtas, releases com tag e notas |
| LT07 | Linguagens e ferramentas | Agile | T15 | Recomendado | D05 | 1, 3 | Ciclos semanais (estilo Shape Up), board, retros e checkpoints |
| DA01 | Dados | PostgreSQL | T02 | Essencial | D04 | 1, 3, 4, 5, 6, 8, 18 | Schemas v1/v2, outbox, locks, índices e EXPLAIN no repositório |
| DA02 | Dados | BigQuery | T09 | Essencial | D06 | 1, 19, 20, 22 | Datasets raw/marts, assinatura Pub/Sub→BigQuery, queries versionadas |
| DA03 | Dados | Snowflake (prioridade baixa: não aparece na vaga) | T09 | Baixa | D06 | 19 | Lab 'Snowflake in 20 minutes' + nota comparando com BigQuery |
| DA04 | Dados | Sistemas de banco de dados | T02 | Essencial | D04 | 1, 2, 3, 4 | Notas de DDIA/Postgres + ADR de isolamento/concorrência |
| DA05 | Dados | Projetos de modelagem de dados | T02 | Essencial | D04 | 3, 10, 19 | ERD v1 (legado) × v2 (domínio) + modelo dimensional no dbt |
| DA06 | Dados | Integração de gestão de dados | T09 | Recomendado | D06 | 11, 19 | Pipelines Postgres/Stripe/eventos→BigQuery + contrato de dados |
| DA07 | Dados | Data analytics | T09 | Recomendado | D06 | 1, 6, 19, 22 | Análises de funil e tempo de ciclo em SQL |
| DA08 | Dados | Business intelligence | T09 | Recomendado | D06 | 19 | Dashboard Looker Studio de Ops/Growth |
| DA09 | Dados | Tecnologias de análise de dados | T09 | Recomendado | D06 | 19 | BigQuery + dbt + Looker Studio + export do GA4 |
| DA10 | Dados | Tomada de decisão orientada por dados | T09 | Recomendado | D06 | 16, 19, 21, 22 | Memos de decisão (experimento A/B, Form Filler, KPIs de Ops) |
| DA11 | Dados | Verificações de qualidade de dados | T09 | Essencial | D06 | 1, 10, 11, 13, 15, 19, 22 | Testes dbt + comparadores de paridade/reconciliação no CI |
| DA12 | Dados | Garantia da qualidade de dados | T09 | Essencial | D06 | 13, 14, 16, 19, 20 | Contratos de dados, validação estrita de mapeamentos, SLAs de frescor |
| DA13 | Dados | Solução de problemas de dados | T09 | Essencial | D06 | 3, 11, 13, 15, 19 | Runbook de discrepâncias + RCA de incidentes de dados plantados |
| EA01 | Engenharia e arquitetura | Engenharia de software | T06 | Essencial | D07 | 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23 | Projeto LeaveFlow completo (código, testes, docs, operação) |
| EA02 | Engenharia e arquitetura | Desenvolvimento de software | T01 | Essencial | D07 | 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22 | Entregas incrementais semanais com demo |
| EA03 | Engenharia e arquitetura | Implementação de software | T01 | Essencial | D07 | 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22 | Features em staging/prd com release notes |
| EA04 | Engenharia e arquitetura | Design de sistema | T04 | Essencial | D07 | 1, 7, 20, 23 | Design docs + diagramas C4/sequência + mocks de system design |
| EA05 | Engenharia e arquitetura | Design de aplicações | T06 | Essencial | D07 | 3, 4, 7 | Camadas Clean (domain/app/adapters) e APIs consistentes |
| EA06 | Engenharia e arquitetura | Design de sistemas para o desenvolvimento de sistemas | T06 | Essencial | D07 | 1, 2, 3, 6, 7, 9, 12 | Rastreabilidade design doc → ADR → PR → release |
| EA07 | Engenharia e arquitetura | Escalabilidade | T04 | Recomendado | D07 | 3, 18, 23 | Teste de carga + relatório de capacidade (Cloud Run, pool, índices) |
| EA08 | Engenharia e arquitetura | Sistemas distribuídos | T04 | Essencial | D08 | 1, 4, 8, 9, 18 | Outbox, Pub/Sub, consumidores idempotentes, sagas |
| EA09 | Engenharia e arquitetura | Design orientado ao domínio (DDD) | T06 | Essencial | D07 | 1, 2, 7 | Context map, Bounded Context Canvas, agregados e eventos |
| EA10 | Engenharia e arquitetura | Integração de sistemas | T10 | Essencial | D08 | 6, 11, 12, 15, 22 | Stripe, Airtable, Document AI/Gemini e legado integrados |
| EA11 | Engenharia e arquitetura | Integrações de API | T03 | Essencial | D08 | 4, 6 | Kit de integração (timeouts, retries, rate limit, assinatura) |
| EA12 | Engenharia e arquitetura | Implementação do ciclo de vida do desenvolvimento de software (SDLC) | T07 | Essencial | D09 | 3, 5 | Fluxo design→PR→CI→staging→prd→monitoramento documentado |
| EA13 | Engenharia e arquitetura | Participação na fase de engenharia | T15 | Recomendado | D07 | 4, 5, 7, 8, 10, 11, 14, 16, 23 | Design reviews escritos (ADRs) antes de implementar |
| EA14 | Engenharia e arquitetura | Engenharia de projetos | T15 | Recomendado | D14 | 2, 11, 23 | Plano da iniciativa de migração executado até produção |
| EA15 | Engenharia e arquitetura | Aplicações de IA | T11 | Essencial | D15 | 16, 17 | AI Form Filler com evals e revisão humana |
| CD01 | Cloud, DevOps e operação | Sistemas baseados em nuvem | T07 | Essencial | D09 | 1, 2, 5 | LeaveFlow rodando no GCP (staging/prd) |
| CD02 | Cloud, DevOps e operação | Serviços serverless em nuvem | T07 | Essencial | D09 | 1, 2, 5, 11, 13, 18 | Serviços e jobs no Cloud Run; badge de Cloud Run |
| CD03 | Cloud, DevOps e operação | Engenharia de soluções em nuvem | T07 | Recomendado | D09 | 5, 8, 20 | ADRs de arquitetura GCP com custo e trade-offs |
| CD04 | Cloud, DevOps e operação | Automação de DevOps | T07 | Essencial | D09 | 5, 8 | cloudbuild.yaml + infraestrutura reprodutível (gcloud/Terraform) |
| CD05 | Cloud, DevOps e operação | Implementação de entrega contínua (CD) | T07 | Essencial | D09 | 5 | Deploy automático em staging e por tag em prd |
| CD06 | Cloud, DevOps e operação | Implantação de sistemas | T07 | Essencial | D09 | 1, 5, 11, 13, 15, 17, 22, 24 | Releases versionadas com rollback por revisão |
| CD07 | Cloud, DevOps e operação | Implantação de aplicações | T07 | Essencial | D09 | 3, 5, 10 | Deploy de serviços Go/Python/Next.js |
| CD08 | Cloud, DevOps e operação | Manutenção de aplicações | T08 | Recomendado | D09 | 10, 11, 24 | Versionamento de workflows, migrações expand/contract, dependências |
| CD09 | Cloud, DevOps e operação | Suporte a sistemas e aplicações | T08 | Essencial | D10 | 1, 5, 11, 13, 15, 18 | Runbooks por alerta e de recuperação caso a caso |
| CD10 | Cloud, DevOps e operação | Monitoramento em nuvem | T08 | Essencial | D09 | 5, 12, 14, 18 | Cloud Monitoring/Logging/Trace configurados |
| CD11 | Cloud, DevOps e operação | Monitoramento de sistemas de TI | T08 | Essencial | D09 | 5, 18 | SLOs, alertas por burn rate e uptime checks |
| CQ01 | Confiabilidade e qualidade | Teste de software | T08 | Essencial | D10 | 3, 4, 6, 8, 9, 12, 17, 22 | Unitários, integração (Testcontainers), contrato, e2e, replay |
| CQ02 | Confiabilidade e qualidade | Feedback sobre código | T15 | Essencial | D13 | 1, 2, 3, 4, 6, 12, 17 | Revisões escritas dos PRs simulados do júnior e dos agentes |
| CQ03 | Confiabilidade e qualidade | Revisão de garantia da qualidade | T08 | Recomendado | D10 | 5, 11, 13, 15, 17, 22 | Checklist de release/QA aplicado em cada release |
| CQ04 | Confiabilidade e qualidade | Operações de controle de qualidade | T08 | Recomendado | D10 | 2, 7, 14, 17 | Gates de CI (lint, testes, arquitetura, evals, contratos) |
| CQ05 | Confiabilidade e qualidade | Melhoria da qualidade | T08 | Recomendado | D10 | 10, 17, 20, 23 | Métricas antes/depois das correções sistêmicas |
| CQ06 | Confiabilidade e qualidade | Identificação de problemas | T08 | Essencial | D10 | 5, 18, 20 | Alertas que detectam as falhas dos game days |
| CQ07 | Confiabilidade e qualidade | Identificação de problemas de software | T08 | Essencial | D10 | 3, 18 | Debug guiado por logs/traces documentado |
| CQ08 | Confiabilidade e qualidade | Diagnóstico e solução de problemas | T08 | Essencial | D10 | 6, 11, 15, 20 | Game days com timeline e mitigação |
| CQ09 | Confiabilidade e qualidade | Solução de problemas técnicos | T08 | Essencial | D10 | 1, 8, 13, 18 | Incidentes plantados resolvidos (DLQ, reconciliação, timezone) |
| CQ10 | Confiabilidade e qualidade | Análise de falhas | T08 | Essencial | D10 | 1, 8, 15, 20 | Postmortems blameless publicados |
| CQ11 | Confiabilidade e qualidade | Análise de defeitos | T08 | Recomendado | D10 | 17, 20 | Registro e classificação de defeitos + análise de erros do Form Filler |
| CQ12 | Confiabilidade e qualidade | Registro de problemas | T08 | Recomendado | D10 | 1, 20 | Issue tracker/incident log mantidos no repositório |
| CO01 | Compliance | Tratamento de informações confidenciais | T13 | Essencial | D11 | 1, 3, 5, 6, 12, 13, 16, 17, 19, 20 | Classificação de dados, logs sem PHI, RBAC, auditoria, retenção |
| OP01 | Operações e negócio | Gestão do fluxo de trabalho de operações | T16 | Essencial | D12 | 1, 14 | Single Queue no Airtable com views por fila/SLA |
| OP02 | Operações e negócio | Desenho de processos | T16 | Recomendado | D12 | 1, 2, 14 | Mapas de processo as-is/to-be |
| OP03 | Operações e negócio | Melhorias em processos empresariais | T16 | Recomendado | D12 | 14, 15 | Automação com métrica de tempo manual antes/depois |
| OP04 | Operações e negócio | Iniciativas de excelência operacional | T16 | Recomendado | D12 | 15, 23 | Redução de falhas recorrentes após game days |
| OP05 | Operações e negócio | Planejamento de ações estratégicas | T15 | Recomendado | D14 | 1, 4, 11, 23, 24 | Plano ajustado pós-diagnóstico, avaliação de lacunas, plano 30-60-90 |
| OP06 | Operações e negócio | Implementação de iniciativas estratégicas | T15 | Recomendado | D14 | 11, 23 | Iniciativa de migração entregue |
| OP07 | Operações e negócio | Tomada de decisão | T15 | Essencial | D14 | 4, 5, 7, 8, 10, 11, 14, 16, 23 | ADRs com alternativas e trade-offs |
| OP08 | Operações e negócio | Gerenciamento de riscos do projeto | T15 | Essencial | D14 | 2, 5, 11 | Registro de riscos + premortem + comunicação de risco |
| OP09 | Operações e negócio | Experiência em startups | T16 | Essencial | D12 | 1, 2, 24 | Simulada (ritmo semanal, cortes de escopo); lacuna real tratada em H |
| LI01 | Liderança | Liderança | T15 | Essencial | D13 | 1, 2, 6, 7, 10, 16, 17, 20, 23 | Artefatos de liderança semanais + simulações |
| LI02 | Liderança | Liderança de equipe | T15 | Essencial | D13 | 1, 2, 6, 7, 10, 16, 17, 20, 23 | Brief de delegação e acompanhamento do 'júnior' |
| LI03 | Liderança | Liderança em melhoria de desempenho | T15 | Recomendado | D13 | 7, 16, 17 | Plano de crescimento do júnior simulado |
| LI04 | Liderança | Coordenação de equipe | T15 | Recomendado | D13 | 16, 22 | Coordenação humano+agentes em fluxo multiagente |
| LI05 | Liderança | Atribuição de tarefas | T15 | Essencial | D13 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24 | Briefs de tarefa com critérios de pronto |
| LI06 | Liderança | Priorização de tarefas | T15 | Essencial | D14 | 1, 4, 9, 12, 22 | Replanejamentos nos checkpoints com cortes explícitos |
| LI07 | Liderança | Delegação | T15 | Essencial | D13 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24 | Delegação do Form Filler (júnior) e de tarefas a agentes |
| LI08 | Liderança | Coaching | T15 | Recomendado | D13 | 6, 7, 10, 17 | Mensagens de desbloqueio com perguntas de coaching |
| LI09 | Liderança | Mentoria | T15 | Recomendado | D13 | 10, 23 | Onboarding doc + (real) mentoria de aluno/colega do CIn |
| LI10 | Liderança | Mentoria para colaboradores juniores | T15 | Essencial | D13 | 1, 6, 7, 10, 17 | Revisões didáticas de PR + roteiros de 1:1 |
| LI11 | Liderança | Treinamento e mentoria da equipe | T15 | Recomendado | D13 | 6, 18, 20, 23 | Docs de padrão (integração, runbooks, dados sensíveis) |
| PC01 | Gestão de projetos e comunicação | Escrita técnica | T15 | Essencial | D14 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24 | Design docs, ADRs, runbooks, README |
| PC02 | Gestão de projetos e comunicação | Elaboração de relatórios técnicos | T15 | Essencial | D14 | 1, 5, 8, 13, 15, 17, 18, 20, 23 | Postmortems, relatório de confiabilidade, avaliação de lacunas |
| PC03 | Gestão de projetos e comunicação | Relatórios para partes interessadas | T15 | Essencial | D14 | 3, 4, 5, 8, 9, 12, 14, 16, 18, 19, 20, 21, 22, 23, 24 | Update semanal para 'CEO'/liderança |
| PC04 | Gestão de projetos e comunicação | Relatórios para partes interessadas do projeto | T15 | Recomendado | D14 | 11, 22 | Status report da iniciativa de migração |
| PC05 | Gestão de projetos e comunicação | Comunicação interna | T15 | Essencial | D14 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24 | Updates diários escritos (em inglês) |
| PC06 | Gestão de projetos e comunicação | Gerenciamento da comunicação do projeto | T15 | Recomendado | D14 | 2, 14, 21 | Plano de comunicação (quem, o quê, quando) |
| PC07 | Gestão de projetos e comunicação | Acompanhamento do progresso de projetos | T15 | Essencial | D14 | 3, 4, 5, 8, 9, 12, 14, 16, 18, 20, 21, 23, 24 | Coluna Status + board + demos semanais |
| PC08 | Gestão de projetos e comunicação | Acompanhamento do cronograma do projeto | T15 | Essencial | D14 | 1, 3, 4, 8, 12, 16, 20, 24 | Checkpoints a cada 4 semanas com horas reais × plano |
| PC09 | Gestão de projetos e comunicação | Coordenação multidisciplinar de projetos | T15 | Recomendado | D14 | 13, 21, 22 | Brief de experimento Eng+Growth+Ops |
| PC10 | Gestão de projetos e comunicação | Colaboração multidisciplinar | T15 | Recomendado | D14 | 13, 21, 22 | Simulações com Growth e Ops |
| PC11 | Gestão de projetos e comunicação | Colaboração multifuncional | T15 | Recomendado | D14 | 13, 22 | Priorização de pedidos conflitantes Growth × Ops |
| PC12 | Gestão de projetos e comunicação | Articulação com departamentos internos | T15 | Recomendado | D14 | 14, 22 | Alinhamento com Ops sobre mudanças no dia a dia |
| PC13 | Gestão de projetos e comunicação | Interface com stakeholders | T15 | Essencial | D14 | 13, 19, 21 | Respostas escritas a pedidos de Growth/Ops |
| PC14 | Gestão de projetos e comunicação | Colaboração com partes interessadas | T15 | Recomendado | D14 | 13, 21, 22 | Brief do experimento construído com Growth |
| PC15 | Gestão de projetos e comunicação | Comunicação com partes interessadas do projeto | T15 | Essencial | D14 | 5, 11, 15 | Comunicação de riscos e incidentes |
| PC16 | Gestão de projetos e comunicação | Construção de relacionamentos com partes interessadas | T15 | Recomendado | D14 | 14, 21 | Rotina com 'clientes internos' (Ops/Growth) |
| PC17 | Gestão de projetos e comunicação | Gestão de partes interessadas | T15 | Recomendado | D14 | 2, 11, 22 | Mapa de stakeholders e plano de comunicação |
| PC18 | Gestão de projetos e comunicação | Gestão de expectativas de partes interessadas | T15 | Essencial | D14 | 8, 13, 14, 21, 22 | Mensagens de atraso/escopo no formato da vaga |
| ID01 | Idioma | Inglês | T17 | Essencial | D17 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24 | Vídeos semanais, EF SET inicial/final, mocks, docs em inglês |
| VC01 | Natureza do cargo | Ciclo completo: build, debug, design, review, ship (90% construção) | T01 | Essencial | D07 | 4, 5, 7, 8, 9, 10, 12, 23, 24 | Demos e releases semanais do LeaveFlow |
| VC02 | Natureza do cargo | Gerenciar diretamente um engenheiro júnior (prioridades, revisão, desbloqueio) | T15 | Essencial | D13 | 1, 2, 6, 7, 10, 16, 17, 20, 23 | Simulações de júnior (PRs, 1:1, desbloqueio, delegação) |
| VC03 | Natureza do cargo | Dono da execução de engenharia de ponta a ponta (prioridades vêm da liderança) | T15 | Essencial | D14 | 9, 23 | Planos semanais derivados de 'prioridades de negócio' simuladas |
| VC04 | Natureza do cargo | Responsável por backend, orquestração de workflows, integrações e confiabilidade | T04 | Essencial | D08 | 5, 6 | Serviços backend + Temporal + integrações + SLOs |
| VC05 | Natureza do cargo | Dono do AI Form Filler (liderando o júnior responsável) | T11 | Essencial | D15 | 16, 17 | Form Filler + brief de delegação + revisões |
| VC06 | Natureza do cargo | Parceria com Growth (experimentos) | T12 | Essencial | D16 | 13, 21, 22 | Experimentos de preço/upsell e brief com Growth |
| VC07 | Natureza do cargo | Parceria com Operations (automação) | T16 | Essencial | D12 | 14 | Single Queue e automações com Ops como cliente |
| VC08 | Natureza do cargo | Entrar no frontend quando necessário | T12 | Recomendado | D16 | 17, 21, 22 | Funil Next.js e console de revisão |
| VC09 | Natureza do cargo | Impacto no negócio > sofisticação: solução confiável mais simples, entregue rápido | T15 | Essencial | D07 | 7, 10 | ADRs 'quando NÃO usar' e cortes de escopo |
| VB01 | Backend Systems & Reliability | Backend conecta intake, pagamentos, agendamento, operações clínicas, documentação médica, marketing de ciclo de vida e analytics | T06 | Essencial | D07 | 1, 3, 7, 17, 23 | Context map + fluxo de caso ponta a ponta |
| VB02 | Backend Systems & Reliability | ~9 serviços poliglotas no Cloud Run (Go, Python, TypeScript) | T07 | Essencial | D09 | 5, 8, 9 | 6-7 serviços Go/Python/TS no Cloud Run |
| VB03 | Backend Systems & Reliability | Workflows event-driven com Pub/Sub + Temporal Cloud | T05 | Essencial | D08 | 8, 9, 10, 12 | Ponte Pub/Sub → sinais do Temporal |
| VB04 | Backend Systems & Reliability | Duas instâncias Cloud SQL PostgreSQL | T07 | Recomendado | D09 | 5 | ADR de topologia Cloud SQL (custo × isolamento) |
| VB05 | Backend Systems & Reliability | BigQuery como camada analítica | T09 | Essencial | D06 | 1, 19, 20, 22 | Datasets e marts no BigQuery |
| VB06 | Backend Systems & Reliability | Ambientes de staging e produção por serviço | T07 | Essencial | D09 | 5 | Pipelines com staging automático e prd por tag |
| VB07 | Backend Systems & Reliability | 20+ integrações de terceiros | T10 | Essencial | D08 | 6, 14, 21, 22 | Kit de integração reutilizado por todas as integrações |
| VB08 | Backend Systems & Reliability | Features que falham com segurança (fail-safe) | T08 | Essencial | D10 | 5, 6, 9, 11, 12, 16 | Design docs com modos de falha + flags de desligamento |
| VB09 | Backend Systems & Reliability | Testes, monitoramento e CI/CD como salvaguardas contra falhas sistêmicas | T08 | Essencial | D10 | 5, 17, 18 | Gates de CI + alertas + rollback |
| VB10 | Backend Systems & Reliability | Orquestração de workflows | T05 | Essencial | D08 | 8, 9, 10, 16, 17 | Workflow CaseLifecycle |
| VB11 | Backend Systems & Reliability | APIs | T03 | Essencial | D02 | 4, 6 | APIs REST com OpenAPI, erros padronizados e paginação |
| VB12 | Backend Systems & Reliability | Pagamentos | T10 | Essencial | D08 | 10, 12, 13 | Integração Stripe (checkout, assinatura, estorno) |
| VB13 | Backend Systems & Reliability | Gestão de estado | T06 | Essencial | D07 | 3, 4, 7, 8, 9, 13, 15 | Máquina de estados do agregado + estado do workflow |
| VB14 | Backend Systems & Reliability | Retries | T03 | Essencial | D08 | 4, 6, 8, 9, 14 | Retries com backoff+jitter só em operações idempotentes |
| VB15 | Backend Systems & Reliability | Idempotência | T03 | Essencial | D02 | 1, 4, 6, 8, 9, 10, 11, 12, 14, 15, 21 | Idempotency keys, inbox, dedupe por event id |
| VB16 | Backend Systems & Reliability | Recuperação de falhas | T08 | Essencial | D08 | 6, 8, 10, 11, 12, 15, 18, 20 | DLQ, replay, compensações, game days |
| VB17 | Backend Systems & Reliability | Reconciliação de dados | T09 | Essencial | D06 | 11, 13, 15, 19, 22 | Jobs de reconciliação Stripe/Airtable/legado |
| VB18 | Backend Systems & Reliability | Observabilidade | T08 | Essencial | D10 | 3, 5, 12, 14, 18 | Logs estruturados, métricas, tracing distribuído |
| VB19 | Backend Systems & Reliability | Debugging em produção | T08 | Essencial | D10 | 13, 18 | Exercício de debug só com logs/traces |
| VB20 | Backend Systems & Reliability | Root-cause analysis | T08 | Essencial | D10 | 1, 8, 13, 18, 19 | RCAs em postmortems e incidentes de dados |
| VB21 | Backend Systems & Reliability | Correções sistêmicas | T08 | Essencial | D10 | 8, 15, 19, 20, 23 | Ações sistêmicas implementadas após cada incidente |
| VB22 | Backend Systems & Reliability | Automação: substituir workflows operacionais manuais por sistemas confiáveis | T16 | Essencial | D12 | 15 | Automações Airtable↔backend com métricas |
| VB23 | Backend Systems & Reliability | Arquitetura event-driven com 20+ integrações | T04 | Essencial | D08 | 6, 7, 8, 9, 10, 21 | Eventos versionados + integrações por eventos |
| VB24 | Backend Systems & Reliability | Migração de modelo legado para novo modelo de domínio, lado a lado em produção | T06 | Essencial | D08 | 11 | Strangler fig com backfill, shadow read e cutover por coorte |
| VB25 | Backend Systems & Reliability | DDD (padrão do código) | T06 | Essencial | D07 | 2, 3, 7, 10 | Agregados, value objects e eventos de domínio |
| VB26 | Backend Systems & Reliability | Clean Architecture | T06 | Essencial | D07 | 7 | Camadas + testes de arquitetura |
| VB27 | Backend Systems & Reliability | CQRS | T06 | Essencial | D07 | 7, 10 | Commands × queries separados onde paga |
| VB28 | Backend Systems & Reliability | Sagas no Temporal | T05 | Essencial | D08 | 1, 8, 10, 12 | Saga com compensações LIFO testadas |
| VB29 | Backend Systems & Reliability | Transactional outbox | T04 | Essencial | D08 | 1, 8, 11, 12 | Outbox + relay com SKIP LOCKED |
| VB30 | Backend Systems & Reliability | Projeções | T06 | Essencial | D07 | 10 | Read models com rebuild por replay |
| VB31 | Backend Systems & Reliability | Bounded contexts bem definidos | T06 | Essencial | D07 | 2, 7, 11 | Context map + canvases |
| VB32 | Backend Systems & Reliability | Revisar trabalho com base nesses padrões e saber quando a solução mais simples é a certa | T06 | Essencial | D07 | 6, 7, 10, 11, 14, 16, 22, 23, 24 | ADRs de simplicidade + revisões de PR |
| VO01 | Operations Systems (Airtable) | Airtable como sistema operacional do time de Operations | T10 | Essencial | D12 | 14, 17 | Base Single Queue desenhada com Ops como cliente |
| VO02 | Operations Systems (Airtable) | Projeção de cada caso na Single Queue | T10 | Essencial | D08 | 14 | ops-sync projeta eventos → registros |
| VO03 | Operations Systems (Airtable) | Consumir de volta no backend as mudanças de Ops via automações do Airtable | T10 | Essencial | D08 | 14, 15 | Automação 'Run a script' → endpoint assinado |
| VO04 | Operations Systems (Airtable) | Mapeamentos de campos | T10 | Essencial | D08 | 14 | Spec de mapeamento versionada + validação |
| VO05 | Operations Systems (Airtable) | Rate limits | T10 | Essencial | D08 | 14 | Token bucket 5 req/s/base, lotes de 10, backoff em 429 |
| VO06 | Operations Systems (Airtable) | Anexos | T10 | Essencial | D08 | 14 | Upload de PDFs idempotente |
| VO07 | Operations Systems (Airtable) | Replay de eventos sem sobrescrever edições manuais de Ops | T10 | Essencial | D08 | 15 | Propriedade por campo + replay com dry-run |
| VO08 | Operations Systems (Airtable) | Recuperação de dados caso a caso | T10 | Essencial | D10 | 15 | CLI de replay por caso + runbook |
| VO09 | Operations Systems (Airtable) | Integridade de campo: um campo errado gera um caso errado | T10 | Essencial | D11 | 14, 15 | Testes de contrato que quebram o build |
| VG01 | Growth Enablement | Parceria com Head of Growth e Frontend Growth Engineer | T12 | Recomendado | D16 | 13, 21, 22 | Briefs e relatórios de experimento |
| VG02 | Growth Enablement | Experimentos de funil, preço, checkout, assinatura e upsell | T12 | Recomendado | D16 | 13, 21, 22 | Experimentos A/B de preço e upsell |
| VG03 | Growth Enablement | Analytics e conversion tracking | T12 | Recomendado | D16 | 1, 21, 22 | Plano de tracking + GA4/GTM |
| VG04 | Growth Enablement | Instrumentação de canais de anúncios | T12 | Recomendado | D16 | 21 | Conversões server-side (GA4 MP, Meta CAPI, Google Ads) |
| VG05 | Growth Enablement | Infraestrutura para testar, aprender e entregar com dados confiáveis | T12 | Recomendado | D16 | 21, 22 | Bucketing determinístico, SRM check, reconciliação de eventos |
| VL01 | Engineering Leadership | Documentar problema, abordagem e plano antes de implementar | T15 | Essencial | D14 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24 | Design docs antes de cada fase |
| VL02 | Engineering Leadership | Update diário conciso (progresso, funciona, não funciona, próximos passos) | T15 | Essencial | D14 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24 | Updates diários em inglês |
| VL03 | Engineering Leadership | Prioridades de negócio → planos técnicos simples com trade-offs (velocidade, escopo, qualidade) | T15 | Essencial | D14 | 4, 7, 9, 13, 21, 22 | Planos quinzenais com trade-offs explícitos |
| VL04 | Engineering Leadership | Compromissos realistas e aviso precoce de risco (o que aconteceu, o que muda, novo prazo) | T15 | Essencial | D14 | 1, 4, 8, 11, 12 | Mensagens de risco nos checkpoints |
| VA01 | AI-Native Engineering | Entrega via sessões supervisionadas de Claude Code e Codex | T14 | Essencial | D15 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24 | Log de sessões e revisões de agentes |
| VA02 | AI-Native Engineering | Regras no nível do repositório | T14 | Essencial | D15 | 1, 5, 6, 9, 23 | CLAUDE.md/AGENTS.md versionados com changelog |
| VA03 | AI-Native Engineering | Guardrails | T14 | Essencial | D15 | 2, 5, 7, 9, 15, 16, 20, 23 | Permissões, hooks, deny lists e evals como gate |
| VA04 | AI-Native Engineering | Testes de arquitetura | T14 | Essencial | D15 | 7 | go-arch-lint / import-linter / dependency-cruiser no CI |
| VA05 | AI-Native Engineering | Fluxos multiagente | T14 | Essencial | D15 | 4, 8, 12, 15, 22 | Planner/implementer/reviewer e testes adversariais |
| VA06 | AI-Native Engineering | Planejar, delegar, revisar e verificar de forma independente o trabalho dos agentes | T14 | Essencial | D15 | 1, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 24 | docs/agent-reviews.md com defeitos pegos |
| V301 | Expectativas 30-60-90 | 30d: entregar o projeto pago em produção | T10 | Essencial | D14 | 11, 12, 13, 17 | Releases com checkout pago (test mode) em prd |
| V302 | Expectativas 30-60-90 | 30d: entender os codebases e explicar como um caso flui de ponta a ponta | T06 | Essencial | D07 | 1, 2, 18, 23 | Doc + vídeo 'como um caso flui' |
| V303 | Expectativas 30-60-90 | 30d: diagnosticar e resolver incidentes sozinho | T08 | Essencial | D10 | 11, 15, 20 | Game days resolvidos sozinho com timeline |
| V304 | Expectativas 30-60-90 | 30d: assumir planejamento, acompanhamento, releases e comunicação escrita | T15 | Essencial | D14 | 5, 11, 13, 15, 17, 22, 24 | Runbook de release + updates + planos |
| V305 | Expectativas 30-60-90 | 30d: avaliação escrita de lacunas (arquitetura, confiabilidade, execução) e o que corrigir primeiro | T15 | Essencial | D14 | 18, 23 | Documento de avaliação de lacunas |
| V306 | Expectativas 30-60-90 | 30d: compromissos sem surpresas | T15 | Essencial | D14 | 8, 12, 20 | Checkpoints com previsão × realizado |
| V307 | Expectativas 30-60-90 | 60d: dono das prioridades, direção técnica, revisões e entregas do júnior | T15 | Essencial | D13 | 10, 16 | Brief de delegação + revisões do júnior |
| V308 | Expectativas 30-60-90 | 60d: entregar melhorias da avaliação de lacunas | T08 | Essencial | D10 | 23 | 3 correções sistêmicas entregues |
| V309 | Expectativas 30-60-90 | 60d: liderar iniciativa grande a partir de objetivo de negócio (restrições, limites, alternativas, plano até produção) | T15 | Essencial | D14 | 11, 24 | Plano e execução da migração |
| V310 | Expectativas 30-60-90 | 60d: eliminar problemas recorrentes com correções sistêmicas | T08 | Essencial | D10 | 15, 20, 23 | Ações de postmortem fechadas |
| V311 | Expectativas 30-60-90 | 60d: propor melhorias antes de pedirem | T15 | Recomendado | D14 | 23 | Lista de propostas não pedidas |
| V312 | Expectativas 30-60-90 | 90d: engenharia mais rápida/confiável que a herdada; melhorias mensuráveis (Growth, Ops, confiabilidade, cliente) | T08 | Essencial | D10 | 15, 22 | Métricas antes/depois por release |
| V313 | Expectativas 30-60-90 | 90d: alavancagem via sistemas, ferramentas, agentes de IA, documentação e delegação | T14 | Essencial | D15 | 22, 23, 24 | Harness de agentes + docs + delegação medidos |
| V314 | Expectativas 30-60-90 | 90d: júnior mais efetivo | T15 | Recomendado | D13 | 17, 23 | Onboarding doc + revisões didáticas |
| V315 | Expectativas 30-60-90 | 90d: identificar oportunidades de alto valor não pedidas | T15 | Recomendado | D12 | 23 | 3 propostas com impacto estimado |
| V316 | Expectativas 30-60-90 | 90d: elevar o padrão de execução (simplicidade, ciclos rápidos, releases seguros, comunicação, accountability) | T15 | Recomendado | D14 | 23, 24 | Retrospectiva final com métricas de execução |
| VR01 | Requisitos | 7+ anos de engenharia de software | T15 | Essencial | — (não mensurável por exercício) | 24 | Não se cobre com estudo: ver análise de distância (H) |
| VR02 | Requisitos | 2+ anos sendo dono de sistemas event-driven em produção | T04 | Essencial | D08 | 8, 15, 24 | Lacuna real; projeto é proxy, ver H |
| VR03 | Requisitos | Experiência em startups ou ambientes rápidos | T16 | Essencial | D12 | 2, 24 | Lacuna real; simulação + vagas intermediárias (H) |
| VR04 | Requisitos | Forte em APIs, webhooks, bancos de dados, integrações e sistemas event-driven | T03 | Essencial | D08 | 6, 24 | Kit de integração, Stripe, Airtable, outbox |
| VR05 | Requisitos | Capaz de trabalhar no full stack quando necessário | T12 | Recomendado | D16 | 17, 21, 22 | Next.js funil + console |
| VR06 | Requisitos | Já liderou ou fez mentoria de engenheiros | T15 | Essencial | D13 | 1, 2, 6, 7, 10, 16, 17, 20, 23, 24 | Simulações + mentoria real recomendada (H) |
| VR07 | Requisitos | Cuidado instintivo com dados sensíveis (ambiente regulado ou disciplina equivalente) | T13 | Essencial | D11 | 3, 12, 13, 16, 20 | Práticas estilo HIPAA no projeto |
| VR08 | Requisitos | Uso intenso de agentes de IA no dia a dia | T14 | Essencial | D15 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24 | Labs AI-native semanais |
| VR09 | Requisitos | Ownership extremo; Growth e Ops como clientes (observar fluxos antes de automatizar) | T16 | Essencial | D12 | 14 | Job stories e mapa as-is antes de automatizar |
| VR10 | Requisitos | Alta accountability; preferir entregar valor a construir algo teoricamente perfeito | T15 | Essencial | D14 | 4, 12 | Cortes de escopo documentados nos checkpoints |
| VD01 | Diferenciais | Feature com LLM + human-in-the-loop no ar (onde falhou, o que aprendeu, como melhorou) | T11 | Recomendado | D15 | 16, 17 | Doc de falhas/melhorias do Form Filler com evals |
| VD02 | Diferenciais | Sistemas de pagamento e assinatura em produção | T10 | Recomendado | D08 | 12, 13, 22 | Stripe test mode completo (lacuna: não é produção real) |
| VD03 | Diferenciais | Workflow engines (Temporal, Cadence, Step Functions) | T05 | Recomendado | D08 | 9, 10, 16 | Temporal 101/102/Versioning + CaseLifecycle |
| VD04 | Diferenciais | Engenharia com HIPAA e manipulação de PHI em produção | T13 | Recomendado | D11 | 3, 13, 16, 20 | Controles estilo HIPAA com dados fictícios (lacuna: não é PHI real) |
| VK01 | Cultura e condições | Aprender rápido e decidir bem | T15 | Essencial | — (não mensurável por exercício) | 1, 4, 23, 24 | Checkpoints com replanejamento baseado em evidência |
| VK02 | Cultura e condições | Trabalhar muito e ser profissional (inclui 60+ h/semana com frequência) | T16 | Essencial | — (não mensurável por exercício) | 24 | Decisão pessoal informada (H); plano não simula 60 h |
| VK03 | Cultura e condições | Foco em resultado de negócio | T16 | Essencial | D12 | 2, 14, 19, 23 | Métricas de negócio nos memos e demos |
| VK04 | Cultura e condições | Alta integridade | T15 | Essencial | — (não mensurável por exercício) | 8, 15, 24 | Postmortems honestos; candidatura sem exageros |
| VK05 | Cultura e condições | Perfil: velocidade > arquitetura de longo prazo, requisitos ambíguos, manter sistemas existentes, generalista | T16 | Essencial | — (não mensurável por exercício) | 3, 11, 23 | Migração do legado + trabalho em várias áreas |
| VK06 | Cultura e condições | Remoto com 8h de sobreposição com 8h-18h ET e alta disponibilidade para incidentes | T08 | Essencial | — (não mensurável por exercício) | 20, 24 | Game days + rotina de horário alinhada a ET |
| VK07 | Cultura e condições | Inglês fluente obrigatório | T17 | Essencial | D17 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24 | Trilha de inglês + vídeos + mocks |
| VK08 | Cultura e condições | Remuneração e condições (US$120-140k, folga flexível, bônus): negociação e modelo de contratação | T16 | Recomendado | — (não mensurável por exercício) | 24 | Pesquisa de faixa, PJ/contractor × EOR (semana 24) |
| VS01 | Stack | Go | T01 | Essencial | D02 | 1, 2, 4, 6, 7, 8, 9, 10, 12 | Serviços Go |
| VS02 | Stack | Python | T01 | Essencial | D01 | 1, 3, 6, 11, 14 | Serviços Python |
| VS03 | Stack | PostgreSQL | T02 | Essencial | D04 | 1, 3, 4, 5 | Cloud SQL/Postgres local |
| VS04 | Stack | TypeScript | T01 | Recomendado | D03 | 1, 6 | Cliente TS + Next.js |
| VS05 | Stack | Next.js | T12 | Recomendado | D16 | 1, 17, 21 | web/ (funil + console) |
| VS06 | Stack | GCP | T07 | Essencial | D09 | 1, 5, 18 | Projeto GCP com budget alerts |
| VS07 | Stack | Cloud Run | T07 | Essencial | D09 | 1, 2, 5, 8, 10, 11, 13, 18 | Serviços/jobs no Cloud Run |
| VS08 | Stack | Cloud SQL | T07 | Essencial | D09 | 5 | Instância Postgres gerenciada |
| VS09 | Stack | Pub/Sub | T04 | Essencial | D08 | 2, 5, 8, 9, 11, 12, 14, 18, 19 | Tópicos, assinaturas, DLQ |
| VS10 | Stack | BigQuery | T09 | Essencial | D06 | 1, 19, 20, 22 | Datasets e marts |
| VS11 | Stack | Cloud Build | T07 | Essencial | D09 | 5 | cloudbuild.yaml |
| VS12 | Stack | Temporal Cloud | T05 | Essencial | D08 | 1, 5, 8, 9, 10, 12, 16, 17, 18 | Worker conectado ao Temporal (Cloud trial ou dev server) |
| VS13 | Stack | Vertex AI (Gemini) | T11 | Essencial | D15 | 16 | Extração com structured output |
| VS14 | Stack | Google Document AI | T11 | Essencial | D15 | 16 | Form Parser no pipeline |
| VS15 | Stack | Stripe | T10 | Essencial | D08 | 4, 12, 13, 19, 20, 22 | billing/ |
| VS16 | Stack | Healthie | T10 | Opcional | D08 | 10, 22 | Adapter de agendamento por interface (fake + docs GraphQL) |
| VS17 | Stack | PandaDoc | T10 | Opcional | D08 | 17 | Envio para assinatura via sandbox ou fake |
| VS18 | Stack | AWS Cognito | T10 | Opcional | D11 | 17, 22 | Auth de staff no console (JWT verificado) |
| VS19 | Stack | Airtable | T10 | Essencial | D08 | 5, 14, 15, 17, 18, 23, 24 | Single Queue + ops-sync |
| VS20 | Stack | Webflow | T12 | Opcional | D16 | 21 | Integração formulário externo → webhook de intake |
| VS21 | Stack | Heyflow | T12 | Opcional | D16 | 21 | Integração formulário externo → webhook de intake |
| VS22 | Stack | Klaviyo | T12 | Opcional | D16 | 21 | Eventos de ciclo de vida (conta grátis ou fake) |
| VS23 | Stack | VWO | T12 | Opcional | D16 | 22 | Comparação comprar × construir para experimentos |
| VS24 | Stack | Google Tag Manager | T12 | Recomendado | D16 | 1, 21 | dataLayer + container GTM |
| VS25 | Stack | Google Analytics | T12 | Recomendado | D16 | 21, 22 | GA4 + Measurement Protocol + export BQ |
| VS26 | Stack | Google Ads | T12 | Opcional | D16 | 21 | Conversões offline/enhanced (conceito + gclid) |
| VS27 | Stack | Meta (Ads / Conversions API) | T12 | Opcional | D16 | 21 | CAPI em modo teste com dedupe por event_id |
| VS28 | Stack | Claude Code | T14 | Essencial | D15 | 1, 2, 3, 4, 8 | CLAUDE.md, hooks, subagentes |
| VS29 | Stack | Codex | T14 | Essencial | D15 | 1, 6, 13 | AGENTS.md, PLANS.md |
| VS30 | Stack | Harnesses de agentes no nível do repositório | T14 | Essencial | D15 | 1, 5, 6, 23 | Regras + hooks + testes + evals versionados |
| VQ01 | Perguntas da candidatura | Q1 What interested you in this role? | T17 | Essencial | D17 | 1, 2, 9, 16, 24 | Resposta final na aba Candidatura |
| VQ02 | Perguntas da candidatura | Q2 Why do you think you're a strong fit? | T17 | Essencial | D17 | 3, 10, 17, 24 | Resposta final na aba Candidatura |
| VQ03 | Perguntas da candidatura | Q3 Hardest part of this role for you, and why? | T17 | Essencial | D17 | 7, 14, 21, 24 | Resposta final na aba Candidatura |
| VQ04 | Perguntas da candidatura | Q4 Production system owned end-to-end (metric, what broke, what changed) | T17 | Essencial | D17 | 5, 12, 17, 18, 23, 24 | Resposta final na aba Candidatura |
| VQ05 | Perguntas da candidatura | Q5 Vídeo: most technically challenging thing you've personally built | T17 | Essencial | D17 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24 | Vídeo final ≤3 min |
| VQ06 | Perguntas da candidatura | Q6 Time you cut scope to hit a deadline | T17 | Essencial | D17 | 1, 6, 11, 19, 24 | Resposta final na aba Candidatura |
| VQ07 | Perguntas da candidatura | Q7 How do you use AI in your engineering workflow today? | T17 | Essencial | D17 | 4, 13, 20, 24 | Resposta final + doc 'How I use AI' |
