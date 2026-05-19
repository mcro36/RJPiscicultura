"""Funções utilitárias e materiais — único módulo que importa bpy diretamente."""
import bpy
import math
from mathutils import Vector

# ── Globals de material (populados por init_materials após clear_scene) ────────
M_SOIL = M_CONC = M_STEEL = M_HDPE = M_WATER = None
M_PVC  = M_WALL = M_ROOF  = M_SHADE = M_GEN  = None
M_PANEL = M_RAS = M_UV    = M_GRASS = None


# ══════════════════════════════════════════════════════════════════════════════
# Cena
# ══════════════════════════════════════════════════════════════════════════════

def clear_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    for blk in (bpy.data.meshes, bpy.data.curves,
                bpy.data.lights, bpy.data.cameras, bpy.data.materials):
        for item in list(blk):
            blk.remove(item)
    # bpy.data.collections não inclui a Scene Collection master — seguro remover
    for col in list(bpy.data.collections):
        bpy.data.collections.remove(col, do_unlink=True)


def get_col(path):
    """Cria ou retorna coleção por caminho 'Pai/Filho/Neto'.
    Cada nível é vinculado ao pai; nomes devem ser únicos globalmente."""
    parts = [p.strip() for p in path.split("/")]
    parent = bpy.context.scene.collection
    col = None
    for part in parts:
        if part in bpy.data.collections:
            col = bpy.data.collections[part]
        else:
            col = bpy.data.collections.new(part)
        if col.name not in [c.name for c in parent.children]:
            parent.children.link(col)
        parent = col
    return col


def to_col(obj, path):
    c = get_col(path)
    if obj.name not in c.objects:
        c.objects.link(obj)
    if obj.name in bpy.context.scene.collection.objects:
        bpy.context.scene.collection.objects.unlink(obj)


def new_obj(name, mesh):
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.scene.collection.objects.link(obj)
    return obj


def put_mat(obj, m):
    if obj.data.materials:
        obj.data.materials[0] = m
    else:
        obj.data.materials.append(m)


# ══════════════════════════════════════════════════════════════════════════════
# Materiais
# ══════════════════════════════════════════════════════════════════════════════

def mk_mat(name, rgb, metallic=0.0, rough=0.6, alpha=1.0):
    if name in bpy.data.materials:
        return bpy.data.materials[name]
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    bsdf = m.node_tree.nodes["Principled BSDF"]
    bsdf.inputs["Base Color"].default_value = (*rgb, 1.0)
    bsdf.inputs["Metallic"].default_value   = metallic
    bsdf.inputs["Roughness"].default_value  = rough
    if alpha < 1.0:
        bsdf.inputs["Alpha"].default_value  = alpha
        # surface_render_method (Blender 4.2+/5.x); fallback para blend_method (≤ 4.1)
        if hasattr(m, 'surface_render_method'):
            m.surface_render_method = "BLENDED"
        elif hasattr(m, 'blend_method'):
            m.blend_method = "BLEND"
    return m


def init_materials():
    global M_SOIL, M_CONC, M_STEEL, M_HDPE, M_WATER
    global M_PVC, M_WALL, M_ROOF, M_SHADE, M_GEN
    global M_PANEL, M_RAS, M_UV, M_GRASS
    M_SOIL  = mk_mat("Terra",       (0.50, 0.33, 0.18), rough=0.95)
    M_CONC  = mk_mat("Concreto",    (0.72, 0.70, 0.67), rough=0.85)
    M_STEEL = mk_mat("Aco",         (0.55, 0.57, 0.60), metallic=0.85, rough=0.30)
    M_HDPE  = mk_mat("Geomembrana", (0.10, 0.10, 0.11), rough=0.70)
    M_WATER = mk_mat("Agua",        (0.07, 0.35, 0.62), rough=0.03, alpha=0.72)
    M_PVC   = mk_mat("PVC",         (0.86, 0.84, 0.80), rough=0.65)
    M_WALL  = mk_mat("Alvenaria",   (0.82, 0.80, 0.76), rough=0.90)
    M_ROOF  = mk_mat("Telha_Metal", (0.45, 0.40, 0.36), rough=0.75)
    M_SHADE = mk_mat("Sombrite",    (0.12, 0.12, 0.12), rough=0.90, alpha=0.65)
    M_GEN   = mk_mat("Gerador",     (0.22, 0.48, 0.22), rough=0.50)
    M_PANEL = mk_mat("PainelElec",  (0.18, 0.20, 0.24), rough=0.40)
    M_RAS   = mk_mat("RAS_HDPE",    (0.14, 0.38, 0.55), rough=0.45)
    M_UV    = mk_mat("UV_Inox",     (0.70, 0.72, 0.74), metallic=0.70, rough=0.25)
    M_GRASS = mk_mat("Grama",       (0.20, 0.45, 0.12), rough=0.95)


# ══════════════════════════════════════════════════════════════════════════════
# Primitivas
# ══════════════════════════════════════════════════════════════════════════════

def add_cyl(name, r, h, loc, m, col_name, rot=(0, 0, 0), segs=32):
    bpy.ops.mesh.primitive_cylinder_add(
        vertices=segs, radius=r, depth=h, location=loc)
    o = bpy.context.active_object
    o.name = name
    o.rotation_euler = rot
    put_mat(o, m)
    to_col(o, col_name)
    return o


def add_box(name, dims, loc, m, col_name):
    bpy.ops.mesh.primitive_cube_add(location=loc)
    o = bpy.context.active_object
    o.name = name
    o.scale = (dims[0] / 2, dims[1] / 2, dims[2] / 2)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    put_mat(o, m)
    to_col(o, col_name)
    return o


def add_cone(name, r1, r2, h, loc, m, col_name, segs=32):
    bpy.ops.mesh.primitive_cone_add(
        vertices=segs, radius1=r1, radius2=r2, depth=h, location=loc)
    o = bpy.context.active_object
    o.name = name
    put_mat(o, m)
    to_col(o, col_name)
    return o


def add_tube(name, r_out, r_in, h, loc, m, col_name, segs=64):
    """Cilindro anelar sem tampo (open-top) — parede de tanque visível de cima."""
    cx, cy, cz = loc
    N = segs
    verts = []
    # anel 0: base exterior  1: topo exterior  2: base interior  3: topo interior
    for zz, rr in ((cz, r_out), (cz + h, r_out), (cz, r_in), (cz + h, r_in)):
        for i in range(N):
            a = 2 * math.pi * i / N
            verts.append((cx + rr * math.cos(a), cy + rr * math.sin(a), zz))
    faces = []
    for i in range(N):
        j = (i + 1) % N
        faces.append((i,     j,     N+j,   N+i  ))  # parede externa
        faces.append((2*N+i, 3*N+i, 3*N+j, 2*N+j))  # parede interna
        faces.append((N+i,   N+j,   3*N+j, 3*N+i))  # anel superior
        faces.append((j,     i,     2*N+i, 2*N+j))  # anel inferior
    me = bpy.data.meshes.new(name)
    me.from_pydata(verts, [], faces)
    me.update()
    obj = new_obj(name, me)
    put_mat(obj, m)
    to_col(obj, col_name)
    return obj


def seg(name, p1, p2, r, m, col_name, segs=8):
    """Segmento de tubo cilíndrico entre dois pontos 3D."""
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    dz = p2[2] - p1[2]
    L  = math.sqrt(dx*dx + dy*dy + dz*dz)
    if L < 0.05:
        return
    cx, cy, cz = (p1[0]+p2[0])/2, (p1[1]+p2[1])/2, (p1[2]+p2[2])/2
    bpy.ops.mesh.primitive_cylinder_add(
        vertices=segs, radius=r, depth=L, location=(cx, cy, cz))
    o = bpy.context.active_object
    o.name = name

    axis  = Vector((dx, dy, dz)).normalized()
    z_up  = Vector((0, 0, 1))
    cross = z_up.cross(axis)

    if cross.length < 1e-5:   # float32 em Blender 5.x exige threshold maior
        # paralelo (+Z) ou anti-paralelo (−Z)
        rot_axis = Vector((1, 0, 0))
        angle    = 0.0 if axis.z > 0 else math.pi
    else:
        rot_axis = cross.normalized()
        angle    = math.acos(max(-1.0, min(1.0, z_up.dot(axis))))

    o.rotation_mode       = 'AXIS_ANGLE'
    o.rotation_axis_angle = (angle, rot_axis.x, rot_axis.y, rot_axis.z)
    put_mat(o, m)
    to_col(o, col_name)
    return o
