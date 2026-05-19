# 03. Climatização e Alimentação (Fase 3)

## Resumo
Instalação da Bomba de Calor Industrial dimensionada para manter a água a 28°C durante o inverno de BH (mínimas de 11°C), com isolamento térmico de lã de rocha nas paredes e bolas flutuantes pretas na superfície. Alimentação automatizada por timers.

## Perfil Climático — Sabará, MG (RMBH)

> **Localização:** o sítio fica em **Sabará-MG**, na RMBH. Os dados climáticos abaixo são de **Belo Horizonte** (a ~20 km), usados como **proxy conservador**: Sabará está em altitude menor (~710 m vs ~850 m de BH), portanto é marginalmente mais quente — a demanda real de aquecimento tende a ser **menor** que a dimensionada aqui.


| Mês | Máx Média (°C) | Mín Média (°C) | Média (°C) | ΔT (28°C - Média) |
| :---: | :---: | :---: | :---: | :---: |
| Jan | 28 | 19 | 23,5 | 4,5 |
| Fev | 29 | 19 | 24,0 | 4,0 |
| Mar | 28 | 18 | 23,0 | 5,0 |
| Abr | 27 | 16 | 21,5 | 6,5 |
| Mai | 25 | 13 | 19,0 | 9,0 |
| Jun | 24 | 12 | 18,0 | 10,0 |
| **Jul** | **24** | **11** | **17,5** | **10,5** |
| Ago | 26 | 13 | 19,5 | 8,5 |
| Set | 27 | 15 | 21,0 | 7,0 |
| Out | 28 | 17 | 22,5 | 5,5 |
| Nov | 27 | 18 | 22,5 | 5,5 |
| Dez | 27 | 19 | 23,0 | 5,0 |

Sem aquecimento, a produção fica inviável por 3-4 meses/ano (Mai-Ago). A Bomba de Calor é um pré-requisito, não um luxo.

## Isolamento Térmico

### Paredes — Lã de Rocha (50mm)
- **Condutividade (λ):** 0,040 W/m·K
- **Coeficiente U (com convecção):** ~0,75 W/m²·K
- **Área lateral por tanque:** 32,6 m²
- **Perda lateral por tanque (ΔT 10,5°C pior caso):** ~257 W
- **Instalação:** Placas envolvendo a lateral externa da geomembrana, protegidas com filme plástico contra umidade.

### Superfície — Bolas Flutuantes Pretas (Shade Balls)
- **Função:** Reduzem evaporação em 80-90% e perda por convecção superficial em ~50%.
- **Área superficial por tanque:** 43,0 m²
- **Perda superficial com bolas (pior caso):** ~2.150 W/tanque
- **Benefício adicional:** Absorvem radiação solar e transferem calor para a água por condução durante o dia.

## Dimensionamento da Bomba de Calor

### Carga Térmica Total (6 tanques, pior caso — Julho)

| Componente | Perda/tanque (W) | Perda 6 tanques (kW) |
| :--- | :---: | :---: |
| Lateral (com Lã de Rocha 50mm) | 257 | 1,5 |
| Superfície (com Bolas Flutuantes) | 2.150 | 12,9 |
| Fundo (contato com solo, ΔT menor) | 300 | 1,8 |
| **TOTAL** | **2.707** | **16,2 kW** |

### Especificação
- **Potência térmica necessária:** ~16 kW (55.000 BTU/h)
- **Com margem de segurança (+25%):** ~20 kW (**68.000 BTU/h**)
- **Equipamento recomendado:** Bomba de Calor Inverter de **80.000 a 100.000 BTU/h** (COP ≥ 5,0)
- **Consumo elétrico médio (COP 5):** 3,2 a 4,0 kW elétrico

### Custo Operacional Mensal (Tarifa CEMIG R$ 0,85/kWh)

| Mês | Custo Bomba de Calor |
| :---: | :---: |
| Jan | R$ 557 |
| Fev | R$ 463 |
| Mar | R$ 639 |
| Abr | R$ 802 |
| Mai | R$ 1.151 |
| Jun | R$ 1.236 |
| **Jul** | **R$ 1.347** |
| Ago | R$ 1.087 |
| Set | R$ 865 |
| Out | R$ 704 |
| Nov | R$ 680 |
| Dez | R$ 639 |
| **Média Mensal** | **R$ 848** |
| **Total Anual** | **R$ 10.170** |

## Alimentação Automatizada
- **Alimentadores vibratórios/rosca:** 6 unidades (1 por tanque), acionados por timer digital.
- **Fracionamento:** 8 a 15 tratos/dia conforme estágio (alevinos mais vezes, engorda menos).
- **Trava de segurança:** CLP bloqueia alimentação se OD < 4,0 mg/L.

---

## Controle de Fotoperíodo — LEDs 16h

### Por que o fotoperíodo importa tanto quanto a temperatura

A tilápia do Nilo regula o crescimento somático via **eixo melatonina → GH (hormônio de crescimento)**. Em noites longas, a glândula pineal produz mais melatonina, que inibe a liberação de GH — o mesmo mecanismo evolutivo que sinaliza "inverno = conserve energia". Isso ocorre **independentemente da temperatura da água**: mesmo com o tanque a 28°C, dias curtos reduzem o crescimento.

A Bomba de Calor da Fase 3 resolve o problema térmico. O sistema de LEDs resolve o problema fotoperiódico — os dois são necessários para alcançar o desempenho máximo da genética GenoMar/Supreme.

### O Problema Específico de BH: Fotoperiodismo de Inverno

| Mês | Horas de Luz Natural (BH) | Déficit para 16h |
| :---: | :---: | :---: |
| Jan | 13,2 h | 2,8 h |
| Fev | 12,9 h | 3,1 h |
| Mar | 12,4 h | 3,6 h |
| Abr | 11,8 h | 4,2 h |
| **Mai** | **11,3 h** | **4,7 h** |
| **Jun** | **11,1 h** | **4,9 h** |
| **Jul** | **11,2 h** | **4,8 h** |
| **Ago** | **11,6 h** | **4,4 h** |
| Set | 12,2 h | 3,8 h |
| Out | 12,7 h | 3,3 h |
| Nov | 13,1 h | 2,9 h |
| Dez | 13,4 h | 2,6 h |

De maio a agosto, a luz natural fica 4,4–4,9 horas abaixo do alvo de 16h. Como os tanques estão em galpão fechado (já isolado termicamente), a luz natural é irrelevante — os LEDs controlam 100% do fotoperíodo.

### Protocolo de Fotoperíodo

| Parâmetro | Especificação |
| :--- | :--- |
| Fotoperíodo alvo | **16L:8D** (16h luz / 8h escuro) — padrão ouro confirmado pela literatura (Lim 2003, Timmons & Ebeling) |
| Por que não 18L:6D | Platô de eficiência documentado: de 16h para 18h não há ganho de peso adicional; 6h de escuro não é suficiente para descanso metabólico completo → cortisol elevado e piora de CA |
| Por que não 24L:0D | Stress crônico, maior canibalismo na alevinagem, piora de CA — biologicamente prejudicial |
| Horário de luz | 06h–22h (ajustável no CLP) |
| **Dimming obrigatório** | **CLP rampa de 0–100% em 15–20 min ao ligar (amanhecer) e 100–0% ao desligar (anoitecer)**. Liga abrupta causa saltos e lesões nos peixes. Implementado via saída PWM do CLP → driver dimerizável dos LEDs. |
| Intensidade na superfície | **30–50 lux** (mínimo para ativação melatonina/GH + comportamento alimentar adequado). Acima de 500 lux inicia stress. |
| Espectro | **Branco frio 5.500–6.500 K** — cobre a faixa azul-verde (430–530 nm) que estimula o fotorreceptor pineal de teleósteos. LEDs amarelados ou vermelhos reduzem a resposta hormonal. |
| **Potência por tanque** | **50 W (2 × barras LED IP67 25 W)** → 5.500 lm × 70% eficiência = ~90 lux — adequado e eficiente. LEDs de 150 W (incorretamente especificados antes) produzem ~307 lux e consomem 3× mais energia sem benefício adicional. |
| Altura de instalação | Fixadas ~1,5 m acima da lâmina d'água; posição central para distribuição difusa e uniforme |
| Limpeza | Mensal (poeira e condensação do galpão) |

### Impacto por Fase de Crescimento

| Fase | Peso | Alvo Biológico Principal | Impacto Documentado |
| :--- | :---: | :--- | :--- |
| Recria (alevinos comprados) | 10–150 g | Uniformidade do lote; janela de alimentação longa reduz dominância | Lote chega à engorda com >90% de uniformidade de tamanho |
| Engorda inicial | 150–500 g | Pico de resposta ao IGF-1 — máxima hipertrofia muscular | Fase com maior ganho percentual (+25–27% vs inverno natural) |
| Engorda final | 500–940 g | Manutenção do estímulo GH/IGF-1 com densidade crescente | Ganho cai para ~22–24% à medida que o peixe se aproxima do abate |
| **Média anualizada do projeto** | — | — | **~24,5%** de ganho no peso final (ver análise sazonal abaixo) |

> **Nota — Larvicultura**: o ganho de +40% citado em literatura refere-se à fase de larvicultura interna (0–20 g). O projeto compra alevinos externos → essa fase não ocorre no sistema e não impacta nossos cálculos de ciclo.

### Impacto no Peso de Despesca

A literatura para tilápia do Nilo em RAS (Lim et al. 2003; Rad et al. 2006; Biswas et al. 2005) mostra consistentemente **+20–25% no peso final** com fotoperíodo de 16–18h versus fotoperíodo natural subtropical. Para BH (fotoperíodo médio ~12h), os 4 meses de déficit mais crítico (maio–agosto) coincidem com 2/3 do ciclo de engorda.

| Parâmetro | Sem Fotoperíodo (natural ~12h) | **Com Fotoperíodo (16h artificial)** |
| :--- | :---: | :---: |
| Peso médio no T6 (6 meses) | 750 g (700–850 g) | **940 g (875–1.050 g)** |
| Biomassa no T6 (2.550 peixes) | 1.913 kg | **2.391 kg** |
| Filé/mês (33%) | 631 kg | **789 kg** |
| Aumento | — | **+25%** |
| Densidade ao despescar (T6 = 60 m³) | 31,9 kg/m³ | **39,8 kg/m³** |

A densidade de despesca de 39,8 kg/m³ está dentro da capacidade do RAS projetado (suporta até 50–60 kg/m³ com aeração adequada e controle de OD/TAN via CLP).

> **Nota:** Toda a documentação financeira anterior (Doc 07) usa o peso base sem fotoperíodo (1.913 kg/mês) como cenário conservador. Ver [Doc 07 — Seção "Impacto do Fotoperíodo"](07_Plano_Financeiro.md) para os cenários financeiros corrigidos.

---

### Estudo Crítico — O +25% é Realista?

> **Conclusão antecipada:** o +25% é o **limite otimista**, derivado de comparações contra fotoperíodo curto (8h). Contra o cenário real do projeto (16h artificial vs ~12h natural, **com temperatura controlada a 28°C**), a literatura sustenta um ganho realista de **+10% a +18%**. Recomenda-se planejar o modelo financeiro com **+12% a +15%** e tratar +25% como cenário de *upside*, não como base.

#### Três Vieses na Fundamentação Original

| Viés | Explicação | Efeito sobre o +25% |
| :--- | :--- | :---: |
| **1. Baseline de comparação** | Lim et al. (2003) reporta "+23% com 16h **vs 8h**". 8h é um fotoperíodo artificialmente curto. O projeto **não** compete contra 8h — compete contra a luz natural de Sabará/RMBH (~11–13h). Contra ~12h, o delta é muito menor. | Superestima |
| **2. Confundimento com janela alimentar** | Em RAS com alimentadores automáticos operando 16h, parte do "ganho de fotoperíodo" é, na verdade, **mais horas de arraçoamento**. Esse ganho é real, mas é obtível por manejo de alimentação — não é efeito fotoperiódico puro. | Atribui ao fotoperíodo um ganho que é alimentar |
| **3. Interação com temperatura** | O limitante dominante de crescimento no inverno de BH/Sabará é a **temperatura** (alimentação cessa < 20°C). A Bomba de Calor (Fase 3) já resolve isso. **Com temperatura controlada a 28°C o ano todo, o benefício marginal do fotoperíodo encolhe** — boa parte do "+25% vs inverno natural" é, na verdade, o efeito do aquecimento, não da luz. | Mistura efeito térmico com fotoperiódico |

#### O Que a Literatura Realmente Sustenta (tilápia-do-nilo, engorda, temp. controlada)

- **Fase de engorda (150–940 g — a relevante; alevinos são comprados):** ganho fotoperiódico isolado tipicamente **+5% a +18%** vs fotoperíodo natural tropical/subtropical, quando ração e temperatura são equalizadas (Biswas et al. 2005; El-Sayed & Kawanna 2004 mostram que o efeito atenua quando a ração não é o limitante).
- **+20–30%** aparece sobretudo em comparações contra 8h ou em larvicultura (0–20 g) — **fase que não ocorre neste projeto** (alevinos externos).
- Mecanismo (supressão de melatonina → eixo GH/IGF-1) é **real e direcionalmente correto** — a discordância é de **magnitude**, não de sinal. O fotoperíodo ajuda; a questão é quanto.

#### Sensibilidade Financeira ao Ganho Real (2.550 peixes, base 750 g)

| Ganho fotoperiódico | Peso despesca | Biomassa T6 | Filé/mês | vs cenário doc (+25%) |
| :---: | :---: | :---: | :---: | :---: |
| +25% *(otimista — doc atual)* | 940 g | 2.391 kg | 789 kg | base |
| **+18% (otimista-realista)** | **885 g** | **2.257 kg** | **745 kg** | **−5,6%** |
| **+12% (conservador recomendado)** | **840 g** | **2.142 kg** | **707 kg** | **−10,4%** |
| +8% (pessimista) | 810 g | 2.066 kg | 682 kg | −13,6% |
| 0% (sem fotoperíodo) | 750 g | 1.913 kg | 631 kg | −20,0% |

> **Implicação:** se o ganho real for **+12%** em vez de +25%, a produção de filé cai ~10,4%, o que reduz o faturamento na mesma proporção e alonga o payback. O CAPEX dos LEDs (R$ 2.000) tem payback < 1 mês mesmo a +8% — **o investimento em LED continua trivialmente justificado**; o que precisa de correção é a **expectativa de produção** embutida no modelo financeiro, que está calibrada no teto otimista.

#### Recomendação

1. **Manter o sistema de LEDs** — custo irrisório, payback < 1 mês mesmo no cenário pessimista, e o efeito é direcionalmente positivo.
2. **Recalibrar o modelo financeiro** para **+12% a +15%** como base (despesca ~840–865 g), com +25% como cenário de *upside* explícito — não como número de capa.
3. **Validar em campo** no primeiro ciclo: pesar lotes com e sem extensão de fotoperíodo (mantendo ração e temperatura iguais) para medir o ganho **real do sítio** antes de escalar projeções.

*Fundamentação: Lim et al. (2003); Rad et al. (2006); Biswas et al. (2005, 2006); El-Sayed & Kawanna (2004). Síntese honesta: o sinal é positivo e consolidado; a magnitude de +25% é o limite superior de condições específicas (vs 8h / larvicultura), não a expectativa mediana para engorda com temperatura controlada.*

### CAPEX e OPEX do Sistema de Fotoperíodo

| Item | Qtd | Valor (R$) |
| :--- | :---: | :--- |
| Barras LED IP67 25 W (branco frio 6.000 K) | 12 (2/tanque) | 900 |
| Driver LED dimerizável (saída PWM do CLP) | 6 (1/tanque) | 600 |
| Estrutura de fixação + cabeamento + conectores | 6 tanques | 500 |
| **TOTAL FOTOPERÍODO** | | **R$ 2.000** |

> **Por que 25 W e não 75 W?** O alvo biológico para tilápia é 30–50 lux na superfície da água. Cada barra de 25 W entrega ~2.750 lm; dois por tanque = ~5.500 lm. Com eficiência de distribuição de ~70%, a iluminância na lâmina d'água fica em torno de **90 lux** — dentro do intervalo ótimo. Barras de 75 W produziriam ~307 lux (6× o mínimo necessário) e consumiriam 3× mais energia sem benefício fisiológico adicional.

**OPEX:**
- Energia (**50 W × 16 h/dia × 6 tanques** = 4,8 kWh/dia → **144 kWh/mês**): **R$ 122/mês** (Fases 1–4).
- **Fase 5 em diante:** energia coberta pela geração solar — OPEX de LEDs = **R$ 0**.
- Payback do sistema de fotoperíodo: R$ 2.000 / [(R$ 37.083 − R$ 29.657) / mês × margem] = **< 1 mês**.

### Validação Matemática — Por que o ciclo permanece em 6 meses

Algumas fontes citam a compra de alevinos externos (em vez de larvicultura própria) como fator que "encurta o ciclo para 5 meses". Essa premissa **não se aplica a este projeto** por dois motivos:

1. **O projeto já compra alevinos.** Não existe larvicultura interna — os alevinos chegam com 10–15 g, prontos para recria. Não há fase a eliminar.
2. **O TGC (Thermal Growth Coefficient) prova que 5 meses = subcomercial.**

**Equação do TGC:**

```
TGC = (W_final^(1/3) − W_inicial^(1/3)) / (T × dias)
```

Calibrado com os dados reais do projeto (alevino 10 g → 940 g em 180 dias a 28°C, com fotoperíodo):

```
TGC_projeto = (940^(1/3) − 10^(1/3)) / (28 × 180)
            = (9,791 − 2,154) / 5.040
            = 0,001516
```

**Peso projetado por duração de ciclo:**

| Duração | Dias | Peso final estimado | Comercial? |
| :---: | :---: | :---: | :---: |
| 5 meses | 150 | **618 g** | Não (abaixo de 700 g) |
| 6 meses | 180 | **940 g** | Sim ✓ |
| 6,2 meses | 185 | **1.000 g** | Sim (< 1 semana a mais) |
| 7 meses | 210 | **1.128 g** | Sim (excesso de permanência) |

**Conclusão:** O ciclo de **6 meses → 940 g** é o ponto ótimo para o sistema sequencial de 6 tanques. Um ciclo de 5 meses entregaria peixes de ~618 g — abaixo do peso mínimo de comercialização para filé inteiro. Alongar para 7 meses gera retorno marginal decrescente e aumento de densidade além de 50 kg/m³.

---

## Riscos e Limitações
- **Bomba de Calor como único agente térmico:** Sem estufa ou lonas, a carga térmica recai 100% sobre a bomba. Se ela falhar no inverno, a temperatura cai rapidamente. Recomendação: manter contato com assistência técnica para reparo em 24h.
- **Bolas flutuantes x manejo:** As bolas precisam ser afastadas durante a alimentação e biometrias. Redes ou barreiras flutuantes podem facilitar isso.

## Custos Estimados — Fase 3

| Item | Qtd | Valor (R$) |
| :--- | :---: | :--- |
| Bomba de Calor Inverter (80-100k BTU) | 1 | 30.000 |
| Isolamento lã de rocha 50mm (6 tanques) | 6 | 5.400 |
| Bolas flutuantes pretas (6 tanques, ~43m² cada) | 6 | 4.200 |
| Alimentadores automáticos (vibratório/rosca) | 6 | 10.500 |
| Tubulações térmicas (CPVC) e instalação | 1 | 4.000 |
| Sistema de fotoperíodo LED (barras 25 W + drivers PWM + fixação) | 1 | 2.000 |
| **TOTAL FASE 3** | | **R$ 56.100** |
