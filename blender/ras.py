import math
import utils as U
from constants import RAS_Y, RAS_Z, RAS_DX, RAS_PX, X_OFF

# Posições derivadas
HC_X  = X_OFF + RAS_DX          # hidrociclone (substitui decantador cônico)
SL_X  = X_OFF + RAS_DX + 2.20   # settler laminar (placas inclinadas)
# RAS_PX = 26.5          — percolador (inalterado)

# Sump Coletor posicionado logo antes do Hidrociclone (alimenta HC por bomba)
SUMP_X = X_OFF + RAS_DX - 1.40  # 1,4 m a oeste do Hidrociclone


def build_ras():
    """
    RAS — linha de tratamento sul do Patamar 2
    ──────────────────────────────────────────
    Fluxo: tanques → hidrociclone → settler laminar → percolador
           → filtro de tela → UV → reservatório → bomba → tanques

    Substituições vs. versão anterior
      - Decantador cônico simples  →  Hidrociclone Ø400 mm  +  Settler laminar 0.8×0.8×1.2 m
      Eficiência TSS: 70–85 %   →  90–95 %
      Manutenção: purga manual 3×/sem  →  purga automática contínua (apex)
    """
    HC  = "RAS/RAS_Hidrociclone"
    SLc = "RAS/RAS_Settler"
    BIO = "RAS/RAS_Percolador"
    EQP = "RAS/RAS_Equipamentos"

    # ══════════════════════════════════════════════════════════════════════════
    # 0. SUMP COLETOR 300 L + BOMBA DE SÓLIDOS 0,5 CV
    #    Recebe dreno de fundo de 6 tanques (60 L/min contínuos).
    #    Tempo de enchimento: 5 min → bomba opera 24/7 em modo contínuo puro.
    #    Bomba centrifuga 60 L/min para o Hidrociclone (cabeça < 3 m).
    # ══════════════════════════════════════════════════════════════════════════
    SUP = "RAS/RAS_Sump"

    # Tanque sump (HDPE 300 L: Ø 0,7 m × h 0,8 m)
    U.add_cyl("Sump_Tanque", 0.35, 0.80,
              (SUMP_X, RAS_Y, RAS_Z + 0.40), U.M_HDPE, SUP, segs=16)
    U.add_cyl("Sump_Tampa",  0.36, 0.03,
              (SUMP_X, RAS_Y, RAS_Z + 0.815), U.M_HDPE, SUP, segs=16)
    # Entrada de drenos (coletor superior lateral — 6 tubos dos tanques chegam aqui)
    U.add_cyl("Sump_Inlet",  0.055, 0.40,
              (SUMP_X - 0.40, RAS_Y, RAS_Z + 0.65),
              U.M_PVC, SUP, rot=(0, math.pi/2, 0), segs=8)
    # Sensor de nível (boia industrial)
    U.add_cyl("Sump_SensorNivel", 0.015, 0.30,
              (SUMP_X + 0.22, RAS_Y, RAS_Z + 0.60), U.M_PANEL, SUP, segs=6)

    # Bomba de sólidos (0,5 CV, impelidor aberto, passa-sólidos)
    U.add_cyl("SumpBomba_Corpo",  0.10, 0.22,
              (SUMP_X, RAS_Y + 0.50, RAS_Z + 0.11), U.M_STEEL, SUP, segs=16)
    U.add_box("SumpBomba_Motor",  (0.22, 0.16, 0.16),
              (SUMP_X, RAS_Y + 0.72, RAS_Z + 0.08), U.M_STEEL, SUP)
    # Tubulação de descarga bomba → Hidrociclone
    U.add_cyl("SumpBomba_Desc",   0.040, 1.45,
              (SUMP_X + 0.72, RAS_Y + 0.50, RAS_Z + 0.20),
              U.M_PVC, SUP, rot=(0, math.pi/2, 0), segs=8)

    # ══════════════════════════════════════════════════════════════════════════
    # 1. HIDROCICLONE Ø400 mm
    #    Corpo cilíndrico (seção de entrada tangencial) + cone apex
    #    Remove > 90 % dos sólidos > 80 µm por força centrífuga (50–200 g)
    #    Purga contínua pelo apex — sem partes móveis, sem manutenção periódica
    # ══════════════════════════════════════════════════════════════════════════

    # Corpo cilíndrico principal
    U.add_cyl("HC_Corpo", 0.210, 0.65,
              (HC_X, RAS_Y, RAS_Z + 0.975), U.M_RAS, HC, segs=32)
    U.add_cone("HC_Cone", 0.210, 0.035, 0.80,
               (HC_X, RAS_Y, RAS_Z + 0.25), U.M_RAS, HC, segs=32)
    U.add_cyl("HC_Tampa", 0.230, 0.025,
              (HC_X, RAS_Y, RAS_Z + 1.313), U.M_STEEL, HC, segs=32)
    U.add_cyl("HC_VortexFinder", 0.058, 0.45,
              (HC_X, RAS_Y, RAS_Z + 1.55), U.M_PVC, HC, segs=12)
    U.add_cyl("HC_Entrada", 0.048, 0.35,
              (HC_X + 0.27, RAS_Y, RAS_Z + 1.20),
              U.M_PVC, HC, rot=(0, math.pi/2, 0), segs=12)
    U.add_cyl("HC_Apex", 0.040, 0.30,
              (HC_X, RAS_Y, RAS_Z - 0.30), U.M_PVC, HC, segs=8)
    U.add_cyl("HC_Valv_Apex", 0.055, 0.12,
              (HC_X, RAS_Y, RAS_Z - 0.08), U.M_STEEL, HC, segs=12)
    U.add_cyl("HC_BombaAlim_Corpo", 0.10, 0.22,
              (HC_X + 0.65, RAS_Y, RAS_Z + 0.11), U.M_STEEL, HC, segs=16)
    U.add_box("HC_BombaAlim_Motor", (0.22, 0.16, 0.16),
              (HC_X + 0.65, RAS_Y - 0.20, RAS_Z + 0.08), U.M_STEEL, HC)

    # ── Settler laminar ───────────────────────────────────────────────────────
    U.add_box("SL_Caixa", (0.82, 0.82, 1.22),
              (SL_X, RAS_Y, RAS_Z + 0.61), U.M_HDPE, SLc)

    plate_ang = math.radians(55)
    plate_l   = 0.68
    plate_dx  = plate_l * math.cos(plate_ang)
    plate_w   = 0.75
    plate_t   = 0.008
    import bpy as _bpy
    for k in range(6):
        offset_z = 0.18 + k * 0.12
        cx_plate = SL_X - 0.28 + plate_dx / 2
        cz_plate = RAS_Z + offset_z + (plate_l * math.sin(plate_ang)) / 2
        _bpy.ops.mesh.primitive_cube_add(location=(cx_plate, RAS_Y, cz_plate))
        pl = _bpy.context.active_object
        pl.name = f"SL_Placa_{k}"
        pl.scale = (plate_dx / 2, plate_w / 2, plate_t / 2)
        pl.rotation_euler = (0, plate_ang, 0)
        _bpy.ops.object.transform_apply(scale=True)
        U.put_mat(pl, U.M_PVC)
        U.to_col(pl, SLc)

    U.add_cyl("SL_Saida", 0.055, 0.35,
              (SL_X + 0.46, RAS_Y, RAS_Z + 1.05),
              U.M_PVC, SLc, rot=(0, math.pi/2, 0), segs=12)
    U.add_cyl("SL_Lodo", 0.040, 0.20,
              (SL_X, RAS_Y, RAS_Z - 0.10), U.M_PVC, SLc, segs=8)

    # ── Percolador + mídias ───────────────────────────────────────────────────
    U.add_box("RAS_Percolador", (4.5, 1.8, 1.4),
              (X_OFF + RAS_PX, RAS_Y, RAS_Z + 0.70), U.M_RAS, BIO)
    for xi in range(5):
        U.add_cyl(f"RAS_Midia_{xi}", 0.015, 1.30,
                  (X_OFF + RAS_PX - 1.6 + xi * 0.65, RAS_Y, RAS_Z + 0.65),
                  U.M_CONC, BIO, segs=6)

    # ── Equipamentos auxiliares ───────────────────────────────────────────────
    U.add_cyl("RAS_FiltroTela", 0.30, 0.80,
              (X_OFF + 29.2, RAS_Y, RAS_Z + 0.40), U.M_STEEL, EQP)
    U.add_cyl("RAS_FT_Eixo", 0.015, 0.82,
              (X_OFF + 29.2, RAS_Y, RAS_Z + 0.41), U.M_STEEL, EQP)
    U.add_cyl("RAS_UV", 0.065, 0.90,
              (X_OFF + 29.2, RAS_Y + 0.55, RAS_Z + 0.45), U.M_UV, EQP,
              rot=(math.pi/2, 0, 0))
    U.add_box("RAS_Reservatorio", (2.4, 1.6, 1.6),
              (X_OFF + 19.2, RAS_Y, RAS_Z + 0.80), U.M_HDPE, EQP)
    U.add_cyl("RAS_Bomba_Corpo", 0.18, 0.36,
              (X_OFF + 17.6, RAS_Y, RAS_Z + 0.18), U.M_STEEL, EQP)
    U.add_box("RAS_Bomba_Motor", (0.32, 0.22, 0.24),
              (X_OFF + 17.6, RAS_Y - 0.28, RAS_Z + 0.12), U.M_STEEL, EQP)
    U.add_box("RAS_ValvBox", (0.70, 0.40, 0.55),
              (X_OFF + 20.0, RAS_Y, RAS_Z + 0.275), U.M_CONC, EQP)

    # ── Contator de Calcário por Fluxo Ascendente ─────────────────────────────
    # Posicionado no nível P3 (após FiltroTela+UV, antes do Reservatório).
    # Fluxo ascendente alimentado pelo desnível de 2,5 m entre P2 e P3.
    # Operação: entrada pelo fundo → sobe por 800-1000 kg de brita calcítica →
    # saída pelo topo lateral → Reservatório → Bomba → tanques.
    # Manutenção: 1×/mês — purga de fundo (2 min) + reposição 4-5 sacos 50 kg.
    # OPEX: R$ 640/mês vs. R$ 2.583/mês (bicarbonato) → economia R$ 23.316/ano.
    CAL = "RAS/RAS_Contator_Calcario"
    CAL_X = X_OFF + 15.5
    CAL_Y = RAS_Y

    # Corpo principal (HDPE, Ø 1,1 m × h 1,5 m)
    U.add_cyl("Calc_Corpo",    0.55, 1.50, (CAL_X, CAL_Y, RAS_Z + 0.75), U.M_HDPE, CAL, segs=24)
    # Tampa superior removível (acesso para reabastecer brita)
    U.add_cyl("Calc_Tampa",    0.57, 0.04, (CAL_X, CAL_Y, RAS_Z + 1.52), U.M_HDPE, CAL, segs=24)
    # Entrada inferior (fluxo ascendente — alimentado por gravidade do UV/FiltroTela)
    U.add_cyl("Calc_Inlet",    0.035, 0.40,
              (CAL_X, CAL_Y, RAS_Z - 0.20), U.M_PVC, CAL, segs=8)
    # Saída superior lateral (água tratada → Reservatório)
    U.add_cyl("Calc_Outlet",   0.035, 0.35,
              (CAL_X + 0.58, CAL_Y, RAS_Z + 1.35),
              U.M_PVC, CAL, rot=(0, math.pi/2, 0), segs=8)
    # Dreno de fundo — purga mensal de finos orgânicos decantados
    U.add_cyl("Calc_Dreno",    0.025, 0.25,
              (CAL_X - 0.58, CAL_Y, RAS_Z + 0.12),
              U.M_PVC, CAL, rot=(0, math.pi/2, 0), segs=8)
    # Rótulo de identificação (caixa fina representando plaqueta)
    U.add_box("Calc_Label",    (0.04, 0.20, 0.08),
              (CAL_X + 0.56, CAL_Y, RAS_Z + 0.75), U.M_PANEL, CAL)

    # ══════════════════════════════════════════════════════════════════════════
    # FASE 6B — FOTOCATÁLISE TiO₂ + UV
    #   Colmeia cerâmica revestida com TiO₂ P25 instalada dentro do reator UV
    #   existente. Os radicais ·OH gerados destroem a geosmina em trânsito →
    #   depuração reduz de 3-5 dias para 24-48 h. CAPEX R$ 4.500.
    #   Economia: R$ 1.090/mês (perda de peso) + R$ 115/mês (bombeamento) =
    #   R$ 1.205/mês. Manutenção: reposição TiO₂ R$ 350-600/ano.
    # ══════════════════════════════════════════════════════════════════════════
    F6B = "RAS/RAS_Fase6B_TiO2"
    UV_X  = X_OFF + 29.2
    UV_CY = RAS_Y + 0.55   # centro Y do reator UV (orientado em Y)
    UV_CZ = RAS_Z + 0.45

    # Colmeia cerâmica TiO₂ — cilindro levemente menor que o tubo UV (Ø 0,10 m)
    # Comprimento 0,45 m para ocupar a zona ativa da lâmpada
    U.add_cyl("UV_TiO2_Colmeia", 0.048, 0.45,
              (UV_X, UV_CY, UV_CZ), U.M_CONC, F6B,
              rot=(math.pi/2, 0, 0), segs=16)
    # Plaqueta de identificação fixada na lateral do corpo UV
    U.add_box("UV_TiO2_Label", (0.04, 0.15, 0.06),
              (UV_X + 0.08, UV_CY, UV_CZ + 0.10), U.M_PANEL, F6B)

    # ══════════════════════════════════════════════════════════════════════════
    # FASE 6C — REATOR DE CRISTALIZAÇÃO DE ESTRUVITA
    #   Recebe lodo do Settler Laminar (saída SL_Lodo) por gravidade.
    #   MgO dosado passivamente → pH 8,5-9,5 → precipitação de estruvita.
    #   Produção: ~45 kg/mês → receita R$ 1.125/mês. CAPEX R$ 8.500.
    #   Cone PVC Ø 0,60 m × h 1,20 m, misturador lento 0,1 CV, secagem ao sol.
    # ══════════════════════════════════════════════════════════════════════════
    F6C = "RAS/RAS_Fase6C_Estruvita"
    # Posicionado a 1,5 m a leste do Settler, mesmo nível Y
    EST_X = SL_X + 1.80
    EST_Y = RAS_Y
    EST_Z = RAS_Z   # fundo ao nível do piso P2

    # Corpo cônico PVC rígido invertido (representado como cilindro + cone)
    U.add_cyl("Estru_Corpo_Cil",  0.30, 0.70,
              (EST_X, EST_Y, EST_Z + 0.85), U.M_PVC, F6C, segs=20)
    U.add_cone("Estru_Corpo_Cone", 0.30, 0.04, 0.50,
               (EST_X, EST_Y, EST_Z + 0.25), U.M_PVC, F6C, segs=20)
    # Suporte metálico (cavalete)
    U.add_box("Estru_Suporte", (0.08, 0.70, 0.04),
              (EST_X, EST_Y, EST_Z + 0.02), U.M_STEEL, F6C)
    # Misturador lento (eixo vertical + motor no topo)
    U.add_cyl("Estru_Eixo",  0.012, 0.90,
              (EST_X, EST_Y, EST_Z + 0.75), U.M_STEEL, F6C, segs=8)
    U.add_box("Estru_Motor", (0.14, 0.10, 0.12),
              (EST_X, EST_Y, EST_Z + 1.26), U.M_STEEL, F6C)
    # Funil dosador de MgO (PVC, topo lateral)
    U.add_cone("Estru_Funil_MgO", 0.12, 0.03, 0.20,
               (EST_X + 0.32, EST_Y, EST_Z + 1.05), U.M_PVC, F6C, segs=12)
    U.add_cyl("Estru_Funil_Tubo",  0.022, 0.18,
              (EST_X + 0.32, EST_Y, EST_Z + 0.88), U.M_PVC, F6C, segs=8)
    # Tubulação de alimentação: saída de lodo do Settler → reator
    U.add_cyl("Estru_AlimTubo",  0.032, 1.85,
              (SL_X + 0.93, EST_Y, EST_Z - 0.08),
              U.M_PVC, F6C, rot=(0, math.pi/2, 0), segs=8)
    # Saída de clarificado (retorna ao Reservatório RAS)
    U.add_cyl("Estru_ClarOut",   0.028, 0.35,
              (EST_X - 0.32, EST_Y, EST_Z + 1.05),
              U.M_PVC, F6C, rot=(0, math.pi/2, 0), segs=8)
    # Dreno inferior cônico — coleta estruvita úmida
    U.add_cyl("Estru_DrainBot",  0.025, 0.20,
              (EST_X, EST_Y, EST_Z - 0.10), U.M_PVC, F6C, segs=8)
    # Plaqueta de identificação
    U.add_box("Estru_Label", (0.04, 0.20, 0.08),
              (EST_X + 0.32, EST_Y, EST_Z + 0.60), U.M_PANEL, F6C)
