# F) Trilha de inglês (1 h/dia, fora das 4 h técnicas)

Foco: **falar com fluência sobre o seu trabalho técnico** e passar em entrevistas comportamentais e técnicas, além de
escrever docs e updates em inglês. Total: {{HORAS_EN}} h. A semana 1 é diagnóstico (D17); da 2 à 24 a estrutura é fixa:

| Dia | Atividade (50 min) | + 10 min (seg-sex) |
|---|---|---|
| Seg | Pronúncia e fluência: shadowing (Rachel's English) + 10 termos da semana no YouGlish | Update diário em inglês |
| Ter | Escuta → fala: episódio/talk técnico e resumo oral gravado de 2 min (semanas 21-24: mock extra) | Update diário |
| Qua | STAR: escrever/refinar uma das 7 respostas e falar 3× cronometrado | Update diário |
| Qui | Escrita técnica: o documento da semana em inglês (design doc, ADR, runbook...) | Update diário |
| Sex | Conversação/mock (self-mock nas semanas 2-8; mocks com pares a partir da 9) | Update diário |
| Sáb | **Vídeo semanal de 2-3 min** sobre algo do projeto + autoavaliação com rubrica | — |

## Semana a semana

{{TABELA_INGLES}}

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
