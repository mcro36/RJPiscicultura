# 01b. Sistema RAS — Funcionamento Detalhado

> Documento técnico complementar de [01 — Infraestrutura e Aeração](01_Infraestrutura_e_Aeracao.md). Detalha o funcionamento dos três subsistemas que garantem a qualidade da água em regime superintensivo: **(1)** justificativa da escolha da Bomba de Recirculação sobre airlift; **(2)** operação contínua do dreno de fundo e trem de sólidos por gravidade; **(3)** biofiltração e desgasificação de CO₂.

---

## Por que Não Airlift — Análise Técnica de Incompatibilidade

### Física do Airlift — O Princípio

O airlift funciona injetando ar comprimido na base de um tubo vertical. A mistura ar-água tem densidade menor que a água pura ao redor, criando empuxo e fluxo ascendente. A variável que governa **tudo** é a **Razão de Submersão (Sr)**:

```
Sr = Hs / (Hs + Hd)
```

Onde:
- **Hs** = comprimento do tubo abaixo da superfície da água (submersão disponível)
- **Hd** = altura de descarga acima da superfície da água (carga hidrostática de trabalho)

A eficiência é uma **função não-linear e abrupta** de Sr:

| Sr | Eficiência hidráulica | Situação |
| :---: | :---: | :--- |
| 0,80 | ~45–55% | Ótimo — padrão em RAS profundos (≥ 3 m) |
| 0,65 | ~30–40% | Aceitável |
| 0,50 | ~15–20% | Marginal |
| 0,35 | ~5–10% | Praticamente inoperante |
| < 0,30 | < 5% | Falha funcional |

---

### Caso A — Circuito Interno (airlift dentro do tanque)

Com airlift submerso em 1,20 m (instalado a 0,20 m do fundo) e descarga **na própria superfície da água**:

```
Hd = 0   →   Sr = 1,20 / (1,20 + 0) = 1,00
```

Sr = 1,0 seria ótimo em termos de eficiência, **mas o fluxo gerado é estritamente vertical**. Não existe componente tangencial — o vórtice Cornell não é criado. O airlift interno mistura o tanque verticalmente mas é incapaz de induzir a rotação centrípeta que concentra sólidos no dreno central. Solução que aeraria sem limpar.

---

### Caso B — Circuito Externo (Cornell: biofiltro em P3 → bocais tangenciais)

Para que o vórtice Cornell funcione, a água precisa sair do tanque, passar pelo biofiltro (localizado 2,5 m acima dos tanques de produção no desnível do terreno) e retornar pelos bocais tangenciais. Adicionando as perdas por fricção nas tubulações (~0,5 m AMT):

```
Hd = 2,5 m (desnível real) + 0,5 m (fricção) = 3,0 m AMT

Sr = 1,20 / (1,20 + 3,0) = 1,20 / 4,20 = 0,286
```

**Sr = 0,286 — abaixo do limiar de funcionamento prático (0,30).** O airlift não tem força hidrostática suficiente para empurrar água até o biofiltro. Na prática, a coluna de ar-água no tubo simplesmente borbulha para cima e retorna ao tanque sem trabalho útil.

---

### A Regra dos 2,5 m — Origem e Dedução

Para atingir **Sr = 0,65** (mínimo aceitável) com Hd = 3,0 m (circuito externo deste projeto):

```
0,65 = Hs / (Hs + 3,0)
Hs = 0,65 × 3,0 / (1 − 0,65) = 5,57 m de lâmina d'água
```

Seriam necessários **tanques com 5,6 m de profundidade** para o airlift funcionar bem neste circuito. Para Hd = 1,5 m (circuito externo típico de RAS com biofiltro baixo), o mínimo seria:

```
Hs = 0,65 × 1,5 / 0,35 = 2,79 m ≈ 2,5–3,0 m
```

Daí vem a regra prática: **airlift externo exige lâmina d'água ≥ 2,5 m**. Tanques rasos de aquicultura intensiva (1,0–1,5 m) são estruturalmente incompatíveis com airlifts em circuito externo.

---

### Penalidade Energética

A eficiência de um airlift a Sr = 0,286 cai para ~5–8%. Para entregar 400 L/min contra 3,0 m AMT:

| Solução | Potência necessária | kWh/mês | Custo/mês |
| :--- | :---: | :---: | :---: |
| Bomba 0,5 CV c/ VFD (η ≈ 60%) | ~160 W médio | ~115 kWh | ~R$ 98 |
| Airlift a Sr = 0,286 (η ≈ 6%) | ~1.600 W de compressão | ~1.152 kWh | ~R$ 979 |

O airlift consumiria **10× mais energia** que a bomba centrífuga para o mesmo trabalho hidráulico, anulando completamente qualquer vantagem de custo de equipamento.

---

### Agravamento ao Longo do Ciclo de Engorda

A lâmina de 1,40 m é o máximo operacional — em vários momentos ela é menor:

| Situação | Lâmina real | Sr (circuito externo) | Status |
| :--- | :---: | :---: | :--- |
| Operação plena (mês 6) | 1,40 m | 0,286 | ❌ Inoperante |
| Abastecimento inicial (mês 1) | ~0,90 m | 0,231 | ❌ Totalmente morto |
| Troca parcial de água | ~1,10 m | 0,268 | ❌ Inoperante |
| Limpeza pós-despesca | ~0,20 m | 0,063 | ❌ Morto |

Em **todos os cenários operacionais reais**, o airlift externo estaria fora da faixa funcional. A Bomba de Recirculação 0,5 CV c/ VFD entrega 400 L/min (ou o que o VFD determinar) **independentemente do nível d'água no tanque**.

---

### Problema Estrutural de Tangencialidade

Mesmo que o airlift vencesse a carga hidrostática (em tanque hipotético de 5,6 m), persistiria um problema fundamental: **a descarga do airlift é vertical**, não tangencial. O vórtice Cornell exige fluxo **tangente à parede** para criar rotação (efeito "xícara de chá" — Força de Bagnold). Um airlift acoplado a um cotovelo 90° externo perderia todo o ganho de pressão nos joelhos e nas tubulações — exatamente a carga que ele mal consegue vencer. A velocidade tangencial resultante na parede seria ~0,003 m/s contra o mínimo Cornell de 0,10–0,20 m/s — 33–67× abaixo do necessário.

---

### Conclusão — Diagrama de Incompatibilidade

```
Tanque 60 m³, Ø 7,40 m, lâmina 1,40 m
         │
         ├── Airlift interno (Sr ≈ 1,0)
         │         ✅ Aeração razoável
         │         ❌ Sem rotação tangencial → não limpa fundo
         │         ❌ Não serve ao biofiltro externo
         │
         └── Airlift externo (Sr = 0,29)
                   ❌ Abaixo do limiar funcional (< 0,30)
                   ❌ Consome 10× mais energia
                   ❌ Piora com tanque parcialmente cheio
                   ❌ Descarga vertical — vórtice Cornell impossível
                   ❌ Necessitaria 5,6 m de profundidade para funcionar

Solução adotada: Bomba 0,5 CV c/ VFD
         ✅ Independe completamente da lâmina d'água
         ✅ 400 L/min controlados pelo VFD por estágio de biomassa
         ✅ Fluxo tangencial via bocal — vórtice Cornell real e mensurável
         ✅ Opera desde o mês 1 (alevinagem, tanque parcialmente cheio)
         ✅ 10× mais eficiente energeticamente
```

> **Referências:** Loyless & Malone (1998), *Evaluation of air-lift pump capabilities for water delivery, aeration, and degasification*; Timmons & Ebeling, *Recirculating Aquaculture*, cap. 5 (Airlift Pumps).

---

## Dreno Central (5%) — Operação Contínua 24/7

> **Fundamento:** Timmons & Ebeling (*RAS*, cap. 6); Cornell Dual-Drain Engineering Guidelines.

O dreno de fundo **não é uma válvula de limpeza periódica** — é um canal permanentemente aberto, operando 24 horas por dia, 7 dias por semana, sem interrupção. Três razões físicas e biológicas tornam isso obrigatório:

### Razão 1 — O Vórtice Não Para

Os bocais tangenciais e a Bomba de Recirculação mantêm a rotação da água ativa ininterruptamente (efeito xícara de chá). Essa força centrípeta concentra fezes e restos de ração exatamente no centro do fundo cônico a todo momento. Fechar o dreno por qualquer período causa acúmulo rápido de lodo no ponto de maior adensamento, degradando o espaço disponível para as tilápias e iniciando o ciclo de mineralização.

### Razão 2 — Prevenção da Quebra Mecânica das Fezes

As fezes de tilápia saem envolvidas por membrana mucosa — enquanto inteiras (> 80 µm), são coletáveis por sedimentação gravitacional. Se o lodo ficar estagnado no fundo, o nado dos peixes e o turbilhonamento da água fragmentam essas partículas em micropartículas < 50 µm. Essas micropartículas:
- Escapam dos decantadores cônico e laminar (Vs abaixo do limiar de captura)
- Atingem o biofiltro, sufocando as bactérias nitrificantes
- Causam aumento abrupto de TAN e queda de OD

> O dreno contínuo a baixa velocidade (< 0,3 m/s) remove as fezes **antes** que o nado dos peixes as fragmente. Por isso o circuito de sólidos opera **integralmente por gravidade**, sem bomba centrífuga — qualquer impelidor a montante dos decantadores recriaria a fragmentação que o dreno contínuo evita (ver Seção *Circuito de Sólidos por Gravidade*).

### Razão 3 — Prevenção da Mineralização (Pico de Amônia)

Matéria orgânica estagnada em contato com água sofre hidrólise bacteriana (bactérias heterotróficas) em horas, convertendo sólido em TAN dissolvido e consumindo OD. O dreno contínuo "limpa o reator químico" antes que a poluição física se converta em poluição química dissolvida.

---

### Cálculo Completo do Fluxo do Dreno de Fundo

**Dados de projeto:**

| Parâmetro | Valor | Fonte |
| :--- | :---: | :--- |
| Tanques | 6 × 60 m³ | Projeto |
| Fração do dreno central | 5% do fluxo total | Cornell Design (5–20%) |
| Fluxo total por tanque (recirculação) | 24,0 m³/h = 400 L/min | Calculado |
| **Dreno de fundo por tanque** | **1,2 m³/h = 20 L/min** | 5% do total |
| **Dreno de fundo total (6 tanques)** | **7,2 m³/h = 120 L/min** | Soma |

> *A fração de 5% (em vez de 10%) reduz o volume de água desviado para o circuito de tratamento, dobrando a concentração de TSS coletado (mesma massa de sólidos em metade do volume) — o que aumenta a eficiência de captura por sedimentação. O dreno 5% ainda excede com folga o limiar mínimo Cornell.*

**Volume diário de água pelo dreno:**
```
7,2 m³/h × 24h = 172,8 m³/dia = 172.800 L/dia
```

**Carga de sólidos estimada no dreno:**

| Parâmetro | Cálculo | Resultado |
| :--- | :--- | :--- |
| Ração fornecida/dia | — | 97 kg/dia |
| Fezes (matéria seca, 3,5% da ração) | 97 × 0,035 | 3,4 kg MS/dia |
| Ração não consumida (< 3%) | 97 × 0,03 | 2,9 kg/dia |
| **Total sólidos orgânicos (MS)** | — | **6,3 kg MS/dia** |
| Fezes úmidas (85% água) | 6,3 / 0,15 | 42 kg/dia |
| **TSS no dreno de fundo** | 6.300 g / 172.800 L | **36 mg/L** |

> *Com a fração de 5% e 400 L/min, o volume diário pelo dreno é de 172.800 L/dia e o TSS bruto é de 36 mg/L (já considerando a fragmentação parcial inerente ao transporte hidráulico).*

**Destino dos sólidos após tratamento (cascata real por gravidade):**

| Etapa | TSS entrada | Eficiência global | TSS saída |
| :--- | :---: | :---: | :---: |
| Dreno de fundo (bruto) | 36 mg/L | — | 36 mg/L |
| Decantador Cônico (> 150 µm) | 36 mg/L | ~35% | **23 mg/L** |
| Decantador Laminar (corte ~62 µm) | 23 mg/L | ~72% | **6,4 mg/L** |
| Loop *kidney* — Filtro de Manga 10 µm (10–30 µm) | *side-stream* | parcial | **→ ~3 mg/L** |
| Polimento Fase 6 (TiO₂/UV — < 10 µm + DOC) | ~3 mg/L | mineralização | **< 2 mg/L** ✓ |

Resultado: TSS entregue ao biofiltro ≈ **3 mg/L** pelo conjunto cônico+laminar (sem fragmentação adicional), refinado a **< 2 mg/L** após o polimento da Fase 6 — dentro da faixa de projeto (3–8 mg/L) com folga. Dimensionamento detalhado dos decantadores na seção seguinte.

---

## Circuito de Sólidos por Gravidade (Cônico + Laminar)

> **Decisão de projeto (revisão 2026-05):** O Hidrociclone e a Bomba de Sólidos foram **substituídos** por um trem de sedimentação gravitacional (Decantador Cônico + Decantador Laminar). Justificativa técnica completa abaixo.

### Por que Não Hidrociclone — Incompatibilidade com Efluente Orgânico

O hidrociclone foi desenvolvido para a mineração: separação de partículas **densas** (2,5–4,0 g/cm³) em alta velocidade. Fezes de tilápia têm propriedades opostas:

| Propriedade | Mineral (ideal p/ HC) | Fezes de tilápia |
| :--- | :---: | :---: |
| Densidade | 2,5–4,0 g/cm³ | **1,01–1,05 g/cm³** |
| Superfície | Hidrofóbica rígida | **Mucosa deformável** |
| Eficiência real | 80–95% | **40–55%** (Timmons & Ebeling, cap. 9) |
| Velocidade de entrada | 3–5 m/s | **fragmenta a membrana mucosa** |

O HC tem três defeitos fatais nesta aplicação:
1. **Fabrica o problema:** a entrada tangencial a 3–5 m/s cisalha as fezes, *gerando* a fração < 20 µm — a mais difícil e cara de remover depois.
2. **Não finaliza sozinho:** entrega apenas 40–55% e exige um settler a jusante de qualquer forma — é um estágio *adicional*, não substituto.
3. **Exige bomba a montante:** mais um motor, mais energia, mais um ponto de fragmentação.

A sedimentação gravitacional opera a < 0,3 m/s: **zero fragmentação**, captura superior para partículas de baixa densidade, e dispensa qualquer bomba.

---

### Base de Dimensionamento

| Parâmetro | Valor |
| :--- | :---: |
| Vazão de dreno (6 tanques) | 120 L/min = 7,2 m³/h = 0,002 m³/s |
| TSS de entrada | 36 mg/L |
| Densidade efetiva da partícula (ρp) | 1.030 kg/m³ (fezes mucosas saturadas) |
| Δρ (ρp − ρw a 28°C) | 34 kg/m³ |
| Constante de Stokes do sistema: `Vs = K·d²` | K = g·Δρ/(18µ) = **22.063 m⁻¹s⁻¹** |

Velocidade de sedimentação e área projetada requerida (`A = Q/Vs`):

| Diâmetro | Vs (m/h) | Área p/ captura total |
| :---: | :---: | :---: |
| 100 µm | 0,794 | 9,1 m² |
| 80 µm | 0,508 | 14,2 m² |
| 50 µm | 0,199 | 36,3 m² |
| 30 µm | 0,072 | 101 m² |
| 20 µm | 0,032 | 226 m² |

> **Conclusão física:** capturar 100% de 20–30 µm por gravidade exigiria 100–226 m² — o joelho de viabilidade está em **~50–62 µm**. Abaixo de 20 µm é domínio exclusivo do filtro de manga (loop kidney) e da oxidação TiO₂/UV (Fase 6).

---

### Estágio 1 — Sump Coletor (300 L)

| Parâmetro | Valor |
| :--- | :--- |
| Volume útil | 300 L |
| Material | PEAD (HDPE), resistente a abrasão |
| Vazão de entrada | 120 L/min por gravidade (dreno P2 → P3) |
| Função | Recepção do dreno, amortecimento de surto, alimentação por gravidade do Cônico |
| Posição | Patamar P3 (Z ≈ 4,5 m), ~0,5 m acima da entrada do Cônico |

O sump **não tem bomba**. Transborda por gravidade para o Decantador Cônico através de um vertedouro lateral. O CLP monitora apenas o **nível** do sump (detecção de entupimento de dreno — ver Doc 02).

### Estágio 2 — Decantador Cônico (1.500 L) — Trap Grosso + Espessador

Dimensionado por tempo de retenção (HRT), não por SOR — sua função é reter a fração grossa (> 150 µm), amortecer vazão e **adensar/estocar o lodo**.

| Parâmetro | Valor |
| :--- | :---: |
| Volume | 1.500 L (HRT = 12 min) |
| Diâmetro / altura total | Ø 1,10 m / ≈ 2,20 m |
| Cone inferior | 60° (autoesvaziante por gravidade) |
| Área de superfície | 0,95 m² → corte efetivo ~300 µm |
| Captura | ~35% da carga (> 150 µm) |
| Lodo gerado | ~73 L/dia (a 3% sólidos) → **1 purga manual/dia** → Graxaria (Fase 4) |

### Estágio 3 — Decantador Laminar — A Captura Fina

Placas inclinadas multiplicam a área projetada (princípio de Hazen): `A_ef = N·B·Lp·cos θ`.

| Parâmetro | Valor |
| :--- | :---: |
| Largura do módulo (B) | 1,0 m |
| Comprimento de placa (Lp) | 1,0 m |
| Inclinação (θ) | 55° |
| Espaçamento (s) | 40 mm |
| Comprimento do tanque (Lb) | 2,0 m |
| Nº de placas | N = Lb·senθ/s = **41 placas** |
| **Área efetiva** | 41 × 1,0 × 1,0 × cos55° = **23,5 m²** |
| **Corte de partícula** | SOR = 7,2/23,5 = 0,306 m/h → **≈ 62 µm** |
| Caixa | 1,0 × 2,0 × 1,4 m (2,8 m³) | HRT ≈ 14 min |
| Material das placas | PVC 2 mm ou colmeia tubular | Limpeza semanal |

**Eficiência combinada por faixa:** > 80 µm ≈ 97% · 50–80 µm ≈ 82% · 30–50 µm ≈ 56% · 20–30 µm ≈ 35% · < 20 µm ≈ 3%.

Saída: ~6 mg/L → segue ao Loop Kidney e ao biofiltro.

---

### Estágio 4 — Loop Kidney: Filtro de Manga 10 µm (10–30 µm)

A fração 10–30 µm que escapa dos decantadores é removida por **filtração de profundidade** num loop lateral (*kidney*) — **nunca na linha principal de recirculação**.

> ⚠️ **Por que side-stream e não na linha principal:** um filtro de manga 10 µm na linha principal (2.400 L/min) receberia ~17 kg de sólidos/dia, saturando em **~1 hora**; ao saturar, sangraria a carga das Bombas de Recirculação e **colapsaria o vórtice nos 6 tanques simultaneamente** — ponto único de falha em vazão de suporte à vida. No loop kidney, a saturação apenas reduz a taxa de polimento, sem afetar o suporte à vida.

| Parâmetro | Valor |
| :--- | :---: |
| Vazão do slipstream | ~120 L/min (5% da linha principal pós-biofiltro) |
| Bomba dedicada | 0,25 CV (≈ R$ 40/mês) — **independente das Bombas de Recirculação** |
| Carcaça | Vaso PVC rígido, fechamento rápido por abraçadeira |
| Elemento | Manga de poliéster agulhado 10 µm (filtração 3D de profundidade) |
| Monitoramento | Sensor de pressão diferencial → CLP → alerta Telegram ao saturar (ver Doc 02) |
| Manutenção | Troca da manga (~2 min); lavagem com jato d'água — **5–15 reusos** antes do corte degradar (não "dezenas") |
| Consumível | ~R$ 50/manga |
| Retorno | Ao sump do biofiltro |

> **Nota de honestidade técnica:** a lavagem de alta pressão abre os poros do agulhado — uma manga 10 µm relavada várias vezes passa a se comportar como ~25–40 µm. Manter estoque de mangas novas e descartar após degradação do corte.

---

### Resumo do Circuito (100% Gravidade no Trem Principal)

```
Dreno 5% (120 L/min, 36 mg/L)
   │ gravidade
   ▼
SUMP 300L ──► CLP monitora nível (entupimento de dreno)
   │ gravidade (vertedouro, Δz ~0,5 m)
   ▼
DECANTADOR CÔNICO 1.500L ──► purga 1×/dia → Graxaria
   │ gravidade
   ▼
DECANTADOR LAMINAR (41 placas, ~62 µm) ──► limpeza semanal
   │ ~6 mg/L
   ▼
BIOFILTRO PERCOLADOR ──► linha principal recirculação
   │
   └──► slipstream 120 L/min → BOMBA 0,25 CV → FILTRO MANGA 10 µm
                                (sensor ΔP/CLP) → retorna ao biofiltro
   │
   ▼
FASE 6 (TiO₂/UV) → mineraliza < 10 µm + DOC → < 2 mg/L
```

**Ganhos da substituição HC → Gravidade:** zero fragmentação no trem principal, eliminação da Bomba de Sólidos (−R$ 1.200 CAPEX, −R$ 57/mês OPEX, −1 motor essencial, −1 ponto de falha), trem principal 100% por gravidade (alinhado à filosofia Cornell), TSS final melhor (~3 mg/L vs ~4 mg/L do HC).

---

## Filtro Percolador — Desgasificação de CO₂ (Alcalinidade Gratuita)

O filtro percolador (biofiltro de nitrificação, 4,5 × 1,8 × 1,4 m com mídia Pall Rings) desempenha uma função química secundária de alto valor: **a desgasificação passiva de CO₂**.

### Mecanismo (Lei de Henry)

Quando a água goteja pelos 1,5 m de altura da mídia, o CO₂ dissolvido — produto da respiração dos peixes — é expulso para a atmosfera por convecção natural. Isso desloca o equilíbrio do sistema de carbonatos:

```
H⁺  +  HCO₃⁻  ⇌  H₂CO₃  ⇌  H₂O  +  CO₂↑ (expulso)
```

O consumo dos H⁺ livres **eleva o pH passiva e gratuitamente**, sem adição de insumos — reduzindo a quantidade de calcário necessária no contator passivo (Fase 2).

### Requisito de Projeto — Laterais Abertas

> ⚠️ **CRÍTICO:** As laterais do filtro percolador devem ser **totalmente abertas e desimpedidas para ventilação**. Encapsular, cobrir ou vedar as laterais impede a convecção do CO₂ e anula esse benefício.

Em ambiente externo com boa circulação de ar (o projeto situa o percolador no Patamar P3, zona aberta), a taxa de arraste é máxima. Em instalações cobertas (galpão), garantir ventilação forçada ou aberturas laterais de pelo menos 50% da área das faces.
