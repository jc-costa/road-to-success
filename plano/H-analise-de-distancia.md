# H) Análise honesta de distância

## Resumo

O plano fecha boa parte da **distância técnica**: em 24 semanas dá para chegar a um nível em que você explica, constrói e
revisa os padrões que a vaga cita (outbox, sagas no Temporal, CQRS, idempotência, reconciliação, sync com Airtable, LLM com
revisão humana) e mostra isso num portfólio sério. O que o plano **não** fecha é a **distância de experiência**: anos sendo
dono de sistemas reais, com dinheiro e pacientes reais, plantão de incidentes e pessoas sob sua responsabilidade.

Pelo critério da vaga (7+ anos, 2+ anos dono de sistemas event-driven em produção, liderança de engenheiros), você está,
honestamente, **a alguns anos** desta posição específica. Tratá-la como estrela-guia e mirar vagas intermediárias com stack
parecida é o caminho mais rápido até ela.

## Requisito por requisito

| Requisito da vaga | Onde você está (com o plano concluído) | Lacuna real | Como fechar |
|---|---|---|---|
| 7+ anos de engenharia de software | Graduação + mestrado + experiência de pesquisa/projetos | Grande; estudo não substitui anos | Tempo com escopo crescente; contar experiência de pesquisa com honestidade |
| 2+ anos dono de sistemas event-driven em produção | Portfólio que reproduz a arquitetura (staging/prd próprios, sem usuários reais) | Grande: não há tráfego, incidentes nem consequências reais | Próximo emprego: ser dono de serviços em produção com on-call |
| Experiência em startup / ambiente rápido | Simulada (ritmo semanal, cortes de escopo, stakeholders) | Média | Próximo emprego em startup pequena (seed a Série B) |
| APIs, webhooks, bancos, integrações, event-driven | Intermediário-avançado demonstrável | Pequena no conhecimento; média em escala | Projeto + entrevistas técnicas + produção real |
| Full stack quando necessário | Intermediário (Next.js, funil, console) | Pequena/média | Mais horas em frontend no emprego |
| Liderou/mentorou engenheiros | Simulações + (recomendado) mentoria real no CIn/open source | Grande | Mentorar 1-2 pessoas já; buscar papel de "tech lead informal" depois |
| Cuidado com dados sensíveis | Práticas estilo HIPAA com dados fictícios | Média: não houve PHI real nem auditoria | Trabalhar em healthtech/fintech; manter a disciplina |
| Uso intenso de agentes de IA | Forte, com harness, guardrails e métricas | Pequena | É hoje um diferencial real seu: documente bem |
| Inglês fluente | Depende do diagnóstico (D17) | A medir | Trilha F; EF SET na semana 24 |
| Diferencial: LLM + HITL em produção | Portfólio com evals e análise de falhas | Média (não é produção) | Primeira feature de IA no emprego; manter o hábito de evals |
| Diferencial: pagamentos/assinaturas em produção | Stripe completo em modo de teste | Média | Produção real no emprego |
| Diferencial: workflow engines | Temporal 101/102/Versioning + saga real no projeto | Pequena/média | Usar Temporal em produção |
| Diferencial: HIPAA/PHI em produção | Simulado | Grande | Healthtech |
| Cultura: 60+ h/semana com frequência | Decisão pessoal | — | Decida antes de aplicar (veja abaixo) |

## O que o plano não consegue provar (e como falar disso)

- **Produção real.** Diga "portfolio system with synthetic data and Stripe test mode". Nunca transforme o LeaveFlow em
  "sistema com usuários". Entrevistadores percebem, e a vaga valoriza integridade explicitamente.
- **Métricas.** Use as métricas do projeto pelo que são: latência medida em teste de carga, paridade da migração, defeitos
  pegos em revisão de agentes. Elas mostram método, não escala.
- **Liderança.** Simulações mostram como você escreve e pensa; a mentoria real (mesmo pequena) é o que responde à pergunta
  "already led or mentored engineers".

## Vagas intermediárias para mirar enquanto segue o plano

| Título (palavras-chave de busca) | Por que encaixa | O que destacar |
|---|---|---|
| Backend Engineer (Go/Python), mid-level, remote LATAM | Núcleo da vaga-alvo em escala menor | LeaveFlow (case-service, billing, outbox), idempotência, testes |
| Software Engineer, Integrations / Integration Engineer | 20+ integrações é o dia a dia da vaga-alvo | Kit de integração, Stripe, Airtable, webhooks, reconciliação |
| Platform / DevOps Engineer (GCP, Cloud Run, CI/CD) | DevOps é um dos seus objetivos; confiabilidade é metade da vaga | Cloud Build, staging/prd, SLOs, game days, custo |
| Workflow / Automation Engineer ("Temporal", "event-driven") | Diferencial direto da vaga-alvo | CaseLifecycle, sagas, versionamento, replay tests |
| Data / Analytics Engineer (BigQuery, dbt) | Porta adjacente; reconciliação e qualidade de dados | dbt com testes, contrato de dados, dashboards |
| MLOps / AI Engineer (Python, Vertex AI, evals) | Usa o mestrado e o Form Filler | Evals, HITL, análise de erros, privacidade |
| Forward Deployed / Solutions Engineer (healthtech, fintech) | Integrações + contato com clientes internos/externos | Airtable/Ops como cliente, comunicação escrita |
| No Brasil: backend em fintech/healthtech com arquitetura event-driven | Ponte mais provável para "2 anos dono de produção" | Mesmo portfólio; inglês como vantagem |

**Canais.** Plataformas que conectam engenheiros da América Latina a empresas dos EUA, como a
[Revelo](https://careers.revelo.com/) (que informa vagas full-time de até US$ 95 mil/ano e exige 3+ anos de experiência) e a
[Strider](https://onstrider.com/); LinkedIn em inglês; candidatura direta em startups que usam o mesmo stack. Repare que a
faixa da vaga-alvo (US$ 120-140 mil) é de nível sênior/lead; para mid-level remoto a partir do Brasil, espere valores menores
e entenda a diferença entre contrato como contractor/PJ e contratação via EOR (impostos, férias, benefícios) antes de negociar.

## Trajetória sugerida

| Período | Meta | Evidência que você acumula |
|---|---|---|
| Meses 0-6 (este plano) | Portfólio + inglês + candidaturas a vagas intermediárias | LeaveFlow, docs, respostas, mocks |
| Meses 6-24 | Ser dono de 1-2 serviços em produção, com on-call | Incidentes resolvidos, postmortems, métricas reais, 1 mentoria |
| Anos 2-4 | Senior / tech lead informal em startup event-driven | Iniciativas lideradas, decisões de arquitetura, juniores orientados |
| Anos 4-6+ | Engineering Lead como o desta vaga | Sistema e pessoas sob sua responsabilidade, resultados de negócio |

Os anos importam por um motivo concreto: reconhecer padrões de incidente, calibrar trade-offs sob pressão e liderar pessoas
são habilidades que só se formam com exposição repetida. Alta ownership acelera a curva, mas não elimina etapas.

## Vale aplicar para esta vaga agora?

Pode aplicar, desde que com expectativa baixa e enquadramento honesto: a descrição pede 7+ anos e startups raramente
flexibilizam isso para um cargo de lead. Use a candidatura como exercício (as 7 perguntas são excelentes para treinar
narrativa) e priorize as vagas intermediárias. Antes de aplicar a qualquer vaga deste perfil, decida conscientemente sobre
o ritmo: a própria vaga diz que não serve para quem quer horários previsíveis e cita 60+ h/semana com frequência,
o que pesa somado ao mestrado.

## Riscos deste plano e mitigação

| Risco | Mitigação |
|---|---|
| 30 h/semana + mestrado → cansaço e abandono | Reforço flex e cortes do mapa de trilhas; nunca cortar sono para cumprir o plano |
| Custo de nuvem fugir do controle | Alertas de orçamento, Cloud SQL parado, adapters fake, desligar tudo na semana 24 |
| Escopo do LeaveFlow crescer demais | Regra: peça nova só com ADR; opcionais (Healthie, PandaDoc, Cognito, Klaviyo, VWO, Snowflake) são os primeiros a sair |
| Diagnóstico errado (nível super ou subestimado) | Refazer variantes nos checkpoints; na dúvida, marcar o nível menor |
| Inglês travar entrevistas | Vídeo semanal obrigatório, mocks com pares desde a semana 9, EF SET no fim para medir |
