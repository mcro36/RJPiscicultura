# 02. Automação e Segurança Energética (Fase 2)

## Resumo
Instalação do sistema de monitoramento de oxigênio (OD) via sensores multiplexados, inversores de frequência para economia de energia e gerador com partida automática. Sem Inteligência Artificial. Sem ar comprimido.

## Central de Controle
- **Controlador:** CLP industrial ou ESP32 com protocolo Modbus.
- **Interface:** Tela de monitoramento local + alertas remotos via WiFi/celular.
- **Inversores de Frequência (WEG):** 2 unidades, instalados nos sopradores da Fase 1. Permitem variação de rotação conforme demanda de OD, economizando até 30% de energia.

## Monitoramento de Oxigênio (Sensores Multiplexados)
Em vez de 6 sensores individuais (custo proibitivo), o projeto usa engenharia de amostragem:

- **Quantidade:** 02 sensores ópticos de OD de nível industrial.
- **Lógica:** O CLP controla um circuito de válvulas solenoides e mini-bombas que trazem amostras sequenciais de cada tanque para uma câmara central de medição.
- **Ciclo:** Cada tanque é amostrado a cada ~10 minutos.
- **Economia:** ~R$ 30.000 comparado com sensores fixos em todos os tanques.

## Lógica do Inversor
- **OD > 6 mg/L:** Sopradores em frequência mínima (economia).
- **OD < 4,5 mg/L:** Frequência aumenta. Se OD < 3,5 mg/L: alerta crítico no celular.
- **Madrugada (22h-06h):** Frequência elevada preventivamente (pico de consumo biológico).

## Monitoramento do Circuito de Sólidos (Gravidade) e Filtro de Polimento

> **Revisão 2026-05:** O Hidrociclone e a Bomba de Sólidos foram eliminados. O trem de sólidos (Sump → Decantador Cônico → Decantador Laminar) opera **100% por gravidade**, sem motor a controlar. Ver [Doc 01 — Circuito de Sólidos por Gravidade](01_Infraestrutura_e_Aeracao.md). O CLP agora monitora **nível do sump** (detecção de entupimento) e **pressão diferencial do filtro de manga** (loop kidney).

### Monitoramento do Sump (Nível) — Detecção de Entupimento

O Sump (300 L) recebe o dreno por gravidade a 120 L/min e transborda por vertedouro para o Decantador Cônico. Sem bomba, não há motor a proteger — o sensor de nível serve exclusivamente como **diagnóstico de falha de dreno**.

| Condição | Ação do CLP |
| :--- | :--- |
| Nível normal (oscilando próximo ao vertedouro) | Operação normal — sem ação |
| Nível LOW (< 50 L) | Alerta Telegram: dreno de um ou mais tanques pode estar entupido |
| Nível HIGH (> 280 L, acima do vertedouro) | Alerta Telegram: vertedouro ou tubulação do Cônico obstruída |
| Energia retorna após queda | Nenhuma ação — circuito é passivo (gravidade) |

> **Vantagem da gravidade:** sem bomba de sólidos, não há "carga essencial" adicional para o gerador, não há partidas de motor, não há ponto único de falha mecânico no trem principal de sólidos. O circuito funciona mesmo durante apagão.

### Monitoramento do Filtro de Manga (Loop Kidney) — Pressão Diferencial

O filtro de polimento de profundidade (manga poliéster agulhado 10 µm) opera num loop lateral (*kidney*, ~120 L/min) com bomba dedicada 0,25 CV. À medida que a manga retém micropartículas (10–30 µm), a perda de carga sobe — o sensor de pressão diferencial detecta a saturação.

```
ΔP manga limpa:      < 0,3 bar  → operação normal
ΔP manga 60–70%:     ~0,6 bar   → CLP pré-alerta (programar troca)
ΔP manga saturada:   ≥ 1,0 bar  → CLP alerta crítico Telegram:
                                   "Filtro de polimento saturado — trocar manga"
```

| Condição | Ação do CLP |
| :--- | :--- |
| ΔP < 0,3 bar | Operação normal |
| ΔP 0,6–1,0 bar | Pré-alerta: programar troca da manga (estoque reserva) |
| ΔP ≥ 1,0 bar | Alerta crítico Telegram + registrar evento |
| Bomba kidney 0,25 CV desligada | Alerta informativo (não crítico — é polimento, não suporte à vida) |

> A saturação do filtro kidney **nunca** ameaça os tanques: por ser side-stream, sua obstrução apenas reduz a taxa de polimento de finos. O suporte à vida (linha principal 2.400 L/min) é totalmente independente deste loop.

### Integração com o Gerador

O trem de sólidos por gravidade **dispensa proteção do gerador** (não tem motor). A bomba kidney 0,25 CV é **carga não essencial** — pode permanecer desligada durante emergência sem risco aos peixes (o polimento de finos é cumulativo, não crítico no curto prazo). Cargas essenciais do gerador permanecem: Sopradores + CLP + sensores.

## Segurança Energética

> **Gerador instalado na Fase 1** — Ver [Doc 01 — CAPEX Fase 1](01_Infraestrutura_e_Aeracao.md). O gerador + QTA (R$ 12.000) foi realocado para a Fase 1 porque os alevinos entram no mês 1 e há biomassa viva antes da automação da Fase 2 estar instalada. O monitoramento multiplexado de OD desta fase complementa o gerador, mas não o substitui.

- **Gerador a Gasolina (8–10 kVA) + QTA:** acionamento < 15 segundos após queda de energia.
- **Cargas protegidas (essenciais):** Sopradores + CLP + sensores.
- **Cargas NÃO protegidas:** Bomba de Calor (a água leva horas para esfriar, mas peixes morrem em minutos sem ar).
- **Combustível:** Manter reserva mínima de 20 litros para ~8 horas de operação.

## Controle de pH — Janela Dinâmica 7,0–7,2

> **Fundamentação:** SRAC Fact Sheets 451–453 (Southern Regional Aquaculture Center); Timmons & Ebeling, *Recirculating Aquaculture Systems*.

### Por que o pH é tão importante quanto o OD?

A toxicidade do nitrogênio amoniacal **não depende do TAN total**, mas da fração de **NH₃ livre**, que é governada pelo pH e pela temperatura. A 28°C (temperatura de operação do projeto), a proporção de amônia tóxica aumenta drasticamente com o pH:

| pH operacional | % do TAN como NH₃ livre | TAN seguro máximo |
| :---: | :---: | :---: |
| 7,8 | ~5,0% | 1,0 mg/L |
| 7,5 | ~2,5% | 2,0 mg/L |
| **7,1** | **~1,0%** | **2,5 mg/L** |
| 7,0 | ~0,8% | 3,1 mg/L |

Em pH 7,1, o TAN pode chegar a **2,5 mg/L** com a mesma (ou menor) concentração de NH₃ tóxica livre do que em pH 7,8 com TAN de 1,0 mg/L.

### Configuração do CLP — Setpoints de pH e TAN (Protocolo Revisado)

| Parâmetro | Valor anterior | **Valor revisado** | Justificativa |
| :--- | :---: | :---: | :--- |
| pH mínimo | não controlado | **7,0** | Abaixo disso: biofiltro perde eficiência |
| pH máximo | não controlado | **7,2** | Acima disso: NH₃ tóxica aumenta |
| Gatilho troca de água (TAN) | 1,0 mg/L | **2,5 mg/L** | Seguro em pH 7,1 a 28°C |
| Gatilho alerta NH₃ livre | não configurado | **> 0,03 mg/L** | Calculado pelo CLP: NH₃ = TAN × f(pH,T) |

### Controle de Fotoperíodo — Rampa PWM (Dimming Obrigatório)

O CLP controla o acionamento dos LEDs de fotoperíodo (Fase 3) via **saída PWM** para os drivers dimerizáveis. O acionamento abrupto (liga/desliga direto) provoca reação de susto nos peixes: saltos, colisão com paredes e bordas, descamação e lesões — com potencial impacto real sobre mortalidade e qualidade do filé.

**Protocolo de rampa:**

| Evento | Horário | Ação do CLP |
| :--- | :---: | :--- |
| Amanhecer (liga) | 06h00 | Rampa PWM: 0% → 100% em **15–20 min** |
| Anoitecer (desliga) | 22h00 | Rampa PWM: 100% → 0% em **15–20 min** |

```
Rotina CLP — Rampa de Amanhecer (06h00):
  Para t = 0 até 1200 s (20 min):
    PWM_duty = (t / 1200) × 100 %
    Aguardar 1 s
  PWM_duty = 100 %  // luz plena

Rotina CLP — Rampa de Anoitecer (22h00):
  Para t = 0 até 1200 s (20 min):
    PWM_duty = 100 % − (t / 1200) × 100 %
    Aguardar 1 s
  PWM_duty = 0 %    // escuro total
```

**Integração com alarmes:**
- Se OD < 3,5 mg/L durante período de luz → CLP **não desliga LEDs** (luz não consome OD; desligar causaria mais stress que o benefício).
- Se sensor de OD falhar → LEDs mantêm ciclo autônomo por relógio interno do CLP.
- Fotoperíodo é considerado **carga não essencial** pelo gerador (gerador protege sopradores e CLP, mas LEDs podem ficar sem luz em emergência sem risco imediato de mortalidade).

---

### Lógica Integrada OD + pH no CLP

```
Loop de controle (varredura a cada 10 min):

  Se pH > 7,2:
    → Verificar se CO₂ está alto (possível excesso de biomassa)
    → Aumentar aeração (sopradores +5 Hz)
    → NÃO adicionar base (o percolador aberto corrige naturalmente)

  Se pH < 7,0:
    → Verificar TAN — se TAN > 1,5 mg/L: nitrificação plena, aguardar
    → Se pH < 6,8: ativar válvula de reposição de água (diluição)
    → Verificar contator de calcário (repor brita se necessário)

  Se TAN > 2,5 mg/L (independente do pH):
    → Abrir válvula de renovação de água (ciclo de 15 min)

  Se NH₃ livre calculada > 0,03 mg/L:
    → Alerta crítico no celular
    → Abertura forçada de renovação + aumento de aeração
```

### Impacto no Consumo de Água e Energia

Manter pH em 7,1 e gatilho TAN em 2,5 mg/L (em vez de 1,0 mg/L) reduz as trocas de água em **~40% ao mês**:

| Efeito | Estimativa de economia |
| :--- | :--- |
| Energia do poço artesiano (menos bombeamento) | R$ 50–80/mês |
| Bomba de Calor (menos água fria adicionada ao sistema) | R$ 88/mês (~10%) |
| **Total estimado de economia mensal** | **~R$ 138–168/mês** |

### Sensor de pH — Especificação

| Item | Especificação |
| :--- | :--- |
| Tipo | Eletrodo de vidro ou ISFET industrial, IP68 |
| Saída | 4–20 mA (compatível com CLP Modbus) |
| Instalação | Na câmara de multiplexação de OD (mesmo ponto) |
| Custo estimado | R$ 800–1.500 |
| Calibração | Quinzenal (soluções tampão pH 7,0 e pH 4,0) |

O sensor de pH é integrado à **câmara central de multiplexação** existente da Fase 2, sem necessidade de nova câmara. O CLP alterna entre a medição de OD e de pH na mesma sequência de amostragem dos 6 tanques.

---

## Riscos e Limitações
- **Tempo de amostragem multiplexada ("janela cega"):** O intervalo de ~10 min entre leituras significa que um colapso de OD pode não ser detectado por até 10,8 min — tempo suficiente para mortalidade em massa a 2.391 kg de biomassa (consumo de O₂: ~13.940 mg/min; queda de 2,5 mg/L em 60.000 L = ~10,8 min até hipóxia crítica). **Mitigação primária:** Sensor de pressão no manifold dos sopradores (R$ 250) — detecta queda ou falha do soprador em segundos, independente do ciclo de OD. Mitigação secundária: inversores operando com margem de segurança (nunca abaixo de 50% de potência na madrugada).
- **Gasolina degradada:** Gasolina armazenada degrada em ~3 meses. Usar aditivo estabilizante ou fazer rodízio mensal do estoque.
- **Deriva do sensor de pH:** Eletrodos de vidro derivam ~0,05 pH/semana. Calibração quinzenal obrigatória. Um pH lido como 7,1 pode ser 7,3 real se o sensor estiver descalibrado — isso anula o benefício da janela dinâmica.

## Custos Estimados — Fase 2

| Item | Qtd | Valor (R$) |
| :--- | :---: | :--- |
| Painel CLP + IHM + componentes | 1 | 10.000 |
| Sensores ópticos OD (industriais) | 2 | 12.000 |
| Sistema multiplexação (válvulas, bombas, câmara) | 1 | 4.000 |
| Inversores de Frequência WEG | 2 | 4.800 |
| Mão de obra técnica (instalação + programação CLP) | 1 | 5.000 |
| Contator de Calcário Passivo (brita calcítica, caixa PVC, tubulação — ver [Doc 06 §6.4](06_Qualidade_Riscos_e_Licenciamento.md)) | 1 | 3.000 |
| Sensor de pressão diferencial (filtro kidney) + integração CLP | 1 | 700 |
| Sensor de pressão no manifold dos sopradores *(detecção imediata de falha de soprador — mitigação da janela cega de OD; alarme Telegram em <5 s)* | 1 | 250 |
| **TOTAL FASE 2** | | **R$ 39.750** |

*Gerador 8–10 kVA + QTA (R$ 12.000) realocado para Fase 1 — ver [Doc 01](01_Infraestrutura_e_Aeracao.md). Sensor de pH eletrodo ISFET IP68 (~R$ 1.000) incluso no orçamento de "Painel CLP + IHM + componentes". Ver [Doc 02 — Seção Controle de pH](02_Automacao_e_Seguranca.md) para especificação.*
