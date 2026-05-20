# 04. Fábrica de Ração (Fase 4)

## Resumo
Implantação de uma fábrica semi-industrial de ração extrusada flutuante, reduzindo o custo do kg de R$ 4,45 (comercial) para R$ 2,10 (própria). A ração flutuante é obrigatória para evitar acúmulo de ração não consumida no fundo dos tanques.

## Justificativa Financeira

> ⚠️ **Valores com fotoperíodo 16h** (despesca 2.391 kg vivo, +25% vs baseline sem fotoperíodo). Ver [Doc 03 — Seção Fotoperíodo](03_Climatizacao_e_Alimentacao.md).

- **Custo mensal com ração comercial:** R$ 16.167/mês (3.633 kg × R$ 4,45)
- **Custo mensal com ração própria:** R$ 7.629/mês (3.633 kg × R$ 2,10)
- **Economia mensal:** R$ 8.538/mês → **R$ 102.456/ano**
- **Payback da fábrica (CAPEX ~R$ 67k c/ soft-starter):** ~7,8 meses após operação.

## Equipamentos

### Extrusora
- **Tipo:** Extrusora mono-rosca semi-profissional (motor 15–25 CV).
- **Capacidade:** 100–200 kg/h (cobre a demanda mensal de 3.633 kg em ~25h de operação/mês).
- **Função:** Expandir o pellet por alta pressão e temperatura, garantindo flutuabilidade (pellet afunda = desperdício + poluição do tanque).
- **Partida:** Obrigatório soft-starter 25 CV. Partida direta de motor 25 CV gera pico de corrente de 6–7× a nominal (~375 A por 2–5 s), causando sag de tensão que pode disparar proteções dos inversores WEG dos sopradores ou do inversor solar. O soft-starter limita a corrente de partida a 2–2,5× nominal (~120 A) e elimina esse risco.

### Processamento
- **Moinho de Martelos:** Moer grãos e ingredientes secos.
- **Misturador Horizontal:** Homogeneizar a dieta.
- **Secagem:** Por convecção natural (bandejas ao sol em estufa de secagem simples) ou secador tipo transportador.
- **Armazenamento:** Sacos de ráfia em local seco e ventilado. Validade da ração caseira: ~30 dias.

## Formulação Base (por 100kg de ração)

### Ração de Engorda (28-32% PB)
| Ingrediente | Quantidade (kg) | Custo/kg | Custo (R$) |
| :--- | :---: | :---: | :---: |
| Farelo de Soja (45% PB) | 40 | R$ 2,20 | R$ 88,00 |
| Milho Moído | 35 | R$ 1,00 | R$ 35,00 |
| Silagem de Pescado | 15 | R$ 0,30 | R$ 4,50 |
| Farinha de Peixe ou Carne | 5 | R$ 4,00 | R$ 20,00 |
| Premix vitamínico/mineral | 3 | R$ 8,00 | R$ 24,00 |
| Óleo de soja | 2 | R$ 6,00 | R$ 12,00 |
| **TOTAL** | **100 kg** | | **R$ 183,50** |
| **Custo por kg** | | | **R$ 1,84** |

*Com margem para energia elétrica, mão de obra e perdas → custo final estimado: **R$ 2,10/kg**.*

### Ração Inicial (40-45% PB)
Para alevinos, a formulação exige maior teor proteico (mais farinha de peixe e soja). Custo estimado: ~R$ 3,00/kg. Porém, o volume consumido nesta fase é muito pequeno (~105 kg/mês), não impactando significativamente o OPEX.

## Silagem Ácida de Pescado (Economia Circular)
- **Matéria-prima:** Resíduos brutos da filetagem (cabeças, espinhas, vísceras, pele) — ~1.387 kg/despesca (58% de 2.391 kg, com fotoperíodo) após separação da barriguinha e recortes para linguiça (ver Doc 08).
- **Processo:** Moer os resíduos + acidificar com ácido fórmico (3% v/p). Estabiliza a proteína por hidrólise ácida. Pronto para uso em 3-7 dias.
- **Armazenamento:** Contêineres IBC rígidos de 1.000L (usados, custo de R$ 80-150 cada).
- **Rendimento:** 15-20% da composição da ração.

*Nota: Com a implantação da Graxaria (seção abaixo), a silagem ácida é substituída/complementada por farinha de peixe de maior concentração proteica, otimizando o FCA.*

---

## Graxaria — Farinha e Óleo de Peixe

### Justificativa
O resíduo bruto da filetagem (~1.387 kg/despesca, com fotoperíodo 16h) contém alto teor proteico e lipídico. A graxaria converte esse resíduo em dois insumos que a fazenda atualmente compra de terceiros: **farinha de peixe** e **óleo de peixe**. A autossuficiência nesses ingredientes reduz o custo da ração de R$ 2,10 para ~R$ 1,83/kg.

### Processo da Graxaria

```
Resíduo bruto (1.423 kg/mês)
   │
   ├─► Cozimento a vapor (digestor) ──────────────────► VAPORES ODOROSOS
   │                                                          │
   ├─► Prensagem (prensa de parafuso)                         ▼
   │      │                                    Condensador + Filtro de Carvão Ativado
   │      ├─► SÓLIDO (torta): secagem ─────────────────► (gases do secador)
   │      │        └─► FARINHA DE PEIXE (~60% PB)
   │      │
   │      └─► LÍQUIDO (caldo): centrifugação → ÓLEO DE PEIXE
   │                                          └─► Água de cola (descarte)
   └─► Produção mensal estimada
```

### Controle de Odor

O cozimento e a secagem de resíduos de peixe geram compostos voláteis de aminas e ácidos graxos com odor intenso. O controle é **obrigatório** tanto para o conforto operacional quanto para a conformidade ambiental (COPAM/FEAM — DN 217/2017 contempla emissões atmosféricas de unidades de processamento).

**Duas fontes de odor e suas mitigações:**

| Fonte | Composto Odoroso | Solução |
| :--- | :--- | :--- |
| Vapores do digestor (cozimento) | Aminas, H₂S, mercaptanas | **Condensador de vapores** — resfria e condensa os gases antes do lançamento; recupera água de processo |
| Ar de exaustão do secador | Compostos orgânicos voláteis (COVs) | **Filtro de carvão ativado** — adsorve COVs residuais pós-condensador |

**Sequência de tratamento:**
1. Vapores do digestor e secador → condensador (resfriamento a água, T < 40°C)
2. Condensado retorna ao processo (reaproveitamento de água)
3. Gás não-condensável → filtro de carvão ativado (leito de 100–200 kg de carvão)
4. Troca do carvão: a cada 3–6 meses dependendo da carga operacional

**Dimensionamento mínimo para 1.423 kg/mês de resíduo:**
- Condensador de tubo e carcaça: área de troca ~2–4 m²
- Filtro de carvão ativado: leito de 100 kg (carvão mineral ou de coco)
- Vida útil do carvão: ~4–6 meses → reposição ~R$ 400–600/troca

### Dimensionamento Mensal

> Valores com fotoperíodo 16h (despesca 2.391 kg vivo, ração própria 3.633 kg/mês).

| Entrada | Qtd (kg/mês) |
| :--- | :---: |
| Resíduo bruto (58% × 2.391 kg despesca) | 1.387 |
| Recortes excedentes (96 total − 60 usados na linguiça) | 36 |
| **Total entrada graxaria** | **1.423 kg** |

| Saída | Rendimento | Produção (kg/mês) | Necessidade ração* | Excedente |
| :--- | :---: | :---: | :---: | :---: |
| Farinha de peixe (~60% PB) | 22% | ~313 kg | ~178 kg | **~135 kg** |
| Óleo de peixe | 6% | ~85 kg | ~71 kg | **~14 kg** |

*Necessidade da ração: 3.633 kg/mês × ~5% farinha + ~2% óleo (fórmula base)

### Impacto na Formulação da Ração

A graxaria torna a fazenda autossuficiente nos dois insumos de origem animal da fórmula:

| Ingrediente | Custo anterior | Custo com graxaria | Economia/mês |
| :--- | :---: | :---: | :---: |
| Farinha de peixe (~178 kg × R$ 4,00) | R$ 712 | R$ 0 | **−R$ 712** |
| Óleo de peixe subst. óleo de soja (~71 kg × R$ 6,00) | R$ 426 | R$ 0 | **−R$ 426** |
| **Total economia** | | | **−R$ 1.138/mês** |

**Novo custo médio da ração com graxaria:** ~R$ 1,83/kg (antes: R$ 2,10/kg)
**Novo custo mensal de ração:** ~R$ 6.649 (antes: R$ 7.629) → **economia de R$ 980/mês**

*O excedente de farinha de peixe (~135 kg/mês) pode ser vendido a R$ 4,00/kg → receita adicional de R$ 540/mês.*

### Equipamentos — Graxaria

| Item | Qtd | Valor (R$) |
| :--- | :---: | :--- |
| Digestor/cozinhador a vapor (200–500 kg/h) | 1 | 12.000 |
| Prensa de parafuso (expeller) | 1 | 8.000 |
| Secador rotativo ou de bandeja | 1 | 10.000 |
| Tanques de armazenamento de óleo | 2 | 2.000 |
| Instalações hidráulicas e elétricas | 1 | 3.000 |
| **Subtotal Processo** | | **R$ 35.000** |
| Condensador de vapores (tubo e carcaça, 2–4 m²) | 1 | 4.500 |
| Filtro de carvão ativado (leito 100 kg) | 1 | 3.500 |
| Tubulação e conexões do sistema de exaustão | 1 | 2.000 |
| **Subtotal Controle de Odor** | | **R$ 10.000** |
| **TOTAL GRAXARIA** | | **R$ 45.000** |

## Riscos e Limitações
- **Formulação nutricional:** Erros na proporção de aminoácidos essenciais (lisina, metionina) podem degradar o FCA. Recomenda-se consultar um zootecnista para validar a fórmula antes de escalar.
- **Controle de umidade:** Ração com umidade > 10% mofa rapidamente. A secagem deve atingir < 10%.
- **Extrusora:** Equipamento de alto custo unitário. Uma falha mecânica sem peça de reposição pode forçar a compra emergencial de ração comercial por semanas.

## Custos Estimados — Fase 4 (Fábrica de Ração + Graxaria + Processamento)

### Fábrica de Ração
| Item | Qtd | Valor (R$) |
| :--- | :---: | :--- |
| Extrusora mono-rosca semi-profissional | 1 | 45.000 |
| Soft-starter 25 CV (partida suave da extrusora — limita pico de corrente para 2–2,5× nominal) | 1 | 4.000 |
| Moinho de Martelos | 1 | 5.000 |
| Misturador Horizontal | 1 | 5.000 |
| Secador / Estrutura de secagem | 1 | 3.000 |
| Contêineres IBC (silagem) | 4 | 600 |
| Insumos iniciais (farelo, premix, etc.) | 1 | 4.000 |
| **Subtotal Ração** | | **R$ 66.600** |

### Graxaria
| Item | Qtd | Valor (R$) |
| :--- | :---: | :--- |
| Digestor/cozinhador a vapor | 1 | 12.000 |
| Prensa de parafuso (expeller) | 1 | 8.000 |
| Secador rotativo ou de bandeja | 1 | 10.000 |
| Tanques de armazenamento de óleo | 2 | 2.000 |
| Instalações hidráulicas e elétricas | 1 | 3.000 |
| Condensador de vapores (tubo e carcaça, 2–4 m²) | 1 | 4.500 |
| Filtro de carvão ativado (leito 100 kg) | 1 | 3.500 |
| Tubulação e conexões do sistema de exaustão | 1 | 2.000 |
| **Subtotal Graxaria** | | **R$ 45.000** |

### Resumo Fase 4
| Módulo | Valor (R$) |
| :--- | :---: |
| Fábrica de Ração (incl. soft-starter) | 66.600 |
| Graxaria (processo + controle de odor) | 45.000 |
| **TOTAL FASE 4** | **R$ 111.600** |

*Equipamentos de processamento de linguiça (moedor, embutideira, seladora, freezer) estão na Fase 1, pois a produção começa na primeira despesca (mês 7). Ver [Doc 01](01_Infraestrutura_e_Aeracao.md).*
