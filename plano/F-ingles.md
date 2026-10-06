<!-- Arquivo gerado por scripts/gerar.py — edite scripts/plano/templates/F-ingles.md. -->

# F) Trilha de inglês (1 h/dia, fora das 4 h técnicas)

Foco: **falar com fluência sobre o seu trabalho técnico** e passar em entrevistas comportamentais e técnicas, além de
escrever docs e updates em inglês. Total: 144 h. A semana 1 é diagnóstico (D17); da 2 à 24 a estrutura é fixa:

| Dia | Atividade (50 min) | + 10 min (seg-sex) |
|---|---|---|
| Seg | Pronúncia e fluência: shadowing (Rachel's English) + 10 termos da semana no YouGlish | Update diário em inglês |
| Ter | Escuta → fala: episódio/talk técnico e resumo oral gravado de 2 min (semanas 21-24: mock extra) | Update diário |
| Qua | STAR: escrever/refinar uma das 7 respostas e falar 3× cronometrado | Update diário |
| Qui | Escrita técnica: o documento da semana em inglês (design doc, ADR, runbook...) | Update diário |
| Sex | Conversação/mock (self-mock nas semanas 2-8; mocks com pares a partir da 9) | Update diário |
| Sáb | **Vídeo semanal de 2-3 min** sobre algo do projeto + autoavaliação com rubrica | — |

## Semana a semana

| Semana | Vocabulário | STAR (quarta) | Documento (quinta) | Conversa/mock (sexta) | Vídeo (sábado) |
|---|---|---|---|---|---|
| 1 | — | — | Amostra escrita do D17 | Resposta não preparada à Q1 | Diagnóstico D17: EF SET + vídeo de 2 min |
| 2 | carreira e apresentação pessoal | Q1 | design doc #1 do LeaveFlow | self-mock: self-introduction de 60 s + 3 perguntas de follow-up | Quem sou eu: formação, o projeto de HPC e por que backend event-driven |
| 3 | APIs e bancos (endpoint, payload, schema, migration, constraint) | Q2 | design doc #2 (o legado) | self-mock: explicar o sistema legado a um entrevistador | O 'sistema legado' do LeaveFlow e suas dívidas |
| 4 | concorrência e idempotência (race condition, retry, duplicate, lock) | Q7 | ADR-001 (idempotência) | self-mock: 'What is idempotency and how did you implement it?' | Idempotência explicada com o case-service |
| 5 | deploy e infraestrutura (pipeline, rollout, rollback, staging, secret) | Q4 | runbook de release | self-mock: walk-through do pipeline de CI/CD | Meu pipeline do commit à produção |
| 6 | integrações (webhook, signature, backoff, jitter, throttling) | Q6 | design doc #3 (padrão de integração) | self-mock: 'How do you handle third-party API failures?' | Como recebo webhooks com segurança |
| 7 | DDD (bounded context, aggregate, invariant, ubiquitous language) | Q3 | ADR-003 (bounded contexts) | self-mock: explicar o context map em 3 min | Os bounded contexts do LeaveFlow |
| 8 | mensageria (at-least-once, ack, dead-letter, ordering key, backlog) | Q5 | postmortem simulado #1 | self-mock: 'Explain the transactional outbox pattern' | Outbox pattern em 2 minutos |
| 9 | workflows (durable execution, signal, timer, activity, determinism) | Q1 | design doc #4 (CaseLifecycle) | peer mock comportamental (Exponent Practice) ou self-mock | Por que usar Temporal (e quando não usar) |
| 10 | sagas e CQRS (compensation, read model, projection, rebuild) | Q2 | ADR-004 (CQRS onde paga) | self-mock: 'Walk me through a saga failure' | Saga com compensações no CaseLifecycle |
| 11 | migração (backfill, cutover, shadow traffic, rollback, parity) | Q6 | plano da iniciativa de migração | peer mock: 'Tell me about a large initiative you led' | Migração lado a lado sem big-bang |
| 12 | pagamentos (checkout, charge, refund, dispute, reconciliation) | Q4 | design doc #5 (pagamentos) | self-mock: system design de checkout com webhooks | Webhooks do Stripe: duplicados, ordem e assinatura |
| 13 | assinaturas e finanças (subscription, dunning, proration, ledger, payout) | Q7 | runbook de discrepância de pagamento | peer mock técnico | Como reconcilio pagamentos |
| 14 | operações (queue, SLA, backlog, handoff, workaround) | Q3 | ADR-005 (sync com Airtable) | self-mock: 'How do you work with non-technical teams?' | Single Queue no Airtable e rate limits |
| 15 | recuperação (replay, conflict, source of truth, drift) | Q5 | runbook de recuperação caso a caso | peer mock: incidente e postmortem | Replay sem sobrescrever edições de Ops |
| 16 | IA aplicada (extraction, schema, confidence, eval, ground truth) | Q1 | ADR-006 (Document AI × Gemini) | self-mock: 'How do you evaluate an LLM feature?' | AI Form Filler: extração e evals |
| 17 | human-in-the-loop (review, override, feedback loop, failure mode) | Q2 | doc 'onde falhou, o que aprendi' | peer mock: projeto com LLM | HITL: onde falhou e como melhorei |
| 18 | observabilidade (SLO, SLI, error budget, trace, span, burn rate) | Q4 | relatório de confiabilidade | self-mock: debugging em produção | SLOs e tracing de um caso |
| 19 | dados (grain, freshness, lineage, data contract, dashboard) | Q6 | contrato de dados | peer mock: SQL/analytics | Qualidade de dados no LeaveFlow |
| 20 | segurança (least privilege, audit trail, PHI, encryption, retention) | Q7 | política de tratamento de dados | self-mock: 'How do you handle sensitive data?' | Incidente simulado e postmortem |
| 21 | growth (funnel, conversion, variant, guardrail metric, attribution) | Q3 | brief do experimento | peer mock comportamental (STAR) | Experimento A/B no funil |
| 22 | experimentação (sample size, significance, SRM, novelty effect) | Q5 | relatório do experimento | mock de system design (Hello Interview) + comportamental | Tracking server-side e deduplicação |
| 23 | liderança (delegation, ownership, trade-off, stakeholder, escalation) | Q4 | avaliação de lacunas | mock de deep dive técnico do projeto + comportamental | Versão candidata do vídeo Q5 (most challenging thing) |
| 24 | entrevistas e negociação (compensation, contractor, overlap, availability) | Q5 | respostas finais das 7 perguntas | mock final completo (comportamental + técnico) com par | Vídeo final Q5 + pitch de 60 s |

## Pronúncia: pontos críticos para falantes de português

| Ponto | Exemplos do seu vocabulário de trabalho |
|---|---|
| /iː/ × /ɪ/ (vogal longa × curta) | **leave** × live, **feature**, **team**, **queue** /kjuː/, **schema** /ˈskiːmə/ |
| Não inserir "i" antes de s + consoante | **Stripe**, **schedule**, **Slack**, **stack**, **staging** (não "estripe", "esteiging") |
| Não inserir vogal no fim | Stripe (não "Stripi"), Go, Next, test, deploy**ed** |
| -ed final: /t/, /d/, /ɪd/ | fix**ed** /t/, deploy**ed** /d/, migrat**ed** /ɪd/; "worked" tem uma sílaba |
| th /θ/ /ð/ | **th**roughput, au**th**entication, **th**ird-party, **th**ese |
| Acento de palavra | de**VEL**opment, **AR**chitecture, a**NAL**ysis, i**DEM**potent (idempotency: eye-dem-**POH**-tən-see), **CACHE** /kæʃ/ |
| Siglas | S-Q-L ou "sequel", A-P-I, G-C-P, P-H-I, H-I-P-A-A ("HIP-uh") |

Use o [YouGlish](https://youglish.com/) para ouvir cada termo dito por engenheiros em palestras reais.

## Vocabulário-base (amplie com o tema de cada semana)

- **Engenharia:** ship, roll out / roll back, cut over, backfill, on-call, page, incident, mitigate, root cause,
  contributing factor, blast radius, trade-off, edge case, flaky test, regression, idempotent, at-least-once, retry with
  backoff, dead-letter queue, source of truth, drift, parity, guardrail.
- **Negócio e Growth:** funnel, conversion rate, drop-off, churn, retention, upsell, pricing test, guardrail metric,
  attribution, cohort, LTV, CAC, unit economics, stakeholder, ownership, scope cut, ETA, commitment.
- **Frases de update e reunião:** "Here's where we are…", "What's working / what isn't…", "The risk is…, and here's how
  I'd mitigate it", "I'd recommend… because…", "What I need from you is a decision on…", "That's a fair point; the
  trade-off is…", "Let me take that offline and follow up in writing."

## STAR para as 7 perguntas

Formato: **S**ituation (1-2 frases) → **T**ask (o que era seu) → **A**ction (o que **você** fez, com detalhe técnico) →
**R**esult (número, aprendizado, o que mudou). Guias: [Tech Interview Handbook: STAR](https://www.techinterviewhandbook.org/star-format)
e [behavioral para seniores](https://www.techinterviewhandbook.org/behavioral-interview-senior-candidates/).
Cada pergunta é praticada 3 vezes ao longo do plano (quarta-feira); os rascunhos estão na aba **Candidatura**
e em [`candidatura.md`](candidatura.md). Monte um "banco de histórias" com 5 histórias reutilizáveis:

1. Acoplamento de simuladores em HPC (o mais desafiador; falhas parciais; resultado).
2. Migração C++ → Python (legado, paridade, risco).
3. Pesquisa em grafos/simulação (aprender rápido, decidir com dados).
4. LeaveFlow: Airtable sync / replay seguro (falha e correção sistêmica).
5. LeaveFlow: AI Form Filler com revisão humana (onde falhou, como melhorou) e um corte de escopo real.

## Vídeo semanal: protocolo

1. Escreva só 5 tópicos (não o texto). Grave de primeira, 2-3 min, câmera na altura dos olhos.
2. Transcreva (legenda automática serve) e conte palavras/min e muletas/min.
3. Preencha a rubrica (fluência, pronúncia, estrutura, vocabulário, tempo; 0-2 cada) de
   [`diagnostico/README.md`](../diagnostico/README.md#rubrica-do-d17-inglês--autoavaliação-do-vídeo-repetida-todo-sábado).
4. Escolha **um** ponto para a semana seguinte. Compare com o vídeo da semana anterior.

## Simulações de entrevista

- Semanas 2-8: self-mock (perguntas de follow-up que você não preparou; grave e reveja).
- Semanas 9-20: mocks com pares quinzenais na [Exponent Practice](https://www.tryexponent.com/blog/introducing-exponent-practice)
  (créditos grátis mensais; antigo Pramp), alternando comportamental, técnico e system design.
- Semanas 21-24: duas por semana (terça + sexta), incluindo system design com o framework do
  [Hello Interview](https://www.hellointerview.com/learn/system-design/in-a-hurry/delivery) e deep dive do LeaveFlow.

## Medição de progresso

EF SET no início (semana 1) e no fim (semana 24) ([efset.org](https://www.efset.org/)), palavras/min e muletas/min por
vídeo, nota da rubrica por semana, e nº de mocks feitos. Registre na aba Diagnóstico (D17) e nos checkpoints.
