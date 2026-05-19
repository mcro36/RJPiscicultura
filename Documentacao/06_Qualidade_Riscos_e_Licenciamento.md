# 05. Qualidade, Riscos e Licenciamento

## Resumo
Consolidação de todos os requisitos de qualidade do produto final (depuração), opções de manejo hídrico (Bioflocos como opcional), mapeamento de riscos técnicos e operacionais, e requisitos legais obrigatórios para operar em Minas Gerais.

---

## 1. Qualidade — Depuração e Tanque de Acabamento (T7)

### O Problema da Geosmina
A geosmina (composto produzido por cianobactérias e actinomicetos nos biofilmes do RAS) causa o "gosto de barro" no filé. Em sistemas intensivos, sua produção é inevitável e contínua.

### Protocolo de Acabamento — T7 Dedicado

O lote de despesca (~2.391 kg vivo, com fotoperíodo 16h) é **obrigatoriamente transferido** para o **T7 — Tanque de Acabamento Comercial**, um tanque dedicado de 60 m³ alimentado exclusivamente com água de poço (não recirculada).

| Parâmetro | Sem Fase 6B (TiO₂+UV) | **Com Fase 6B** |
| :--- | :---: | :---: |
| Tempo no T7 | 3–5 dias | **24–48 horas** |
| Objetivo | Purga de geosmina + esvaziamento do trato | **Apenas** esvaziamento do trato digestório |
| Água | Poço artesiano — 100% virgem | Poço artesiano — 100% virgem |

Ver [Doc 09 — Módulo 6B](09_Fase6_Otimizacao_Quimica.md) para a fundamentação da redução de tempo.

**Teste sensorial obrigatório** antes de qualquer lote sair para venda: cozinhar amostra e avaliar sabor/odor.

### Por que o T7 é Mandatório — Três Razões Técnicas

A redução do tempo de depuração de 3–5 dias para 24–48 h (via Módulo 6B) levanta a questão: pode-se fazer o acabamento no próprio tanque de engorda, eliminando o T7? A resposta é **não**. O T7 exerce três funções hidráulicas e sanitárias que vão além da purga de geosmina.

#### Razão 1 — Pulmão Térmico (Função Oculta)

A água do poço artesiano (Sabará-MG, já existente no sítio; uso mínimo dispensa outorga) emerge a ~18°C. O sistema RAS opera a 26–28°C. O T7 funciona como **tanque de pré-aquecimento e estabilização** da água de reposição:

- Quando o CLP abre a solenoide de renovação (TAN > 2,5 mg/L ou evento de despesca), a água nova passa pelo T7 antes de entrar no sistema.
- Sem T7: injeção direta de água a 18°C em ambiente de 26°C → **choque térmico de ΔT = 8°C**, estressando os peixes e comprometendo a imunidade. Risco elevado de surtos de Ictio (ponto branco) e outras doenças oportunistas.
- Com T7: a Bomba de Calor pre-aquece a água no T7; os tanques de produção recebem água já estabilizada.

#### Razão 2 — Isolamento do Loop RAS (Qualidade Premium)

O loop de recirculação é **unificado**: a água passa por todos os seis tanques de produção, biofiltro, UV e retorna. Se o lote em final de ciclo permanecer no seu tanque de engorda durante o jejum:

- Os peixes dos T1–T5 continuam comendo e excretando normalmente.
- A água que chega ao "tanque de jejum improvisado" carrega muco, feromônios de estresse de outros lotes e nitrato de até 200 mg/L acumulado no sistema.
- Para um filé Premium vendido a R$ 45/kg, os **últimos 2 dias exigem água 100% virgem de poço**, isenta de qualquer efluente coletivo. Isso confere o "brilho final" na carne e elimina o retrogosto de confinamento.

#### Razão 3 — Biosegurança na Despesca

A operação de captura de 1.900 kg de peixe com redes gera impacto biológico significativo:

- Peixes batem a cauda e liberam grande volume de muco, escamas e compostos de estresse na água.
- Se feita em um tanque de produção, esse pulso de matéria orgânica vai diretamente para o biofiltro percolador e pode turvar a água dos outros cinco tanques ativos.
- No **T7 isolado**, a despesca é contida: a água do T7 vai para descarte/esterqueira após o processo, sem qualquer interferência na biossegurança dos tanques em produção.

### O Novo Papel do T7 após a Fase 6B

Com a instalação do Módulo 6B (Fotocatálise TiO₂+UV), o T7 **muda de nome mas não de função**:

| | Antes da Fase 6B | **Após a Fase 6B** |
| :--- | :--- | :--- |
| Nome | Tanque de Depuração | **Tanque de Acabamento Comercial (T7-ACE)** |
| Tempo de permanência | 3–5 dias | **24–48 horas** |
| Função principal | Purga de geosmina + esvaziamento trato | Esvaziamento do trato + pulmão térmico + isolamento |
| Giro de estoque | 1 lote por semana | **1 lote por 2 dias → maior rotatividade** |

O ganho operacional é expressivo: o T7 que antes ficava "travado" com um lote por até 5 dias passa a liberar espaço a cada 2 dias, reduzindo o tempo entre a despesca e o abate e melhorando o fluxo de caixa mensal.

### Impacto Financeiro
- Peixes SEM acabamento adequado: desconto de 30–50% no preço do kg.
- Peixes COM acabamento no T7: **R$ 45/kg de filé** (preço conservador de atacado B2B).

---

## 2. Manejo Hídrico — Bioflocos (Opcional)
A tecnologia BFT (Biofloc Technology) é uma **opção complementar**, não obrigatória.

### Por que é opcional?
- Exige monitoramento diário de relação C:N (Carbono/Nitrogênio) com precisão laboratorial.
- Dosagem incorreta de melaço pode causar explosão bacteriana → consumo massivo de O₂ → mortalidade.
- O sistema RJ Piscicultura já controla sólidos via Vórtice + Dual Drain (Fase 1) e renova água conforme necessidade.

### Quando considerar BFT?
- Se os custos com ração forem muito altos e a reposição de água for limitada.
- Se houver um técnico dedicado com experiência em microbiologia aquícola.

### Sem BFT — Protocolo Padrão
- Trocas parciais de água (5-10% do volume) quando Amônia > 1,0 mg/L ou Nitrito > 0,5 mg/L.
- Limpeza de sólidos contínua pelo dreno central (Dual Drain).

---

## 3. Riscos Técnicos e Operacionais

### Risco Crítico: Falha de Energia
- **Probabilidade:** Média (BH tem rede estável, mas chuvas de verão causam quedas).
- **Impacto:** Mortalidade de 100% em 30-60 minutos sem aeração com biomassa alta.
- **Mitigação:** Gerador 8-10 kVA com QTA (Fase 2).

### Risco Crítico: Falha da Bomba de Calor no Inverno
- **Probabilidade:** Baixa (equipamentos industriais são confiáveis).
- **Impacto:** Queda de temperatura progressiva (não imediata). Peixes param de comer em <20°C, mortalidade em <15°C.
- **Mitigação:** Manter contrato de assistência técnica com prazo de atendimento de 24h. As bolas flutuantes e a lã de rocha retardam a perda térmica, dando tempo para reparo.

### Risco Moderado: FCA Real > 1.3
- **Causa:** Ração de baixa qualidade, arraçoamento excessivo, estresse térmico.
- **Impacto:** Redução de margem de lucro.
- **Mitigação:** Biometrias quinzenais para ajustar quantidade de ração. Não ultrapassar a taxa de arraçoamento recomendada.

### Risco Moderado: Mortalidade por Doença
- **Causa:** Estreptococose, Columnaris (comuns em tilápia confinada).
- **Impacto:** Perda de até 30-50% do lote.
- **Mitigação:** Manejo sanitário (banhos de sal 3-5 g/L), boa qualidade de água, ração com premix vitamínico, quarentena de alevinos novos.

### Risco Operacional: Falta de Alevinos de Qualidade
- **Causa:** Fornecedores sazonais ou problemas genéticos.
- **Mitigação:** Manter ao menos 2 fornecedores homologados (ex: GenoMar, Aquabel, Supreme).

---

## 4. Licenciamento Obrigatório — Minas Gerais

### 4.1 Licenciamento Ambiental (COPAM/FEAM)
- **Base legal:** DN COPAM nº 217/2017, Código **G-02-12-7** (Aquicultura, exceto tanque-rede).
- **Sistema:** SLA (Sistema de Licenciamento Ambiental) via portal [Eco Sistemas](https://ecossistemas.meioambiente.mg.gov.br).
- **Modalidade:** Depende do porte e potencial poluidor. Provável enquadramento em **LAS (Licenciamento Ambiental Simplificado)** por RAS/Cadastro.
- **Custo estimado:** R$ 2.000 a R$ 8.000 (taxas + responsável técnico).

### 4.2 Outorga de Recursos Hídricos (IGAM)
- **Finalidade:** Autorização para captação de água (poço artesiano ou rede) e lançamento de efluentes.
- **Sistema:** SOUT via portal Eco Sistemas.
- **Dispensa:** Se captação < 0,5 L/s (superficial) ou < 10 m³/dia (subterrânea), enquadra-se como "uso insignificante".
- **Custo estimado:** R$ 500 a R$ 2.000.

### 4.3 Cadastro no IMA (Instituto Mineiro de Agropecuária)
- **Finalidade:** Registro do estabelecimento aquícola, sanidade animal, biosseguridade.
- **Custo estimado:** Gratuito (isento de taxas).

### 4.4 Inspeção Sanitária (SIE-MG ou SIM)
- **SIM (Serviço de Inspeção Municipal):** Permite venda dentro do município. Mais simples.
- **SIE (Serviço de Inspeção Estadual):** Permite venda em todo o estado de MG. Obrigatório para escalar.
- **SIF (Serviço de Inspeção Federal):** Para venda nacional ou exportação. Complexo e caro — deixar para expansão futura.
- **Custo estimado (SIE):** R$ 1.000 a R$ 5.000.

### Custo Total Estimado de Licenciamento
| Item | Valor |
| :--- | :--- |
| Licenciamento Ambiental COPAM | R$ 5.000 |
| Outorga IGAM | R$ 1.000 |
| Cadastro IMA | Gratuito |
| SIE-MG | R$ 3.000 |
| **TOTAL** | **R$ 9.000** |

---

## 5. Checklist de Conformidade Legal (Pré-Operação)
- [ ] Cadastro no portal Eco Sistemas (pessoa física ou jurídica).
- [ ] Verificar dominialidade da água via IDE Sisema.
- [ ] Contratar responsável técnico (engenheiro de pesca ou zootecnista).
- [ ] Solicitar LAS via SLA.
- [ ] Solicitar Outorga via SOUT.
- [ ] Registrar no IMA.
- [ ] Solicitar SIM ou SIE para processamento e venda.

---

## 6. Química da Água e Gestão de Alcalinidade

> **Base técnica:** Timmons & Ebeling (*Recirculating Aquaculture Systems*, 4ª ed.), Summerfelt (Freshwater Institute), SRAC Fact Sheets 451–453, Embrapa Pesca e Aquicultura.

Esta seção trata da dinâmica química da água como um **reator químico contínuo**, não como elemento estático. Ignorar esses processos resulta em custos ocultos elevados e projeções financeiras incorretas.

---

### 6.1 Equilíbrio NH₃/NH₄⁺ — A Toxicidade Depende do pH e da Temperatura

As tilápias excretam **Nitrogênio Amoniacal Total (TAN)** pelas brânquias, que existe em equilíbrio dinâmico entre duas formas:

```
NH₄⁺  +  OH⁻  ⇌  NH₃ (aq)  +  H₂O
(íon amônio — baixa toxicidade)    (amônia livre — altamente tóxica)
```

**O pH e a temperatura determinam qual fração domina:**

| pH | Temp. | % do TAN como NH₃ tóxica |
| :---: | :---: | :---: |
| 7,8 | 28°C | ~5,0% |
| 7,5 | 28°C | ~2,5% |
| 7,2 | 28°C | ~1,2% |
| **7,1** | **28°C** | **~1,0%** |
| 7,0 | 28°C | ~0,8% |
| 7,8 | 20°C | ~2,5% |

**Implicação crítica para o projeto:**

A operação a 28°C (climatização da Fase 3) torna o controle de pH ainda mais importante — a mesma concentração de TAN gera **o dobro de amônia tóxica** a 28°C versus 20°C. Sistemas que operam com pH próximo a 8,0 (comum sem monitoramento ativo) estão expondo os peixes a concentrações perigosas de NH₃ mesmo com TAN aparentemente baixo.

#### Produção de TAN Estimada para Este Sistema

- Ração diária total (regime estável): ~97 kg/dia
- Proteína bruta da ração: ~30% → 29,1 kg proteína/dia
- Nitrogênio total ingerido: 29,1 / 6,25 = **4,66 kg N/dia**
- Retido nos peixes (~30%): 1,40 kg N/dia
- **Excretado como TAN: ~3,26 kg N/dia**

---

### 6.2 Nitrificação — Estequiometria e Destruição de Alcalinidade

O filtro percolador (biofiltro) hospeda duas colônias de bactérias autotróficas que oxidam o TAN em duas etapas:

**Etapa 1 — Nitrosomonas:**
```
NH₄⁺  +  1,5 O₂  →  NO₂⁻  +  H₂O  +  2H⁺
```

**Etapa 2 — Nitrobacter:**
```
NO₂⁻  +  0,5 O₂  →  NO₃⁻
```

**O custo oculto:** Cada reação da Etapa 1 libera **2 íons H⁺** (ácido puro). Esses íons atacam o bicarbonato (HCO₃⁻) da água:

```
H⁺  +  HCO₃⁻  →  H₂CO₃  →  H₂O  +  CO₂↑
```

A lei estequiométrica (Timmons et al.) quantifica essa destruição:

> **7,14 g de alcalinidade (como CaCO₃) são consumidos por cada grama de N-NH₃ nitrificado.**

#### Cálculo do Consumo Diário de Alcalinidade

| Parâmetro | Valor |
| :--- | :--- |
| TAN excretado/nitrificado | ~3.260 g N/dia |
| Alcalinidade destruída (× 7,14) | ~23.300 g CaCO₃/dia = **23,3 kg CaCO₃/dia** |
| Equivalente em NaHCO₃ (× 1,68) | ~**39 kg NaHCO₃/dia** |
| Custo NaHCO₃ industrial (R$ 3,50/kg) | **~R$ 136/dia → R$ 2.583/mês → R$ 31.000/ano** |

> ⚠️ **Este custo estava ausente do OPEX original do projeto.** Ver atualização no [Doc 07](07_Plano_Financeiro.md).

A remoção rápida de sólidos pelo conjunto **Decantador Cônico + Laminar (gravidade)** tem impacto direto aqui: ao impedir que o Nitrogênio Orgânico Particulado (NOP) das fezes se mineralize em NH₄⁺ adicional, o sistema reduz a carga sobre o biofiltro em **~30%** (literatura: Timmons et al.), reduzindo proporcionalmente o consumo de alcalinidade.

---

### 6.3 Estratégia de pH 7,0–7,2 (Janela Dinâmica de Controle)

**Fundamento (SRAC Fact Sheets 451–453):** O peixe não sofre com o TAN total — ele sofre com a fração de NH₃ livre. Manter o pH estritamente entre **7,0 e 7,2** mantém a NH₃ livre sempre abaixo de 0,025 mg/L, mesmo com TAN de até 2,5 mg/L:

| Cenário | pH | TAN | NH₃ livre | Segurança |
| :--- | :---: | :---: | :---: | :---: |
| Protocolo antigo | 7,8 | 1,0 mg/L | 0,050 mg/L | Margem estreita |
| **Protocolo novo** | **7,1** | **2,5 mg/L** | **0,025 mg/L** | **Mais seguro** |

**Como isso reduz o consumo de água:**

O CLP atualmente aciona a renovação de água quando TAN > 1,0 mg/L. Com a janela de pH 7,1, o gatilho pode ser **reconfigurado para TAN > 2,5 mg/L**, sem aumentar o risco biológico. Resultado:

- **~40% menos trocas de água** por mês
- Menor consumo de energia do poço artesiano
- Menor perda de calor térmico (menos água fria inserida no sistema aquecido a 28°C)
- Estimativa de economia na Bomba de Calor: **−R$ 88/mês** (~10% da energia de climatização)

**Equipamento necessário:** Sensor de pH (eletrodo de vidro ou ISFET industrial, ~R$ 800–1.500) a ser integrado ao CLP da Fase 2. Ver [Doc 02](02_Automacao_e_Seguranca.md) para detalhes de programação.

---

### 6.4 Contator de Calcário por Fluxo Ascendente (Solução de Alcalinidade)

Em vez de dosar bicarbonato de sódio diariamente (operação complexa, custo alto), a solução adotada é um **contator passivo de calcário calcítico** — equipamento sem partes móveis, fundamentado no Produto de Solubilidade (Ksp) do CaCO₃.

#### Princípio de Funcionamento

A água ácida (pH baixo, após nitrificação) entra pelo fundo do contator e sobe por um leito de **brita calcítica** (calcário calcítico moído, 10–20 mm). O CO₂ dissolvido e os H⁺ dissolvem lentamente a superfície dos grãos:

```
CaCO₃ (s)  +  CO₂ (aq)  +  H₂O  →  Ca²⁺  +  2 HCO₃⁻
CaCO₃ (s)  +  2H⁺        →  Ca²⁺  +  H₂O  +  CO₂↑
```

O resultado é a reposição natural de alcalinidade (HCO₃⁻) e elevação gradual do pH até o equilíbrio de saturação (~7,2–7,5), sem dosagem química manual.

#### Posicionamento no Sistema

O projeto possui **desnível natural de 2,5 m** entre os patamares P3 e P2, que fornece a carga hidráulica necessária para o fluxo ascendente sem bombeamento adicional. O contator é posicionado no nível P3 (RAS), após o filtro de tela e UV e antes do reservatório de retorno.

```
Tanques (P2, Z=6,0m)
    ↓ dreno central
Sump → Decantador Cônico → Decantador Laminar → Percolador → Filtro Manga Kidney + UV
    ↓ gravidade (talude 2,5m)
[CONTATOR DE CALCÁRIO — entrada fundo, saída topo]
    ↓
Reservatório → Bomba → Tanques
```

#### Especificação Técnica

| Item | Especificação |
| :--- | :--- |
| Tanque | PEAD (HDPE) 3.000 L, Ø 1,1 m × h 1,5 m |
| Mídia filtrante | Brita calcítica calcítica 10–20 mm (> 95% CaCO₃) |
| Carga do leito | ~800–1.000 kg de brita |
| Vazão de projeto | 8–15 m³/h (velocidade ascensional ~1–3 m/h) |
| Reposição | 4–5 sacos de 50 kg por mês |
| Purga de fundo | 1× por mês, 2 minutos (válvula de esfera manual) |

#### Comparativo Financeiro

| | Bicarbonato de Sódio | **Contator de Calcário** |
| :--- | :---: | :---: |
| OPEX anual | R$ 31.000 | **R$ 7.680** |
| OPEX mensal | R$ 2.583 | **R$ 640** |
| CAPEX (instalação única) | R$ 0 | R$ 3.000 |
| Complexidade operacional | Diária (pesagem + dosagem) | Mensal (reabastecer + purgar) |
| Payback do investimento | — | **< 1 mês** |
| **Economia anual** | — | **R$ 23.320** |

---

### 6.5 Desgasificação de CO₂ pelo Percolador (Alcalinidade Gratuita)

**Fundamento (Lei de Henry):** O CO₂ dissolvido na água dos tanques está em equilíbrio com o bicarbonato. Quando a água goteja pelos 1,5 m de mídia Pall Rings do percolador, ocorre intensa transferência de massa gasosa — o CO₂ é expulso para a atmosfera por convecção natural.

A sacada química: ao remover CO₂ gasoso do meio, o equilíbrio do sistema de carbonatos é deslocado passivamente:

```
H⁺  +  HCO₃⁻  ⇌  H₂CO₃  ⇌  H₂O  +  CO₂↑ (expulso pelo vento)
```

Consumindo os H⁺ livres → **elevação natural e gratuita do pH**, sem adição de insumos.

**Requisito de projeto:** As laterais do filtro percolador devem ser **totalmente desimpedidas e abertas para ventilação**. Encapsular ou cobrir o percolador elimina o arraste de gás e anula esse benefício. Em conjunto com o contator de calcário, esta desgasificação passiva reduz ainda mais a demanda química.

#### Benefício adicional para o UV

A remoção de sólidos finos pelo filtro de manga kidney (10 µm) antes do UV garante máxima **transmitância UV** (254 nm). Compostos orgânicos dissolvidos (COD) e turbidez absorvem a radiação UV antes que ela atinja os patógenos — reduzindo a dose efetiva e aumentando o consumo da lâmpada. TSS de ~3 mg/L (eficiência do conjunto Decantador Cônico + Laminar + Filtro Kidney) garante transmitância acima de 65–70%, dentro da faixa ideal para UV de 55 W.
