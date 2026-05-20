# 07. Plano Financeiro Consolidado

## Resumo
Documento mestre com todas as métricas financeiras do projeto: CAPEX por fase (incluindo usina solar fotovoltaica), OPEX mensal detalhado, capital de giro, fluxo de caixa e projeção de payback.

---

## Premissas Operacionais

> ⚠️ **Revisão (2026-05):** Premissas atualizadas para incluir **fotoperíodo de 16h** (LEDs — Fase 3, CAPEX R$ 2.000). Com 16h de luz artificial, o peso médio de despesca sobe de 750 g para **940 g** (+25%), elevando a produção mensal de filé de 631 kg para **789 kg**. Ver [Doc 03 — Seção Fotoperíodo](03_Climatizacao_e_Alimentacao.md) para a fundamentação. As tabelas financeiras abaixo já refletem esse cenário.

- **Capacidade:** 6 tanques de 60m³ (360m³ total).
- **Ciclo:** 6 meses por lote. Cada tanque opera de forma independente.
- **Despesca mensal (regime estável, com fotoperíodo 16h):** ~2.391 kg vivo (940 g × 2.550 peixes).
- **Rendimento de filé:** 33% → ~789 kg filé/mês.
- **Rendimento barriguinha:** 5% → ~120 kg/mês (fator limitante da linguiça).
- **Rendimento recortes:** 4% → ~96 kg/mês.
- **Resíduo graxaria:** 58% → ~1.387 kg/mês.
- **Mix de venda:** B2B Restaurantes 80% / B2C Feiras 20%.
- **Preço de venda filé (projeção realista 2026):** R$ 41,00/kg (B2B) | R$ 51,00/kg (B2C) | **Médio ponderado: R$ 43,00/kg**. *(Revisão 2026-05: reduzido de R$ 47 para R$ 43 — projeção realista RMBH com rampa comercial.)*
- **Preço de venda linguiça (charcutaria premium, > filé):** R$ 50,00/kg (B2B) | R$ 60,00/kg (B2C) | **Médio ponderado: R$ 52,00/kg**.
- **Volume de filé:** 789 kg/mês produzidos. Cenários **filé-only**: 789 kg vendidos. Cenário **com linguiça**: 669 kg vendidos (120 kg migram para a formulação da linguiça — correção da dupla contagem).
- **FCA biológico:** ~1,5 (kg ração/kg ganho) — valor implícito e consistente no modelo (3.633 kg ração/mês ÷ 2.391 kg ganho/mês = 1,52). O FCA **não muda** com ração própria (é métrica zootécnica); a ração própria reduz o **custo por kg de ração** (R$ 4,45 → R$ 2,10 → R$ 1,83 c/ graxaria), não a conversão. *(Correção 2026-05: a versão anterior registrava "1,0 (ração própria)", o que era conceitualmente incorreto — FCA econômico ≠ FCA biológico.)*
- **Tarifa CEMIG (rural):** R$ 0,85/kWh (com impostos).

*Baseline conservador sem fotoperíodo: 1.913 kg vivo / 631 kg filé / mês (fotoperíodo natural ~12h BH). Ver seção "Impacto do Fotoperíodo" ao final deste documento para a comparação completa.*

---

## CAPEX — Investimento por Fase

| Fase | Descrição | Valor (R$) |
| :---: | :--- | :--- |
| 1 | Infraestrutura (7 tanques — 6 produção + 1 T7), Aeração EPDM, **Bombas Recirculação 0,5 CV c/ VFD**, Processamento Linguiça, Sump + **Decantador Cônico + Laminar + Loop Kidney**, **Galpão SIE + tampas EPS + redundância N+1**, **Gerador 8–10 kVA + QTA** | **209.850** |
| 2 | Automação e Segurança (CLP, sensores OD+pH, inversores, **contator de calcário**, **sensor ΔP filtro kidney**, **sensor pressão manifold sopradores**) | **39.750** |
| 3 | Climatização, Alimentação e **Fotoperíodo 16h (LEDs)** (Bomba de Calor, isolamento, luminárias) | **56.100** |
| 4 | Fábrica de Ração + Graxaria (c/ controle de odor, **soft-starter extrusora**) | 111.600 |
| 5 | Energia Solar (sistema **28 kWp** completo — redimensionado para cobrir Bombas de Recirculação 0,5 CV c/ VFD) | **119.800** |
| **6** | **Otimização Química e Economia Circular (TiO₂+UV + Reator Estruvita)** | **13.000** |
| | Licenciamento (COPAM, IGAM, SIE) | 9.000 |
| **TOTAL** | | **R$ 559.100** |

*Revisão 2026-05-19: Gerador + QTA (R$ 12.000) realocado da Fase 2 para a Fase 1 (risco operacional — alevinos entram no mês 1); soft-starter 25 CV (R$ 4.000) adicionado à Fase 4 (proteção de partida da extrusora); sensor de pressão manifold sopradores (R$ 250) adicionado à Fase 2 (mitigação da janela cega de OD). Impacto no CAPEX total: +R$ 4.250 (de R$ 554.850 para R$ 559.100). O principal PRONAF deve ser ajustado de R$ 554.850 para R$ 559.100 antes da submissão formal.*

*Fase 1 inclui: 7º tanque T7 Acabamento Comercial (R$ 8.000), 6 Bombas de Recirculação **0,5 CV c/ VFD** inline (R$ 7.200), equipamentos de linguiça (R$ 13.000), Sump Coletor 300L HDPE (R$ 800), **Decantador Cônico 1.500L (R$ 1.400) + Decantador Laminar (R$ 1.800) + interligação por gravidade (R$ 600) + Loop Kidney: bomba 0,25 CV (R$ 600) e carcaça + mangas poliéster 10 µm (R$ 450)** — Hidrociclone e Bomba de Sólidos eliminados (circuito 100% gravidade, ver Doc 01) —, **Galpão de processamento SIE (R$ 60.000), placas EPS tampa-tanques (R$ 15.000), redundância N+1 (R$ 4.000) e Gerador 8–10 kVA + QTA (R$ 12.000)**. Fase 2 inclui contator de calcário passivo (R$ 3.000), sensor de pH integrado ao CLP, sensor de pressão diferencial do filtro kidney (R$ 700) e sensor de pressão no manifold dos sopradores (R$ 250). Fase 3 inclui sistema de fotoperíodo: **12 barras LED IP67 25 W (2/tanque, 50 W/tanque) + drivers PWM dimerizáveis + cabeamento** (R$ 2.000). Fase 4: Fábrica Ração R$ 66.600 (incl. soft-starter) + Graxaria R$ 45.000 (com controle de odor). Fase 5: solar redimensionado para **28 kWp** para cobrir a carga das Bombas de Recirculação 0,5 CV c/ VFD (+691 kWh/mês).*

---

## OPEX Mensal (Cenário Base: Fases 1 a 3)
Sem Fábrica de Ração própria e sem Energia Solar. **Com fotoperíodo 16h** (LEDs ativos).

> ⚠️ **Versão revisada (2026-05):** (1) A versão anterior omitia o custo de gestão de alcalinidade — com o Contator de Calcário, esse custo cai para R$ 640/mês. (2) Com a inclusão do sistema de fotoperíodo (16h LEDs), a despesca mensal aumenta de 1.913 kg para 2.391 kg (+25%), elevando a ração para 3.633 kg/mês e o faturamento de filé-only de R$ 27.133 para **R$ 33.927/mês** (a R$ 43/kg ponderado). Ver [Doc 03 — Seção Fotoperíodo](03_Climatizacao_e_Alimentacao.md) e [Doc 06 — Seção 6](06_Qualidade_Riscos_e_Licenciamento.md).

| Item | Valor Mensal (R$) |
| :--- | :--- |
| **Ração Comercial (3.633 kg × R$ 4,45 — biomassa +25% c/ fotoperíodo)** | **16.167** |
| Energia — Sopradores (2 × 2CV, inverter) | 1.050 |
| Energia — Bomba Kidney (0,25 CV, polimento side-stream 24/7) | 40 |
| Energia — CLP, alimentadores, iluminação | 170 |
| Energia — Bomba de Calor (sazonal; −10% pela estratégia pH 7,1) | 760 |
| **Energia — LEDs Fotoperíodo (6 tanques × 50 W × 16 h/dia = 144 kWh/mês)** | **122** |
| **Energia — Bombas de Recirculação (6 × 0,5 CV c/ VFD, 691 kWh/mês)** | **587** |
| Alevinos (~2.900/mês, reversão sexual) | 1.160 |
| Mão de obra (1 técnico/proprietário) | 3.000 |
| Manutenção e insumos | 800 |
| Processamento (abate/filetagem) | 1.200 |
| **Gestão de Alcalinidade — Contator de Calcário (brita calcítica + manutenção)** | **640** |
| **OPEX Total (Média)** | **R$ 25.696** |
| Faturamento — filé-only (789 kg × R$ 43 médio ponderado) | R$ 33.927 |
| **Lucro Líquido Mensal (base filé-only Fases 1-3)** | **R$ 8.231** |

*Ração aumenta de R$ 12.950 para R$ 16.167 (+R$ 3.217) pelo maior consumo proporcionado pela biomassa 25% maior. LEDs (R$ 122/mês) e Bombas de Recirculação (R$ 587/mês) são zerados na Fase 5 (cobertos pela solar 28 kWp). Bomba de Calor R$ 760/mês (−10%): janela pH 7,1 reduz trocas de água fria em ~40%. A Bomba de Sólidos 0,5 CV (R$ 57/mês) foi eliminada — trem de sólidos por gravidade; substituída pela bomba kidney 0,25 CV (R$ 40/mês), economia líquida de R$ 17/mês.*

### Comparativo: Com Contator vs. Sem Contator (Bicarbonato Industrial)

*Valores abaixo usam o baseline conservador sem fotoperíodo para referência histórica.*

| Cenário | Alcalinidade/mês | OPEX total/mês | Lucro Mensal | Payback (Fases 1-3) |
| :--- | :---: | :---: | :---: | :---: |
| Sem contator (bicarbonato), sem fotoperíodo | R$ 2.583 | R$ 23.818 | R$ 5.839 | ~49 meses |
| Com contator (calcário), sem fotoperíodo | R$ 640 | R$ 21.787 | R$ 7.870 | ~37 meses |
| **Com contator + fotoperíodo 16h (filé-only R$ 43)** | **R$ 640** | **R$ 25.696** | **R$ 8.231** | **~48 meses** |
| Economia anual do contator | | | **R$ 23.316/ano** | Payback contator < 1 mês |

---

## Impacto da Verticalização (Fases 4 e 5)

### Fase 4: Fábrica de Ração
- Produzindo ração própria a R$ 2,10/kg (engorda).
- O custo de ração cai de **R$ 16.167** (comercial, com fotoperíodo) para **R$ 7.629** (3.633 kg × R$ 2,10).
- **Economia mensal:** R$ 8.538.
- **Novo Lucro Mensal (após Fase 4):** ~R$ 20.213.

### Fase 4 + Graxaria: Farinha e Óleo Próprios
- Com 2.391 kg de despesca, o resíduo sobe para ~1.387 kg/mês.
- Graxaria internaliza a farinha de peixe (~178 kg/mês) e o óleo (~71 kg/mês) usados na ração própria.
- Custo de ração cai de R$ 7.629 para ~**R$ 6.649** (−R$ 980/mês).
- Excedente de farinha (~123 kg × R$ 4,00) gera receita de R$ 492/mês.
- Custo operacional da graxaria: +R$ 350/mês.
- **Ganho líquido da graxaria:** ~R$ 1.122/mês.

### Fase 4 + Linguiça de Tilápia
- Com 120 kg/mês de barriguinha (+25% vs 96 kg): **270 kg linguiça/mês** → receita de R$ 8.745/mês.
- Insumos (temperos, tripa, embalagem): −R$ 1.875/mês (escala com volume).
- **Ganho líquido da linguiça:** +R$ 6.870/mês.

### Fase 5: Energia Solar Fotovoltaica (28 kWp)
- O custo total de energia (Sopradores + Bomba Kidney + CLP + LEDs + **Bombas de Recirculação 0,5 CV c/ VFD**) cai de R$ 2.722 para a taxa mínima rural trifásica de **R$ 290** (toda a carga coberta pelo sistema 28 kWp).
- **Economia mensal:** R$ 2.449.
- **Novo Lucro Mensal Final (após Fases 4 e 5 + linguiça + graxaria):** **~R$ 27.331** (faturamento R$ 43.347 − OPEX R$ 16.016; margem 63,0%).

---

## Capital de Giro (6 Meses sem Faturamento)
Nos primeiros 6 meses, os tanques estão sendo ativados e nenhum lote atingiu peso de despesca. O OPEX roda gradualmente.
**Capital de giro necessário: ~R$ 90.000** (deve estar reservado antes de iniciar).

---

## Payback e Projeção

> Valores revisados (2026-05) incluindo: (1) Contator de Calcário (+R$ 3.000 CAPEX Fase 2; OPEX R$ 640/mês); (2) **Fotoperíodo 16h** (+R$ 2.000 CAPEX Fase 3; OPEX R$ 122/mês Fases 1–4; +25% despesca); (3) **T7 + Bombas de Recirculação 0,5 CV c/ VFD** (+R$ 15.200 CAPEX Fase 1; OPEX R$ 587/mês Fases 1–4; cobertas pela solar 28 kWp na Fase 5); (4) **Solar redimensionada para 28 kWp** (+R$ 28.600 CAPEX Fase 5); (5) **Trem de sólidos por gravidade** (Cônico+Laminar+Kidney substituem HC+Bomba Sólidos: +R$ 3.650 CAPEX Fase 1, +R$ 700 CAPEX Fase 2, −R$ 17/mês OPEX); (6) **Galpão SIE + tampas EPS + redundância N+1** (+R$ 79.000 CAPEX Fase 1: galpão de processamento SIE R$ 60.000, placas EPS tampa-tanques R$ 15.000, redundância N+1 R$ 4.000).

| Cenário | CAPEX Total | Capital Giro | Investimento Total | Lucro Mensal | Payback |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Operação Básica (Fases 1-3, c/ fotoperíodo, filé-only R$ 43) | R$ 305.450 | R$ 90.000 | R$ 395.450 | R$ 8.231 | **48 meses (4,0 anos)** |
| Operação Completa (Fases 1-5, sem linguiça/graxaria, filé-only) | R$ 532.850 | R$ 90.000 | R$ 622.850 | R$ 19.194 | **32 meses (2,7 anos)** |
| Operação Completa + Linguiça + Graxaria (Fases 1–5) | R$ 532.850 | R$ 90.000 | R$ 622.850 | R$ 27.331 | **23 meses (1,9 anos)** |
| **Operação Completa + Fase 6 (TiO₂ + Estruvita)** | **R$ 545.850** | **R$ 90.000** | **R$ 635.850** | **R$ 30.100** | **21 meses (1,8 anos)** |

*Nota: Fase 5 (Solar 28 kWp) pode ser financiada via PRONAF Eco. Fase 6 tem payback próprio de ~4,7 meses com fotoperíodo (CAPEX R$ 13.000 / ganho ~R$ 2.768/mês). Ver [Doc 09](09_Fase6_Otimizacao_Quimica.md) para detalhamento.*

### Impacto do Contator de Calcário no Payback

Sem o contator (bicarbonato industrial, R$ 2.583/mês) e sem fotoperíodo, o payback do cenário básico seria **~50 meses (4,2 anos)**. O contator (R$ 3.000 CAPEX) reduz ~13 meses. O fotoperíodo (R$ 2.000 CAPEX) reduz mais ~10 meses adicionais. Juntos, transformam o payback básico de 50 meses para **~35 meses** (com o CAPEX de infraestrutura completo, incluindo galpão SIE) com apenas R$ 5.000 investidos nesses dois itens.

### Impacto da Fase 6 (Módulos 6B + 6C)

Com fotoperíodo, a Fase 6 gera ~R$ 2.768/mês (payback de **~4,7 meses**). O lucro sobe de R$ 27.331 para **~R$ 30.100/mês** no cenário completo (ver Doc 09 para detalhamento).

---

## Resumo Executivo (Cenário Operação Completa + Linguiça + Graxaria + Fotoperíodo)

> Valores revisados incluindo: Contator de Calcário (R$ 640/mês), fotoperíodo 16h (+25% produção, R$ 2.000 CAPEX), Bombas de Recirculação 0,5 CV c/ VFD (R$ 7.200 CAPEX; solar 28 kWp). LEDs e Bombas de Recirculação cobertos pela geração solar na Fase 5.

| Métrica | Valor |
| :--- | :--- |
| Investimento Total (Fases 1-5 + Giro) | R$ 622.850 |
| Faturamento Bruto Mensal (filé 669 kg × R$ 43 + linguiça 270 kg × R$ 52 + farinha) | R$ 43.347 |
| Faturamento Anual | R$ 520.164 |
| OPEX Mensal (ração própria + solar + graxaria + linguiça + alcalinidade + bomba kidney) | R$ 16.016 |
| OPEX Anual | R$ 192.192 |
| **Lucro Mensal** | **R$ 27.331** |
| **Lucro Anual** | **R$ 327.972** |
| Margem Operacional | 63,0% |
| Payback | **1,9 anos** |

### Comparativo de Cenários (Revisado 2026-05 com Fotoperíodo)

| Cenário | Faturamento Mensal | Lucro Mensal | Margem | Payback |
| :--- | :---: | :---: | :---: | :---: |
| Base sem contator, sem fotoperíodo | R$ 29.657 | R$ 5.839 | 19,7% | ~4,2 anos |
| Base com contator, sem fotoperíodo (Fases 1-3) | R$ 29.657 | R$ 7.870 | 26,5% | 3,1 anos |
| **Base com contator + fotoperíodo (Fases 1-3, filé-only R$ 43)** | **R$ 33.927** | **R$ 8.231** | **24,3%** | **4,0 anos** |
| Completo s/ linguiça, com fotoperíodo (Fases 1–5, filé-only) | R$ 33.927 | R$ 19.194 | 56,6% | 2,7 anos |
| **Completo + linguiça + graxaria + fotoperíodo (Fases 1–5)** | **R$ 43.347** | **R$ 27.331** | **63,0%** | **1,9 anos** |
| **Completo + Fase 6 + fotoperíodo** | **R$ 44.747** | **R$ 30.100** | **67,3%** | **1,8 anos** |

### Projeção para o Milhão
Com lucro anual de ~R$ 327.972, a marca de **R$ 1.000.000 em lucros acumulados** é atingida em **~3,0 anos** após o início das despescas (cenário completo Fases 1–5 + linguiça + graxaria, preços realistas 2026).

---

## Impacto do Fotoperíodo (16h) — Análise Incremental

| Parâmetro | Sem Fotoperíodo | **Com Fotoperíodo 16h** | Variação |
| :--- | :---: | :---: | :---: |
| Peso médio de despesca | 750 g | **940 g** | +25% |
| Despesca mensal | 1.913 kg | **2.391 kg** | +478 kg |
| Filé/mês | 631 kg | **789 kg** | +158 kg |
| Faturamento filé (R$ 43/kg) | R$ 27.133 | **R$ 33.927** | +R$ 6.794 |
| Ração (comercial) | R$ 12.950 | **R$ 16.167** | +R$ 3.217 |
| Ração (própria, Fase 4) | R$ 6.111 | **R$ 7.629** | +R$ 1.518 |
| LEDs OPEX (Fases 1-4) | R$ 0 | **R$ 122** | — |
| LEDs OPEX (Fase 5+) | R$ 0 | **R$ 0** | (solar) |
| Linguiça (R$ 52/kg, c/ Fase 4) | 216 kg → R$ 11.232 | **270 kg → R$ 14.040** | +R$ 2.808 |
| CAPEX adicional | — | **R$ 2.000** | LEDs + wiring |
| **Ganho líquido/mês (Fases 1-3)** | — | **+R$ 3.455** | — |
| **Ganho líquido/mês (completo)** | — | **+R$ 8.084** | — |
| **Payback do investimento em LEDs** | — | **< 1 mês** | — |

*Fundamentação: Lim et al. (2003) — +23% crescimento com 16h vs 8h; Rad et al. (2006) — +31% com 18h; mecanismo: supressão de melatonina → desbloqueio do eixo GH/IGF-1. Para BH especificamente, o déficit de fotoperíodo de inverno (maio–agosto, 11,1–11,6h) afeta 2/3 do ciclo de engorda. Ver [Doc 03 — Seção Fotoperíodo](03_Climatizacao_e_Alimentacao.md).*
