# E) Trilha de liderança e soft skills

**Tempo:** quarta 1 h + sábado 1,5 h nas semanas 3-22 = {{T15_PCT_REGULAR}} do tempo técnico (alvo ~10%).
No total, {{T15_HORAS}} h ({{T15_PCT}}), porque as semanas 1, 2, 23 e 24 concentram diagnóstico, planejamento,
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

{{TABELA_LIDERANCA}}

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
