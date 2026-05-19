import bpy
import math
import utils as U
from constants import (TW, TL, Z_S, Z_N, SLOPE,
                       L1_Y0, L1_Y1, L1_Z,
                       L2_Y0, L2_Y1, L2_Z,
                       P3_Y0, P3_Y1, P3_Z, X_OFF,
                       L15H2_VERTS, L15H1_VERTS)

# ── Polígono da estrada rural (coords Blender locais, via transformação afim) ──
# Side A — margem exterior (sul/leste): V1→V3→V4→V5→V6→V7
_ROAD_A = [
    ( -3.70,   -0.56),
    (  8.86,   -9.33),
    ( 23.46,  -10.25),
    ( 38.17,   -7.61),
    ( 50.13,   -3.86),
    ( 42.22,  104.28),
]
# Side B — margem interior (norte/oeste): V2→V13→V12→V11→V10→V9→V8
_ROAD_B = [
    ( -6.44,   -7.29),
    (  4.10,   -3.45),
    ( 17.37,   -4.32),
    ( 33.62,   -2.65),
    ( 44.22,   -0.16),
    ( 44.18,    3.95),
    ( 37.94,  103.97),
]


def _terrain_z(y):
    return Z_S + y * SLOPE


def _cut_z(y):
    """Cota após corte/aterro para Y dado.
    2 patamares (P3 base e P2 topo), 1 talude a 45° entre eles.
    P2 (topo) vai até a borda norte.
    P3 (base) começa em Y=4.
    """
    # Patamares planos
    if L2_Y0 <= y <= L2_Y1:  # P2 topo (antigos L1 e L2 juntos)
        return L2_Z
    if P3_Y0 <= y <= P3_Y1:  # P3 base
        return P3_Z

    # Talude da rua para o patamar base (Y:0 → Y:1)
    if 0.0 <= y < P3_Y0:
        t = y / P3_Y0
        z_rua = 4.0  # cota da estrada (conforme constants.py)
        return z_rua + t * (P3_Z - z_rua)

    # Talude 45° entre P3 e P2 — dZ=1,0 m, run=2,0 m
    if P3_Y1 < y < L2_Y0:   # talude P3 → P2
        t = (y - P3_Y1) / (L2_Y0 - P3_Y1)
        return P3_Z + t * (L2_Z - P3_Z)

    return None


def build_terrain():
    NX, NY = 61, 137       # resolução ~0.5 m

    verts, faces = [], []
    for iy in range(NY):
        for ix in range(NX):
            x  = ix * TW / (NX - 1)
            y  = iy * TL / (NY - 1)
            # Usa o terreno SRTM real (não o modelo linear) para decidir corte/aterro.
            # zn_real reflete a variação O→L do lote; zn_lin mantido apenas como fallback
            # para Y fora do alcance do SRTM.
            zn = _terrain_z_natural(x, y)   # ← SRTM real (substituiu _terrain_z)
            zc = _cut_z(y)
            # Mantém a cota do patamar mesmo em áreas de aterro
            z  = zc if zc is not None else zn
            z  = max(z, Z_S)
            verts.append((x, y, z))

    for iy in range(NY - 1):
        for ix in range(NX - 1):
            a = iy * NX + ix
            faces.append((a, a+1, a+NX+1, a+NX))

    me = bpy.data.meshes.new("Terreno")
    me.from_pydata(verts, [], faces)
    me.update()
    obj = U.new_obj("Terreno", me)
    U.put_mat(obj, U.M_SOIL)
    U.to_col(obj, "Terreno")

    # Faixa de grama sobreposta nos 3 patamares
    for (y0, y1, z) in [
        (L2_Y0, L2_Y1, L2_Z + 0.01),
        (P3_Y0, P3_Y1, P3_Z + 0.01),
    ]:
        me2 = bpy.data.meshes.new(f"Grama_{z:.2f}")
        gv  = [(0, y0, z), (TW, y0, z), (TW, y1, z), (0, y1, z)]
        me2.from_pydata(gv, [], [(0, 1, 2, 3)])
        me2.update()
        go = U.new_obj(f"Grama_{z:.2f}", me2)
        U.put_mat(go, U.M_GRASS)
        U.to_col(go, "Terreno")


# ── Dados reais de elevação SRTM30 (NASA) — área estendida 20 m além do lote ─
# Grade 8 colunas × 12 linhas cobrindo X: [-20, TW+20] e Y: [-20, TL+20]
# Linhas: sul-ext (row 0) → norte-ext (row 11)
# Colunas: oeste-ext (col 0) → leste-ext (col 7)
# Fonte: OpenTopoData /v1/srtm30m — coordenadas GPS reais do lote em BH
# u_start = -20/TW = -0.6667,  u_end = 1+20/TW = 1.6667
# v_start = -20/TL = -0.2926,  v_end = 1+20/TL = 1.2926
_ELEV_GRID = [
    [830, 829, 827, 826, 825, 823, 822, 820],  # row  0 — 20 m ao sul
    [831, 830, 829, 827, 826, 824, 823, 821],  # row  1
    [833, 831, 830, 828, 827, 826, 824, 822],  # row  2  ← borda sul do lote
    [834, 833, 831, 830, 828, 827, 825, 823],  # row  3
    [836, 834, 832, 831, 829, 827, 826, 825],  # row  4
    [836, 835, 833, 831, 830, 828, 827, 825],  # row  5
    [836, 835, 833, 832, 831, 829, 827, 826],  # row  6
    [837, 835, 834, 832, 831, 829, 828, 826],  # row  7
    [836, 835, 833, 832, 831, 830, 828, 826],  # row  8
    [836, 834, 833, 832, 831, 830, 828, 826],  # row  9  ← borda norte do lote
    [834, 833, 833, 832, 831, 829, 828, 826],  # row 10
    [833, 832, 832, 831, 830, 829, 828, 827],  # row 11 — 20 m ao norte
]
_ELEV_NU    = 8
_ELEV_NV    = 12
_ELEV_MIN   = 820.0
_ELEV_MAX   = 837.0
# Limites normalizados da grade (u/v fora de [0,1] = fora do lote)
_U_START    = -20.0 / TW        # -0.6667
_U_END      =  1.0 + 20.0 / TW  #  1.6667
_V_START    = -20.0 / TL        # -0.2926
_V_END      =  1.0 + 20.0 / TL  #  1.2926


def _terrain_z_natural(lx, y):
    """Interpolação bilinear dos dados reais SRTM30 — área estendida.

    lx ∈ [-20, TW+20]  — X local (pode sair do lote)
    y  ∈ [-20, TL+20]  — Y global (pode sair do lote)

    Gradientes reais medidos no lote:
      E–O: ~4 m (oeste é mais alto que leste)
      S–N: ~3 m (norte é mais alto que sul)
    """
    u  = lx / TW
    v  = y  / TL

    # Mapeia u/v para índice da grade estendida
    ug = (u - _U_START) / (_U_END - _U_START) * (_ELEV_NU - 1)
    vg = (v - _V_START) / (_V_END - _V_START) * (_ELEV_NV - 1)

    iu0 = max(0, min(_ELEV_NU - 2, int(ug)))
    iv0 = max(0, min(_ELEV_NV - 2, int(vg)))
    du  = max(0.0, min(1.0, ug - iu0))
    dv  = max(0.0, min(1.0, vg - iv0))

    e00 = _ELEV_GRID[iv0    ][iu0    ]
    e10 = _ELEV_GRID[iv0    ][iu0 + 1]
    e01 = _ELEV_GRID[iv0 + 1][iu0    ]
    e11 = _ELEV_GRID[iv0 + 1][iu0 + 1]

    elev = (e00 * (1 - du) * (1 - dv) +
            e10 *      du  * (1 - dv) +
            e01 * (1 - du) *      dv  +
            e11 *      du  *      dv  )

    return Z_S + (elev - _ELEV_MIN) / (_ELEV_MAX - _ELEV_MIN) * (Z_N - Z_S)


def _find_y_for_z(lx, zc, n=400):
    """Varre Y de 0 a TL — mantido para compatibilidade."""
    return _find_y_for_z_ext(lx, zc, 0.0, TL, n)


def _find_y_for_z_ext(lx, zc, y0, y1, n=400):
    """Varre Y de y0 a y1 e retorna o Y onde terrain_z_natural == zc."""
    py = y0
    pz = _terrain_z_natural(lx, y0)
    step = (y1 - y0) / n
    for i in range(1, n + 1):
        cy = y0 + i * step
        cz = _terrain_z_natural(lx, cy)
        if (pz - zc) * (cz - zc) < 0:
            t = (zc - pz) / (cz - pz)
            return py + t * step
        py, pz = cy, cz
    return None


def build_natural_terrain():
    """Terreno natural (sem corte/aterro) posicionado ao leste do lote.
    A malha usa _terrain_z_natural(lx, y) com dados reais SRTM30m.
    As curvas de nível são traçadas por varredura, não como linhas retas.

    Coleções geradas:
      Terreno_Natural/Nat_Lote    — malha da área do lote (lx 0..TW, y 0..TL)
      Terreno_Natural/Nat_Entorno — 4 faixas de 20 m ao redor do lote
      Terreno_Natural             — curvas de nível + borda vermelha do lote
    """
    EXPAND = 20.0
    LX0, LX1 = -EXPAND, TW + EXPAND    # -20 .. 50
    LY0, LY1 = -EXPAND, TL + EXPAND    # -20 .. 88.37

    # ── Malha do ENTORNO — 4 faixas de 20 m, resolução ~1 m → Nat_Entorno ────
    # Faixas não se sobrepõem ao lote: Sul/Norte cobrem largura total, O/L só y∈[0,TL]
    # Strip sul para em y = -6.5 (borda exterior do acostamento da rua)
    # A rua ocupa y ∈ [-6, 0]; acostamento sul chega a -6.5 → entorno termina ali.
    _strips = [
        # (lx0,    lx1,       y0,    y1,    nx,  ny )
        (LX0,    LX1,       LY0,  -6.5,   71,  14),  # sul — para antes da rua
        (LX0,    LX1,       TL,    LY1,   71,  21),  # norte
        (LX0,    0.0,       0.0,   TL,    21,  69),  # oeste
        (TW,     LX1,       0.0,   TL,    21,  69),  # leste
    ]
    env_v, env_f = [], []
    for (lx0, lx1, y0, y1, snx, sny) in _strips:
        base = len(env_v)
        for iy in range(sny):
            for ix in range(snx):
                lx = lx0 + ix * (lx1 - lx0) / (snx - 1)
                y  = y0  + iy * (y1  - y0 ) / (sny - 1)
                env_v.append((X_OFF + lx, y, _terrain_z_natural(lx, y)))
        for iy in range(sny - 1):
            for ix in range(snx - 1):
                a = base + iy * snx + ix
                env_f.append((a, a + 1, a + snx + 1, a + snx))

    me_e = bpy.data.meshes.new("Terreno_Natural_Entorno")
    me_e.from_pydata(env_v, [], env_f)
    me_e.update()
    obj_e = U.new_obj("Terreno_Natural_Entorno", me_e)
    U.put_mat(obj_e, U.M_SOIL)
    U.to_col(obj_e, "Loteamento/Entorno")

    # ── Curvas de nível — divididas entre Nat_Lote e Nat_Entorno ────────────────
    # Um ponto pertence ao lote se lx ∈ [0, TW] E y ∈ [0, TL].
    # Cada curva é percorrida e quebrada em sub-segmentos contíguos por região.
    NX_CV = 100
    LIFT  = 0.06

    z_max_cv = Z_N   # = 10
    intervals = []
    zz = 0.0
    while zz <= z_max_cv + 0.01:
        intervals.append(round(zz, 2))
        zz = round(zz + 0.5, 2)

    # 4 acumuladores: [lote_principal, lote_secundária, ext_principal, ext_secundária]
    lot_mv, lot_me = [], []   # lote  — curva principal
    lot_sv, lot_se = [], []   # lote  — curva secundária
    ext_mv, ext_me = [], []   # entorno — curva principal
    ext_sv, ext_se = [], []   # entorno — curva secundária

    def _flush_seg(seg, vv, ee):
        """Adiciona um sub-segmento de pontos aos acumuladores vv/ee."""
        if len(seg) < 2:
            return
        base = len(vv)
        vv.extend(seg)
        for k in range(len(seg) - 1):
            ee.append((base + k, base + k + 1))

    for zc in intervals:
        is_main = (round(zc) == zc)
        lv, le = (lot_mv, lot_me) if is_main else (lot_sv, lot_se)
        ev, ee = (ext_mv, ext_me) if is_main else (ext_sv, ext_se)

        # Acumula pontos separados por região
        cur_lot, cur_ext = [], []
        for ix in range(NX_CV):
            lx = LX0 + ix * (LX1 - LX0) / (NX_CV - 1)
            y  = _find_y_for_z_ext(lx, zc, LY0, LY1)
            if y is None:
                # Interrupção → fecha segmentos em curso
                _flush_seg(cur_lot, lv, le)
                _flush_seg(cur_ext, ev, ee)
                cur_lot, cur_ext = [], []
                continue

            wx = X_OFF + lx
            z  = _terrain_z_natural(lx, y) + LIFT
            pt = (wx, y, z)

            if 0.0 <= lx <= TW and 0.0 <= y <= TL:
                # Ponto dentro do lote: remove curva em toda a extensão
                if y >= 0.0:
                    # Área do nat_gradeado: ignora a curva para não sobrepor
                    if cur_lot: _flush_seg(cur_lot, lv, le)
                    if cur_ext: _flush_seg(cur_ext, ev, ee)
                    cur_lot, cur_ext = [], []
                    continue

                if cur_ext:
                    _flush_seg(cur_ext, ev, ee)
                    cur_ext = []
                cur_lot.append(pt)
            else:
                # Ponto no entorno — fecha segmento do lote se havia um
                if cur_lot:
                    _flush_seg(cur_lot, lv, le)
                    cur_lot = []
                cur_ext.append(pt)

        _flush_seg(cur_lot, lv, le)
        _flush_seg(cur_ext, ev, ee)

    def _make_cv(name, vv, ee, color, col):
        if not vv:
            return
        me_c = bpy.data.meshes.new(name)
        me_c.from_pydata(vv, ee, [])
        me_c.update()
        obj_c = U.new_obj(name, me_c)
        mat = bpy.data.materials.get(f"Mat_{name}")
        if not mat:
            mat = bpy.data.materials.new(f"Mat_{name}")
            mat.use_nodes = True
            mat.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = color
        obj_c.data.materials.append(mat)
        U.to_col(obj_c, col)

    DARK  = (0.40, 0.18, 0.04, 1.0)   # marrom-terra escuro — principal
    LIGHT = (0.68, 0.54, 0.38, 1.0)   # bege — secundária

    _make_cv("Curvas_Lote_Princ",   lot_mv, lot_me, DARK,  "Loteamento/Lote_16")
    _make_cv("Curvas_Lote_Sec",     lot_sv, lot_se, LIGHT, "Loteamento/Lote_16")
    _make_cv("Curvas_Entorno_Princ", ext_mv, ext_me, DARK,  "Loteamento/Entorno")
    _make_cv("Curvas_Entorno_Sec",   ext_sv, ext_se, LIGHT, "Loteamento/Entorno")

    # ── Borda do lote (caixilho vermelho — apenas o lote, não a área estendida)
    bv = []
    NB = 60
    for ix in range(NB):    # sul
        lx = ix * TW / (NB - 1)
        bv.append((X_OFF + lx, 0.0, _terrain_z_natural(lx, 0.0) + LIFT))
    for iy in range(NB):    # leste
        y = iy * TL / (NB - 1)
        bv.append((X_OFF + TW, y, _terrain_z_natural(TW, y) + LIFT))
    for ix in range(NB):    # norte (invertido)
        lx = TW - ix * TW / (NB - 1)
        bv.append((X_OFF + lx, TL, _terrain_z_natural(lx, TL) + LIFT))
    for iy in range(NB):    # oeste (invertido)
        y = TL - iy * TL / (NB - 1)
        bv.append((X_OFF + 0.0, y, _terrain_z_natural(0.0, y) + LIFT))

    be = [(i, i + 1) for i in range(len(bv) - 1)] + [(len(bv) - 1, 0)]
    me_b = bpy.data.meshes.new("Lote_Borda_Nat")
    me_b.from_pydata(bv, be, [])
    me_b.update()
    obj_b = U.new_obj("Lote_Borda_Nat", me_b)
    mat_borda = bpy.data.materials.get("Mat_Borda")
    if not mat_borda:
        mat_borda = bpy.data.materials.new("Mat_Borda")
        mat_borda.use_nodes = True
        mat_borda.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = \
            (1.0, 0.15, 0.15, 1.0)
    obj_b.data.materials.append(mat_borda)
    U.to_col(obj_b, "Loteamento")


def _resample_polyline(pts, n):
    """Reamostragem por comprimento de arco — retorna n pontos igualmente espaçados."""
    segs = [math.hypot(pts[i+1][0]-pts[i][0], pts[i+1][1]-pts[i][1])
            for i in range(len(pts)-1)]
    total = sum(segs)
    cum = [0.0]
    for s in segs:
        cum.append(cum[-1] + s)
    result = []
    for k in range(n):
        d = k / (n - 1) * total
        for j in range(len(segs)):
            if cum[j] <= d <= cum[j+1]:
                t = (d - cum[j]) / segs[j] if segs[j] > 1e-12 else 0.0
                x = pts[j][0] + t * (pts[j+1][0] - pts[j][0])
                y = pts[j][1] + t * (pts[j+1][1] - pts[j][1])
                result.append((x, y))
                break
    return result


def build_road():
    """Estrada rural — polígono GPS via transformação afim (relatório 2026-05).

    Side A (margem exterior sul/leste)  : V1→V3→V4→V5→V6→V7
    Side B (margem interior norte/oeste): V2→V13→V12→V11→V10→V9→V8
    Ambas reamostradas para N=60 pontos (arc-length) e unidas como ribbon mesh.
    Superfície = terreno natural SRTM − 0.30 m (corte leve).
    """
    COL = "Infraestrutura/Infra_Estrada"
    DZ  = -0.30
    N   = 60

    a_pts = _resample_polyline(_ROAD_A, N)
    b_pts = _resample_polyline(_ROAD_B, N)

    # ── Leito asfáltico ───────────────────────────────────────────────────────
    verts = []
    for lx, y in a_pts:
        verts.append((X_OFF + lx, y, _terrain_z_natural(lx, y) + DZ))
    for lx, y in b_pts:
        verts.append((X_OFF + lx, y, _terrain_z_natural(lx, y) + DZ))
    faces = [(i, i+1, N+i+1, N+i) for i in range(N-1)]

    me = bpy.data.meshes.new("Estrada_Leito")
    me.from_pydata(verts, [], faces)
    me.update()
    obj = U.new_obj("Estrada_Leito", me)
    mat_road = bpy.data.materials.get("Mat_Asfalto")
    if not mat_road:
        mat_road = bpy.data.materials.new("Mat_Asfalto")
        mat_road.use_nodes = True
        bsdf = mat_road.node_tree.nodes["Principled BSDF"]
        bsdf.inputs["Base Color"].default_value = (0.18, 0.18, 0.18, 1.0)
        bsdf.inputs["Roughness"].default_value  = 0.92
    obj.data.materials.append(mat_road)
    U.to_col(obj, COL)

    # ── Faixa central amarela (ribbon de 0.12 m) ──────────────────────────────
    lv, lf = [], []
    for i in range(N):
        lxa, ya = a_pts[i]
        lxb, yb = b_pts[i]
        lxm, ym = (lxa + lxb) * 0.5, (ya + yb) * 0.5
        # direção de avanço ao longo da estrada
        if i < N - 1:
            ddx = (a_pts[i+1][0] - a_pts[i][0] + b_pts[i+1][0] - b_pts[i][0]) * 0.5
            ddy = (a_pts[i+1][1] - a_pts[i][1] + b_pts[i+1][1] - b_pts[i][1]) * 0.5
        else:
            ddx = (a_pts[i][0] - a_pts[i-1][0] + b_pts[i][0] - b_pts[i-1][0]) * 0.5
            ddy = (a_pts[i][1] - a_pts[i-1][1] + b_pts[i][1] - b_pts[i-1][1]) * 0.5
        ln = math.hypot(ddx, ddy)
        if ln < 1e-9:
            continue
        nx_v, ny_v = -ddy / ln, ddx / ln   # perpendicular (gira 90°)
        hw = 0.06
        zm = _terrain_z_natural(lxm, ym) + DZ + 0.02
        lv.append((X_OFF + lxm - nx_v * hw, ym - ny_v * hw, zm))
        lv.append((X_OFF + lxm + nx_v * hw, ym + ny_v * hw, zm))
    for i in range(len(lv) // 2 - 1):
        a = i * 2
        lf.append((a, a+2, a+3, a+1))
    if lv:
        me_l = bpy.data.meshes.new("Estrada_FaixaCentral")
        me_l.from_pydata(lv, [], lf)
        me_l.update()
        obj_l = U.new_obj("Estrada_FaixaCentral", me_l)
        mat_l = bpy.data.materials.get("Mat_FaixaCentral")
        if not mat_l:
            mat_l = bpy.data.materials.new("Mat_FaixaCentral")
            mat_l.use_nodes = True
            mat_l.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = \
                (0.85, 0.75, 0.02, 1.0)
            mat_l.node_tree.nodes["Principled BSDF"].inputs["Roughness"].default_value = 0.60
        obj_l.data.materials.append(mat_l)
        U.to_col(obj_l, COL)


def build_nat_grading():
    """Aplica os 2 patamares do projeto ao terreno natural do segundo lote.

    Calcula volumes de corte e aterro e imprime no console.

    Regra por célula:
      z_nat > z_plat  →  corte  (remove terra)
      z_nat < z_plat  →  aterro (adiciona terra)
      z_nat = z_nat   →  fora de patamar (talude ou sul do galpão)

    Objetos gerados:
      Terreno_Nat_Gradeado — terreno após aplicar os patamares (malha cinza)
      Terreno_Nat_Aterro   — overlay laranja nos volumes de aterro (leste)
      (ambos em Terreno_Natural/Nat_Gradeado)
    """
    EXPAND = 20.0

    NX, NY     = 61, 137
    cell_w     = TW / (NX - 1)
    cell_h     = TL / (NY - 1)
    cell_area  = cell_w * cell_h

    cut_vol  = 0.0
    fill_vol = 0.0

    # ── Pré-computa grid: z_nat, z_disp, is_fill ─────────────────────────────
    # A malha do patamar assume a cota de projeto sempre que estiver dentro
    # da área do projeto, independentemente se é corte ou aterro.
    grid = []   # (z_nat, z_disp)
    for iy in range(NY):
        for ix in range(NX):
            lx    = ix * cell_w
            y     = iy * cell_h
            z_nat = _terrain_z_natural(lx, y)
            z_cut = _cut_z(y)

            if z_cut is not None:
                diff = z_nat - z_cut   # positivo = corte; negativo = aterro
                if diff > 0:
                    cut_vol += diff * cell_area
                else:
                    fill_vol += (-diff) * cell_area
                z_disp  = z_cut
            else:
                z_disp  = z_nat

            grid.append((z_nat, z_disp))

    # ── Relatório de volumes ──────────────────────────────────────────────────
    net = cut_vol - fill_vol
    print()
    print("  ┌─ Lote_16 — Balanço de Terraplanagem (2 patamares) ──────────┐")
    print(f"  │  Corte  (terra retirada) : {cut_vol:8.1f} m³                   │")
    print(f"  │  Aterro (terra inserida) : {fill_vol:8.1f} m³                   │")
    print(f"  │  Balanço (corte − aterro): {net:+8.1f} m³                   │")
    if net > 0:
        print(f"  │  → Sobra {net:.1f} m³ → bota-fora ou aterro leste           │")
    else:
        print(f"  │  → Déficit {-net:.1f} m³ → importar material externo        │")
    print("  └──────────────────────────────────────────────────────────────┘")
    print()

    # ── Malha do terreno gradeado (O Piso dos Patamares) ─────────────────────
    vg, fg = [], []
    for iy in range(NY):
        for ix in range(NX):
            lx = ix * cell_w
            y  = iy * cell_h
            _, z_disp = grid[iy * NX + ix]
            vg.append((X_OFF + lx, y, z_disp))
    for iy in range(NY - 1):
        for ix in range(NX - 1):
            a = iy * NX + ix
            fg.append((a, a + 1, a + NX + 1, a + NX))

    me_g = bpy.data.meshes.new("Lote_16_gradeado")
    me_g.from_pydata(vg, [], fg)
    me_g.update()
    obj_g = U.new_obj("Lote_16_gradeado", me_g)
    U.put_mat(obj_g, U.M_SOIL)
    U.to_col(obj_g, "Loteamento/Lote_16")

    # ── Taludes de borda (Paredes de conexão com o entorno) ──────────────────
    # Fecha o visual entre a cota do patamar e a cota natural do lote
    vt, ft = [], []

    def add_boundary_segment(ix1, iy1, ix2, iy2):
        z_nat1, z_disp1 = grid[iy1 * NX + ix1]
        z_nat2, z_disp2 = grid[iy2 * NX + ix2]
        
        lx1, y1 = ix1 * cell_w, iy1 * cell_h
        lx2, y2 = ix2 * cell_w, iy2 * cell_h
        
        if abs(z_nat1 - z_disp1) > 0.05 or abs(z_nat2 - z_disp2) > 0.05:
            base = len(vt)
            # Ordem (disp1, disp2, nat2, nat1) para normais corretas (visto de dentro/fora)
            vt.append((X_OFF + lx1, y1, z_disp1)) # 0: Base 1
            vt.append((X_OFF + lx2, y2, z_disp2)) # 1: Base 2
            vt.append((X_OFF + lx2, y2, z_nat2))  # 2: Topo 2
            vt.append((X_OFF + lx1, y1, z_nat1))  # 3: Topo 1
            ft.append((base, base + 1, base + 2, base + 3))

    # Perímetro em sentido anti-horário
    for iy in range(NY - 1): # Oeste
        add_boundary_segment(0, iy, 0, iy + 1)
    for ix in range(NX - 1): # Norte
        add_boundary_segment(ix, NY - 1, ix + 1, NY - 1)
    for iy in range(NY - 1, 0, -1): # Leste
        add_boundary_segment(NX - 1, iy, NX - 1, iy - 1)
    for ix in range(NX - 1, 0, -1): # Sul
        add_boundary_segment(ix, 0, ix - 1, 0)

    if ft:
        me_t = bpy.data.meshes.new("Lote_16_taludes")
        me_t.from_pydata(vt, [], ft)
        me_t.update()
        obj_t = U.new_obj("Lote_16_taludes", me_t)
        U.put_mat(obj_t, U.M_SOIL)
        U.to_col(obj_t, "Loteamento/Lote_16")


def _bilinear_pt(u, v, p00, p10, p11, p01):
    """Interpolação bilinear de ponto XY num quadrilátero irregular.

    Parametrização: u,v ∈ [0,1]
      p00=(u=0,v=0)  p10=(u=1,v=0)  p11=(u=1,v=1)  p01=(u=0,v=1)
    """
    x = (1-u)*(1-v)*p00[0] + u*(1-v)*p10[0] + u*v*p11[0] + (1-u)*v*p01[0]
    y = (1-u)*(1-v)*p00[1] + u*(1-v)*p10[1] + u*v*p11[1] + (1-u)*v*p01[1]
    return x, y


def _quad_area(p00, p10, p11, p01):
    """Área aproximada do quadrilátero via Shoelace (cantos em ordem)."""
    pts = [p00, p10, p11, p01]
    n = len(pts)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += pts[i][0] * pts[j][1]
        area -= pts[j][0] * pts[i][1]
    return abs(area) / 2.0


def _build_lote(col, p00, p10, p11, p01, borda_color, mesh_name,
                nx=36, ny=52, draw_border=True):
    """Gera malha + curvas de nível + (opcional) borda para um lote quadrilátero irregular.

    p00=(u=0,v=0), p10=(u=1,v=0), p11=(u=1,v=1), p01=(u=0,v=1) em coord. locais (lx,y).
    Ordem deve ser não auto-intersectante (verificar antes de chamar).
    draw_border=False: suprime a borda (útil quando a borda é desenhada externamente).
    """
    LIFT = 0.06

    # ── 1. Malha do terreno ──────────────────────────────────────────────────
    verts, faces = [], []
    for iv in range(ny):
        for iu in range(nx):
            u  = iu / (nx - 1)
            v  = iv / (ny - 1)
            lx, y = _bilinear_pt(u, v, p00, p10, p11, p01)
            verts.append((X_OFF + lx, y, _terrain_z_natural(lx, y)))
    for iv in range(ny - 1):
        for iu in range(nx - 1):
            a = iv * nx + iu
            faces.append((a, a + 1, a + nx + 1, a + nx))

    me = bpy.data.meshes.new(mesh_name)
    me.from_pydata(verts, [], faces)
    me.update()
    obj = U.new_obj(mesh_name, me)
    U.put_mat(obj, U.M_SOIL)
    U.to_col(obj, col)

    # ── 2. Curvas de nível — varredura em linhas v=const ─────────────────────
    z_samples = [_terrain_z_natural(*_bilinear_pt(ui/3, vi/3, p00, p10, p11, p01))
                 for ui in range(4) for vi in range(4)]
    z_lo = math.floor(min(z_samples) * 2) / 2
    z_hi = math.ceil (max(z_samples) * 2) / 2

    main_v, main_e = [], []
    sec_v,  sec_e  = [], []

    def _flush(seg, vv, ee):
        if len(seg) < 2:
            return
        base = len(vv)
        vv.extend(seg)
        for k in range(len(seg) - 1):
            ee.append((base + k, base + k + 1))

    NV_SCAN = 72   # linhas v
    NU_CV   = 80   # pontos por linha

    zc = z_lo
    while zc <= z_hi + 0.01:
        is_main = (round(zc * 2) % 2 == 0)
        vv, ee  = (main_v, main_e) if is_main else (sec_v, sec_e)
        for iv in range(NV_SCAN):
            v = iv / (NV_SCAN - 1)
            cur = []
            prev_z, prev_lxy = None, None
            for iu in range(NU_CV):
                u = iu / (NU_CV - 1)
                lx, y = _bilinear_pt(u, v, p00, p10, p11, p01)
                z = _terrain_z_natural(lx, y)
                if prev_z is not None and (prev_z - zc) * (z - zc) < 0:
                    t  = (zc - prev_z) / (z - prev_z)
                    cx = prev_lxy[0] + t * (lx - prev_lxy[0])
                    cy = prev_lxy[1] + t * (y  - prev_lxy[1])
                    cur.append((X_OFF + cx, cy, zc + LIFT))
                prev_z, prev_lxy = z, (lx, y)
            _flush(cur, vv, ee)
        zc = round(zc + 0.5, 2)

    DARK  = (0.40, 0.18, 0.04, 1.0)
    LIGHT = (0.68, 0.54, 0.38, 1.0)
    for cname, cvv, cee, color in [
        (f"CV_{mesh_name}_Princ", main_v, main_e, DARK),
        (f"CV_{mesh_name}_Sec",   sec_v,  sec_e,  LIGHT),
    ]:
        if not cvv:
            continue
        me_c = bpy.data.meshes.new(cname)
        me_c.from_pydata(cvv, cee, [])
        me_c.update()
        obj_c = U.new_obj(cname, me_c)
        mat_c = bpy.data.materials.get(f"Mat_{cname}")
        if not mat_c:
            mat_c = bpy.data.materials.new(f"Mat_{cname}")
            mat_c.use_nodes = True
            mat_c.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = color
        obj_c.data.materials.append(mat_c)
        U.to_col(obj_c, col)

    # ── 3. Borda do lote — percorre as 4 arestas do quad ─────────────────────
    if draw_border:
        NB = 40
        bv = []
        for iu in range(NB):                         # aresta v=0 (u: 0→1)
            lx, y = _bilinear_pt(iu/(NB-1), 0.0, p00, p10, p11, p01)
            bv.append((X_OFF + lx, y, _terrain_z_natural(lx, y) + LIFT))
        for iv in range(NB):                         # aresta u=1 (v: 0→1)
            lx, y = _bilinear_pt(1.0, iv/(NB-1), p00, p10, p11, p01)
            bv.append((X_OFF + lx, y, _terrain_z_natural(lx, y) + LIFT))
        for iu in range(NB):                         # aresta v=1 (u: 1→0)
            lx, y = _bilinear_pt(1.0 - iu/(NB-1), 1.0, p00, p10, p11, p01)
            bv.append((X_OFF + lx, y, _terrain_z_natural(lx, y) + LIFT))
        for iv in range(NB):                         # aresta u=0 (v: 1→0)
            lx, y = _bilinear_pt(0.0, 1.0 - iv/(NB-1), p00, p10, p11, p01)
            bv.append((X_OFF + lx, y, _terrain_z_natural(lx, y) + LIFT))

        be = [(i, i + 1) for i in range(len(bv) - 1)] + [(len(bv) - 1, 0)]
        me_b = bpy.data.meshes.new(f"{mesh_name}_Borda")
        me_b.from_pydata(bv, be, [])
        me_b.update()
        obj_b = U.new_obj(f"{mesh_name}_Borda", me_b)
        mat_b = bpy.data.materials.get(f"Mat_Borda_{mesh_name}")
        if not mat_b:
            mat_b = bpy.data.materials.new(f"Mat_Borda_{mesh_name}")
            mat_b.use_nodes = True
            mat_b.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = borda_color
        obj_b.data.materials.append(mat_b)
        U.to_col(obj_b, col)

    return _quad_area(p00, p10, p11, p01)


def build_lote15h2():
    """Lote 15h2 — faixa estreita a LESTE do Lote_16 (relatório 2026-05).

    Vertices (V1 NW, V2 NE, V3 SE, V4 SW) convertidos via transformação afim
    usando os 4 cantos GPS do Lote_16 como referência.

    Geometria: X ∈ [30, 44], inteiramente leste de Lote_16. Sem sobreposição.

    Ordenação bilinear não auto-intersectante:
      p00=V4(30, 0)   p10=V3(44, 4)   p11=V2(40, 72)   p01=V1(30, 68)

    Coleção: Loteamento/Lote_15h2
    """
    V1, V2, V3, V4 = L15H2_VERTS   # NW(30,68), NE(40,72), SE(44,4), SW(30,0)
    area = _build_lote(
        "Loteamento/Lote_15h2",
        p00=V4, p10=V3, p11=V2, p01=V1,
        borda_color=(0.55, 0.10, 0.85, 1.0),   # roxo (conforme relatório)
        mesh_name="Lote_15h2",
    )
    print()
    print("  ┌─ Lote_15h2 — relatório 2026-05 ─────────────────────────────┐")
    print(f"  │  V1 NW = Lote16 NE  : ({V1[0]:.2f}, {V1[1]:.2f})              │")
    print(f"  │  V2 NE = L15h1 P1   : ({V2[0]:.2f}, {V2[1]:.2f})              │")
    print(f"  │  V3 SE              : ({V3[0]:.2f},  {V3[1]:.2f})               │")
    print(f"  │  V4 SW = Lote16 SE  : ({V4[0]:.2f},  {V4[1]:.2f})                │")
    print(f"  │  Área (Shoelace)    : {area:.0f} m²  (relatório: 828 m²)      │")
    print("  └──────────────────────────────────────────────────────────────┘")


def _pentagon_border(col, pts, mat_color, mesh_name, lift=0.06, nb_per_edge=30):
    """Desenha o fio de borda de um polígono arbitrário (lista de pontos locais).

    pts — lista de (lx, y) em coords locais, ordem do perímetro.
    Cada aresta é subdividida em nb_per_edge segmentos seguindo a elevação SRTM.
    """
    bv = []
    n = len(pts)
    for i in range(n):
        p0 = pts[i]
        p1 = pts[(i + 1) % n]
        for k in range(nb_per_edge):
            t  = k / nb_per_edge
            lx = p0[0] + t * (p1[0] - p0[0])
            y  = p0[1] + t * (p1[1] - p0[1])
            bv.append((X_OFF + lx, y, _terrain_z_natural(lx, y) + lift))

    be = [(i, i + 1) for i in range(len(bv) - 1)] + [(len(bv) - 1, 0)]
    me_b = bpy.data.meshes.new(mesh_name)
    me_b.from_pydata(bv, be, [])
    me_b.update()
    obj_b = U.new_obj(mesh_name, me_b)
    mat_b = bpy.data.materials.get(f"Mat_{mesh_name}")
    if not mat_b:
        mat_b = bpy.data.materials.new(f"Mat_{mesh_name}")
        mat_b.use_nodes = True
        mat_b.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = mat_color
    obj_b.data.materials.append(mat_b)
    U.to_col(obj_b, col)


def build_lote15h1():
    """Lote 15h1 — pentágono a NORTE de Lote_16 e Lote_15h2 (relatório 2026-05).

    Vértices convertidos via transformação afim (mesmos 4 cantos GPS do Lote_16):
      P1 SE = L15h2 V2  (40.20, 72.20)
      P2 NE             (37.87,103.14)
      P3 NW             ( 0.00,100.72)
      P4 SW = L16 NW    ( 0.00, 68.37)
      P5 S  = L16 NE    (30.00, 68.37)

    Geometria: Y ≥ 68.37 (todo ao norte de Lote_16). Sem sobreposição.

    Implementação: 2 quads bilineares + borda pentagonal.
      Quad A (principal N-E): p00=P5, p10=P1, p11=P2, p01=P3
      Quad B (triângulo SW):  p00=P5, p10=P3, p11=P4, p01=P5  (fan degenerado)

    Coleção: Loteamento/Lote_15h1
    """
    P1, P2, P3, P4, P5 = L15H1_VERTS
    COL = "Loteamento/Lote_15h1"

    # Quad A: p00=P5(30,68.37), p10=P1(40,72), p11=P2(38,103), p01=P3(0,101)
    _build_lote(COL, p00=P5, p10=P1, p11=P2, p01=P3,
                borda_color=(0.15, 0.65, 1.00, 1.0),
                mesh_name="Lote_15h1_A", nx=28, ny=36, draw_border=False)

    # Quad B fan: p00=p01=P5, p10=P3(0,101), p11=P4(0,68.37)
    # Colapsa em triângulo P5→P3→P4 (margem SW entre L16 NW e L15h1)
    _build_lote(COL, p00=P5, p10=P3, p11=P4, p01=P5,
                borda_color=(0.15, 0.65, 1.00, 1.0),
                mesh_name="Lote_15h1_B", nx=20, ny=28, draw_border=False)

    # Borda do pentágono completo (P1→P2→P3→P4→P5→P1)
    _pentagon_border(COL, [P1, P2, P3, P4, P5],
                     (0.15, 0.65, 1.00, 1.0), "Lote_15h1_Borda")

    # Área Shoelace do pentágono
    pts = [P1, P2, P3, P4, P5]
    area = abs(sum(pts[i][0]*pts[(i+1)%5][1] - pts[(i+1)%5][0]*pts[i][1]
                   for i in range(5))) / 2.0
    print()
    print("  ┌─ Lote_15h1 — relatório 2026-05 ─────────────────────────────┐")
    print(f"  │  P1 SE = L15h2 V2   : ({P1[0]:.2f}, {P1[1]:.2f})              │")
    print(f"  │  P2 NE              : ({P2[0]:.2f},{P2[1]:.2f})              │")
    print(f"  │  P3 NW              : ({P3[0]:.2f},{P3[1]:.2f})              │")
    print(f"  │  P4 SW = L16 NW     : ({P4[0]:.2f}, {P4[1]:.2f})              │")
    print(f"  │  P5 S  = L16 NE     : ({P5[0]:.2f}, {P5[1]:.2f})              │")
    print(f"  │  Área (Shoelace)    : {area:.0f} m²  (relatório: 1255 m²)    │")
    print("  └──────────────────────────────────────────────────────────────┘")
