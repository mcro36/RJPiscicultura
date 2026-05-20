# RJ Piscicultura — Piscicultura Intensiva de Tilápia

Sistema de produção intensiva de tilápia em **7 tanques de 60 m³** (6 produção + 1 depuração) com tecnologia RAS (*Recirculating Aquaculture System*), ciclo escalonado de 6 meses e despesca mensal contínua. Localizado em **Sabará, MG** (Região Metropolitana de BH).

---

## Números-Chave

| Métrica | Valor |
| :--- | :--- |
| Capacidade total | 420 m³ (7 × 60 m³) |
| Despesca mensal | ~2.391 kg vivo (~940 g/peixe c/ fotoperíodo 16h) |
| Faturamento mensal (operação completa) | R$ 43.347 |
| Lucro mensal (operação completa) | R$ 27.331 |
| Margem operacional | 63,0% |
| CAPEX Total (Fases 1–5) | R$ 559.100 |
| Payback (operação completa + linguiça + graxaria) | 1,9 anos |
| Lucro mensal (expansão 12 tanques, pós-PRONAF) | R$ 57.187 |
| Ganho cumulativo expansão vs amortização (13 anos) | +R$ 3,7 milhões |

---

## Tecnologia

O projeto adota o design **Cornell Dual-Drain** com bomba de recirculação 0,5 CV c/ VFD por tanque (400 L/min, vórtice tangencial), trem de sólidos 100% gravitacional (Cônico 1.500L + Laminar 41 placas + Loop Kidney 10 µm) e biofiltro percolador com desgasificação passiva de CO₂.

### Fases de Implementação

| Fase | Descrição | CAPEX |
| :---: | :--- | ---: |
| 1 | Infraestrutura: 7 tanques, aeração EPDM, Cornell Dual-Drain, trem de sólidos, galpão SIE, linguiça, **gerador 8–10 kVA + QTA** | R$ 209.850 |
| 2 | Automação: sensores OD multiplexados, inversores WEG, sensor pressão manifold | R$ 39.750 |
| 3 | Climatização: Bomba de Calor Inverter, EPS, fotoperíodo LEDs 16h | R$ 68.100 |
| 4 | Fábrica de Ração: extrusora + soft-starter + graxaria (silagem ácida de pescado) | R$ 111.600 |
| 5 | Energia Solar 28 kWp (cobre 100% do consumo) | R$ 119.800 |
| 6 | Otimização Química: TiO₂/UV polimento + Reator Estruvita | R$ 68.000 |

### Modelo de Verticalização

```
Alevino → Produção RAS → Filé (R$ 43/kg) ──► B2B Restaurantes (80%)
                       → Linguiça Premium (R$ 52/kg) ──► B2C Feiras (20%)
                       → Farinha/Óleo (Graxaria)
                       → Ração própria (R$ 2,10/kg vs R$ 4,45 comercial)
                       → Estruvita fertilizante (R$ 25/kg)
                       → Energia Solar (28 kWp, custo zero pós-Fase 5)
```

---

## Estrutura do Repositório

```
/
├── README.md                    ← Esta página
├── Doc/                ← Documentação técnica completa (13 docs)
│   ├── README.md                ← Índice da documentação
│   ├── 01_Infraestrutura_e_Aeracao.md
│   ├── 01b_Sistema_RAS.md       ← Cornell dual-drain, trem sólidos, biofiltro
│   ├── 02_Automacao_e_Seguranca.md
│   ├── 03_Climatizacao_e_Alimentacao.md
│   ├── 04_Fabrica_de_Racao.md
│   ├── 05_Energia_Solar.md
│   ├── 06_Qualidade_Riscos_e_Licenciamento.md
│   ├── 07_Plano_Financeiro.md
│   ├── 08_Canais_de_Venda_e_Produtos.md
│   ├── 09_Fase6_Otimizacao_Quimica.md
│   ├── 10_Estrategia_Financiamento_e_Expansao.md
│   └── 11_Benchmark_Sistemas.md
└── blender/                     ← Modelos 3D da instalação
```

---

## Princípios de Engenharia

1. **Verticalização Total:** ração própria + energia própria dobram a margem
2. **Gravidade > Bombas:** trem de sólidos 100% gravitacional — zero fragmentação, zero bomba de sólidos
3. **Bomba 0,5 CV c/ VFD > Airlift:** Sr = 0,286 no circuito externo — airlift inoperante a 1,40 m de lâmina (análise completa em [01b](Doc/01b_Sistema_RAS.md))
4. **Isolamento > Potência:** EPS + Bomba de Calor Inverter — retenção térmica mais barata que aquecimento bruto
5. **Reinvestimento > Amortização:** ROI novo tanque ~365% a.a. vs PRONAF 4,5% a.a. — ganho cumulativo +R$ 3,7M em 13 anos

---

## Financiamento

**PRONAF Investimento** — R$ 559.100 (100% CAPEX), taxa 4,5% a.a., carência 24 meses, amortização 96 meses (Price). Parcela mensal: ~R$ 6.946. Custo total de crédito: ~R$ 157.960 (28,3% sobre o principal).

---

## Contato

**mcro36@outlook.com** — Sabará, MG (RMBH)
