<!-- Arquivo gerado por scripts/gerar.py — edite scripts/plano/templates/00-visao-geral-e-ajuste.md. -->

# 0) Visão geral, rotina e ajuste pós-diagnóstico

## 1. Premissas e números

| Item | Valor |
|---|---|
| Duração | 24 semanas × 6 dias = 144 dias |
| Tempo diário | 4 h técnicas + 1 h de inglês |
| Total | 576 h técnicas + 144 h de inglês |
| Prática no tempo técnico | **84%** (mínimo pedido: 50%; nenhuma semana fica abaixo disso) |
| Distribuição por modo | Projeto 58% · Escrita de artefatos 13% · Estudo (leitura/vídeo) 12% · Labs guiados 9% · Revisão de agentes 4% · Reforço flex 4% |
| Liderança e comunicação (T15) | 10,8% nas semanas 3-22 (alvo ~10%); 12,0% no total, porque as semanas 1, 2, 23 e 24 concentram diagnóstico, planejamento e avaliação de lacunas |
| Tópicos cobertos | 238 (98 da seção 4 + 140 da seção 3), cada um com pelo menos uma semana |
| Recursos | 146 links conferidos em outubro de 2026 (principais + apoio) |

**Sobre os "81 itens".** O pedido fala em 81 itens no checklist, mas a lista colada tem 98. Todos os 98 estão na
[matriz de cobertura](matriz-de-cobertura.md), além de 140 tópicos extraídos da descrição da vaga (seção 3).

**Prática vs. estudo.** O plano é deliberadamente de construção: a teoria entra "na hora certa" (leitura dirigida às quartas,
capítulos ligados ao que está sendo construído e documentação oficial dentro dos blocos de projeto). Se o diagnóstico mostrar
base fraca em um tema, a regra de ajuste abaixo troca horas de projeto por estudo nesse tema.

**Dados.** O projeto usa **apenas dados fictícios** (Faker e documentos sintéticos). Nunca use dados reais de pacientes,
nem os seus. Isso também é parte da avaliação "cuidado instintivo com dados sensíveis".

## 2. Rotina sugerida (horário de Brasília)

A vaga exige 8 h de sobreposição com 8h-18h ET. Isso equivale a **9h-19h em Brasília** quando os EUA estão em horário de
verão (EDT, mar-nov) e **10h-20h** no resto do ano (EST). Treinar nesse horário desde já ajuda.

| Horário | Bloco | Observação |
|---|---|---|
| 09:00-11:00 | Técnico 1 (estudo, lab ou projeto) | Cabeça fresca para o que é mais difícil do dia |
| 11:15-13:15 | Técnico 2 (projeto/escrita) | Commit no fim do bloco |
| 14:00-15:00 | Inglês | Os 10 min finais (seg-sex) são o update diário em inglês |
| fim do dia | 5 min | Atualizar a coluna **Status** do cronograma |

Ajuste ao mestrado: 30 h/semana somadas ao mestrado é muito. Se a carga do CIn apertar numa semana, consuma primeiro o
**reforço flex**, depois os itens "o que pular se atrasar" do [mapa de trilhas](A-mapa-de-trilhas.md). Nunca pule os
checkpoints, o vídeo semanal nem o update diário.

## 3. Ajuste pós-diagnóstico

### 3.1 Pontuação

1. Faça os 17 exercícios da semana 1 (enunciados em [`diagnostico/exercicios.md`](../diagnostico/exercicios.md)).
2. Registre o nível de cada um na aba **Diagnóstico**: Iniciante = 1, Intermediário = 2, Avançado = 3.
3. Para cada trilha, use a **menor** nota dos exercícios que a medem (coluna *Trilhas afetadas*). Ex.: T01 = mín(D01, D02, D03, D05).
4. Copie o nível para a coluna *Nível no diagnóstico* da Matriz (cada tópico aponta para o seu exercício).

### 3.2 Regras de ajuste (aplicar na semana 1, sábado, e revisar na semana 2)

| Situação | O que fazer | Por quê |
|---|---|---|
| Trilha **essencial** com nota 1 | (a) A semana 2 vira fundamentos dessa trilha (os blocos de "refazer diagnóstico" e o bloco de Tour of Go/pgexercises/TS são trocados pelo recurso principal dela). (b) Os 4 próximos blocos de reforço flex (sábados) vão para ela. (c) Se ainda for 1 no refazer da semana 2, converta 1 h/semana de **projeto** dessa trilha em **estudo** nas 4 semanas seguintes. | Construir sobre base fraca gera retrabalho; o projeto continua, só que mais devagar. |
| Trilha com nota 3 | Os blocos de **estudo** dela viram opcionais e as horas liberadas vão para a trilha essencial de menor nota. Os blocos de **projeto** ficam (são a evidência do portfólio). | Não gastar tempo aprendendo o que já sabe; manter a prova prática. |
| Trilha recomendada/opcional com nota 1 | Nada muda na semana 2. Se atrasar, aplique primeiro os cortes do mapa de trilhas. | Recomendadas nunca tiram horas das essenciais. |
| Inglês (D17) ≤ B1 | Até a semana 8: troque a conversa de sexta por conversação guiada (professor ou parceiro) e acrescente 10 min de shadowing na terça. | Fluência é requisito eliminatório da vaga. |
| Inglês ≥ C1 | Troque a pronúncia de segunda por um mock extra a partir da semana 5. | Converter vantagem em prática de entrevista. |
| Duas ou mais essenciais com nota 1 | Reduza o escopo do projeto: Healthie, PandaDoc, Cognito, Klaviyo, VWO e Snowflake saem; Terraform vira gcloud scriptado; Growth (semanas 21-22) fica só com o A/B e o tracking server-side. Isso libera ~20 h. | Protege as trilhas que a vaga mais cobra. |

### 3.3 Exemplo de ajuste

Resultado hipotético: D01 Python = 3, D02 Go = 1, D04 SQL = 2, D09 Cloud = 1, D17 = B2.

- **Semana 2:** o bloco "refazer diagnóstico" vira Learn Go with Tests (2 h); o Tour of Go continua (2 h).
- **Flex dos sábados, semanas 3-6:** Go (semanas 3-4) e Cloud Run (semanas 5-6).
- **Python = 3:** o flex da semana 3 (previsto para typing/pydantic) vai para Go; o intake-legacy continua em Python
  porque é evidência de portfólio. A leitura de Cosmic Python fica: ela é sobre arquitetura, não sobre a linguagem.
- **Refazer na semana 2** (variante do D02): se Go continuar 1, a quinta da semana 4 passa a ter 2 h de estudo (Effective Go +
  Learn Go with Tests) e 2 h de projeto, nas semanas 4 a 7.
- Registre a decisão em `docs/plano-ajustado-v1.md` (é um ADR do seu próprio plano).

## 4. Checkpoints (semanas 4, 8, 12, 16, 20, 24)

No bloco de liderança de sábado (1,5 h):

1. Atualize a coluna do checkpoint na Matriz (*CP sem. N*) para os tópicos trabalhados no ciclo.
2. Some as horas reais (coluna Status) e compare com o plano. Atraso > 10%? Aplique cortes do mapa de trilhas.
3. Refaça uma variante curta (30 min) do exercício de diagnóstico do grupo mais fraco.
4. Escreva `docs/checkpoints/cpN.md`: o que foi entregue, o que não foi, o que muda, novo prazo (o formato de aviso de risco da vaga).
5. Replaneje as 4 semanas seguintes (quais flex vão para onde).

## 5. Custos e guarda-corpos

- Alertas de orçamento do GCP desde o dia 1 (US$10/25/50). Cloud SQL no menor tier e **parado quando não estiver em uso**;
  desenvolvimento diário com Postgres local em Docker.
- Free tier do GCP cobre a maior parte de Cloud Run, Pub/Sub, BigQuery e Cloud Build neste volume
  ([página oficial](https://cloud.google.com/free)); confira os limites atuais antes de começar.
- Temporal Cloud: créditos para novos usuários ([anúncio oficial](https://temporal.io/blog/get-usd1-000-in-free-credits-and-build-better-workflows-with-temporal-cloud), exige cartão).
  Plano B: dev server local + vídeo da execução.
- Airtable Free: 1.000 chamadas de API por mês por workspace e 5 req/s por base
  ([limites](https://support.airtable.com/docs/managing-api-call-limits-in-airtable)). Por isso o ops-sync tem um adapter fake
  para desenvolvimento e testes de carga; a base real fica para testes ponta a ponta.
- Stripe sempre em modo de teste. Document AI e Gemini: 30 documentos sintéticos custam pouco, mas acompanhe no billing.
- Semana 24: desligue tudo que gera custo.
