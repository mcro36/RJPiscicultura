import bpy
import math
import utils as U
from constants import (TK_R, TK_THICK, TK_WALL, TK_WD, TK_X,
                       L1_Z, L1_TY, L2_Z, L2_TY, P3_Z, T7_Y, X_OFF)


def build_tank(tag, cx, cy, base_z, col_name):
    segs = 64

    # Anel estrutural galvanizado — tubo aberto (sem tampo), interior visível
    U.add_tube(f"{tag}_frame", TK_R + TK_THICK, TK_R, TK_WALL,
               (cx, cy, base_z), U.M_STEEL, col_name, segs=segs)

    # Liner HDPE — parede 3 cm, aberto no topo
    U.add_tube(f"{tag}_liner", TK_R, TK_R - 0.03, TK_WALL,
               (cx, cy, base_z), U.M_HDPE, col_name, segs=segs)

    # Fundo cônico 5 % (r2=largo na borda/topo, r1=pequeno no dreno/fundo)
    # Piso cai do bordo (base_z) até o dreno central (base_z − 0.185 m)
    cone_d = TK_R * 0.05           # 0.185 m — queda vertical
    cone_cz = base_z - cone_d / 2  # centro geométrico do cone
    U.add_cone(f"{tag}_cone", 0.14, TK_R - 0.04, cone_d,
               (cx, cy, cone_cz), U.M_HDPE, col_name, segs=segs)

    # Bocal/standpipe do dreno central PVC Ø110 mm
    # Sobe do fundo do cone (base_z − cone_d) até a borda superior do tanque
    pipe_h  = TK_WALL + cone_d
    pipe_cz = base_z - cone_d + pipe_h / 2
    U.add_cyl(f"{tag}_drain_c", 0.055, pipe_h,
              (cx, cy, pipe_cz), U.M_PVC, col_name, segs=12)

    # Coletas laterais superiores — 2 saídas Ø160 mm opostas
    for ang in (0, 180):
        r  = math.radians(ang)
        ox = cx + (TK_R - 0.05) * math.cos(r)
        oy = cy + (TK_R - 0.05) * math.sin(r)
        U.add_cyl(f"{tag}_lat_{ang}", 0.08, 0.25,
                  (ox, oy, base_z + TK_WD - 0.12), U.M_PVC, col_name,
                  rot=(math.pi/2, 0, r), segs=12)

    # Bocais de entrada tangencial — 2 × Ø63 mm
    for ang in (60, 240):
        r  = math.radians(ang)
        bx = cx + (TK_R - 0.08) * math.cos(r)
        by = cy + (TK_R - 0.08) * math.sin(r)
        U.add_cyl(f"{tag}_inlet_{ang}", 0.035, 0.28,
                  (bx, by, base_z + TK_WD * 0.55), U.M_PVC, col_name,
                  rot=(math.pi/2, 0, r), segs=12)


def build_all_tanks():
    # Patamar 1 — T1, T2, T3
    for i, x in enumerate(TK_X):
        build_tank(f"T{i+1}", X_OFF + x, L1_TY, L1_Z, "Tanques/Tanques_L1")

    # Patamar 2 — T4, T5, T6
    for i, x in enumerate(TK_X):
        build_tank(f"T{i+4}", X_OFF + x, L2_TY, L2_Z, "Tanques/Tanques_L2")

    # T7 — depuração + buffer térmico (Patamar 3)
    build_tank("T7", X_OFF + TK_X[1], T7_Y, P3_Z, "Tanques/Tanques_P3")
