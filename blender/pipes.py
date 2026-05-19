import utils as U
from constants import (TW, TL, Z_N,
                       L1_Z, L1_Y1, L1_TY,
                       L2_Z, L2_Y0, L2_Y1, L2_TY,
                       P3_Z, P3_Y0, P3_Y1,
                       TK_X, TK_R, T7_Y,
                       RAS_Y, RAS_Z, RAS_DX, RAS_PX,
                       TRENCH_X, L1_CORR, L2_CORR, X_OFF)

# Cotas de tubulações enterradas (60 cm abaixo do piso de cada patamar)
# L1_Z = L2_Z = 6.0  →  ZP1 = ZP2 = 5.41  (plataforma P2 unificada)
ZP1 = L1_Z - 0.59   # 5.41 — abaixo do fundo dos tanques L1 e L2 (L1_Z=L2_Z=6.0)
ZP2 = L2_Z - 0.59   # 5.41 — mesmo nível que ZP1
ZP3 = P3_Z - 0.59   # 4.41 — abaixo do piso P3 (T7, RAS e galpão no mesmo nível)

# Diâmetros nominais
R_FD   = 0.055   # Ø110 — dreno de fundo
R_LAT  = 0.080   # Ø160 — coleta superficial
R_RET  = 0.045   # Ø90  — retorno pressurizado
R_POC  = 0.050   # Ø100 — água de poço
R_RING = 0.038   # Ø75  — ring main aeração
R_AR   = 0.025   # Ø50  — ramal aeração por tanque


def build_pipes():
    DRN  = "Tubulacoes/Tub_Drenagem"   # drenos de fundo + coleta superficial
    RET  = "Tubulacoes/Tub_Retorno"    # retorno pressurizado RAS → tanques
    POC  = "Tubulacoes/Tub_Poco"       # água do poço
    LDO  = "Tubulacoes/Tub_Lodo"       # descarte de lodo
    RING = "Aeracao/Aer_RingMain"      # tronco + cabeçalhos do ring main
    RAM  = "Aeracao/Aer_Ramais"        # ramais curtos por tanque

    # ══════════════════════════════════════════════════════════════════════════
    # DRENAGEM — rota: tanque → vala leste (TRENCH_X) → desce por patamar → RAS (P3)
    # Todos enterrados em ZP1/ZP2/ZP3, abaixo do fundo dos tanques → sem colisão
    # ══════════════════════════════════════════════════════════════════════════

    # ── Dreno fundo Ø110 — L1 → vala leste → desce até L2_TY (une com tronco L2) ──
    # L1 e L2 no mesmo patamar P2 (ZP1=ZP2=5.41) → tronco vai sul até L2_TY
    for i, x in enumerate(TK_X):
        U.seg(f"P_FdL1_E{i}", (X_OFF + x, L1_TY, ZP1),
              (X_OFF + TRENCH_X, L1_TY, ZP1), R_FD, U.M_PVC, DRN)
    # Tronco sul: L1_TY → L2_TY — une com o tronco de L2 (P_FdL2_trk)
    U.seg("P_FdL1_trkA", (X_OFF + TRENCH_X, L1_TY, ZP1),
          (X_OFF + TRENCH_X, L2_TY, ZP2), R_FD, U.M_PVC, DRN)

    # ── Dreno fundo Ø110 — L2 (P2) → vala leste → desce a P3 ──────────────
    for i, x in enumerate(TK_X):
        U.seg(f"P_FdL2_E{i}", (X_OFF + x, L2_TY, ZP2),
              (X_OFF + TRENCH_X, L2_TY, ZP2), R_FD, U.M_PVC, DRN)
    U.seg("P_FdL2_trk", (X_OFF + TRENCH_X, L2_TY,  ZP2),
          (X_OFF + TRENCH_X, RAS_Y, RAS_Z + 0.10), R_FD, U.M_PVC, DRN)

    # Entrada comum no hidrociclone (RAS)
    U.seg("P_Fd_dec", (X_OFF + TRENCH_X, RAS_Y, RAS_Z + 0.10),
          (X_OFF + RAS_DX, RAS_Y, RAS_Z + 0.10), R_FD, U.M_PVC, DRN)

    # ── T7 dreno → descarte (fora do loop RAS, esgota dentro de P3) ──────────
    # T7 e galpão estão no mesmo patamar P3; dreno vai a ponto de descarte sul
    U.seg("P_FdT7_E",   (X_OFF + TK_X[1], T7_Y,   ZP3),
          (X_OFF + TRENCH_X,    T7_Y,   ZP3), R_FD, U.M_PVC, DRN)
    U.seg("P_FdT7_trk", (X_OFF + TRENCH_X, T7_Y,  ZP3),
          (X_OFF + TRENCH_X,    P3_Y0 + 0.5, ZP3), R_FD, U.M_PVC, DRN)

    # ══════════════════════════════════════════════════════════════════════════
    # COLETA SUPERFICIAL Ø160 — saída lateral dos tanques → percolador
    # ══════════════════════════════════════════════════════════════════════════

    for i, x in enumerate(TK_X):
        U.seg(f"P_LatL1_E{i}", (X_OFF + x, L1_TY, ZP1 + 0.08),
              (X_OFF + TRENCH_X, L1_TY, ZP1 + 0.08), R_LAT, U.M_PVC, DRN)
        U.seg(f"P_LatL2_E{i}", (X_OFF + x, L2_TY, ZP2 + 0.08),
              (X_OFF + TRENCH_X, L2_TY, ZP2 + 0.08), R_LAT, U.M_PVC, DRN)

    # Tronco vala leste → percolador
    # L1 e L2 no mesmo patamar → tronco L1 vai sul até L2_TY e une com tronco L2
    U.seg("P_Lat_trkL1", (X_OFF + TRENCH_X, L1_TY, ZP1 + 0.08),
          (X_OFF + TRENCH_X, L2_TY, ZP2 + 0.08), R_LAT, U.M_PVC, DRN)
    U.seg("P_Lat_trkL2", (X_OFF + TRENCH_X, L2_TY, ZP2 + 0.08),
          (X_OFF + TRENCH_X, RAS_Y, RAS_Z + 0.90), R_LAT, U.M_PVC, DRN)
    U.seg("P_Lat_perc",  (X_OFF + TRENCH_X, RAS_Y, RAS_Z + 0.90),
          (X_OFF + RAS_PX,    RAS_Y, RAS_Z + 0.90), R_LAT, U.M_PVC, DRN)

    # ══════════════════════════════════════════════════════════════════════════
    # RETORNO PRESSURIZADO Ø90 — bomba RAS (P3) → tanques L1 e L2
    # Rota: bomba → leste (TRENCH_X) → norte pela vala → oeste a cada tanque
    # ══════════════════════════════════════════════════════════════════════════

    pump_x, pump_y = X_OFF + 17.6, RAS_Y
    # Bomba → vala leste (segmento compartilhado, dentro de P3)
    U.seg("P_Ret_pump_E", (pump_x, pump_y, ZP3),
          (X_OFF + TRENCH_X, pump_y, ZP3), R_RET, U.M_PVC, RET)

    # Sobe pela vala: P3 → P2
    U.seg("P_Ret_P3P2", (X_OFF + TRENCH_X, pump_y, ZP3),
          (X_OFF + TRENCH_X, L2_Y0, ZP2), R_RET, U.M_PVC, RET)

    # L2: ramal norte dentro de P2 até L2_TY, depois ramal oeste
    U.seg("P_RetL2_trkN", (X_OFF + TRENCH_X, L2_Y0,  ZP2),
          (X_OFF + TRENCH_X, L2_TY, ZP2), R_RET, U.M_PVC, RET)
    for i, x in enumerate(TK_X):
        U.seg(f"P_RetL2_W{i}", (X_OFF + TRENCH_X, L2_TY, ZP2),
              (X_OFF + x, L2_TY, ZP2), R_RET, U.M_PVC, RET)

    # L1: tronco norte desde L2_TY (L1/L2 no mesmo patamar) até L1_TY
    # L1_Y0 eliminado como ponto intermediário — trecho contínuo de L2_TY a L1_TY
    U.seg("P_RetL1_trkN", (X_OFF + TRENCH_X, L2_TY,  ZP2),
          (X_OFF + TRENCH_X, L1_TY, ZP1), R_RET, U.M_PVC, RET)
    for i, x in enumerate(TK_X):
        U.seg(f"P_RetL1_W{i}", (X_OFF + TRENCH_X, L1_TY, ZP1),
              (X_OFF + x, L1_TY, ZP1), R_RET, U.M_PVC, RET)

    # T7: ramal norte dentro de P3 até T7_Y, depois oeste até tanque
    U.seg("P_RetT7_trkN", (X_OFF + TRENCH_X, pump_y, ZP3),
          (X_OFF + TRENCH_X, T7_Y,  ZP3), R_RET, U.M_PVC, RET)
    U.seg("P_RetT7_W",    (X_OFF + TRENCH_X, T7_Y,  ZP3),
          (X_OFF + TK_X[1],  T7_Y, ZP3), R_RET, U.M_PVC, RET)

    # ══════════════════════════════════════════════════════════════════════════
    # ÁGUA DO POÇO Ø100 — externo N → T7 (P3)
    # ══════════════════════════════════════════════════════════════════════════

    # L1_Y1 = L2_Y1 = TL → segmento P_Poco_P1P2 seria comprimento zero; removido
    U.seg("P_Poco_ext",  (X_OFF + 15.0, TL + 2.5, Z_N - 0.60),
          (X_OFF + 15.0, L1_Y1, ZP1), R_POC, U.M_PVC, POC)
    U.seg("P_Poco_P2P3", (X_OFF + 15.0, L2_Y1, ZP2),
          (X_OFF + 15.0, P3_Y1, ZP3), R_POC, U.M_PVC, POC)
    U.seg("P_Poco_T7",   (X_OFF + 15.0, P3_Y1, ZP3),
          (X_OFF + TK_X[1], T7_Y + TK_R + 0.1, ZP3), R_POC, U.M_PVC, POC)

    # ══════════════════════════════════════════════════════════════════════════
    # RING MAIN AERAÇÃO Ø75
    # Tronco N-S em TRENCH_X percorre os 2 patamares (P2 e P3) + 1 transição.
    # Cabeçalhos de distribuição nos corredores L1_CORR e L2_CORR.
    # Ramais curtos perpendiculares à parede sul de cada tanque.
    # Nenhum tubo atravessa o interior dos tanques.
    # ══════════════════════════════════════════════════════════════════════════

    # Tronco principal N-S (leste de tudo) — P2 unificado (L1+L2) + ramal P3
    # Sopradores em L2 → anel alimenta L2 e L1 (mesmo patamar P2) e P3 (sul)
    # P_Ring_P2 cobre todo P2: L2_Y0=42 → L2_Y1=TL=68.37  (inclui zona L1)
    # P_Ring_P2_P1 e P_Ring_P1 removidos — eram redundantes com L1_Z=L2_Z
    U.seg("P_Ring_P2",    (X_OFF + TRENCH_X, L2_Y0,  L2_Z + 0.02),
          (X_OFF + TRENCH_X, L2_Y1, L2_Z + 0.02), R_RING, U.M_PVC, RING)
    # Ramal sul: P2 → P3 (desce pelo talude P3→P2)
    U.seg("P_Ring_P2_P3", (X_OFF + TRENCH_X, L2_Y0,  L2_Z + 0.02),
          (X_OFF + TRENCH_X, P3_Y1, P3_Z + 0.02), R_RING, U.M_PVC, RING)
    U.seg("P_Ring_P3",    (X_OFF + TRENCH_X, P3_Y1,  P3_Z + 0.02),
          (X_OFF + TRENCH_X, P3_Y0, P3_Z + 0.02), R_RING, U.M_PVC, RING)

    # Cabeçalho P1 no corredor sul (Y = L1_CORR ≈ 57.5, 1 m ao sul da borda L1)
    U.seg("P_Ring_L1_hdr", (X_OFF + TRENCH_X,       L1_CORR, L1_Z + 0.02),
          (X_OFF + TK_X[0] - TK_R, L1_CORR, L1_Z + 0.02), R_RING, U.M_PVC, RING)
    # Ramais curtos S→N até a parede sul de cada tanque L1
    for i, x in enumerate(TK_X):
        U.seg(f"P_Ar_L1_{i}", (X_OFF + x, L1_CORR,       L1_Z + 0.02),
              (X_OFF + x, L1_TY - TK_R, L1_Z + 0.02), R_AR, U.M_PVC, RAM)

    # Cabeçalho P2 no corredor inter-fileiras (Y = L2_CORR ≈ 43.3)
    # Borda N de T7 = T7_Y+TK_R=35.7; Borda S de L2 = L2_TY-TK_R=44.3 → clearance ✓
    U.seg("P_Ring_L2_hdr", (X_OFF + TRENCH_X,       L2_CORR, L2_Z + 0.02),
          (X_OFF + TK_X[0] - TK_R, L2_CORR, L2_Z + 0.02), R_RING, U.M_PVC, RING)
    # Ramais S→N até parede sul de cada tanque L2
    for i, x in enumerate(TK_X):
        U.seg(f"P_Ar_L2_{i}", (X_OFF + x, L2_CORR,       L2_Z + 0.02),
              (X_OFF + x, L2_TY - TK_R, L2_Z + 0.02), R_AR, U.M_PVC, RAM)

    # Ramal N→S até parede norte de T7 (único tanque em P3, via corredor P3)
    T7_CORR = T7_Y + TK_R + 0.5   # corredor norte de T7 ≈ 36.2
    U.seg("P_Ring_T7_hdr", (X_OFF + TRENCH_X, T7_CORR, P3_Z + 0.02),
          (X_OFF + TK_X[1], T7_CORR, P3_Z + 0.02), R_RING, U.M_PVC, RING)
    U.seg("P_Ar_T7", (X_OFF + TK_X[1], T7_CORR, P3_Z + 0.02),
          (X_OFF + TK_X[1], T7_Y + TK_R, P3_Z + 0.02), R_AR, U.M_PVC, RAM)

    # Sopradores (em L2) → entrada no tronco ring main
    # sop_x = TW-4.5 = 25.5, sop_y = L2_TY-2.0 = 46.0 (mesmo que infra.py)
    U.seg("P_Sop_Ring", (X_OFF + TW - 4.5, L2_TY - 2.0, L2_Z + 0.30),
          (X_OFF + TRENCH_X, L2_TY, L2_Z + 0.02), R_RING, U.M_PVC, RING)
