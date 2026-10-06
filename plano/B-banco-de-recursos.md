<!-- Arquivo gerado por scripts/gerar.py — não edite à mão. -->

# B) Banco de recursos

Links conferidos por busca na web em outubro de 2026. **Principal** = os 2 a 4 materiais de cada trilha (item B do pedido). **Apoio** = documentação usada em atividades específicas do cronograma. Horas são estimativas de consumo do material (não o tempo de prática no projeto). "Google Skills" é o novo nome do Google Cloud Skills Boost (os links antigos redirecionam).

A trilha T00 (diagnóstico) usa os materiais da pasta [`diagnostico/`](../diagnostico/README.md); a de reforço flex usa os recursos da trilha que estiver sendo reforçada.


## T01 — Linguagens e ferramentas (Go, Python, TypeScript, Git/GitHub)

| ID | Papel | Material | Tipo | Custo | Horas | Nível | Semanas |
|---|---|---|---|---|---|---|---|
| R101 | Principal | [A Tour of Go](https://go.dev/tour/) | Curso interativo | Grátis | 6 | Iniciante | 2, 4 |
| R102 | Principal | [Learn Go with Tests (Chris James)](https://quii.gitbook.io/learn-go-with-tests) | Livro online + exercícios | Grátis | 20 | Iniciante → Intermediário | 4 |
| R103 | Principal | [TypeScript Handbook (oficial)](https://www.typescriptlang.org/docs/handbook/intro.html) | Documentação | Grátis | 8 | Iniciante → Intermediário | 2, 6 |
| R104 | Principal | [Pro Git, 2ª ed. (Chacon & Straub)](https://git-scm.com/book/en/v2) | Livro online | Grátis | 6 | Iniciante → Avançado | 1 |
| R105 | Apoio | [Effective Go](https://go.dev/doc/effective_go) | Documentação | Grátis | 3 | Intermediário | 4 |
| R106 | Apoio | [Go by Example](https://gobyexample.com/) | Exemplos anotados | Grátis | 4 | Iniciante → Intermediário | 4 |
| R107 | Apoio | [GitHub Skills (cursos interativos)](https://learn.github.com/skills) | Laboratório | Grátis | 3 | Iniciante → Intermediário | 2 |
| R108 | Apoio | [FastAPI: Tutorial - User Guide](https://fastapi.tiangolo.com/tutorial/) | Documentação | Grátis | 6 | Intermediário | 3, 6 |

## T02 — Bancos de dados, SQL e modelagem (PostgreSQL)

| ID | Papel | Material | Tipo | Custo | Horas | Nível | Semanas |
|---|---|---|---|---|---|---|---|
| R201 | Principal | [PostgreSQL docs: cap. 13 Concurrency Control (MVCC, isolamento)](https://www.postgresql.org/docs/current/mvcc.html) | Documentação | Grátis | 5 | Intermediário | 3 |
| R202 | Principal | [PostgreSQL Exercises](https://pgexercises.com/) | Laboratório | Grátis | 8 | Iniciante → Avançado | 2, 6 |
| R203 | Principal | [Use The Index, Luke (Markus Winand)](https://use-the-index-luke.com/) | Livro online | Grátis | 6 | Intermediário | 3, 18 |
| R204 | Apoio | [PostgreSQL docs: 13.3 Explicit Locking](https://www.postgresql.org/docs/current/explicit-locking.html) | Documentação | Grátis | 1 | Intermediário | 4 |

## T03 — APIs, webhooks e integrações (HTTP, idempotência, retries, rate limits)

| ID | Papel | Material | Tipo | Custo | Horas | Nível | Semanas |
|---|---|---|---|---|---|---|---|
| R301 | Principal | [Stripe: Designing robust and predictable APIs with idempotency](https://stripe.com/blog/idempotency) | Artigo | Grátis | 1 | Intermediário | 4 |
| R302 | Principal | [Amazon Builders' Library: Timeouts, retries and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) | Artigo | Grátis | 1 | Intermediário | 6 |
| R303 | Principal | [Amazon Builders' Library: Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/) | Artigo | Grátis | 1 | Intermediário | 4 |
| R304 | Principal | [Standard Webhooks: especificação](https://github.com/standard-webhooks/standard-webhooks/blob/main/spec/standard-webhooks.md) | Especificação (repositório) | Grátis | 1 | Intermediário | 6 |

## T04 — Sistemas distribuídos e arquitetura event-driven (Pub/Sub, outbox)

| ID | Papel | Material | Tipo | Custo | Horas | Nível | Semanas |
|---|---|---|---|---|---|---|---|
| R401 | Principal | [Designing Data-Intensive Applications, 2ª ed. (Kleppmann & Riccomini, 2026)](https://dataintensive.net/) | Livro | Pago (livro O'Reilly; veja biblioteca/assinatura) | 25 | Intermediário → Avançado | 4, 8, 9 |
| R402 | Principal | [microservices.io: Pattern: Transactional outbox](https://microservices.io/patterns/data/transactional-outbox) | Artigo/padrão | Grátis | 1 | Intermediário | 8 |
| R403 | Principal | [Pub/Sub: Exactly-once delivery](https://docs.cloud.google.com/pubsub/docs/exactly-once-delivery) | Documentação | Grátis | 2 | Intermediário | 8 |
| R404 | Apoio | [microservices.io: Pattern: Saga](https://microservices.io/patterns/data/saga.html) | Artigo/padrão | Grátis | 1 | Intermediário | 8 |
| R405 | Apoio | [Pub/Sub: Dead-letter topics](https://cloud.google.com/pubsub/docs/handling-failures) | Documentação | Grátis | 1 | Intermediário | 8 |
| R406 | Apoio | [Pub/Sub: Order messages](https://cloud.google.com/pubsub/docs/ordering) | Documentação | Grátis | 1 | Intermediário | 8 |

## T05 — Orquestração de workflows (Temporal, sagas)

| ID | Papel | Material | Tipo | Custo | Horas | Nível | Semanas |
|---|---|---|---|---|---|---|---|
| R501 | Principal | [Temporal 101: Introducing the Temporal Platform (Go ou Python)](https://learn.temporal.io/courses/temporal_101/) | Curso hands-on | Grátis | 2 | Iniciante | 9 |
| R502 | Principal | [Temporal 102: Exploring Durable Execution](https://learn.temporal.io/courses/temporal_102/) | Curso hands-on | Grátis | 4 | Intermediário | 9 |
| R503 | Principal | [Temporal: Versioning Workflows](https://learn.temporal.io/courses/versioning) | Curso hands-on | Grátis | 1,5 | Intermediário | 10 |
| R504 | Principal | [Temporal: Saga Pattern Made Easy](https://temporal.io/blog/saga-pattern-made-easy) | Artigo | Grátis | 1 | Intermediário | 10 |
| R505 | Apoio | [Temporal: Go SDK developer guide](https://docs.temporal.io/develop/go) | Documentação | Grátis | 4 | Intermediário | 9 |
| R506 | Apoio | [Temporal: Python SDK developer guide](https://docs.temporal.io/develop/python) | Documentação | Grátis | 3 | Intermediário | 9, 16, 17 |
| R507 | Apoio | [Temporal Cloud: US$1,000 em créditos para novos usuários](https://temporal.io/blog/get-usd1-000-in-free-credits-and-build-better-workflows-with-temporal-cloud) | Artigo (oferta) | Créditos de teste (exige cartão) | 0,5 | — | 10 |

## T06 — Arquitetura de domínio (DDD, Clean Architecture, CQRS, projeções, migração lado a lado)

| ID | Papel | Material | Tipo | Custo | Horas | Nível | Semanas |
|---|---|---|---|---|---|---|---|
| R601 | Principal | [Architecture Patterns with Python / Cosmic Python (Percival & Gregory)](https://www.cosmicpython.com/) | Livro online | Grátis | 15 | Intermediário | 3, 7, 10 |
| R602 | Principal | [Learning Domain-Driven Design (Vlad Khononov, O'Reilly)](https://www.oreilly.com/library/view/learning-domain-driven-design/9781098100124) | Livro | Pago (O'Reilly) | 12 | Intermediário | 7 |
| R603 | Principal | [Wild Workouts (Go DDD/Clean/CQRS) + e-book Go With The Domain](https://github.com/ThreeDotsLabs/wild-workouts-go-ddd-example) | Repositório + e-book | Grátis (e-book via newsletter) | 10 | Intermediário → Avançado | 7, 10 |
| R604 | Principal | [Martin Fowler: Strangler Fig](https://martinfowler.com/bliki/StranglerFigApplication.html) | Artigo | Grátis | 0,5 | Intermediário | 11 |
| R605 | Apoio | [Martin Fowler: Parallel Change (expand/contract)](https://martinfowler.com/bliki/ParallelChange.html) | Artigo | Grátis | 0,5 | Intermediário | 11 |
| R606 | Apoio | [Domain-Driven Design Reference (Eric Evans) e o 'blue book'](https://www.domainlanguage.com/ddd/reference/) | Referência (PDF) | Grátis (o livro completo é pago) | 3 | Intermediário | 2, 7, 11 |
| R607 | Apoio | [DDD Crew: DDD Starter Modelling Process](https://github.com/ddd-crew/ddd-starter-modelling-process) | Repositório/guia | Grátis | 2 | Iniciante → Intermediário | 2, 7 |
| R608 | Apoio | [Go With The Domain (e-book da Three Dots Labs)](https://threedots.tech/go-with-the-domain/) | E-book | Grátis (via newsletter) | 8 | Intermediário | 7 |

## T07 — Cloud GCP e DevOps (Cloud Run, Cloud SQL, Cloud Build, CI/CD)

| ID | Papel | Material | Tipo | Custo | Horas | Nível | Semanas |
|---|---|---|---|---|---|---|---|
| R701 | Principal | [Google Skills (ex-Cloud Skills Boost): Develop Serverless Applications on Cloud Run](https://www.cloudskillsboost.google/course_templates/741) | Laboratório (skill badge) | Grátis ou por créditos do Google Skills (confira na página) | 5,25 | Intermediário | 2, 5 |
| R702 | Principal | [Cloud Build: Deploying to Cloud Run using Cloud Build](https://docs.cloud.google.com/build/docs/deploying-builds/deploy-cloud-run) | Documentação | Grátis | 2 | Intermediário | 5 |
| R703 | Principal | [Cloud SQL: Connect to Cloud SQL for PostgreSQL from Cloud Run (quickstart)](https://docs.cloud.google.com/sql/docs/postgres/connect-instance-cloud-run) | Documentação/lab | Grátis (recursos GCP consomem créditos) | 2 | Intermediário | 5 |
| R704 | Principal | [Google Skills: Build Infrastructure with Terraform on Google Cloud](https://www.cloudskillsboost.google/course_templates/636) | Laboratório (skill badge) | Grátis ou por créditos do Google Skills (confira na página) | 5 | Intermediário (opcional) | 8 |
| R705 | Apoio | [Cloud Run: Configure secrets for services (Secret Manager)](https://docs.cloud.google.com/run/docs/configuring/services/secrets) | Documentação | Grátis | 1 | Intermediário | 5, 10 |
| R706 | Apoio | [Google Cloud: créditos de US$300 e Free Tier](https://cloud.google.com/free) | Página oficial | Grátis | 0,5 | — | 1, 5 |
| R707 | Apoio | [Software Engineering at Google, cap. 24: Continuous Delivery](https://abseil.io/resources/swe-book/html/ch24.html) | Livro online | Grátis | 1,5 | Intermediário | 5 |

## T08 — Confiabilidade, testes e observabilidade (SRE, incidentes, RCA)

| ID | Papel | Material | Tipo | Custo | Horas | Nível | Semanas |
|---|---|---|---|---|---|---|---|
| R801 | Principal | [Site Reliability Engineering (Google)](https://sre.google/sre-book/table-of-contents/) | Livro online | Grátis | 12 | Intermediário | 5, 15, 18 |
| R802 | Principal | [The Site Reliability Workbook (Google)](https://sre.google/workbook/table-of-contents/) | Livro online | Grátis | 8 | Intermediário | 18, 19 |
| R803 | Principal | [OpenTelemetry Go: Getting Started by Example](https://opentelemetry.io/docs/languages/go/getting-started/) | Documentação/tutorial | Grátis | 3 | Intermediário | 18 |
| R804 | Principal | [Google Skills: Monitor and Log with Google Cloud Observability](https://www.skills.google/course_templates/749) | Laboratório (skill badge) | Grátis ou por créditos do Google Skills (confira na página) | 4,25 | Iniciante → Intermediário | 18 |
| R805 | Apoio | [PagerDuty Incident Response Documentation](https://response.pagerduty.com/) | Guia | Grátis | 2 | Intermediário | 11, 15, 18, 20 |
| R806 | Apoio | [PagerDuty Postmortem Documentation](https://postmortems.pagerduty.com/) | Guia | Grátis | 1,5 | Intermediário | 8, 15, 20 |
| R807 | Apoio | [Testcontainers for Go: módulo Postgres](https://golang.testcontainers.org/modules/postgres/) | Documentação | Grátis | 1 | Intermediário | 4, 8 |
| R808 | Apoio | [Software Engineering at Google (livro completo, caps. de testes)](https://abseil.io/resources/swe-book/html/toc.html) | Livro online | Grátis | 6 | Intermediário | 3 |
| R809 | Apoio | [Cloud Logging: Structured logging](https://docs.cloud.google.com/logging/docs/structured-logging) | Documentação | Grátis | 1 | Intermediário | 3, 5, 18 |
| R810 | Apoio | [Cloud Trace overview](https://docs.cloud.google.com/trace/docs/overview) | Documentação | Grátis | 1 | Intermediário | 18 |
| R811 | Apoio | [Cloud Monitoring: Alerting overview](https://docs.cloud.google.com/monitoring/alerts) | Documentação | Grátis | 1 | Intermediário | 5, 12, 14, 18 |
| R812 | Apoio | [Getting started with Testcontainers for Python](https://testcontainers.com/guides/getting-started-with-testcontainers-for-python/) | Tutorial | Grátis | 1 | Intermediário | 3 |

## T09 — Dados, analytics e qualidade (BigQuery, dbt, reconciliação, BI)

| ID | Papel | Material | Tipo | Custo | Horas | Nível | Semanas |
|---|---|---|---|---|---|---|---|
| R901 | Principal | [Google Skills: Derive Insights from BigQuery Data](https://www.cloudskillsboost.google/course_templates/623) | Laboratório (skill badge) | Grátis ou por créditos do Google Skills (confira na página) | 4 | Iniciante | 19 |
| R902 | Principal | [Google Skills: Build a Data Warehouse with BigQuery](https://www.cloudskillsboost.google/course_templates/624) | Laboratório (skill badge) | Grátis ou por créditos do Google Skills (confira na página) | 5,25 | Intermediário | 19 |
| R903 | Principal | [dbt Fundamentals (dbt Learn)](https://learn.getdbt.com/courses/dbt-fundamentals) | Curso | Grátis | 5 | Iniciante → Intermediário | 19 |
| R904 | Principal | [dbt docs: Add data tests to your DAG](https://docs.getdbt.com/docs/build/data-tests) | Documentação | Grátis | 1,5 | Intermediário | 19 |
| R905 | Apoio | [BigQuery sample dataset for Google Analytics ecommerce (GA4)](https://developers.google.com/analytics/bigquery/web-ecommerce-demo-dataset) | Dataset público + docs | Grátis (sandbox/free tier) | 1 | Intermediário | 1, 22 |
| R906 | Apoio | [Pub/Sub: BigQuery subscriptions](https://docs.cloud.google.com/pubsub/docs/bigquery) | Documentação | Grátis | 1 | Intermediário | 19 |
| R907 | Apoio | [BigQuery sandbox (consultar sem cartão)](https://cloud.google.com/blog/products/data-analytics/query-without-a-credit-card-introducing-bigquery-sandbox) | Artigo oficial | Grátis | 0,5 | Iniciante | 1 |
| R908 | Apoio | [Snowflake in 20 minutes (tutorial oficial)](https://docs.snowflake.com/en/user-guide/getting-started-tutorial-log-in.html) | Tutorial | Grátis (trial de 30 dias) | 1 | Iniciante (prioridade baixa) | 19 |

## T10 — Integrações do domínio (Stripe, Airtable; Healthie, PandaDoc, Cognito)

| ID | Papel | Material | Tipo | Custo | Horas | Nível | Semanas |
|---|---|---|---|---|---|---|---|
| R1001 | Principal | [Stripe: Build a subscriptions integration (Checkout)](https://docs.stripe.com/billing/subscriptions/build-subscriptions) | Documentação/guia | Grátis (modo de teste) | 4 | Intermediário | 12, 22 |
| R1002 | Principal | [Stripe: Receive Stripe events in your webhook endpoint](https://docs.stripe.com/webhooks) | Documentação | Grátis | 2 | Intermediário | 12 |
| R1003 | Principal | [Airtable Web API: Introduction + Rate limits](https://airtable.com/developers/web/api/introduction) | Documentação | Grátis (plano Free: 1.000 chamadas/mês) | 3 | Intermediário | 14 |
| R1004 | Principal | [Airtable automation action: Run a script](https://support.airtable.com/articles/6328053615-airtable-automation-action-run-a-script) | Documentação | Grátis | 1 | Intermediário | 15 |
| R1005 | Apoio | [Stripe: Test clocks](https://docs.stripe.com/docs/billing/testing/test-clocks) | Documentação | Grátis | 1 | Intermediário | 13 |
| R1006 | Apoio | [Stripe: Test card numbers / testing](https://docs.stripe.com/testing) | Documentação | Grátis | 0,5 | Iniciante | 12 |
| R1007 | Apoio | [Stripe: Payout reconciliation](https://docs.stripe.com/payouts/reconciliation) | Documentação | Grátis | 1 | Intermediário | 13 |
| R1008 | Apoio | [Stripe: Using webhooks with subscriptions](https://docs.stripe.com/billing/subscriptions/webhooks) | Documentação | Grátis | 1 | Intermediário | 12, 13 |
| R1009 | Apoio | [Airtable Web API: Upload attachment](https://airtable.com/developers/web/api/upload-attachment) | Documentação | Grátis | 0,5 | Intermediário | 14 |
| R1010 | Apoio | [Airtable Webhooks API overview](https://support.airtable.com/docs/airtable-webhooks-api-overview) | Documentação | Grátis | 1 | Intermediário | 14, 15 |
| R1011 | Apoio | [Airtable: Managing API call limits (limites por plano)](https://support.airtable.com/docs/managing-api-call-limits-in-airtable) | Documentação | Grátis | 0,5 | — | 14 |
| R1012 | Apoio | [Healthie API docs (GraphQL)](https://docs.gethealthie.com/) | Documentação | Grátis para ler (sandbox depende de conta) | 2 | Intermediário (opcional) | 22 |
| R1013 | Apoio | [PandaDoc API: Authentication overview (Dev Center/sandbox)](https://developers.pandadoc.com/reference/auth-overview) | Documentação | Grátis para ler (sandbox conforme plano) | 1 | Intermediário (opcional) | 17 |
| R1014 | Apoio | [Amazon Cognito: Verifying JSON web tokens](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-using-tokens-verifying-a-jwt.html) | Documentação | Grátis para ler (free tier AWS) | 1 | Intermediário (opcional) | 17, 22 |
| R1015 | Apoio | [Stripe API: Idempotent requests](https://docs.stripe.com/api/idempotent_requests) | Documentação | Grátis | 0,5 | Intermediário | 12 |
| R1016 | Apoio | [Stripe: Customer portal](https://docs.stripe.com/customer-management) | Documentação | Grátis | 1 | Intermediário | 13 |

## T11 — IA aplicada (Document AI, Gemini, human-in-the-loop, evals)

| ID | Papel | Material | Tipo | Custo | Horas | Nível | Semanas |
|---|---|---|---|---|---|---|---|
| R1101 | Principal | [Vertex AI: Structured output (Gemini com response schema)](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/control-generated-output) | Documentação | Grátis para ler (uso consome créditos) | 2 | Intermediário | 16 |
| R1102 | Principal | [Document AI: Form Parser](https://docs.cloud.google.com/document-ai/docs/form-parser) | Documentação | Grátis para ler (uso consome créditos) | 2 | Intermediário | 16 |
| R1103 | Principal | [Google Skills: Automate Data Capture at Scale with Document AI](https://www.cloudskillsboost.google/course_templates/674) | Laboratório (skill badge) | Grátis ou por créditos do Google Skills (confira na página) | 4 | Intermediário | 16 |
| R1104 | Principal | [Hamel Husain: Your AI Product Needs Evals](https://hamel.dev/blog/posts/evals/index.html) | Artigo | Grátis | 1,5 | Intermediário | 16, 17 |
| R1105 | Apoio | [Google Skills: Prompt Design in Vertex AI](https://www.cloudskillsboost.google/course_templates/976) | Laboratório (skill badge) | Grátis | 3,75 | Iniciante | consulta |
| R1106 | Apoio | [Anthropic: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) | Artigo | Grátis | 1 | Intermediário | 17 |
| R1107 | Apoio | [DOL: formulário WH-380-E (certificação médica FMLA, público)](https://www.dol.gov/sites/dolgov/files/WHD/legacy/files/WH-380-E.pdf) | Formulário público (PDF) | Grátis | 0,5 | — | 1, 16 |
| R1108 | Apoio | [DOL: FMLA forms](https://www.dol.gov/agencies/whd/fmla/forms) | Página oficial | Grátis | 0,5 | — | consulta |

## T12 — Growth engineering e frontend (Next.js, A/B, tracking, anúncios)

| ID | Papel | Material | Tipo | Custo | Horas | Nível | Semanas |
|---|---|---|---|---|---|---|---|
| R1201 | Principal | [Next.js Learn: Foundations (App Router, dashboard app)](https://nextjs.org/learn/dashboard-app) | Curso interativo | Grátis | 10 | Iniciante → Intermediário | 17, 21 |
| R1202 | Principal | [Google Tag Manager: The data layer](https://developers.google.com/tag-platform/tag-manager/datalayer) | Documentação | Grátis | 1 | Intermediário | 21 |
| R1203 | Principal | [Trustworthy Online Controlled Experiments (Kohavi, Tang, Xu)](https://experimentguide.com/) | Livro | Pago (Cambridge University Press) | 10 | Intermediário | 21, 22 |
| R1204 | Principal | [GrowthBook and Next.js (App Router)](https://docs.growthbook.io/guide/nextjs-app-router) | Documentação (open source) | Grátis | 2 | Intermediário | 21 |
| R1205 | Apoio | [Google Analytics 4: Set up events](https://developers.google.com/analytics/devguides/collection/ga4/events) | Documentação | Grátis | 1 | Iniciante | 21 |
| R1206 | Apoio | [GA4 Measurement Protocol](https://developers.google.com/analytics/devguides/collection/protocol/ga4) | Documentação | Grátis | 1,5 | Intermediário | 21 |
| R1207 | Apoio | [Meta Conversions API: Using the API](https://developers.facebook.com/documentation/ads-commerce/conversions-api/using-the-api) | Documentação | Grátis | 1,5 | Intermediário (opcional) | 21 |
| R1208 | Apoio | [Google Ads Help: About enhanced conversions](https://support.google.com/google-ads/answer/9888656?hl=en) | Documentação | Grátis | 0,5 | Intermediário (opcional) | 21 |
| R1209 | Apoio | [Klaviyo: Events API overview](https://developers.klaviyo.com/en/reference/events_api_overview) | Documentação | Grátis | 1 | Intermediário (opcional) | 21 |
| R1210 | Apoio | [VWO Developers](https://developers.vwo.com) | Documentação | Grátis | 1 | Intermediário (opcional) | 22 |
| R1211 | Apoio | [Heyflow Help Center](https://help.heyflow.com) | Documentação | Grátis | 0,5 | Iniciante (opcional) | 21 |

## T13 — Segurança e compliance (estilo HIPAA, PHI, acesso, auditoria)

| ID | Papel | Material | Tipo | Custo | Horas | Nível | Semanas |
|---|---|---|---|---|---|---|---|
| R1301 | Principal | [HHS: Summary of the HIPAA Security Rule](https://www.hhs.gov/hipaa/for-professionals/security/laws-regulations/index.html) | Guia oficial | Grátis | 2 | Iniciante → Intermediário | 3, 20 |
| R1302 | Principal | [HHS: Guidance on De-identification of PHI (Safe Harbor / Expert Determination)](https://www.hhs.gov/hipaa/for-professionals/special-topics/de-identification/index.html) | Guia oficial | Grátis | 2 | Intermediário | 3, 20 |
| R1303 | Principal | [Google Cloud: HIPAA compliance on Google Cloud](https://docs.cloud.google.com/docs/security/compliance/hipaa) | Documentação | Grátis | 1,5 | Intermediário | 16 |
| R1304 | Principal | [OWASP API Security Top 10 (2023)](https://owasp.org/API-Security/editions/2023/en/0x11-t10/) | Guia | Grátis | 2 | Intermediário | 6, 12, 13, 20 |
| R1305 | Apoio | [Sensitive Data Protection overview (ex-DLP)](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview) | Documentação | Grátis | 1 | Intermediário | 16, 20 |
| R1306 | Apoio | [Cloud Audit Logs overview](https://docs.cloud.google.com/logging/docs/audit) | Documentação | Grátis | 1 | Intermediário | 20 |
| R1307 | Apoio | [HHS: NPRM de atualização da Security Rule (fact sheet)](https://www.hhs.gov/hipaa/for-professionals/security/hipaa-security-rule-nprm/factsheet/index.html) | Guia oficial | Grátis | 0,5 | Intermediário | 20 |

## T14 — Engenharia AI-native (Claude Code, Codex, guardrails, testes de arquitetura, multiagente)

| ID | Papel | Material | Tipo | Custo | Horas | Nível | Semanas |
|---|---|---|---|---|---|---|---|
| R1401 | Principal | [Claude Code docs: How Claude remembers your project (CLAUDE.md)](https://code.claude.com/docs/en/memory) | Documentação | Grátis | 1 | Intermediário | 1, 23 |
| R1402 | Principal | [Anthropic: Best practices for Claude Code](https://www.anthropic.com/engineering/claude-code-best-practices) | Guia | Grátis | 1,5 | Intermediário | 1, 3, 7, 9, 10, 11, 14, 18, 19, 21 |
| R1403 | Principal | [OpenAI Codex: Custom instructions with AGENTS.md](https://developers.openai.com/codex/guides/agents-md) | Documentação | Grátis | 1 | Intermediário | 1, 6 |
| R1404 | Principal | [Anthropic Academy: Claude Code in Action](https://anthropic.skilljar.com/claude-code-in-action) | Curso | Grátis | 2 | Intermediário | 2 |
| R1405 | Apoio | [Claude Code docs: Hooks reference](https://code.claude.com/docs/en/hooks) | Documentação | Grátis | 1 | Intermediário | 2, 5 |
| R1406 | Apoio | [Claude Code docs: Create custom subagents](https://code.claude.com/docs/en/sub-agents) | Documentação | Grátis | 1 | Intermediário | 4, 8, 12, 15, 22 |
| R1407 | Apoio | [Claude Code docs: Configure permissions](https://code.claude.com/docs/en/permissions) | Documentação | Grátis | 0,5 | Intermediário | 5, 15, 20 |
| R1408 | Apoio | [Import Linter (Python): layers contract](https://import-linter.readthedocs.io/en/stable/contract_types/layers/) | Documentação | Grátis | 0,5 | Intermediário | 7 |
| R1409 | Apoio | [go-arch-lint (Go)](https://pkg.go.dev/github.com/fe3dback/go-arch-lint) | Ferramenta/documentação | Grátis | 0,5 | Intermediário | 7 |
| R1410 | Apoio | [dependency-cruiser (TypeScript/JS)](https://github.com/sverweij/dependency-cruiser) | Ferramenta/repositório | Grátis | 0,5 | Intermediário | consulta |
| R1411 | Apoio | [OpenAI Codex: Best practices](https://developers.openai.com/codex/learn/best-practices) | Guia | Grátis | 1 | Intermediário | consulta |
| R1412 | Apoio | [AGENTS.md (formato aberto)](https://agents.md/) | Especificação | Grátis | 0,5 | Iniciante | 6 |
| R1413 | Apoio | [OpenAI Cookbook: Using PLANS.md for multi-hour problem solving](https://developers.openai.com/cookbook/articles/codex_exec_plans) | Guia | Grátis | 1 | Intermediário | 13 |

## T15 — Liderança, gestão de projetos e comunicação (~10% do tempo técnico)

| ID | Papel | Material | Tipo | Custo | Horas | Nível | Semanas |
|---|---|---|---|---|---|---|---|
| R1501 | Principal | [Google Technical Writing (One e Two)](https://developers.google.com/tech-writing) | Curso | Grátis | 6 | Iniciante → Intermediário | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24 |
| R1502 | Principal | [Design Docs at Google (Malte Ubl)](https://www.industrialempathy.com/posts/design-docs-at-google/) | Artigo | Grátis | 0,5 | Intermediário | 2, 3, 6, 9, 11, 12, 23 |
| R1503 | Principal | [Lara Hogan: Feedback and performance resources (Feedback Equation)](https://larahogan.me/resources/feedback/) | Guias/templates | Grátis | 2 | Iniciante → Intermediário | 6, 10, 17 |
| R1504 | Principal | [Shape Up (Ryan Singer, Basecamp)](https://basecamp.com/shapeup) | Livro online | Grátis | 5 | Intermediário | 1, 4, 8, 9, 12, 13, 16, 22 |
| R1505 | Apoio | [ADR Templates (MADR, Nygard, Y-statements)](https://adr.github.io/adr-templates/) | Templates | Grátis | 0,5 | Iniciante | 4, 7, 10, 14 |
| R1506 | Apoio | [Lara Hogan: One-on-one meetings resources](https://larahogan.me/resources/one-on-ones/) | Guias/templates | Grátis | 1 | Iniciante | 7 |
| R1507 | Apoio | [Google eng-practices: How to write code review comments](https://google.github.io/eng-practices/review/reviewer/comments.html) | Guia | Grátis | 0,5 | Iniciante → Intermediário | 6 |
| R1508 | Apoio | [HBR: Performing a Project Premortem (Gary Klein)](https://hbr.org/2007/09/performing-a-project-premortem) | Artigo | Grátis/paywall parcial | 0,5 | Intermediário | 2, 5, 11 |
| R1509 | Apoio | [GitLab Handbook: Communication (assíncrona/remota)](https://handbook.gitlab.com/handbook/communication/) | Handbook | Grátis | 1,5 | Intermediário | 3, 14, 21 |
| R1510 | Apoio | [StaffEng: Staff Engineer (Will Larson)](https://staffeng.com/book) | Livro/guias | Guias grátis no site; livro pago | 4 | Intermediário → Avançado | consulta |
| R1511 | Apoio | [Google eng-practices: Code review (guia completo)](https://google.github.io/eng-practices/review/) | Guia | Grátis | 2 | Intermediário | 17 |

## T16 — Produto, operações e negócio (processos, automação de Ops, startup)

| ID | Papel | Material | Tipo | Custo | Horas | Nível | Semanas |
|---|---|---|---|---|---|---|---|
| R1601 | Principal | [Paul Graham: Do Things that Don't Scale](https://paulgraham.com/ds.html) | Ensaio | Grátis | 0,5 | Iniciante | 2, 14 |
| R1602 | Principal | [YC Startup School](https://www.startupschool.org/) | Curso | Grátis | 10 | Iniciante | consulta |
| R1603 | Principal | [DOL Fact Sheet #28G: Medical Certification under the FMLA (domínio)](https://www.dol.gov/agencies/whd/fact-sheets/28g-fmla-serious-health-condition) | Guia oficial | Grátis | 0,5 | Iniciante | 1 |
| R1604 | Principal | [YC Startup Library](https://www.ycombinator.com/library) | Biblioteca (vídeos/ensaios) | Grátis | 4 | Iniciante | 14 |
| R1605 | Apoio | [DDD Crew: EventStorming glossary & cheat sheet](https://github.com/ddd-crew/eventstorming-glossary-cheat-sheet) | Guia/repositório | Grátis | 1 | Iniciante | 1, 2, 14 |

## T17 — Inglês técnico e entrevistas (1h/dia, fora das 4h técnicas)

| ID | Papel | Material | Tipo | Custo | Horas | Nível | Semanas |
|---|---|---|---|---|---|---|---|
| R1701 | Principal | [EF SET (teste de inglês grátis, alinhado ao CEFR)](https://www.efset.org/) | Teste | Grátis | 1 | Todos | 1 |
| R1702 | Principal | [YouGlish (pronúncia em contexto real)](https://youglish.com/) | Ferramenta | Grátis | 10 | Todos | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24 |
| R1703 | Principal | [Rachel's English: Free American Accent Course](https://rachelsenglish.com/free/) | Curso/vídeos | Grátis | 10 | Intermediário | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24 |
| R1704 | Principal | [Tech Interview Handbook: Behavioral interviews](https://www.techinterviewhandbook.org/behavioral-interview/) | Guia | Grátis | 3 | Intermediário | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24 |
| R1705 | Apoio | [Tech Interview Handbook: STAR format](https://www.techinterviewhandbook.org/star-format) | Guia | Grátis | 0,5 | Intermediário | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24 |
| R1706 | Apoio | [Exponent Practice (mocks entre pares; antigo Pramp)](https://www.tryexponent.com/blog/introducing-exponent-practice) | Plataforma | Créditos grátis mensais + plano pago | 10 | Intermediário | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24 |
| R1709 | Apoio | [Software Engineering Daily (podcast técnico)](https://softwareengineeringdaily.com/) | Podcast | Grátis | 20 | Intermediário | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 |

## T18 — Carreira e candidatura (semanas 23-24)

| ID | Papel | Material | Tipo | Custo | Horas | Nível | Semanas |
|---|---|---|---|---|---|---|---|
| R1707 | Principal | [Hello Interview: System Design Delivery Framework](https://www.hellointerview.com/learn/system-design/in-a-hurry/delivery) | Guia | Grátis (parte premium) | 2 | Intermediário | 23 |
| R1708 | Principal | [Tech Interview Handbook: Behavioral interviews for senior candidates](https://www.techinterviewhandbook.org/behavioral-interview-senior-candidates/) | Guia | Grátis | 1 | Intermediário | consulta |
| R1801 | Principal | [Revelo: vagas remotas em empresas dos EUA para engenheiros da América Latina](https://careers.revelo.com/) | Plataforma de vagas | Grátis | 1 | — | 24 |
| R1802 | Principal | [Strider: vagas remotas para devs da América Latina](https://onstrider.com/) | Plataforma de vagas | Grátis | 1 | — | 24 |
