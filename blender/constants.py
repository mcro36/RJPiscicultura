"""Constantes geométricas do projeto — sem dependências de bpy."""
import math

# ── Terreno ────────────────────────────────────────────────────────────────────
TW    = 30.00          # largura X  (Oeste→Leste)
TL    = 68.37          # comprimento Y (Sul→Norte)
Z_N   = 10.0           # cota face norte
Z_S   =  0.0           # cota face sul
SLOPE = (Z_N - Z_S) / TL   # 0.14637 m/m

# ── Deslocamento do Projeto (X) ──────────────────────────────────────────────
# O projeto principal agora reside no terreno natural gradeado (unificado na origem)
X_OFF = 0.0

# ── 2 Patamares — calibrados contra terreno SRTM real ────────────────────────
#
#  Redesign 2026-05: redução de 4 para 2 patamares efetivos.
#  O antigo "P4 Galpão" separado causava piso abaixo do nível da rua.
#  Solução: galpão e T7/RAS no patamar base (P3); tanques L1 e L2 unificados
#  em P2 (mesmo Z=6.0) — sem talude intermediário entre fileiras.
#
#  O terreno SRTM é plano em Z≈5–7 com aclive sul→norte de ≈2,5 m e
#  gradiente forte oeste→leste de ≈5 m.  Estrada ao sul ≈ Z=4,0.
#
#  P3 base │talude H=1│  P2 (L1+L2 unificados, topo)
#  Z=5.0   │ run=2.0m │  Z=6.0
#  Y[1–40] │ Y[40–42] │  Y[42–68.37]
#
#  Dentro de P3 (mesmo piso Z=5.0):
#    Y  1–23 → zona galpão (filetagem, ração, depósito, gerador)
#    Y 24–25 → corredor de serviço / acesso externo
#    Y 26–40 → zona T7 + RAS (decantador, percolador, UV, reservatório)
#
#  Dentro de P2 (mesmo piso Z=6.0):
#    L2_TY=48.0 → fileira sul (T4–T6)
#    L1_TY=62.2 → fileira norte (T1–T3)
#    L1_Y0=56.0 → referência interna de separação das fileiras (sem talude)
#
#  Earthwork estimado (Z_nat SRTM amostrado nos X dos tanques):
#    P3  Z_nat≈5.5  → patamar 5.0 → corte leve ≤1.0 m na faixa oeste
#    P2  Z_nat≈6.7  → patamar 6.0 → corte moderado ~0.7 m (fileiras L1 e L2)
#
#  Drenos gravitacionais: ZP1=ZP2=5.41 → ZP3=4.41 → RAS_Z=4.50 ✓
#  Piso galpão Z=5.0 → estrada Z≈4.0 → acesso com rampa ≈1 m / 10 m = 10% ✓
#

# P3 — Patamar base: Galpão (Y:1-23) + T7 + RAS (Y:26-40) — mesmo piso (P3_Y0=1.0)
P3_Y0, P3_Y1, P3_Z = 1.00, 40.00, 5.0

# P2 — Patamar topo unificado: fileiras L1 e L2 (T1–T6) no mesmo Z=6.0
L2_Y0, L2_Y1, L2_Z = 42.00, TL, 6.0

# L1 como sub-zona de P2 (sem patamar separado — L1_Z = L2_Z)
L1_Z  = L2_Z      # 6.0 — mesmo piso de P2
L1_Y0 = 56.00     # referência interna: separa fileira L2 (sul) de L1 (norte)
L1_Y1 = TL

# ── Tanques geomembrana HDPE ──────────────────────────────────────────────────
TK_D     = 7.40     # diâmetro
TK_R     = TK_D / 2
TK_WALL  = 1.65     # altura estrutura total
TK_WD    = 1.40     # lâmina d'água útil
TK_THICK = 0.06     # espessura do anel galvanizado

# Espaçamento EMBRAPA: 2.0 m borda-a-borda → 9.40 m centro-a-centro
TK_CC = TK_D + 2.0

# X dos 3 tanques por fileira — margem lateral = (30 - 3×7.4 - 2×2.0) / 2 = 1.9 m
TK_X = [1.9 + TK_R + i * TK_CC for i in range(3)]   # [5.6, 15.0, 24.4]

# Y centrais das fileiras (mantidos fixos para não deslocar tanques ao mudar patamares)
P3_T7_ZONE_Y0 = 26.00
L1_TY = 62.19
L2_TY = 48.00
T7_Y  = 32.00

# Corredores de aeração (sul de cada fileira, sem cruzar tanques)
L1_CORR = L1_TY - TK_R - 1.0   # 57.49 — corredor sul L1
L2_CORR = L2_TY - TK_R - 1.0   # 43.30 — corredor sul L2

# Vala coletora de drenos (leste de todos os tanques)
TRENCH_X = TK_X[2] + TK_R + 0.6    # 28.70 — eixo da vala leste

# ── RAS (posicionado em P3) ───────────────────────────────────────────────────
RAS_Y  = P3_T7_ZONE_Y0 + 1.30  # 27.30 — linha do RAS (via âncora interna)
RAS_Z  = P3_Z  - 0.50          #  4.50 — rebaixado 0,50 m abaixo do piso P3 (P3_Z=5.0)
RAS_DX = 22.0            # X do hidrociclone
RAS_PX = 26.5            # X do percolador

# ── Lote 15h2 e 15h1 — coordenadas Blender corrigidas via transformação afim ──
#
#  Erro anterior: escala lat/lon simples pressuponha Y‖norte geográfico.
#  Na realidade o Lote_16 está rotacionado ~20° no campo → a conversão
#  correta usa os 4 cantos GPS do próprio Lote_16 como referência afim:
#
#    GPS anchor SW (V3): (-19.916518, -43.804262) → Blender (0,  0   )
#    GPS anchor SE (V4): (-19.916418, -43.803995) → Blender (30, 0   )
#    GPS anchor NE (V1): (-19.915841, -43.804226) → Blender (30, 68.37)
#    GPS anchor NW (V2): (-19.915950, -43.804490) → Blender ( 0, 68.37)
#
#  Matriz afim inversa (u,v):
#    u = 1307·Δlat + 3256·Δlon    →  x = u × TW
#    v = 1531·Δlat -  573·Δlon    →  y = v × TL
#  onde Δlat = lat+19.916518,  Δlon = lon+43.804262
#
#  Lote 15h2 — quadrilátero, LESTE do Lote_16 (faixa estreita N-S)
#    V1 NW (-19.915841,-43.804226) → (30.00, 68.37)  = Lote16 NE (snapped)
#    V2 NE (-19.915784,-43.804145) → (40.20, 72.20)  = L15h1 P1
#    V3 SE (-19.916337,-43.803883) → (44.12,  4.09)
#    V4 SW (-19.916417,-43.803996) → (30.00,  0.00)  = Lote16 SE (snapped)
#
#  Lote 15h1 — pentágono, NORTE do Lote_16 e Lote_15h2
#    P1 SE (-19.915785,-43.804145) → (40.20, 72.20)  = L15h2 V2
#    P2 NE (-19.915535,-43.804269) → (37.87,103.14)
#    P3 NW (-19.915681,-43.804597) → ( 0.00,100.72)
#    P4 SW (-19.915950,-43.804490) → ( 0.00, 68.37)  = Lote16 NW (snapped)
#    P5 S  (-19.915841,-43.804226) → (30.00, 68.37)  = Lote16 NE (snapped)
#
# Lote 15h2 — (V1 NW, V2 NE, V3 SE, V4 SW)
L15H2_VERTS = ((30.00, 68.37), (40.20, 72.20), (44.12, 4.09), (30.00, 0.00))

# Lote 15h1 — pentágono (P1 SE, P2 NE, P3 NW, P4 SW, P5 S-central)
L15H1_VERTS = ((40.20, 72.20), (37.87, 103.14), (0.00, 100.72), (0.00, 68.37), (30.00, 68.37))
