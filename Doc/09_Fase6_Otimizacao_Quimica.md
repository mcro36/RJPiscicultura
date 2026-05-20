# 09. Fase 6 — Otimização Química e Economia Circular

## Resumo

A Fase 6 fecha o ciclo de economia circular do sistema RAS, convertendo dois passivos operacionais (perda de peso na depuração e lodo do decantador) em vantagens financeiras diretas. É composta por dois módulos genuinamente novos — Módulo 6B e Módulo 6C — implementáveis após a consolidação da Fase 2 ou em paralelo com a Fase 5.

> **Nota:** O Módulo 6A (Contator de Calcário) **já foi incorporado ao projeto na Fase 2** (CAPEX R$ 3.000, OPEX R$ 640/mês). Não é recontabilizado aqui. Ver [Doc 06 — Seção 6.4](06_Qualidade_Riscos_e_Licenciamento.md) e [Doc 02](02_Automacao_e_Seguranca.md).

---

## Módulo 6B — Fotocatálise Heterogênea (TiO₂ + UV)

### Fundamento Químico

O esterilizador UV de 55 W existente emite radiação em 254 nm. Ao revestir uma colmeia de cerâmica porosa com nano-dióxido de titânio (TiO₂), cria-se um fotocatalisador que gera **radicais hidroxila (·OH)** de alto poder oxidante quando iluminado pela lâmpada UV já instalada:

```
TiO₂  +  hν (254 nm)  →  TiO₂ (e⁻ + h⁺)
h⁺  +  H₂O  →  ·OH  +  H⁺
·OH  +  Geosmina (C₁₂H₂₂O)  →  CO₂  +  H₂O  (mineralização)
```

Os radicais ·OH destroem a geosmina — composto responsável pelo "gosto de barro" no filé — **durante a recirculação contínua**, sem exigir tanque separado ou reagentes adicionais.

### Impacto na Depuração (T7 — Tanque de Acabamento Comercial)

| Parâmetro | Sem Módulo 6B | **Com Módulo 6B** |
| :--- | :---: | :---: |
| Concentração de geosmina nos tanques | Alta (produção contínua) | Baixa (destruição contínua no loop) |
| Tempo no T7 | 3–5 dias | **24–48 horas** |
| Finalidade do T7 | Purga geosmina + esvaziamento trato | **Esvaziamento do trato + pulmão térmico + isolamento** |
| Bombeamento de água nova (poço) | 100% do período | **40%** (60% menos trocas) |

> **O T7 permanece obrigatório mesmo com 24h de permanência.** A redução de tempo elimina a função de "purga de geosmina", mas o T7 ainda exerce funções hidráulicas e sanitárias insubstituíveis: (1) pulmão térmico para pré-aquecer água de poço a 18°C antes de entrar no RAS a 28°C, (2) isolamento do loop coletivo para acabamento em água 100% virgem (Premium R$ 45/kg), e (3) confinamento do impacto biológico da despesca longe do biofiltro dos tanques ativos. Ver [Doc 06 — Seção 1](06_Qualidade_Riscos_e_Licenciamento.md) para a fundamentação completa.

### Quantificação da Perda de Peso na Depuração

Durante 3–5 dias de jejum com fluxo contínuo de água, as tilápias sofrem estresse metabólico e perdem massa por catabolismo proteico:

> Cálculo com fotoperíodo 16h (despesca 2.391 kg/mês, +25% vs baseline conservador). Ver [Doc 03 — Seção Fotoperíodo](03_Climatizacao_e_Alimentacao.md).

| Parâmetro | Cálculo | Resultado |
| :--- | :--- | :--- |
| Biomassa despescada/mês | — | **2.391 kg** (com fotoperíodo) |
| Perda de peso no jejum (3%) | 2.391 × 0,03 | **71,7 kg/mês** |
| Custo de produção/kg vivo | Ração + mão de obra + energia | ~R$ 19/kg |
| **Perda financeira mensal eliminada** | 71,7 × R$ 19 | **R$ 1.362/mês** |
| **Perda financeira anual eliminada** | | **R$ 16.346/ano** |

### Economia Adicional: Bombeamento do Poço

Com depuração de 24h (vs. 5 dias), o consumo de água nova do poço durante este processo cai ~60%:

- Estimativa de economia em energia de bombeamento: **R$ 115/mês** (R$ 1.380/ano)

### Especificação Técnica do Módulo 6B

| Item | Especificação |
| :--- | :--- |
| Integração | Colmeia cerâmica revestida com TiO₂ P25 (Degussa/Evonik) |
| Instalação | Dentro do reator UV de 55 W existente (sem alteração elétrica) |
| Fluxo de tratamento | Toda a recirculação do RAS passa pelo UV contínuo |
| **Papel no trem de sólidos** | **Polimento final < 10 µm + DOC** — mineraliza o que decantadores (> 30 µm) e filtro kidney (10–30 µm) não capturam (ver [Doc 01](01_Infraestrutura_e_Aeracao.md)) |
| Superfície catalítica | ~0,15 m² (colmeia de cordierita, célula 2 mm) |
| Vida útil do catalisador | 12–18 meses (fotodegradação gradual) |
| Reposição anual TiO₂ | R$ 350–600/ano |
| Limpeza da lâmpada UV | Quinzenal (quartzo não pode ter biofilm) |

### Limitações e Riscos do Módulo 6B

- **Geosmin ≠ eliminada na fonte:** O TiO₂+UV destrói a geosmina em trânsito, mas cianobactérias e actinomicetos continuam produzindo-a nos biofilmes. A depuração de 24h ainda é necessária para esvaziamento do trato digestivo.
- **Turbidez reduz eficiência:** Com TSS > 15 mg/L, partículas absorvem UV antes de atingir o catalisador. O conjunto **Decantador Cônico + Laminar + Filtro Kidney** (entrega ~3 mg/L TSS) garante transmitância UV adequada — o TiO₂/UV atua exclusivamente sobre a fração coloidal < 10 µm e o DOC verdadeiramente dissolvido, que nenhum método físico remove.
- **Qualificação necessária:** A colmeia TiO₂ deve ser fornecida por fabricante com laudo de concentração e pureza do revestimento para garantir a cinética de degradação esperada.

### CAPEX do Módulo 6B

| Item | Valor (R$) |
| :--- | :--- |
| Colmeia cerâmica TiO₂ (customizada para Ø do reator UV existente) | 3.800 |
| Instalação e fixação no reator | 700 |
| **TOTAL MÓDULO 6B** | **R$ 4.500** |

---

## Módulo 6C — Reator de Cristalização de Estruvita

### Fundamento Químico

O lodo extraído pelo Decantador Cônico e Laminar contém **fósforo inorgânico (PO₄³⁻)** e **amônio (NH₄⁺)** em concentrações elevadas. Na presença de íons magnésio (Mg²⁺) e pH entre 8,5–9,5, esses compostos precipitam espontaneamente como **estruvita** (fosfato de amônio e magnésio):

```
Mg²⁺  +  NH₄⁺  +  PO₄³⁻  +  6H₂O  →  MgNH₄PO₄·6H₂O  ↓
                                         (Estruvita)
```

A estruvita é um fertilizante de liberação lenta com alta concentração de P₂O₅ (28,9%) e N (5,7%), muito valorizado em floricultura e horticultura urbana.

### Cálculo de Produção Mensal de Estruvita

> Cálculo com fotoperíodo 16h (ração 3.633 kg/mês = 121 kg/dia, +25% vs baseline). A maior ração gera mais fósforo no lodo e mais estruvita.

| Parâmetro | Cálculo | Resultado |
| :--- | :--- | :--- |
| Fósforo na ração (1,5% MS) | **121 kg/dia** × 0,015 | 1,815 kg P/dia |
| P excretado nas fezes (70% do ingerido) | 1,815 × 0,70 | 1,271 kg P/dia |
| P mensal no lodo | 1,271 × 30 | **38,1 kg P/mês** |
| Eficiência de cristalização (19% do P total) | 38,1 × 0,19 | 7,2 kg P/mês disponível |
| Estruvita (245 g/mol por 31 g P) | 7,2 × (245/31) | **56,9 kg/mês ≈ 57 kg/mês** |
| **Receita (57 kg × R$ 25/kg)** | | **R$ 1.425/mês** |
| **Receita anual** | | **R$ 17.100/ano** |

*A eficiência de 19% é conservadora: considera que 81% do P permanece na forma orgânica (não precipitável) nas condições do reator. Em sistemas otimizados, a recuperação pode atingir 30–40%.*

### Consumo de MgO

| Parâmetro | Cálculo | Resultado |
| :--- | :--- | :--- |
| Mg necessário (razão molar 1:1 com P) | **7,2 kg P** × (24,3/31) | 5,64 kg Mg/mês |
| MgO equivalente (fator 40,3/24,3) | 5,64 × 1,66 | 9,4 kg MgO/mês |
| Custo MgO industrial (R$ 4/kg) | 9,4 × R$ 4 | **R$ 38/mês** |

### Ajuste de pH no Reator de Estruvita

O reator opera na **corrente isolada de lodo** (separada do loop principal RAS que opera em pH 7,1). A adição de MgO ao lodo ácido eleva naturalmente o pH para 8,5–9,5 pela seguinte reação:

```
MgO  +  H₂O  →  Mg(OH)₂  →  Mg²⁺  +  2OH⁻  (pH ↑)
```

**Esta é a razão pela qual o MgO funciona como reagente único:** ele simultaneously fornece o Mg²⁺ para a reação e o OH⁻ para ajustar o pH, eliminando a necessidade de dosadores separados de base.

### Monitoramento de Ca²⁺ vs Mg²⁺ (Qualidade do Produto)

O reator opera na corrente isolada de lodo (separada do loop RAS), o que já mitiga a competição de Ca²⁺ com Mg²⁺ pelo PO₄³⁻ dentro do RAS. Porém, a precipitação competitiva de **hidroxiapatita** (Ca₅(PO₄)₃OH) pode ocorrer dentro do próprio reator se a razão Ca:Mg estiver elevada no lodo, reduzindo o rendimento de estruvita e contaminando o produto.

**Protocolo recomendado:**
- Mensalmente: medir Ca²⁺ e Mg²⁺ no lodo de entrada com kit colorimétrico (~R$ 5/teste).
- Razão Mg:Ca > 1 (molar) favorece estruvita. Se Ca²⁺ > Mg²⁺: aumentar dose de MgO ou pré-tratar o lodo com aeração (precipita CaCO₃ antes do reator).
- Sintoma de contaminação por hidroxiapatita: produto final esbranquiçado (estruvita pura é cristalina/transparente).

### Especificação Técnica do Módulo 6C

| Item | Especificação |
| :--- | :--- |
| Reator | Cone de PVC rígido invertido, Ø 0,60 m × h 1,20 m |
| Alimentação | Saída de lodo do Decantador Cônico/Laminar (por gravidade) |
| Misturação | Misturador de hélice lento (20–40 rpm, motor 0,1 CV) |
| pH operacional | 8,5–9,5 (garantido pela adição de MgO) |
| Tempo de retenção | 2–4 horas |
| Coleta do produto | Saída cônica inferior → secagem ao sol → ensacamento |
| Clarificado | Retorna ao Reservatório RAS (baixo P residual) |
| Operação | 1× ao dia: dosar MgO, aguardar, drenar estruvita úmida |
| Secagem | 24–48h ao sol (estrutura de tela sombrite) |

### Mercado em BH — Estruvita como Fertilizante Premium

| Canal | Preço estimado | Volume mensal | Receita |
| :--- | :---: | :---: | :---: |
| Hortas urbanas / produtores orgânicos | R$ 20–30/kg | 38 kg | R$ 950 |
| Floriculturas / viveiros | R$ 25–35/kg | 19 kg | R$ 570 |
| **Total conservador** | **R$ 25/kg médio** | **57 kg** | **R$ 1.425/mês** |

### CAPEX do Módulo 6C

| Item | Valor (R$) |
| :--- | :--- |
| Reator cônico PVC rígido (Ø 0,6 m × h 1,2 m) + suporte | 2.800 |
| Misturador lento 0,1 CV + eixo + hélice inox | 2.200 |
| Tubulação PVC lodo (Decantador Cônico/Laminar → reator) | 800 |
| Dosador passivo de MgO (funil de PVC + válvula) | 500 |
| Estrutura de secagem (tela sombrite + cavaletes) | 700 |
| Sacos e embalagem para produto final (estoque inicial) | 500 |
| Insumos iniciais (MgO 50 kg estoque) | 1.000 |
| **TOTAL MÓDULO 6C** | **R$ 8.500** |

---

## Comparativo Financeiro — Fase 6 (Módulos 6B + 6C)

> Baseline: nossos números consolidados (Doc 07). O Módulo 6A (Contator de Calcário) já está incluído na Fase 2 e **não é recontabilizado** aqui.

### CAPEX Total da Fase 6

| Módulo | Descrição | CAPEX (R$) |
| :---: | :--- | :--- |
| 6B | Fotocatálise TiO₂ + UV (colmeia cerâmica customizada) | 4.500 |
| 6C | Reator de Cristalização de Estruvita | 8.500 |
| **TOTAL FASE 6** | | **R$ 13.000** |

### Impacto no OPEX e Receitas (Anual)

| Linha | Sem Fase 6 | **Com Fase 6** | Impacto |
| :--- | :---: | :---: | :---: |
| Perda peso depuração (3% biomassa) | **R$ 16.346** | R$ 0 | **−R$ 16.346** (eliminado) |
| Energia poço (depuração) | R$ 1.380 | R$ 552 | **−R$ 828** |
| Manutenção TiO₂ (6B) | R$ 0 | R$ 600 | **+R$ 600** (gasto novo) |
| Reagentes MgO (6C) | R$ 0 | **R$ 456** | **+R$ 456** (gasto novo) |
| Receita — Estruvita (6C) | R$ 0 | **R$ 17.100** | **+R$ 17.100** (nova receita) |
| **Balanço anual** | | | **+R$ 33.216/ano** |
| **Balanço mensal** | | | **+R$ 2.768/mês** |

### Indicadores de Viabilidade

| Indicador | Valor |
| :--- | :--- |
| CAPEX Fase 6 | R$ 13.000 |
| Ganho mensal líquido | **R$ 2.768/mês** |
| **Payback da Fase 6** | **~4,7 meses** |
| Novo lucro mensal (completo + Fase 6) | **R$ 32.975/mês** (Fases 1–5: R$30.207 + R$2.768) |
| Melhora no payback geral do projeto | ~1 mês antecipado |

*Diferença de ~R$50 para o valor de R$33.022/mês do Doc 07 é de arredondamento nas linhas de OPEX. Doc 07 é o documento mestre.*

### Sequência de Implantação Recomendada

```
Fase 1 → Fase 2 (inclui 6A Contator) → Fase 3 → Fase 4 → Fase 5
                                                           ↕
                                              Fase 6B+6C (paralelo ou logo após)
```

A Fase 6B pode ser instalada assim que o sistema UV estiver operacional (Fase 1+). A Fase 6C requer o Decantador Cônico + Laminar da **Fase 1** (trem de sólidos por gravidade) para ter a corrente de lodo adequada.

---

## OPEX Consolidado com Fase 6 (Operação Completa — Fases 1–6, com Fotoperíodo 16h)

> Valores baseados em despesca de 2.391 kg vivo/mês (fotoperíodo 16h, +25% vs baseline conservador). Ver [Doc 07](07_Plano_Financeiro.md) para a reconciliação financeira completa.

| Item | Valor Mensal (R$) |
| :--- | :--- |
| Ração Própria c/ Graxaria (Fase 4; 3.633 kg × ~R$ 1,83) | 6.649 |
| Energia Total — Solar (Fase 5, tarifa mínima rural; LEDs cobertos) | 290 |
| Bomba Kidney (0,25 CV, polimento side-stream 24/7) | 40 |
| Alevinos (~2.900/mês, reversão sexual) | 1.160 |
| Mão de obra | 3.000 |
| Manutenção e insumos gerais | 800 |
| Processamento (filetagem, linguiça, graxaria) | 1.200 + 1.875 + 350 |
| Alcalinidade — Contator Calcário (6A, já Fase 2) | 640 |
| MgO + insumos estruvita (6C) | 38 |
| Manutenção TiO₂ / UV (6B, proporcional) | 50 |
| **OPEX TOTAL** | **R$ 16.092** |

| Faturamento | Valor Mensal (R$) |
| :--- | :--- |
| Filé B2B/B2C (**669 kg × R$ 43 médio** — 120 kg migram p/ linguiça) | **28.767** |
| Linguiça de tilápia (**270 kg × R$ 52 médio** — charcutaria premium) | **14.040** |
| Farinha de peixe excedente (graxaria, ~135 kg) | **540** |
| **Estruvita (6C, 57 kg × R$ 25)** | **1.425** |
| **FATURAMENTO TOTAL** | **R$ 44.772** |

| **LUCRO MENSAL FINAL** | **~R$ 28.680** |

*Revisão 2026-05: preços realistas (filé R$ 43, linguiça R$ 52) e volume de filé corrigido (669 kg, sem dupla contagem). Diferença de ~R$1.420 em relação ao Doc 07 (Fase 6: R$ 30.100) se deve ao tratamento dos insumos de linguiça (esta tabela os inclui no OPEX; Doc 07 os trata no bloco de verticalização). **O Doc 07 é o documento mestre para valores financeiros definitivos.***

---

## Checklist de Implantação da Fase 6

- [ ] Solicitar orçamento de colmeia TiO₂ de fornecedor especializado (especificar Ø e comprimento do reator UV existente).
- [ ] Confirmar granulometria do lodo do Decantador Cônico/Laminar (precisa conter P inorgânico solúvel — testar amostra com kit de P).
- [ ] Adquirir MgO grau industrial (PA não é necessário, grau agrícola suficiente).
- [ ] Construir estrutura de secagem de estruvita (pode ser simples, ao lado do galpão).
- [ ] Verificar mercado local em BH: contatar floriculturas, hortas urbanas e produtores orgânicos para pré-venda.
- [ ] Solicitar laudo de fertilizante ao IMA-MG para comercialização do subproduto (Instrução Normativa SDA 05/2016).
