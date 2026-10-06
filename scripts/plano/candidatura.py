"""Aba 'Candidatura': rascunhos das 7 respostas (em inglês, como a candidatura pede) e checklist.

Trechos entre colchetes [ ] são dados que só você tem: preencha com números reais ou apague.
Nunca apresente o LeaveFlow como sistema de produção com usuários reais: é portfólio com dados fictícios.
"""

# (pergunta, rascunho em inglês, evidência a usar, o que falta / cuidado, semana para finalizar)
RESPOSTAS = [
    (
        "Q1. What interested you in this role?",
        "Three things. First, the problem: helping people without a primary care doctor get through a medical leave is as much a workflow problem as a clinical one. "
        "Intake, payment, scheduling, documentation and operations all have to line up, and when one step silently fails, a real person can lose income or job protection. "
        "Second, the shape of the work: owning a live event-driven system (Pub/Sub + Temporal, 20+ integrations) while a legacy model is migrated to a new domain model side by side in production. "
        "That is exactly the kind of system I have been training myself to build: I rebuilt a smaller version of it end to end (Go and Python services on Cloud Run, transactional outbox, "
        "Temporal sagas, Stripe, a two-way Airtable queue and an LLM form filler with human review). "
        "Third, how you build: supervised Claude Code and Codex sessions with repo-level rules, architecture tests and independent verification is how I already work, "
        "and I want to do it where the results have business consequences.",
        "Projeto LeaveFlow (semanas 3-23); fluxo AI-native (item D); motivação real com o domínio de saúde.",
        "Personalize a primeira frase com um motivo seu (verdadeiro). Máx. ~150 palavras.",
        "Semana 24 (rascunhos nas semanas 2, 9 e 16)",
    ),
    (
        "Q2. Why do you think you're a strong fit?",
        "I am earlier in my career than the 7+ years you list, so I will be specific about evidence instead. "
        "(1) Integration under messy conditions: at [lab/company] I wrote the Python layer that couples [simulator A] and [simulator B] on HPC clusters, "
        "handling partial failures, restarts and consistency between processes that know nothing about each other ([scale: N jobs / nodes / hours]). "
        "(2) Legacy migration: I migrated a computer vision system from C++ to Python [while validating output parity against the old version], the same discipline you need "
        "for a side-by-side domain migration: parity checks, incremental cutover, no big bang. "
        "(3) I built and operated a portfolio replica of your architecture with the patterns you named: DDD/Clean Architecture, CQRS projections, transactional outbox, Temporal sagas, "
        "idempotent Stripe webhooks with reconciliation, and an Airtable sync with per-field ownership so replays never overwrite Ops edits, plus SLOs, game days and blameless postmortems. "
        "(4) I write before I build: design docs, ADRs and short daily updates. (5) I use Claude Code and Codex every day with rules files, hooks and architecture tests, and I verify agent output myself. "
        "Brasília is one to two hours ahead of ET, so 8am-6pm ET sits fully inside my working day.",
        "Experiência real (HPC, migração C++→Python, pesquisa em grafos/simulação) + LeaveFlow + artefatos de liderança.",
        "Preencha os colchetes com números reais. Se a migração não teve verificação de paridade, não diga que teve.",
        "Semana 24 (rascunhos nas semanas 3, 10 e 17)",
    ),
    (
        "Q3. Based on the job description, what will be the hardest part of this role for you, and why?",
        "Two things, honestly. The first is the scale of real production ownership: I have owned [research pipelines / internal systems], but not a revenue-generating, "
        "event-driven system with 20+ third-party integrations and on-call duty. In my first 30 days the risk is being slower to triage an incident in an unfamiliar codebase. "
        "My mitigation is what I already practice: map how a case flows end to end in week one, read the runbooks and recent incidents, shadow the alerts, and write down what I learn "
        "so the next person does not have to rediscover it. "
        "The second is managing a junior engineer while being hands-on 90% of the time. I have [mentored / been a teaching assistant / helped colleagues], but never as a direct manager. "
        "I would make it concrete from day one: a written brief with a definition of done for each piece of work, small PRs reviewed the same day, and a weekly 1:1 focused on unblocking and growth.",
        "Análise de distância (item H); simulações de liderança (item E); game days.",
        "Não transforme fraqueza em falsa qualidade. Mostre o plano concreto de mitigação.",
        "Semana 24 (rascunhos nas semanas 7, 14 e 21)",
    ),
    (
        "Q4. Describe one production system you owned end-to-end. What business metric did it affect? What broke, and what did you change so it wouldn't break the same way again?",
        "[Prefer a real system. If the C++→Python computer vision migration or the HPC coupling script ran for real users or a real lab pipeline, use it with its real metric. "
        "Only if you have nothing real, use LeaveFlow and say up front that it is a portfolio system with synthetic data.] "
        "Portfolio version: 'The system I owned end to end is LeaveFlow, a portfolio system I designed to mirror a medical-leave case pipeline (synthetic data, Stripe test mode). "
        "The metric I optimized was the time from intake to a case being actionable by Ops (target under one minute) and payment-to-case consistency (zero unmatched payments). "
        "What broke: in a load test with 200 new cases, the Airtable projection hit the 5 requests/second per-base limit, retries piled up, and a replay overwrote a field Ops had edited by hand. "
        "What I changed: a token-bucket limiter with batches of 10, per-field ownership with version checks so a projection can never overwrite an Ops-owned field, a dry-run replay tool, "
        "and a daily reconciliation job with an alert. Afterwards, [result: 0 overwrites across N replays; p95 lag X seconds].'",
        "Semanas 14-15 (Airtable), 13 (reconciliação), 17 (doc de lições do Form Filler) e postmortems.",
        "A pergunta diz 'production system': se usar o LeaveFlow, deixe explícito que é portfólio. Use só falhas que aconteceram de fato.",
        "Semana 24 (rascunhos nas semanas 5, 12, 18 e 23)",
    ),
    (
        "Q5. (Vídeo) Tell us about the most technically challenging thing you've personally built. What did you personally own, what made it difficult, and what was the outcome?",
        "Script outline (2-3 min, speak, do not read): "
        "0:00-0:15 context in one sentence ('I built the coupling layer that lets two scientific simulators run as one job on an HPC cluster'). "
        "0:15-0:45 what you personally owned (design, code, tests, running it). "
        "0:45-1:45 the two hardest technical problems, with specifics (e.g., keeping both processes consistent when one restarts; data exchange format and performance; debugging on a shared cluster). "
        "1:45-2:20 the outcome with numbers ([runtime, scale, who used it]). "
        "2:20-2:40 what you would do differently and how that shaped how you build event-driven systems today. "
        "Alternative: the LeaveFlow Airtable sync or the AI form filler, if that is genuinely the hardest thing you built.",
        "Projeto real de HPC (preferido, por ser pessoal e verificável) ou LeaveFlow.",
        "Grave a versão candidata na semana 23 e a final na 24. ≤3 min, câmera na altura dos olhos, sem leitura.",
        "Semana 24 (rascunhos nas semanas 8, 15 e 22)",
    ),
    (
        "Q6. Tell us about a time you cut scope to hit a deadline. What did you cut, how did you decide, and what happened afterward?",
        "[Prefer a real example from your master's or HPC work: a paper/conference deadline, a cluster allocation window, a demo for your advisor.] "
        "Structure: the deadline and what was at stake; the options you considered; what you cut and what you protected (correctness, data safety); how you told the people affected; "
        "what happened afterward (did you add it back, was the cut right?). "
        "Portfolio example, only if it really happened: 'In week 12 of my plan I had to ship payments by a fixed checkpoint. I cut the Healthie and PandaDoc integrations down to interfaces with fakes "
        "and postponed the customer portal, but kept idempotent webhooks, reconciliation and refunds as saga compensations, because those protect money and data. "
        "I wrote the cut and the new dates in my weekly update. [Afterwards: e.g., the portal took one day to add back because the interfaces were in place.]'",
        "Checkpoints 1-3 (cortes registrados em docs/checkpoints) ou caso real do mestrado.",
        "Use a regra do Shape Up: escopo varia, prazo e qualidade não. Mostre o critério da decisão.",
        "Semana 24 (rascunhos nas semanas 6, 11 e 19)",
    ),
    (
        "Q7. How do you use AI in your engineering workflow today? Be specific about tools and how you use them.",
        "I use Claude Code as my main agent and Codex for parallel and background tasks. Concretely: "
        "(1) Repo-level rules: an AGENTS.md is the single source of conventions (commands, layering rules, a 'never do' list, definition of done), loaded by both tools, "
        "and I update it every time I catch a repeated mistake. "
        "(2) Guardrails: permission deny rules for secrets and infrastructure paths, a hook that runs lint and tests before a task can finish, architecture tests (go-arch-lint, import-linter) in CI, "
        "and evals as a gate for the LLM extraction feature, so a prompt change only merges if the metrics improve. "
        "(3) Workflow: I write the plan first (plan mode or a PLANS.md), delegate scoped tasks, and run multi-agent loops where one session implements and a separate one writes adversarial tests "
        "without seeing the implementation. "
        "(4) Verification: I read every diff, run the tests and the race detector myself, break a test on purpose to confirm it can fail, and log what agents got wrong in docs/agent-reviews.md "
        "([N] entries so far; the most common misses were [non-deterministic workflow code, retries on non-idempotent calls, sensitive data in logs]).",
        "Labs AI-native semanais (item D), docs/agent-reviews.md, docs/how-i-use-ai.md (semana 24).",
        "Troque os colchetes por números do seu log. Não cite ferramenta que você não usou de fato.",
        "Semana 24 (rascunhos nas semanas 4, 13 e 20)",
    ),
]

CHECKLIST = [
    "Repositório público do LeaveFlow com README de portfólio (problema, arquitetura, como rodar, métricas, limitações e 'dados 100% fictícios')",
    "Vídeo demo de 3 min + walkthrough 'como um caso flui' (5 min)",
    "Design docs, ADRs, 3 postmortems, avaliação de lacunas e onboarding doc publicados em docs/",
    "docs/agent-reviews.md e docs/how-i-use-ai.md com exemplos reais (evidência para Q7)",
    "7 respostas finais revisadas (gramática + números reais nos colchetes)",
    "Vídeo de inglês Q5 com ≤3 min, gravado sem leitura, autoavaliado com a rubrica",
    "CV em inglês de 1 página com bullets de impacto (verbo + o quê + métrica) e link do portfólio",
    "LinkedIn em inglês alinhado ao CV; GitHub com projetos fixados e README de perfil",
    "Pelo menos 4 mocks feitos (2 comportamentais, 1 system design, 1 deep dive técnico) com notas de melhoria",
    "EF SET refeito (comparar com a semana 1) e certificado no LinkedIn, se o resultado ajudar",
    "Disponibilidade escrita: 8h-18h ET = 9h-19h ou 10h-20h em Brasília (conforme horário de verão nos EUA), plano para incidentes fora do horário",
    "Pesquisa de remuneração e modelo de contratação (contractor/PJ × EOR), valor mínimo aceitável e impostos estimados",
    "Lista de 20 vagas intermediárias-alvo (item H) e 3-5 candidaturas piloto enviadas antes desta vaga",
    "Decisão pessoal sobre o ritmo exigido (60+ h/semana com frequência) registrada antes de aplicar",
    "Custos do GCP desligados ou dentro do orçamento; nenhum segredo no repositório (rodar secret scanning)",
]
