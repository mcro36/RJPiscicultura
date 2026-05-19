# 11. Benchmark de Sistemas — BFT vs RAS Acadêmico vs Projeto RJ

## Resumo
Comparação técnico-econômica de três sistemas superintensivos de produção de tilápia, **normalizada para a mesma produção** (28.692 kg vivo/ano), nas condições de Sabará-MG/RMBH (aquecimento obrigatório para os três; dados climáticos de BH como proxy conservador). O Projeto RJ Fases 1-3 totaliza R$ 305.450 — mas **R$ 60.000 disso é o galpão de processamento SIE** (infraestrutura regulatória, que os baselines BFT/RAS-acadêmico de literatura também não incluem). O **núcleo de cultivo comparável** (~R$ 245.000) ainda custa **~55% de um RAS acadêmico** (~R$ 450.000); a verticalização (ração própria + solar + linguiça premium + graxaria) reduz o OPEX para **R$ 6,70/kg vivo** e eleva a margem a **63,0%** (preços realistas 2026: filé R$ 43, linguiça R$ 52; payback **1,9 ano** após incorporar galpão SIE + tampas EPS + redundância N+1).

---

## 1. Metodologia e Procedência dos Dados

### 1.1 Base de Normalização

Todos os sistemas dimensionados para a saída real do Projeto RJ:

| Parâmetro de normalização | Valor |
| :--- | :---: |
| Produção anual (peso vivo) | **28.692 kg/ano** (2.391 kg/mês) |
| Produção anual (filé, 33%) | 9.468 kg/ano (789 kg/mês) |
| Ciclo | 6 meses, escalonado (despesca mensal) |
| Local | Sabará-MG / RMBH (clima de BH como proxy conservador; aquecimento obrigatório nos 3 sistemas) |
| Peso de despesca | 940 g (referência do projeto, com fotoperíodo) |
| Tarifa de energia | R$ 0,85/kWh (CEMIG rural) |
| Preço de referência do filé | R$ 43,00/kg (médio ponderado B2B/B2C, realista 2026) |
| Preço de referência da linguiça | R$ 52,00/kg (charcutaria premium, > filé) |

### 1.2 Procedência (honestidade de dados)

| Sistema | Fonte dos números | Confiabilidade |
| :--- | :--- | :---: |
| **Projeto RJ** | Docs 01/07 deste repositório (estado atual) | ✅ Firme (projeto detalhado) |
| **BFT (Biofloco)** | Literatura: Avnimelech *Biofloc Technology – A Practical Guide* (2015); Emerenciano et al. (2017); Wasielesky/FURG; operações comerciais BR | ⚠️ Faixa de referência |
| **RAS acadêmico** | Literatura: Timmons & Ebeling *Recirculating Aquaculture* (4ª ed.); Summerfelt/Freshwater Institute; SRAC Fact Sheets | ⚠️ Faixa de referência |

> ⚠️ **Limitação metodológica:** os números de BFT e RAS acadêmico são **faixas de referência da literatura normalizadas** para 28,7 t/ano — não medições de uma planta específica. São apresentados como intervalo [mín–máx] + estimativa central, com a base de cálculo declarada. Os números do Projeto RJ são valores firmes do projeto detalhado. Comparações com incerteza > ±25% estão sinalizadas.

### 1.3 Camadas de Comparação

Para isolar o efeito da **verticalização** (estratégia do Projeto RJ):

- **Núcleo produtivo:** sistema de cultivo "puro" (sem fábrica de ração, sem solar, sem processamento) — comparação técnica justa entre as três tecnologias.
- **Sistema completo:** a estratégia real do Projeto RJ (ração própria + solar 28 kWp + processamento + economia circular).

---

## 2. Definição dos Três Sistemas

| | **BFT — Biofloco** | **RAS Acadêmico (livro-texto)** | **Projeto RJ (RAS custo-engenheirado)** |
| :--- | :--- | :--- | :--- |
| Filosofia | O floco microbiano *é* o tratamento de N | Água limpa; remoção mecânica + biofiltro | Água limpa custo-engenheirada + verticalização |
| Remoção de sólidos | Não há (clarificador p/ sangrar floco) | Drum filter (microtela 60 µm) | Trem por gravidade (cônico+laminar+kidney) |
| Biofiltração | Floco heterotrófico (gestão C:N) | MBBR ou trickling tower dedicado | Percolador multifunção (nitrifica + desgasa CO₂ + alcalinidade) |
| Oxigenação | Aeração pesada (resp. do floco) | O₂ puro (LOX + cones/LHO) | Blowers canal lateral + difusores EPDM |
| Controle de N | Relação C:N (dosagem de carbono) | Nitrificação em biofiltro | Nitrificação + janela pH 7,0–7,2 |
| Produto | Commodity (risco off-flavor alto) | Premium possível | Premium B2B verticalizado |

---

## 3. CAPEX — Núcleo Produtivo (28,7 t/ano)

Valores em R$ mil. Faixa [mín–máx] e **central**.

| Subsistema | **BFT** | **RAS Acadêmico** | **Projeto RJ (Fases 1-3)** |
| :--- | :---: | :---: | :---: |
| Tanques revestidos + estrutura | 50–65 | 45–55 | **56,0** (7×60 m³) |
| Aeração / movimentação | 28–42 *(pesada)* | 12–20 | **14,5** (blowers+EPDM) |
| Oxigenação O₂ puro (LOX+cones) | — | 40–85 | — |
| Remoção de sólidos | 5–10 *(clarificador)* | 35–75 *(drum filter)* | **3,65** (cônico+laminar+kidney) |
| Biofiltração dedicada | — *(floco)* | 30–55 *(MBBR)* | incluso (percolador) |
| Desgasificação CO₂ | incl. aeração | 8–15 *(coluna)* | incluso (percolador) |
| Bombas recirculação | 3–6 *(mistura)* | 15–25 | **7,2** (6×0,5 CV VFD) |
| UV / ozônio | 6–12 | 10–25 | incluso (Fase 6) |
| Aquecimento (inverno BH) | 25–35 | 25–35 | incluso (Fase 3) |
| Instrumentação / CLP | 15–22 | 35–60 *(por tanque)* | incluso (Fase 2 multiplexado) |
| Dosagem fonte de C (melaço) | 3–6 | — | — |
| Elétrica / hidráulica / civil | 15–28 | 25–45 | incluso |
| **Total núcleo (R$ mil)** | **190–260** | **370–540** | **305,45** |
| **— do qual galpão SIE (regulatório, não cultivo)** | — | — | **60,00** |
| **— núcleo de cultivo comparável** | **~220** | **~450** | **~245** |
| **Estimativa central (núcleo cultivo)** | **~R$ 220.000** | **~R$ 450.000** | **~R$ 245.000** |
| **CAPEX cultivo por kg/ano de capacidade** | **R$ 7,67** | **R$ 15,68** | **R$ 8,54** |

> *Cálculo: RJ Fases 1-3 = R$ 197.850 (F1) + R$ 51.500 (F2) + R$ 56.100 (F3) = R$ 305.450. Para comparação justa, exclui-se o galpão de processamento SIE (R$ 60.000) — infraestrutura regulatória que os baselines BFT/RAS-acadêmico de literatura também não modelam. Núcleo de cultivo comparável ≈ R$ 245.000 ÷ 28.692 kg/ano = R$ 8,54/kg-ano.*

**Achado central:** mesmo após incorporar galpão SIE + tampas EPS + redundância N+1, o **núcleo de cultivo** custo-engenheirado do Projeto RJ (~R$ 245.000) custa **~55% de um RAS acadêmico** (~R$ 450.000) para a mesma produção, permanecendo próximo ao BFT (~R$ 220.000). O gap de ~R$ 205.000 vem de quatro decisões de engenharia: (1) trem de sólidos por gravidade no lugar de drum filter (−R$ 30 a 70 k); (2) blowers + EPDM no lugar de O₂ puro (−R$ 40 a 85 k); (3) percolador multifunção no lugar de MBBR + coluna de CO₂ dedicados (−R$ 38 a 70 k); (4) sensores multiplexados no lugar de instrumentação por tanque (−R$ 20 a 38 k).

---

## 4. CAPEX — Sistema Completo

| Camada | **BFT** | **RAS Acadêmico** | **Projeto RJ** |
| :--- | :---: | :---: | :---: |
| Núcleo Fases 1-3 (inclui galpão SIE) | ~230 | ~450 | 305,45 |
| Fábrica de ração própria (Fase 4) | não modelado | não modelado | +107,60 |
| Energia solar 28 kWp (Fase 5) | não modelado | não modelado | +119,80 |
| Otimização química 6B/6C | não modelado | não modelado | +13,00 |
| Licenciamento | variável | variável | +9,00 |
| **CAPEX total (R$ mil)** | **~230+** | **~450+** | **554,85** |
| Capital de giro | ~70–90 | ~80–100 | 90,00 |

A verticalização **dobra o CAPEX do núcleo** — decisão deliberada que converte margem de ~24% em **63,0%** (ver §7).

---

## 5. OPEX Mensal (2.391 kg vivo/mês)

Valores em R$. Faixa e **central**.

| Item | **BFT** | **RAS Acadêmico** | **RJ Núcleo (F1-3)** | **RJ Completo (F1-5)** |
| :--- | :---: | :---: | :---: | :---: |
| Ração | 12.000–15.000 | 12.500–15.500 | **16.167** *(comercial)* | **6.649** *(própria)* |
| Fonte de carbono (melaço) | 800–1.600 | — | — | — |
| Energia elétrica | 5.000–8.500 *(aeração pesada)* | 5.500–8.000 *(O₂+bombas)* | **2.729** | **290** *(solar)* |
| O₂ líquido (LOX, recorrente) | — | 2.500–4.500 | — | — |
| Alcalinidade | 1.200–2.200 *(BFT consome muito)* | 600–1.200 | **640** | 640 |
| Alevinos | 1.160 | 1.160 | 1.160 | 1.160 |
| Mão de obra | 3.000–4.000 | 3.500–5.000 | 3.000 | 3.000 |
| Manutenção / insumos / process. | 2.000–3.500 | 2.500–4.000 | 2.000+ | ~4.300 |
| **OPEX total/mês** | **~R$ 28.800** | **~R$ 31.900** | **R$ 25.696** | **R$ 16.016** |
| **OPEX por kg vivo** | **R$ 12,05** | **R$ 13,34** | **R$ 10,75** | **R$ 6,70** |

> *Cálculo R$/kg = OPEX mês ÷ 2.391 kg. Centrais BFT/RAS são o ponto médio das faixas. RJ = Doc 07 (firme).*

**Direcionadores do OPEX do Projeto RJ completo (R$ 6,70/kg, ~metade dos baselines):**
- Ração própria: R$ 2,10/kg vs R$ 4,45/kg comercial → −R$ 9.518/mês
- Solar 28 kWp: energia cai de R$ 2.729 para R$ 290 → −R$ 2.439/mês
- Sem O₂ líquido (blowers+EPDM) e sem fonte de carbono (não é BFT)

---

## 6. Custos Normalizados (Comparação Precisa)

| Métrica normalizada | **BFT** | **RAS Acadêmico** | **RJ Núcleo** | **RJ Completo** |
| :--- | :---: | :---: | :---: | :---: |
| CAPEX / kg-ano capacidade *(núcleo cultivo)* | R$ 7,67 | R$ 15,68 | R$ 8,54 | R$ 19,34 *(completo)* |
| OPEX / kg vivo | R$ 12,05 | R$ 13,34 | R$ 10,75 | **R$ 6,70** |
| Energia / kg vivo | 3,0–5,0 kWh | 2,0–4,0 kWh | **1,39 kWh** | **1,39 kWh** |
| Água / kg vivo | 50–150 L | 100–300 L | ~50–200 L | ~50–200 L |
| FCA | 1,0–1,4 | 1,1–1,3 | 1,2–1,3 | **1,0** *(própria)* |

> Energia/kg do RJ = 3.328 kWh/mês ÷ 2.391 kg = **1,39 kWh/kg** — baixo para RAS porque não há O₂ puro nem drum filter motorizado; difusores EPDM elevam a OTE para ~40%.

---

## 7. Síntese Econômica — Receita Comum e Margem

Para precisão, comparo as três tecnologias **vendendo o mesmo produto ao mesmo preço** (sem o prêmio de verticalização), e depois mostro o efeito da verticalização do Projeto RJ.

### 7.1 Cenário Núcleo — Mesma Receita (filé R$ 43/kg realista, 789 kg/mês = R$ 33.927/mês)

| | **BFT** | **RAS Acadêmico** | **RJ Núcleo** |
| :--- | :---: | :---: | :---: |
| Faturamento/mês | R$ 33.927 | R$ 33.927 | R$ 33.927 |
| OPEX/mês | R$ 28.800 | R$ 31.900 | R$ 25.696 |
| Lucro operacional/mês | R$ 5.127 | R$ 2.027 | **R$ 8.231** |
| **Margem operacional** | **15,1%** | **6,0%** | **24,3%** |

> ⚠️ **Ressalva BFT:** o risco crônico de off-flavor (geosmina do consórcio microbiano) pode forçar venda com deságio de 30–50% se a depuração não for rigorosa — o que derrubaria a margem do BFT abaixo de 22,3% no mundo real para produto premium.

### 7.2 Cenário Completo — Verticalização do Projeto RJ

| | **RJ Completo (Fases 1-5 + linguiça + graxaria)** |
| :--- | :---: |
| Faturamento/mês (filé 669 kg × R$ 43 + linguiça 270 kg × R$ 52 + farinha) | R$ 43.347 |
| OPEX/mês | R$ 16.016 |
| Lucro/mês | **R$ 27.331** |
| **Margem operacional** | **63,0%** |
| Payback (Fases 1-5) | **~1,9 anos** |

A verticalização (ração própria + solar + linguiça premium R$ 52/kg + graxaria) eleva a margem de 24,3% (núcleo, filé-only R$ 43) para **63,0%** — um diferencial estrutural que nenhum dos baselines de literatura modela. A linguiça, precificada acima do filé, passa a ser o item de maior margem do portfólio.

---

## 8. Manejo e Variáveis Críticas

| Dimensão | **BFT** | **RAS Acadêmico** | **Projeto RJ** |
| :--- | :---: | :---: | :---: |
| Variável crítica diária | Relação C:N, volume de floco (cone Imhoff) | OD, TAN, vazão do drum, biofiltro | OD, pH 7,0–7,2, vórtice, ΔP kidney |
| Criticidade de OD | **Extrema** (respiração do floco) | Alta (compensada por O₂ puro) | Alta |
| Estabilidade da água | ⚠️ Sensível ("floco vira") | Estável | Estável (controle químico Doc 02) |
| Insumo recorrente crítico | Melaço (fonte de C) | O₂ líquido (LOX) | Brita calcítica (contator) |
| Off-flavor | ⚠️ **Alto** | Médio-baixo | ✅ Baixo (depuração + TiO₂/UV) |
| Skill do operador | Alto (microbiologia aplicada) | Alto (instrumentação) | Alto (RAS + química) |
| Tolerância a erro operacional | Baixa | Média | Média |
| Automação | Média | Alta | Alta (CLP multiplexado) |

---

## 9. Risco e Resiliência

| Eixo de risco | **BFT** | **RAS Acadêmico** | **Projeto RJ** |
| :--- | :---: | :---: | :---: |
| Janela sem energia/aeração | **minutos** | **minutos** | **minutos** (gerador+solar mitigam) |
| Colapso de qualidade da água | Alto (floco instável) | Médio | Médio |
| Dependência de insumo externo | Melaço (logística) | LOX (entrega recorrente) | Brita (estável, barato) |
| Risco de mercado | Alto (commodity) | Médio | Baixo (premium B2B contratado) |
| Risco de off-flavor | Alto | Médio-baixo | Baixo |
| Complexidade de falha | Alta | Alta | Alta |

> **Eixo de empate negativo nos três:** a janela anti-apagão é de minutos (vs horas-dias de um viveiro). Recomenda-se protocolo formal de contingência de aeração (autonomia do gerador, O₂ de emergência por estágio de biomassa).

---

## 10. Matriz de Decisão — Quando Cada Sistema Vence

```
BFT vence quando:        capital inicial é restrição dominante,
                         produto é commodity/volume, água é escassa,
                         operador domina gestão de floco.

RAS acadêmico vence:     quando se exige sistema validado/replicável
                         com documentação científica e suporte de
                         fornecedor turnkey; aceita CAPEX e OPEX altos.

Projeto RJ vence quando: mercado é filé premium B2B (off-flavor é
                         passivo inaceitável), terreno já é próprio, há
                         inverno (RMBH/Sabará), e o operador tem capacidade
                         de gerir verticalização. Resultado: OPEX/kg ~metade,
                         margem 65%, payback ~1,7 ano.
```

**Conclusão:** o Projeto RJ não é "um RAS acadêmico mais caro". Seu **núcleo de cultivo** (~R$ 245k, excluído o galpão SIE regulatório) custa **~55% de um RAS livro-texto** graças à engenharia de custo; sua **verticalização** é o que gera a margem de 65%. O preço é complexidade operacional alta e CAPEX total elevado (R$ 554,85k incluindo galpão SIE + verticalização) — todos deliberados e justificados pelo posicionamento premium.

---

## 11. Limitações e Incerteza dos Dados

1. **BFT e RAS acadêmico são faixas de literatura**, não plantas medidas. Incerteza estimada: CAPEX ±25%, OPEX ±20%. As estimativas centrais são pontos médios conservadores.
2. **Energia do BFT** é o item de maior incerteza — varia muito com a tecnologia de aeração (fine-bubble vs airlift) e densidade de floco (±40%).
3. **LOX (RAS acadêmico)** depende fortemente de logística regional; em MG o custo recorrente pode variar ±30%.
4. **Off-flavor do BFT** não foi monetizado no cenário 7.1 (assumiu-se depuração perfeita) — no mundo real, deságio provável reduziria ainda mais a margem do BFT.
5. **Projeto RJ** = projeto detalhado, não planta operando; sujeito aos riscos de execução dos Docs 01–10.
6. Comparação válida **para Sabará-MG/RMBH** (aquecimento obrigatório; clima de BH como proxy conservador). Em clima quente com terra/água baratas, o ranking econômico muda.

---

## 12. Referências

- Timmons, M.B.; Ebeling, J.M. *Recirculating Aquaculture*, 4ª ed. — RAS clear-water, dimensionamento de drum filter, biofiltro, oxigenação.
- Summerfelt, S.T. (Freshwater Institute) — engenharia de RAS, Cornell dual-drain.
- Avnimelech, Y. *Biofloc Technology – A Practical Guide Book* (2015) — BFT, relação C:N, manejo de floco.
- Emerenciano, M. et al. (2017) — revisões de BFT para tilápia.
- Wasielesky, W. / FURG — centro brasileiro de referência em bioflocos.
- SRAC Fact Sheets 451–453 — química de N/pH em aquicultura.
- Docs 01–10 deste repositório — dados firmes do Projeto RJ.
