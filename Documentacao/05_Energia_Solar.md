# 05. Energia Solar Fotovoltaica (Fase 5)

## Resumo
Implantação de uma usina solar fotovoltaica de **28 kWp** para suprir a demanda energética total do projeto (sopradores, bomba de calor, automação, bombas de recirculação e fábrica de ração), reduzindo a conta de luz para a taxa mínima e aumentando o lucro operacional.

## Demanda Energética do Projeto
A operação do sistema RJ Piscicultura consome energia de forma contínua:

| Equipamento | Potência Média (kW) | Horas/dia | kWh/mês |
| :--- | :---: | :---: | :---: |
| Sopradores (2 × 2CV, com inverter) | 1,80 | 24 | 1.296 |
| Bomba de Calor (média anual) | 1,40 | 24 | 997 |
| CLP, sensores, alimentadores | 0,28 | 24 | 200 |
| **LEDs Fotoperíodo (6 tanques × 50 W = 300 W)** | **0,30** | **16** | **144** |
| **Bombas de Recirculação (6 × 0,5 CV c/ VFD — média ~160 W = 0,96 kW)** | **0,96** | **24** | **691** |
| **TOTAL** | **4,74** | | **3.328 kWh/mês** |

*Custo estimado mensal na tarifa CEMIG (R$ 0,85/kWh):* **~R$ 2.829/mês** (inclui LEDs e Bombas de Recirculação ativos desde a Fase 1; cobertos pela solar na Fase 5).

## Dimensionamento do Sistema
Belo Horizonte possui excelente irradiação solar, com média de **5,0 Horas de Sol Pico (HSP)** por dia ao longo do ano.

- **Consumo alvo:** 3.328 kWh/mês (inclui LEDs fotoperíodo + Bombas de Recirculação 0,5 CV c/ VFD)
- **Fator de perdas do sistema:** 20% (rendimento de 80%)
- **Cálculo da Potência:** `3.328 / (5,0 × 30 × 0,80) = 27,7 kWp → arredondado para **28 kWp***`

> *Um sistema de 28 kWp gera ~3.360 kWh/mês (5,0 HSP × 30 dias × 0,80), cobrindo 101% da demanda. O upgrade das Bombas de Recirculação de 0,1 CV para 0,5 CV c/ VFD elevou o consumo de 332 kWh para 691 kWh/mês (+359 kWh), exigindo redimensionamento de 25 kWp para 28 kWp.*

### Especificação Recomendada
- **Potência instalada:** 28 kWp
- **Painéis:** ~51 módulos de 550W (tecnologia Monocristalino TOPCon para maior eficiência).
- **Inversor:** 1 inversor string de 30 kW.
- **Área necessária:** ~148 m² de telhado (livre de sombreamento) ou estrutura de solo.

## Impacto da Legislação (Lei 14.300 - Marco Legal da GD)
Como o projeto consome energia 24h por dia e o sol gera apenas durante o dia (~10h), estima-se que **45% do consumo será simultâneo** à geração (sem taxas) e **55% será injetado na rede** e compensado à noite.

A energia injetada está sujeita à cobrança do **Fio B** (uso da rede de distribuição):
- **Cenário atual (2026):** O produtor paga 60% do valor do Fio B sobre a energia compensada.
- Isso significa que o crédito gerado na rede da CEMIG vale cerca de 75% da tarifa cheia.
- Apesar da taxação, a economia efetiva no OPEX é superior a **85%**. A conta cairá do patamar de R$ 2.523 para apenas a **taxa mínima de disponibilidade + iluminação pública** (estimada em ~R$ 290/mês para tarifa rural trifásica).

## Benefício Financeiro
- **Economia mensal:** ~R$ 2.539/mês (R$ 2.829 − R$ 290 taxa mínima rural trifásica)
- **Economia anual:** ~R$ 30.468/ano
- **Payback da usina solar (28 kWp):** ~4,7 anos.
- **Vida útil dos painéis:** 25 anos.

> **Nota:** O consumo das Bombas de Recirculação 0,5 CV c/ VFD (+R$ 587/mês antes da solar) é **integralmente coberto** pelo sistema 28 kWp. Após a Fase 5, o impacto líquido das bombas no OPEX é R$ 0.

## Riscos e Limitações
- **Sombreamento:** Instalações próximas a árvores de grande porte reduzem a eficiência drástica. Em áreas rurais, estruturas de solo afastadas dos tanques podem ser melhores que o telhado.
- **Limpeza:** O acúmulo de poeira reduz a geração em até 15%. É necessária a lavagem dos painéis a cada 3-4 meses (fora do período de chuvas).

## Custos Estimados — Fase 5

| Item | Qtd | Valor (R$) |
| :--- | :---: | :--- |
| Sistema Fotovoltaico 28 kWp (painéis + inversor + estruturas) | 1 | 113.100 |
| Projeto de engenharia, ART e homologação CEMIG | 1 | 3.500 |
| Mão de obra de instalação e elétrica | 1 | 3.200 |
| **TOTAL FASE 5** | | **R$ 119.800** |
