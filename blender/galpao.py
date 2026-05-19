import bpy
import math
import utils as U
from constants import P3_Y0, P3_Z, X_OFF


def build_galpao():
    EST  = "Galpao/Galpao_Estrutura"    # paredes, piso, telhado, portão, divisórias
    FIL  = "Galpao/Galpao_Filetagem"    # mesas, câmara fria, freezers, tanque lavagem
    RAC  = "Galpao/Galpao_Racao"        # extrusora, moinho, misturador, IBCs
    DEP  = "Galpao/Galpao_Deposito"     # prateleiras, sacos, estoque
    GRX  = "Galpao/Galpao_Graxaria"     # anexo externo graxaria

    GX   = X_OFF + 3.0
    GY0  = P3_Y0 + 0.5   # 4.5 — 0.5 m de buffer da borda sul de P3
    GW   = 22.0
    GL   = 16.0
    GH   = 4.2
    RH   = 2.0
    GZ   = P3_Z          # piso do galpão = piso do patamar base P3
    HALF = GW / 2

    # ── Paredes alvenaria ─────────────────────────────────────────────────────
    U.add_box("G_Parede_S", (GW+0.4, 0.20, GH), (GX+HALF, GY0,      GZ+GH/2), U.M_WALL, EST)
    U.add_box("G_Parede_N", (GW+0.4, 0.20, GH), (GX+HALF, GY0+GL,   GZ+GH/2), U.M_WALL, EST)
    U.add_box("G_Parede_O", (0.20,   GL,   GH), (GX,       GY0+GL/2, GZ+GH/2), U.M_WALL, EST)
    U.add_box("G_Parede_L", (0.20,   GL,   GH), (GX+GW,    GY0+GL/2, GZ+GH/2), U.M_WALL, EST)

    # ── Piso ──────────────────────────────────────────────────────────────────
    U.add_box("G_Piso", (GW, GL, 0.12), (GX+HALF, GY0+GL/2, GZ-0.06), U.M_CONC, EST)

    # ── Telhado duas águas ────────────────────────────────────────────────────
    me = bpy.data.meshes.new("G_Telhado")
    verts = [
        (GX - 0.4,      GY0 - 0.4,    GZ + GH),
        (GX + HALF,     GY0 - 0.4,    GZ + GH + RH),
        (GX + GW + 0.4, GY0 - 0.4,    GZ + GH),
        (GX - 0.4,      GY0+GL + 0.4, GZ + GH),
        (GX + HALF,     GY0+GL + 0.4, GZ + GH + RH),
        (GX + GW + 0.4, GY0+GL + 0.4, GZ + GH),
    ]
    fcs = [(0,1,4,3), (1,2,5,4), (0,2,1), (3,4,5)]
    me.from_pydata(verts, [], fcs)
    me.validate()
    me.update()
    tobj = U.new_obj("G_Telhado", me)
    U.put_mat(tobj, U.M_ROOF)
    U.to_col(tobj, EST)

    # ── Portão + divisórias ───────────────────────────────────────────────────
    U.add_box("G_Portao_L",  (0.06, 5.0, 4.0),
              (GX+GW+0.06, GY0+GL/2, GZ+2.0), U.M_STEEL, EST)
    U.add_box("G_Div_Filet", (GW, 0.12, GH-0.4),
              (GX+HALF, GY0+5.5,  GZ+(GH-0.4)/2), U.M_WALL, EST)
    U.add_box("G_Div_Racao", (GW, 0.12, GH-0.4),
              (GX+HALF, GY0+11.0, GZ+(GH-0.4)/2), U.M_WALL, EST)

    # ── Filetagem ─────────────────────────────────────────────────────────────
    U.add_box("G_Mesa_Filet", (4.0, 1.0, 0.90), (GX+5.0,  GY0+2.5, GZ+0.45),    U.M_STEEL, FIL)
    U.add_box("G_Mesa_Emb",   (2.5, 1.0, 0.90), (GX+9.5,  GY0+2.5, GZ+0.45),    U.M_STEEL, FIL)
    U.add_cyl("G_TqLavagem",   0.45, 0.55,       (GX+14.0, GY0+1.8, GZ+0.275),   U.M_STEEL, FIL)
    U.add_box("G_Freezer_1",  (0.85, 0.85, 1.95),(GX+17.5, GY0+1.5, GZ+0.975),   U.M_STEEL, FIL)
    U.add_box("G_Freezer_2",  (0.85, 0.85, 1.95),(GX+19.2, GY0+1.5, GZ+0.975),   U.M_STEEL, FIL)
    U.add_box("G_CamaraFria", (3.0, 2.5, GH-0.3),(GX+1.8,  GY0+1.5, GZ+(GH-0.3)/2), U.M_WALL, FIL)

    # ── Fábrica de ração ──────────────────────────────────────────────────────
    U.add_box("G_Extrusora",  (3.2, 0.75, 1.30), (GX+5.0,  GY0+8.0, GZ+0.65),   U.M_STEEL, RAC)
    U.add_cyl("G_Ext_Bocal",   0.14, 0.70,        (GX+6.7,  GY0+8.0, GZ+0.85),   U.M_STEEL, RAC,
              rot=(0, math.pi/2, 0))
    U.add_box("G_Moinho",     (0.90, 0.90, 1.20), (GX+10.5, GY0+7.5, GZ+0.60),   U.M_STEEL, RAC)
    U.add_cyl("G_Misturador",  0.55, 1.30,        (GX+13.5, GY0+8.0, GZ+0.65),   U.M_STEEL, RAC,
              rot=(math.pi/2, 0, 0))
    U.add_box("G_Secador",    (2.5, 1.2, 0.60),   (GX+17.5, GY0+8.0, GZ+0.30),   U.M_STEEL, RAC)
    for ii in range(4):
        U.add_box(f"G_IBC_{ii}", (1.00, 1.20, 1.20),
                  (GX+1.5+ii*1.35, GY0+9.5, GZ+0.60), U.M_HDPE, RAC)

    # ── Depósito ──────────────────────────────────────────────────────────────
    U.add_box("G_EPS_Stack",   (5.0, 3.5, 1.60),  (GX+9.0,  GY0+13.5, GZ+0.80), U.M_CONC,  DEP)
    U.add_box("G_Prateleira",  (6.0, 0.50, 2.00), (GX+4.0,  GY0+13.0, GZ+1.00), U.M_STEEL, DEP)
    U.add_box("G_Sacos_Racao", (4.0, 2.0,  1.50), (GX+17.5, GY0+13.5, GZ+0.75), U.M_PVC,   DEP)

    # ── Graxaria — anexo externo norte ────────────────────────────────────────
    grx = GX + HALF - 2.5
    gry = GY0 + GL + 0.2
    U.add_box("Grax_PS",         (5.0, 0.20, 3.5),      (grx+2.5, gry,     GZ+1.75),      U.M_WALL,  GRX)
    U.add_box("Grax_PN",         (5.0, 0.20, 3.5),      (grx+2.5, gry+6.0, GZ+1.75),      U.M_WALL,  GRX)
    U.add_box("Grax_PO",         (0.20, 6.0, 3.5),      (grx,      gry+3.0, GZ+1.75),      U.M_WALL,  GRX)
    U.add_box("Grax_PL",         (0.20, 6.0, 3.5),      (grx+5.0,  gry+3.0, GZ+1.75),      U.M_WALL,  GRX)
    U.add_box("Grax_Cob",        (5.4,  6.4, 0.10),     (grx+2.5,  gry+3.0, GZ+3.55),      U.M_ROOF,  GRX)
    U.add_cyl("Grax_Digestor",    0.65, 1.90,            (grx+1.5,  gry+1.8, GZ+0.95),      U.M_STEEL, GRX)
    U.add_box("Grax_Prensa",     (0.65, 0.45, 0.95),    (grx+3.2,  gry+2.0, GZ+0.475),     U.M_STEEL, GRX)
    U.add_cyl("Grax_Condensador", 0.28, 1.00,            (grx+4.2,  gry+3.8, GZ+0.50),      U.M_STEEL, GRX)
    U.add_box("Grax_FiltCarv",   (0.50, 0.50, 0.80),    (grx+2.5,  gry+4.8, GZ+0.40),      U.M_STEEL, GRX)
    U.add_cyl("Grax_Chamine",     0.10, 3.50,            (grx+4.6,  gry+5.5, GZ+5.30),      U.M_STEEL, GRX)
