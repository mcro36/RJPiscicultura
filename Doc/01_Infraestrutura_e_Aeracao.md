# 01. Infraestrutura e Aeração (Fase 1)

## Resumo
Montagem dos 7 tanques circulares de geomembrana (60m³ cada, Ø 7,40m × 1,40m útil) em dois patamares com desnível de 2,5m — 6 tanques de produção escalonada + 1 T7 Acabamento Comercial (depuração). O sistema utiliza Bomba de Recirculação dedicada para circulação e manutenção do vórtice Cornell, com design Cornell Dual-Drain para autolimpeza eficiente.

## Modelo Operacional (Ciclo dos Tanques)
Os peixes **permanecem no mesmo tanque** durante todo o ciclo de 6 meses. Não há transferência entre tanques.

1. Mês 1: T1 recebe alevinos.
2. Mês 2: T2 recebe alevinos. T1 continua crescendo.
3. Meses 3-6: Os demais tanques são ativados sequencialmente.
4. Mês 7: T1 atinge peso de despesca (~800g). Peixes são transferidos ao **T7 — Tanque de Acabamento Comercial** (24–48 h com Fase 6B, ou 3–5 dias sem ela). T1 é limpo e repovoado com alevinos. Ver [Doc 06 — Seção 1](06_Qualidade_Riscos_e_Licenciamento.md) para as três razões pelas quais o T7 dedicado é obrigatório mesmo com apenas 24h de permanência.
5. Mês 8: T2 é despescado. E assim por diante — **uma despesca por mês**.

## Dimensionamento de Biomassa (Regime Estável, com Fotoperíodo 16h)

Após os primeiros 6 meses, cada tanque estará em um estágio diferente do ciclo. Os pesos abaixo refletem o desempenho **com fotoperíodo artificial de 16h** (LEDs, Fase 3), que eleva o peso médio de despesca de 750 g para ~940 g (+25%). Ver [Doc 03 — Seção Fotoperíodo](03_Climatizacao_e_Alimentacao.md) para a fundamentação técnica.

| Tanque | Mês do Ciclo | Peso Médio (g) | Nº Peixes | Biomassa (kg) |
| :---: | :---: | :---: | :---: | :---: |
| Ciclo 1 | 1 | 12–65 | 2.900 | 109 |
| Ciclo 2 | 2 | 65–190 | 2.750 | 344 |
| Ciclo 3 | 3 | 190–375 | 2.650 | 745 |
| Ciclo 4 | 4 | 375–625 | 2.600 | 1.297 |
| Ciclo 5 | 5 | 625–875 | 2.570 | 1.924 |
| **Ciclo 6** | **6** | **875–1.050** | **2.550** | **2.391** |
| **TOTAL** | | | | **6.810 kg** |

*Mortalidade acumulada considerada: ~10% alevinagem, ~3% recria, ~1–2% engorda.*

> **Referência (sem fotoperíodo — cenário conservador):** pesos 700–850 g, biomassa T6 = 1.913 kg, total 5.453 kg. Usado como linha de base nas versões iniciais do Doc 07; ver seção "Impacto do Fotoperíodo" em [Doc 07](07_Plano_Financeiro.md) para a comparação financeira completa.

## Aeração (O Pulmão)
- **Sopradores de Canal Lateral:** 2 unidades de 2.0 CV, operando em rede mestra de PVC (75-100mm) com distribuição em anel (Ring Main).
- **Difusores:** Difusores Tubulares de Membrana EPDM lastreados no fundo de cada tanque. Vantagens sobre a mangueira microperfurada convencional: bolhas finas 1–3 mm (vs 3–5 mm), OTE ~35–45% (vs ~25–35%), membrana autossélante (sem refluxo ou incrustação biológica), vida útil 6–10 anos (vs 3–5 anos) e compatibilidade direta com os sopradores de canal lateral existentes.

## Hidrodinâmica: Design Cornell Dual-Drain
Para garantir a autolimpeza eficiente em tanques de 7,4m de diâmetro, o projeto adota o design comprovado pela Cornell University:

### Entrada Tangencial
- A tubulação de retorno de água (da Bomba de Recirculação) entra no tanque por **bocais tangenciais ajustáveis** posicionados na parede, na altura da linha d'água.
- A força do jato de entrada cria a rotação constante (vórtice).

### Duplo Dreno
- **Dreno central de fundo (5-20% do fluxo):** Remove água concentrada em sólidos (fezes e restos de ração). O fundo do tanque deve ter inclinação cônica mínima de 5% em direção ao centro.
- **Dreno lateral elevado (80-95% do fluxo):** Remove água "limpa" da coluna superior para recirculação.

### Bomba de Recirculação (Circulação e Vórtice Cornell)
- **6 bombas centrífugas inline de 0,5 CV c/ inversor de frequência (VFD)** (1 por tanque de produção), instaladas na linha de retorno do biofiltro.
- Ponto de operação de projeto: **400 L/min** a 4,5 m AMT (desnível biofiltro P3 → bocais P1/P2 + perdas por fricção).
- O VFD ajusta a rotação conforme a biomassa do tanque: 40% de velocidade nos meses 1–2 (~160 L/min, ~25 W) → 90% no mês 6 (~400 L/min, ~290 W). Média ponderada ao longo do ciclo de 6 estágios: **~160 W/bomba**.
- A água retorna pelo bocal tangencial, criando e mantendo o vórtice Cornell ativo ininterruptamente com velocidade tangencial de 0,10–0,20 m/s na parede — conforme especificação Cornell.
- Consumo elétrico total médio: 6 × ~160 W = **~960 W** (~691 kWh/mês; custo ~R$ 587/mês a R$ 0,85/kWh).

### Limpeza por Gravidade
- O desnível de 2,5m entre os patamares do terreno permite que a descarga do dreno central dos tanques superiores escoe por gravidade para um decantador no nível inferior.

---

## Por que Não Airlift — Síntese

O airlift é **estruturalmente incompatível** com este projeto por dois motivos físicos:

1. **Razão de Submersão insuficiente:** no circuito externo (biofiltro P3 → bocais tangenciais), `Sr = 1,20 / (1,20 + 3,0) = 0,286` — abaixo do limiar funcional de 0,30. Para atingir Sr = 0,65 (mínimo aceitável) seriam necessários **5,6 m de lâmina d'água**; os tanques têm 1,40 m.
2. **Descarga vertical:** o airlift não gera fluxo tangencial — o vórtice Cornell exige velocidade tangencial de 0,10–0,20 m/s na parede; um airlift acoplado a cotovelo 90° entregaria ~0,003 m/s (33–67× abaixo do mínimo Cornell).

**Penalidade energética:** ~1.600 W de compressão vs ~160 W da Bomba 0,5 CV c/ VFD para o mesmo trabalho hidráulico — **10× mais consumo**. Em todos os cenários operacionais reais (alevinagem, troca parcial, pós-despesca), o airlift externo estaria fora da faixa funcional.

> Análise completa com dedução de Sr, Casos A/B, Regra dos 2,5 m, agravamento ao longo do ciclo e Diagrama de Incompatibilidade: **[01b — Sistema RAS](01b_Sistema_RAS.md)**.
>
> **Referências:** Loyless & Malone (1998), *Evaluation of air-lift pump capabilities for water delivery, aeration, and degasification*; Timmons & Ebeling, *Recirculating Aquaculture*, cap. 5 (Airlift Pumps).

---

## Tratamento de Sólidos e Biofiltração

O dimensionamento completo do circuito de tratamento de água — dreno central 24/7 (3 razões físicas + cálculo de fluxo e TSS), Decantador Cônico 1.500L, Decantador Laminar (41 placas, corte ~62 µm), Loop Kidney 10 µm e Filtro Percolador com desgasificação de CO₂ — está documentado em:

> **[01b — Sistema RAS: Funcionamento Detalhado](01b_Sistema_RAS.md)**

---

## Riscos e Limitações
- **Velocidade do vórtice:** Se a vazão da Bomba de Recirculação for insuficiente para manter a rotação em tanques de 7,4m, pode ser necessário adicionar mais de um ponto de injeção tangencial por tanque (2 a 3 bocais distribuídos).
- **Fundo cônico:** A inclinação mínima de 5% é essencial. Sem ela, os sólidos não migram para o dreno central e a qualidade da água degrada.
- **Terraplenagem:** Tanques de 60m³ pesam 60 toneladas. Em terreno inclinado, a compactação mecanizada do solo de base é obrigatória para evitar recalque diferencial.
- **Percolador vedado:** Encobrir as laterais do percolador elimina o stripping de CO₂ e aumenta o consumo mensal de calcário no contator passivo.

## Processamento — Linguiça de Tilápia

A produção de linguiça começa na **primeira despesca (mês 7)**, junto com a filetagem. Os equipamentos são instalados na Fase 1 para que o processamento integral já esteja operacional desde o início do faturamento. Ver dimensionamento completo em [Doc 08 — Canais de Venda e Produtos](08_Canais_de_Venda_e_Produtos.md).

| Item | Qtd | Valor (R$) |
| :--- | :---: | :--- |
| Moedor industrial de carne | 1 | 4.000 |
| Embutideira industrial | 1 | 4.500 |
| Seladora a vácuo | 1 | 2.500 |
| Freezer horizontal adicional (200 L) | 1 | 2.000 |
| **Subtotal Linguiça** | | **R$ 13.000** |

---

## Custos Estimados — Fase 1

### Infraestrutura e Aeração
| Item | Qtd | Valor (R$) |
| :--- | :---: | :--- |
| Tanques geomembrana (60m³) c/ estrutura metálica (6 produção + 1 T7) | 7 | 56.000 |
| Sopradores Canal Lateral 2.0 CV | 2 | 10.000 |
| Material hidráulico (tubulações, drenos, bocais tangenciais) | 1 | 8.000 |
| Difusores Tubulares de Membrana EPDM (aeração de fundo, conexões) | 1 | 4.500 |
| Bombas de Recirculação 0,5 CV inline c/ VFD (1 por tanque de produção) | 6 | 7.200 |
| Terraplenagem e preparação do terreno (2 patamares) | 1 | 7.000 |
| Elétrica básica (quadro, cabos, disjuntores) | 1 | 3.500 |
| Primeiro lote de alevinos (genética GenoMar/Supreme) | 1 | 2.500 |
| Ferramentas de manejo (redes, balanças, kits teste) | 1 | 1.500 |
| Sump Coletor 300L HDPE (recebe dreno central dos 6 tanques) | 1 | 800 |
| Decantador Cônico 1.500L PEAD (cone 60° autoesvaziante + válvula de purga) | 1 | 1.400 |
| Decantador Laminar (caixa 2,8 m³ + 41 placas PVC + estrutura 55°) | 1 | 1.800 |
| Interligação por gravidade (vertedouros, tubulações, conexões) | 1 | 600 |
| Loop Kidney — bomba dedicada 0,25 CV (polimento side-stream) | 1 | 600 |
| Loop Kidney — carcaça PVC fecho rápido + 3 mangas poliéster 10 µm | 1 | 450 |
| Galpão de processamento SIE (sala de abate + câmara fria + antecâmara + paredes laváveis; **não cobre os tanques**) | 1 | 60.000 |
| Placas rígidas de EPS para tampar os 7 tanques (cobertura térmica + bloqueio de luz natural p/ controle de fotoperíodo) | 7 | 15.000 |
| Gerador a Gasolina 8–10 kVA + Quadro de Transferência Automática (QTA) *(segurança energética — obrigatório na Fase 1 pois os alevinos entram no mês 1; ver justificativa abaixo)* | 1 | 12.000 |
| Redundância N+1 (bomba recirculação 0,5 CV reserva + cap óptico OD reserva + eletrodo pH reserva) | 1 | 4.000 |
| **Subtotal Infraestrutura** | | **R$ 196.850** |

### Processamento — Linguiça
| Item | Qtd | Valor (R$) |
| :--- | :---: | :--- |
| Moedor industrial de carne | 1 | 4.000 |
| Embutideira industrial | 1 | 4.500 |
| Seladora a vácuo | 1 | 2.500 |
| Freezer horizontal adicional (200 L) | 1 | 2.000 |
| **Subtotal Linguiça** | | **R$ 13.000** |

| | |
| :--- | :--- |
| **TOTAL FASE 1** | **R$ 209.850** |

> **Por que o gerador está na Fase 1 (não na Fase 2):** Os alevinos entram no mês 1 e já há biomassa viva desde a primeira semana. Uma falha elétrica noturna (apagão de minutos) com sopradores parados causa colapso de OD e pode dizimar um tanque inteiro — R$ 9.000 em insumos + 6 meses de produção perdidos. O custo de proteção (R$ 12.000) é irrisório frente ao risco. A automação multiplexada de OD (Fase 2) complementa o gerador mas não o substitui: sem energia, nenhum sensor adiantará. **O gerador é a primeira linha de defesa, não uma conveniência de Fase 2.**

> **Nota de reconciliação térmica:** as placas de EPS exercem a função de redução de perda térmica de superfície e bloqueio de luz natural (essencial para o controle de fotoperíodo por LED). Isso **torna redundante a linha "bolas flutuantes" da Fase 3** (Doc 03, ~R$ 4.200) — recomenda-se substituir, não somar, na próxima revisão do Doc 03 para evitar dupla contagem de tratamento de superfície.
