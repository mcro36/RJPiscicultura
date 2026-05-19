import bpy
import math
import utils as U
from constants import (TW, TL, Z_N,
                       L1_Y0, L1_Z,
                       L2_Y0, L2_Y1, L2_Z, L2_TY,
                       P3_Y0, P3_Y1, P3_Z,
                       TK_R, TK_X, X_OFF)

SOP  = "Aeracao/Aer_Sopradores"    # abrigo + corpos dos sopradores
CLP  = "Infra/Infra_CLP"           # painel CLP, UPS
ENG  = "Infra/Infra_Energia"       # gerador, QTA
POC  = "Infra/Infra_Poco"          # casa do poço
ACS  = "Infra/Infra_Acessos"       # rampas, muretas, portão, calçada
LDO  = "Tubulacoes/Tub_Lodo"       # descarte de lodo RAS → irrigação


def build_infra():

    # ── Casa dos sopradores ───────────────────────────────────────────────────
    sop_x = X_OFF + TW - 4.5
    sop_y = L2_TY - 2.0
    U.add_box("Sop_Abrigo",  (3.5, 2.5, 2.50), (sop_x, sop_y, L2_Z+1.25), U.M_WALL,  SOP)
    U.add_box("Sop_Telhado", (3.7, 2.7, 0.08), (sop_x, sop_y, L2_Z+2.54), U.M_ROOF,  SOP)
    for ii in range(2):
        U.add_box(f"Soprador_{ii+1}", (0.70, 0.42, 0.58),
                  (sop_x-0.6, sop_y-0.45+ii*0.90, L2_Z+0.29), U.M_STEEL, SOP)
        U.add_cyl(f"Sop_Silenc_{ii}", 0.12, 0.35,
                  (sop_x-0.6, sop_y-0.45+ii*0.90, L2_Z+0.90),
                  U.M_STEEL, SOP, segs=12)

    # ── Painel CLP ────────────────────────────────────────────────────────────
    clp_y = L2_TY + TK_R + 0.5   # dentro de P2, sul dos tanques L2
    U.add_box("CLP_Armario", (0.80, 0.30, 2.00), (X_OFF + TW-1.0, clp_y, L2_Z+1.00), U.M_PANEL, CLP)
    U.add_box("CLP_Porta",   (0.78, 0.02, 1.95), (X_OFF + TW-1.0, clp_y-0.15, L2_Z+0.975), U.M_STEEL, CLP)

    # ── UPS 600 VA ────────────────────────────────────────────────────────────
    U.add_box("UPS", (0.42, 0.28, 0.60), (X_OFF + TW-1.0, clp_y+1.0, L2_Z+0.30), U.M_PANEL, CLP)

    # ── Gerador 8–10 kVA + QTA ───────────────────────────────────────────────
    # Posicionado no corredor de serviço de P3 (Y≈24.5, entre galpão e zona T7/RAS)
    gen_x = X_OFF + TW - 3.5
    gen_y = 24.5
    U.add_box("Gen_Abrigo", (3.0, 2.0, 2.20), (gen_x, gen_y, P3_Z+1.10), U.M_WALL,  ENG)
    U.add_box("Gen_Corpo",  (1.50, 0.75, 0.85), (gen_x, gen_y, P3_Z+0.425), U.M_GEN, ENG)
    U.add_cyl("Gen_Exaust",  0.085, 0.65, (gen_x+0.6, gen_y, P3_Z+1.28), U.M_STEEL, ENG)
    U.add_box("QTA",        (0.60, 0.28, 1.20), (gen_x-1.8, gen_y, P3_Z+0.60), U.M_PANEL, ENG)

    # ── Poço artesiano ────────────────────────────────────────────────────────
    U.add_box("Poco_Casa",     (1.40, 1.40, 1.60), (X_OFF + 15.0, TL+2.6, Z_N+0.80),  U.M_CONC,  POC)
    U.add_cyl("Poco_Tubo",      0.10, 3.20,         (X_OFF + 15.0, TL+2.6, Z_N+2.40),  U.M_STEEL, POC)
    U.add_cyl("Poco_Cavalete",  0.05, 1.00,         (X_OFF + 15.0, TL+0.5, Z_N-0.50),
              U.M_STEEL, POC, rot=(math.pi/2, 0, 0))
    U.add_box("Poco_Medidor",  (0.20, 0.15, 0.25), (X_OFF + 15.0, TL+0.5, Z_N-0.10),  U.M_STEEL, POC)

    # ── Rampa leste: P3 (base) → P2 ─────────────────────────────────────────
    # Corredor Y=40–42, dZ=1,0 m, run=2 m → 50 % de inclinação (acesso de serviço)
    me1 = bpy.data.meshes.new("Rampa_P3_L2")
    rv1 = [(X_OFF + TW-5.0, P3_Y1, P3_Z), (X_OFF + TW, P3_Y1, P3_Z),
           (X_OFF + TW,     L2_Y0, L2_Z), (X_OFF + TW-5.0, L2_Y0, L2_Z)]
    me1.from_pydata(rv1, [], [(0, 1, 2, 3)])
    me1.update()
    U.put_mat(U.new_obj("Rampa_P3_L2", me1), U.M_CONC)
    U.to_col(bpy.data.objects["Rampa_P3_L2"], ACS)

    # Rampa L2→L1 removida: L1_Z = L2_Z = 6.0 (mesmo patamar P2), sem desnível.

    # ── Portão principal + calçada ────────────────────────────────────────────
    U.add_box("Portao_Princ",   (0.10, 5.0, 2.20),
              (X_OFF + TW+0.1, TL/2, L2_Z+1.10), U.M_STEEL, ACS)
    U.add_box("Calcada_Acesso", (TW-2.0, 5.0, 0.10),
              (X_OFF + TW/2, TL/2, L2_Z-0.05), U.M_CONC, ACS)

    # ── Muretas de contenção H=0.6 m (borda sul dos patamares reais) ────────
    # Mureta_56 (L1_Y0) removida: L1_Z=L2_Z → sem desnível em Y=56
    for (yb, zb) in [(L2_Y0, L2_Z), (P3_Y0, P3_Z)]:
        U.add_box(f"Mureta_{int(yb)}", (TW, 0.25, 0.60),
                  (X_OFF + TW/2, yb, zb+0.30), U.M_CONC, ACS)

    # ── Descarte de lodo RAS → irrigação (dentro de P3: zona RAS → zona galpão)
    # Tubulação enterrada 60 cm abaixo do piso, segue para saída sul do lote
    U.seg("P_Lodo_desc", (X_OFF + 22.0, 27.0, P3_Z - 0.60),
          (X_OFF + 15.0, P3_Y0, P3_Z - 0.90), 0.040, U.M_PVC, LDO)
