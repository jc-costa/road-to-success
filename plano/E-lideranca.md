<!-- Arquivo gerado por scripts/gerar.py — edite scripts/plano/templates/E-lideranca.md. -->

# E) Trilha de liderança e soft skills

**Tempo:** quarta 1 h + sábado 1,5 h nas semanas 3-22 = 10,8% do tempo técnico (alvo ~10%).
No total, 69 h (12,0%), porque as semanas 1, 2, 23 e 24 concentram diagnóstico, planejamento,
avaliação de lacunas e plano 30-60-90. Quase tudo é **escrita de artefatos reais** do projeto, não leitura.

## Personagens simulados

Você vai "trabalhar" com estes papéis (todos fictícios). Escreva para eles como escreveria numa startup remota.

| Papel | O que pede | Como você responde |
|---|---|---|
| Liderança (CEO/CTO) | Prioridades de negócio e prazos | Update semanal, status report, comunicação de risco |
| Head of Growth | Testes de preço, funil, tracking "para amanhã" | Plano mínimo viável, trade-offs, prazo realista |
| Frontend Growth Engineer | Contratos de API, eventos | Specs de eventos e APIs, revisões |
| Ops lead | Menos trabalho manual, nada de surpresa na Single Queue | Observar antes de automatizar, mensagens de mudança, runbooks |
| Engenheiro(a) júnior | Tarefas, revisão, desbloqueio, crescimento | Briefs com critério de pronto, revisões didáticas, 1:1, coaching |

**Como gerar o "PR do júnior" com erros plantados:** numa sessão separada, peça a um agente para implementar a tarefa
"como um dev júnior com pouca experiência, incluindo 5-7 erros realistas" das categorias que você quer treinar
(idempotência, segredos, PHI em log, tratamento de erro, testes, escopo), e para **salvar a lista de erros num arquivo que
você não vai abrir**. Revise o PR sem ver a lista; depois compare e registre quantos você achou (como no D13).

## Templates (copie para `docs/templates/` no LeaveFlow)

**Update diário (inglês, ≤6 linhas, todo dia útil)**
```
Progress: <o que entrou, com link>
Working: <o que está funcionando/validado>
Not working: <o que falhou e o que você já tentou>
Next: <próximo passo concreto>
Risks/asks: <bloqueio ou pedido, se houver>
```

**Comunicação de risco/atraso** (o formato da vaga)
```
What happened: <fato, sem rodeio>
What changes: <escopo/qualidade/prazo afetados e opções>
New date: <data realista + o que precisa ser verdade para cumpri-la>
What I need: <decisão ou ajuda de quem lê>
```

**Design doc (1-2 páginas):** contexto e problema · objetivos e não-objetivos · proposta · alternativas com trade-offs ·
modos de falha e comportamento seguro · plano em marcos com critério de pronto · riscos · perguntas em aberto.
Referência: [Design Docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/).

**ADR curto:** título · status · contexto · decisão · alternativas · consequências (inclua "o que não faremos agora").
Templates: [adr.github.io](https://adr.github.io/adr-templates/).

**Postmortem blameless:** resumo · impacto · timeline · causa raiz e fatores contribuintes · o que funcionou · ações
sistêmicas com dono e prazo. Guia: [PagerDuty](https://postmortems.pagerduty.com/).

**Brief de delegação:** objetivo de negócio · escopo e fora de escopo · restrições (dados sensíveis, idempotência) ·
critério de pronto · pontos de verificação (quando você revisa) · como pedir ajuda · prazo e por que esse prazo.

**Comentário de revisão (Feedback Equation):** observação + impacto + pergunta ou pedido, com rótulo BLOQUEANTE /
SUGESTÃO / NIT / ELOGIO. Guias: [Lara Hogan](https://larahogan.me/resources/feedback/) e
[Google eng-practices](https://google.github.io/eng-practices/review/reviewer/comments.html).

**1:1 (30 min):** como a pessoa está · bloqueios · feedback nos dois sentidos · crescimento (1 habilidade por mês) ·
combinados. Recursos: [Lara Hogan, one-on-ones](https://larahogan.me/resources/one-on-ones/).

**Priorização com trade-offs:** para cada pedido, impacto no negócio, esforço, risco, custo de atrasar e o que sai do
escopo para caber; termine com a recomendação e o que você precisa que o stakeholder decida.
Base: [Shape Up](https://basecamp.com/shapeup) (apetite fixo, escopo variável).

## Blocos de liderança, semana a semana

| Semana | Dia | Horas | Atividade concreta | Entregável |
|---|---|---|---|---|
| 1 | 3 (Qua) | 1 | D13 Liderança: revisar o PR do júnior + roteiro de 1:1 | Comentários + roteiro + nível D13 |
| 1 | 3 (Qua) | 1 | D14 Comunicação: design doc de 1 página + update + mensagem de atraso | 3 textos + nível D14 |
| 1 | 5 (Sex) | 1 | Shape Up: 'Principles of Shaping' e 'Set Boundaries' (appetite) — base para cortar escopo | Notas: 5 ideias aplicáveis ao plano |
| 1 | 6 (Sáb) | 1,5 | Calibração: aplicar as regras de ajuste (item 0) e escrever 'Plano ajustado v1' (o que ganha/perde horas e por quê) | docs/plano-ajustado-v1.md |
| 2 | 3 (Qua) | 1 | Doc 'Fluxo de um caso v0' (1 página, hipótese a validar nas próximas semanas) | docs/fluxo-do-caso-v0.md |
| 2 | 6 (Sáb) | 1,5 | Design doc #1: LeaveFlow — problema, escopo, não-objetivos, contextos, marcos das 24 semanas, riscos | docs/design-docs/001-leaveflow.md |
| 2 | 6 (Sáb) | 1,5 | Registro de riscos v0 + plano de comunicação (CEO, Growth, Ops, júnior: o quê, quando, por qual canal) | docs/riscos.md + docs/comunicacao.md |
| 3 | 3 (Qua) | 1 | Design doc #2 (1 página): 'Por que o legado é assim' — limites e dívidas conhecidas (base da migração) | docs/design-docs/002-legado.md |
| 3 | 6 (Sáb) | 1,5 | Retro semanal + update semanal para o 'CEO' + atualizar Status no cronograma | docs/updates/semana-03.md |
| 4 | 3 (Qua) | 1 | ADR-001: idempotência via tabela de chaves (alternativas: Redis, chave natural) com trade-offs | docs/adr/001-idempotencia.md |
| 4 | 6 (Sáb) | 1,5 | Checkpoint 1: atualizar a Matriz (nível atual), horas reais × plano, replanejar 4 semanas e decidir cortes | docs/checkpoints/cp1.md |
| 5 | 3 (Qua) | 1 | Runbook de release v1: checklist pré/pós deploy, rollback por revisão do Cloud Run, quem avisar | docs/runbooks/release.md |
| 5 | 6 (Sáb) | 1,5 | Update semanal + registro de riscos (custo GCP, trial do Temporal Cloud, cota do Airtable Free) | docs/updates/semana-05.md |
| 6 | 3 (Qua) | 1 | Design doc #3: 'Padrão de integração LeaveFlow' (inbox, retries, DLQ, idempotência) escrito para o júnior seguir | docs/design-docs/003-integracoes.md |
| 6 | 6 (Sáb) | 1,5 | Simulação júnior #1: revisar PR 'do júnior' gerado com 6 erros plantados (retry não idempotente, segredo em log...) usando a Feedback Equation | Revisão escrita + o que ensinar |
| 7 | 3 (Qua) | 1 | ADR-003: limites dos bounded contexts e o que NÃO separar agora (monólito modular × serviços) | docs/adr/003-bounded-contexts.md |
| 7 | 6 (Sáb) | 1,5 | 1:1 simulado com o 'júnior' (roteiro: objetivos, bloqueios, feedback, plano de crescimento) | docs/lideranca/1on1-01.md |
| 8 | 3 (Qua) | 1 | Postmortem simulado #1 (blameless): 'mensagem duplicada gerou e-mail duplo' — timeline, causa raiz, correção sistêmica | docs/postmortems/001.md |
| 8 | 6 (Sáb) | 1,5 | Checkpoint 2: Matriz + horas; se houver atraso, mensagem de risco (o que aconteceu, o que muda, novo prazo) | docs/checkpoints/cp2.md |
| 9 | 3 (Qua) | 1 | Design doc #4: CaseLifecycle — estados, sinais, timeouts; o que fica no workflow × no agregado | docs/design-docs/004-caselifecycle.md |
| 9 | 6 (Sáb) | 1,5 | Update semanal + plano das próximas 2 semanas com trade-offs (velocidade × escopo × qualidade) | docs/updates/semana-09.md |
| 10 | 3 (Qua) | 1 | ADR-004: CQRS só onde paga (read models para Ops e analytics) e quando NÃO usar | docs/adr/004-cqrs.md |
| 10 | 6 (Sáb) | 1,5 | Simulação júnior #2: júnior travado em bug de não-determinismo — mensagem de desbloqueio com perguntas de coaching (sem dar a resposta) | docs/lideranca/desbloqueio-01.md |
| 11 | 3 (Qua) | 1 | Plano de iniciativa grande (formato 60 dias): objetivo de negócio, restrições, limites do sistema atual, alternativas (big-bang × strangler × dual-write), plano até produção, riscos | docs/design-docs/005-migracao.md |
| 11 | 4 (Qui) | 1 | Premortem da migração (HBR): 10 modos de falha e mitigação | Seção de riscos do plano |
| 11 | 6 (Sáb) | 1,5 | Status report da iniciativa para stakeholders (1 página) com a decisão pedida (go/no-go para 50%) | docs/updates/status-migracao.md |
| 12 | 3 (Qua) | 1 | Design doc #5: pagamentos — estados e falhas (recusa, webhook atrasado, duplicado) e o que acontece com o caso em cada uma | docs/design-docs/006-pagamentos.md |
| 12 | 6 (Sáb) | 1,5 | Checkpoint 3: Matriz, horas, replanejamento; decidir o que vira opcional (valor > perfeição) | docs/checkpoints/cp3.md |
| 13 | 3 (Qua) | 1 | Runbook 'discrepância de pagamento' (investigação, quem avisar, correção caso a caso) | docs/runbooks/discrepancia-pagamento.md |
| 13 | 6 (Sáb) | 1,5 | Simulação: Head of Growth pede 'teste de preço amanhã' — responder com plano mínimo viável, riscos e prazo realista | Resposta escrita |
| 14 | 3 (Qua) | 1 | ADR-005: projeção event-driven + reconciliação periódica; orçamento de chamadas de API | docs/adr/005-sync-airtable.md |
| 14 | 6 (Sáb) | 1,5 | Update semanal + mensagem de alinhamento para Ops (o que muda no dia a dia, o que não muda, como reportar problemas) | docs/updates/semana-14.md |
| 15 | 3 (Qua) | 1 | Runbook de recuperação caso a caso (DLQ, diff, replay, verificação com Ops) + comunicação com Ops durante incidente | docs/runbooks/recuperacao-airtable.md |
| 15 | 6 (Sáb) | 1,5 | Postmortem do game day (blameless) + 3 correções sistêmicas priorizadas | docs/postmortems/002.md |
| 16 | 3 (Qua) | 1 | ADR-006: Document AI × Gemini × híbrido (precisão, custo, privacidade/BAA, latência) | docs/adr/006-extracao.md |
| 16 | 6 (Sáb) | 1,5 | Checkpoint 4 + brief de delegação: 'o Form Filler é do júnior' — escopo, critérios de pronto, pontos de verificação | docs/checkpoints/cp4.md + docs/lideranca/delegacao-form-filler.md |
| 17 | 3 (Qua) | 1 | Leitura dirigida: Google eng-practices, guia de code review (padrão de revisão e comentários) | Checklist de revisão para o júnior |
| 17 | 3 (Qua) | 1 | Doc 'Onde o AI Form Filler falhou, o que aprendi, como melhorei' (vira evidência para a candidatura) | docs/form-filler-licoes.md |
| 17 | 6 (Sáb) | 1,5 | Simulação júnior #3: PR do júnior no Form Filler com erros plantados (PHI em log, limiar fixo no código, sem teste) — revisão + coaching | Revisão escrita |
| 18 | 3 (Qua) | 1 | Runbooks por alerta (significado, impacto, primeiros 5 min, escalonamento) como padrão do repositório | docs/runbooks/alertas.md |
| 18 | 6 (Sáb) | 1,5 | Update semanal + relatório técnico de confiabilidade (SLOs atuais, lacunas, próximos passos) | docs/relatorios/confiabilidade.md |
| 19 | 3 (Qua) | 1 | Contrato de dados (eventos → BigQuery): donos, SLAs de frescor, mudanças compatíveis | docs/contrato-de-dados.md |
| 19 | 6 (Sáb) | 1,5 | Relatório para Growth/Ops: o que os dados dizem e suas limitações | docs/relatorios/dados-semana-19.md |
| 20 | 3 (Qua) | 1 | Política de tratamento de dados (1 página) + checklist de PR 'dados sensíveis' para júnior e agentes | docs/seguranca/politica-dados.md |
| 20 | 6 (Sáb) | 1,5 | Checkpoint 5: Matriz, horas; postmortem do game day publicado; replanejar as 4 semanas finais | docs/checkpoints/cp5.md + docs/postmortems/003.md |
| 21 | 3 (Qua) | 1 | Brief do experimento com Growth: hipótese, métrica primária, guardrails, tamanho de amostra, duração, critério de decisão | docs/growth/brief-exp-01.md |
| 21 | 6 (Sáb) | 1,5 | Update semanal + alinhamento com o 'Head of Growth' sobre o que é confiável medir (limites de atribuição) | docs/updates/semana-21.md |
| 22 | 3 (Qua) | 1 | Relatório do experimento para stakeholders (decisão, aprendizado, próximo teste) | docs/growth/relatorio-exp-01.md |
| 22 | 6 (Sáb) | 1,5 | Simulação: pedidos conflitantes de Growth e Ops na mesma semana — priorização escrita com trade-offs e comunicação para ambos | docs/lideranca/priorizacao-01.md |
| 23 | 1 (Seg) | 2 | Avaliação de lacunas (formato da vaga): arquitetura, confiabilidade, execução; o que corrigir primeiro e por quê (impacto × esforço × risco) | docs/avaliacao-de-lacunas.md |
| 23 | 3 (Qua) | 1 | Onboarding doc para um júnior (setup, arquitetura, como contribuir, padrões de revisão) | docs/onboarding.md |
| 23 | 6 (Sáb) | 1,5 | 3 oportunidades de alto valor não pedidas, com estimativa de impacto | docs/propostas.md |
| 23 | 6 (Sáb) | 1,5 | Update semanal + retrospectiva das 23 semanas (ciclos, releases, comunicação, accountability) | docs/retro-final.md |
| 24 | 3 (Qua) | 1 | Plano 30-60-90 pessoal para uma vaga como esta (2 primeiras semanas em detalhe) | docs/carreira/plano-30-60-90.md |
| 24 | 6 (Sáb) | 1,5 | Checkpoint 6 final: Matriz (nível final), análise de distância atualizada, plano dos próximos 3 meses | docs/checkpoints/cp6.md |

## Prática real (fora do simulado)

O requisito "já liderou ou mentorou engenheiros" pede experiência real. Durante as 24 semanas, consiga pelo menos uma:

- Mentorar um aluno de graduação do CIn (monitoria, iniciação científica, projeto de disciplina) com 1:1 quinzenal e
  revisão de código: anote o que mudou no trabalho da pessoa.
- Revisar PRs num projeto open source com regularidade (comentários educados e específicos, como nos templates).
- Pedir ao seu orientador ou a um colega sênior que revise um design doc seu e registrar o feedback.

## Autoavaliação dos artefatos (nos checkpoints)

| Pergunta | Sim/Não |
|---|---|
| Um leitor sem contexto entende o problema e a decisão em 2 minutos? | |
| Há alternativas reais com trade-offs, não só a escolhida? | |
| Os riscos têm sinal de alerta precoce e mitigação? | |
| Prazos e compromissos foram cumpridos ou avisados **antes** de estourar? | |
| O feedback ao júnior ensina o padrão em vez de só apontar o erro? | |
