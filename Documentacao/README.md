# Projeto RJ Piscicultura — Piscicultura Intensiva

Sistema de produção intensiva de tilápia em **7 tanques de 60m³** (6 produção + 1 T7 depuração/acabamento) com ciclo escalonado de 6 meses, despesca mensal de ~2.391 kg vivo (~940 g/peixe, com fotoperíodo 16h), filé a R$ 43/kg ponderado e linguiça artesanal premium a R$ 52/kg. Localizado em **Sabará, MG** (Região Metropolitana de Belo Horizonte — RMBH); canais B2B/B2C na RMBH. Dados climáticos/solares usam BH como proxy conservador (Sabará fica a ~20 km, altitude ~710 m vs ~850 m de BH → marginalmente mais quente, o que reduz a demanda de aquecimento — premissa conservadora).

## Números-Chave
| Métrica | Valor |
| :--- | :--- |
| Capacidade total | 420m³ (7 × 60m³ — 6 produção + 1 T7) |
| Faturamento mensal (filé + linguiça + graxaria, operação completa) | R$ 43.347 |
| CAPEX Base (Fases 1-3, c/ fotoperíodo) | R$ 305.450 |
| CAPEX Completo (Fases 1-5) | R$ 532.850 |
| Lucro mensal (operação completa + linguiça + graxaria + fotoperíodo) | R$ 27.331 |
| Margem operacional | 63,0% |
| Payback (cenário completo Fases 1-5 + linguiça) | 1,9 anos |
| Mix de venda | 80% B2B (restaurantes) / 20% B2C (feiras) |
| Lucro mensal (expansão 12 tanques, pós-PRONAF) | R$ 57.187 *(12 prod. + 1 dep. T7, Fases 1–5)* |
| Ganho cumulativo da expansão vs amortização antecipada (13 anos) | +R$ 3,7 milhões |

## Documentação Técnica

| # | Documento | Fase | Conteúdo |
| :---: | :--- | :---: | :--- |
| 01 | [Infraestrutura e Aeração](01_Infraestrutura_e_Aeracao.md) | 1 | 7 tanques (6+T7), Difusores EPDM, Bomba Recirculação 0,5 CV, Cornell Dual-Drain, síntese airlift, CAPEX Fase 1 |
| 01b | [Sistema RAS — Funcionamento Detalhado](01b_Sistema_RAS.md) | 1 | Por que não airlift (física Sr, casos A/B, 10×), dreno 24/7, cônico+laminar+kidney (Stokes), filtro percolador CO₂ |
| 02 | [Automação e Segurança](02_Automacao_e_Seguranca.md) | 2 | Sensores OD multiplexados, inversores, gerador |
| 03 | [Climatização e Alimentação](03_Climatizacao_e_Alimentacao.md) | 3 | Bomba de Calor, lã de rocha, bolas flutuantes, **fotoperíodo 16h (LEDs 50 W/tanque, dimming PWM)** |
| 04 | [Fábrica de Ração + Graxaria + Linguiça](04_Fabrica_de_Racao.md) | 4 | Extrusora, formulação, graxaria (farinha+óleo), linguiça de tilápia |
| 05 | [Energia Solar](05_Energia_Solar.md) | 5 | Sistema **28 kWp** (dimensionado para Bombas 0,5 CV c/ VFD), Fio B, dimensionamento |
| 06 | [Qualidade, Riscos e Licenciamento](06_Qualidade_Riscos_e_Licenciamento.md) | — | Depuração, riscos, licenças MG (COPAM/IGAM/IMA) |
| 07 | [Plano Financeiro](07_Plano_Financeiro.md) | — | CAPEX, OPEX, capital de giro, fluxo de caixa |
| 08 | [Canais de Venda e Produtos](08_Canais_de_Venda_e_Produtos.md) | — | Mix B2B/B2C, linguiça de tilápia, faturamento revisado |
| 09 | [Fase 6 — Otimização Química](09_Fase6_Otimizacao_Quimica.md) | 6 | TiO₂+UV, reator estruvita, economia circular |
| 10 | [Estratégia de Financiamento e Expansão](10_Estrategia_Financiamento_e_Expansao.md) | — | Cronograma PRONAF, amortizar vs reinvestir, plano 12 tanques |
| 11 | [Benchmark de Sistemas](11_Benchmark_Sistemas.md) | — | BFT vs RAS acadêmico vs Projeto RJ: CAPEX, OPEX, manejo, métricas normalizadas |

## Software
- [Plano de Evolução do Simulador](PLANO_EVOLUCAO_SIMULADOR.md) — Regras de negócio para a aplicação React/Next.js.

## Princípios de Engenharia
1. **Verticalização Total:** Produzir a própria ração (Fase 4) e energia (Fase 5) dobra a margem de lucro.
2. **Bomba de Recirculação dedicada:** 6 bombas inline 0,5 CV c/ VFD criam o vórtice Cornell a 400 L/min com controle preciso de vazão por estágio de biomassa; difusores EPDM elevam OTE de aeração para ~40%.
3. **Isolamento > Potência:** Retenção térmica é mais barata que aquecimento mecânico.
4. **Modularidade:** Crescimento em 5 fases, permitindo que a operação inicial financie as expansões tecnológicas.
5. **Reinvestimento > Amortização:** ROI de um novo tanque (~365% a.a., payback ~3,3 meses) supera em ~81× o custo do PRONAF (4,5% a.a.) — o excedente de caixa deve expandir a produção, não quitar dívida barata. Ganho cumulativo em 13 anos: +R$ 3,7 milhões vs amortização antecipada.
