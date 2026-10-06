# Road to Success: plano de 24 semanas para vagas de Backend / Engineering Lead

Plano de estudos completo para se preparar para vagas como **Engineering Lead: Backend Systems & Growth** (healthtech nos
EUA, stack Go/Python/TypeScript, GCP, Pub/Sub, Temporal, Stripe, Airtable, IA) e, no caminho, para vagas intermediárias
remotas de Software Engineer (backend, DevOps, MLOps) em empresas dos EUA.

| | |
|---|---|
| Duração | 24 semanas × 6 dias · 4 h técnicas + 1 h de inglês por dia |
| Horas | {{HORAS_TEC}} h técnicas ({{PCT_PRATICA}} prática) + {{HORAS_EN}} h de inglês |
| Cobertura | {{N_TOPICOS}} tópicos (todos os itens das seções 3 e 4 do pedido), cada um com semana e forma de comprovação |
| Projeto | **LeaveFlow**: intake e gestão de casos de afastamento médico com dados fictícios, construído semana a semana |
| Recursos | {{N_RECURSOS}} materiais com links conferidos em outubro de 2026, priorizando gratuitos e oficiais |

## Comece por aqui

1. Leia a [visão geral e as regras de ajuste](plano/00-visao-geral-e-ajuste.md) (10 min).
2. Importe as planilhas: [`planilhas/plano-de-estudos.xlsx`](planilhas/plano-de-estudos.xlsx) (todas as abas) ou os CSVs
   em [`planilhas/`](planilhas/) no Google Sheets. Instruções em [G](plano/G-cronograma.md).
3. **Semana 1:** faça os 17 exercícios de [diagnóstico](diagnostico/README.md) e preencha a aba Diagnóstico.
4. No sábado da semana 1, aplique as regras de ajuste e escreva o seu "plano ajustado v1".
5. A partir daí, siga a aba **Cronograma diário** e atualize a coluna Status todo dia. Checkpoints nas semanas 4, 8, 12, 16, 20 e 24.

## Mapa dos entregáveis

| Item pedido | Onde está |
|---|---|
| (0) Premissas, rotina, ajuste pós-diagnóstico, checkpoints, custos | [plano/00-visao-geral-e-ajuste.md](plano/00-visao-geral-e-ajuste.md) |
| A) Mapa de tópicos em trilhas | [plano/A-mapa-de-trilhas.md](plano/A-mapa-de-trilhas.md) |
| B) Banco de recursos | [plano/B-banco-de-recursos.md](plano/B-banco-de-recursos.md) · aba Recursos |
| C) Projeto de portfólio integrador (LeaveFlow) | [plano/C-projeto-portfolio.md](plano/C-projeto-portfolio.md) |
| D) Fluxo de trabalho AI-native | [plano/D-fluxo-ai-native.md](plano/D-fluxo-ai-native.md) |
| E) Liderança e soft skills | [plano/E-lideranca.md](plano/E-lideranca.md) |
| F) Inglês | [plano/F-ingles.md](plano/F-ingles.md) |
| G) Cronograma em planilha (6 abas + extra) | [plano/G-cronograma.md](plano/G-cronograma.md) · [planilhas/](planilhas/) |
| Matriz de cobertura (todos os tópicos) | [plano/matriz-de-cobertura.md](plano/matriz-de-cobertura.md) · aba Matriz de cobertura |
| Candidatura (7 respostas + checklist) | [plano/candidatura.md](plano/candidatura.md) · aba Candidatura |
| H) Análise honesta de distância e vagas intermediárias | [plano/H-analise-de-distancia.md](plano/H-analise-de-distancia.md) |
| Exercícios de diagnóstico, materiais e gabaritos | [diagnostico/](diagnostico/README.md) |

## Como o plano é mantido

Os dados (tópicos, trilhas, recursos, cronograma, diagnóstico, candidatura) ficam em [`scripts/plano/`](scripts/plano/).
O script [`scripts/gerar.py`](scripts/gerar.py) gera todos os CSVs, o XLSX e as tabelas dos documentos, e **falha** se:
algum dia não somar 4 h técnicas + 1 h de inglês; alguma semana tiver menos de 50% de prática; algum tópico ficar sem
semana; algum código de tópico, trilha ou recurso não existir; ou alguma trilha tiver menos de 2 ou mais de 4 recursos
principais. Para mudar o plano, edite os dados e rode:

```bash
pip install openpyxl   # única dependência
python3 scripts/gerar.py
```

Os materiais do diagnóstico foram testados: o SQL do D04 e o gabarito rodam no PostgreSQL 16, e o teste de regressão do
D10 falha no código original e passa com a correção do gabarito.
