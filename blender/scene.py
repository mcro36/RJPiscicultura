import bpy
import math
from constants import TW, TL


def build_lighting():
    # Sol principal — ângulo de fim de tarde
    bpy.ops.object.light_add(type='SUN', location=(TW/2, TL/2, 50))
    sun = bpy.context.active_object
    sun.name = "Sol"
    sun.data.energy       = 4.5
    sun.rotation_euler    = (math.radians(50), 0, math.radians(-55))

    # Fill suave para reduzir sombras duras
    bpy.ops.object.light_add(type='AREA', location=(TW/2, TL/2, 45))
    fill = bpy.context.active_object
    fill.name             = "Fill"
    fill.data.energy      = 400
    fill.data.size        = 100.0
    fill.rotation_euler   = (math.radians(75), 0, 0)

    # Fundo de céu (world)
    world = bpy.context.scene.world
    if not world:
        world = bpy.data.worlds.new("Mundo")
        bpy.context.scene.world = world
    world.use_nodes = True
    bg = world.node_tree.nodes.get("Background")
    if bg:
        bg.inputs["Color"].default_value    = (0.48, 0.70, 0.90, 1.0)
        bg.inputs["Strength"].default_value = 0.8


def build_camera():
    """
    Flythrough 300 frames @ 24 fps ≈ 12,5 s
      F  1– 60  entrada aérea SE sobre galpão
      F 60–120  sobrevoo L2 + RAS
      F120–170  sobe ao L1, detalhe T1-T3
      F170–220  órbita NW→NE
      F220–260  baixa para nível dos tanques
      F260–300  elevação final, visão geral
    """
    bpy.ops.object.camera_add(location=(55, -8, 32))
    cam = bpy.context.active_object
    cam.name          = "Camera_Principal"
    cam.data.lens     = 28        # grande-angular suave
    cam.data.clip_end = 500.0
    bpy.context.scene.camera = cam

    sc = bpy.context.scene
    sc.frame_start = 1
    sc.frame_end   = 300
    sc.render.fps  = 24

    # (frame, loc_x, loc_y, loc_z, rot_x°, rot_z°)
    keyframes = [
        (  1,  55, -8,  32,  58, -50),
        ( 60,  20, 10,  18,  52, -10),
        (120,  15, 35,  14,  48,   2),
        (170,  15, 55,  17,  52,   3),
        (220, -12, 50,  22,  55,  32),
        (260,  35, 50,  22,  55, -30),
        (300,  15, 25,  50,  78,   0),
    ]
    for f, lx, ly, lz, rx, rz in keyframes:
        sc.frame_set(f)
        cam.location       = (lx, ly, lz)
        cam.rotation_euler = (math.radians(rx), 0, math.radians(rz))
        cam.keyframe_insert("location")
        cam.keyframe_insert("rotation_euler")

    # Suavizar curvas — compatível com Blender ≤ 4.3 e 4.4+ / 5.x (slotted actions)
    anim = cam.animation_data
    if anim and anim.action:
        action = anim.action
        fcurves = []
        if hasattr(action, 'fcurves'):
            # Blender ≤ 4.3: acesso direto
            fcurves = list(action.fcurves)
        elif hasattr(action, 'layers') and action.layers:
            # Blender 4.4+ / 5.x: slot correto via anim_data.action_slot
            slot = getattr(anim, 'action_slot', None)
            if slot is None and hasattr(action, 'slots') and action.slots:
                slot = action.slots[0]
            if slot:
                for layer in action.layers:
                    for strip in layer.strips:
                        try:
                            cbag = strip.channelbag(slot)
                            fcurves.extend(cbag.fcurves)
                        except (AttributeError, TypeError):
                            pass
        for fc in fcurves:
            for kp in fc.keyframe_points:
                kp.interpolation = 'BEZIER'


def setup_render():
    sc = bpy.context.scene
    sc.render.engine       = 'CYCLES'
    sc.cycles.samples      = 128
    sc.cycles.use_denoising = True
    sc.render.resolution_x = 1920
    sc.render.resolution_y = 1080

    fmt = sc.render.image_settings
    try:
        fmt.file_format              = 'FFMPEG'
        sc.render.ffmpeg.format      = 'MPEG4'
        sc.render.ffmpeg.codec       = 'H264'
        sc.render.ffmpeg.constant_rate_factor = 'MEDIUM'
        sc.render.filepath           = "//RJ_Piscicultura_3D.mp4"
        print("  Saída: H264 MP4 -> RJ_Piscicultura_3D.mp4")
    except TypeError:
        # Blender 5.x removeu FFMPEG de image_settings — usa sequência PNG
        fmt.file_format              = 'PNG'
        fmt.color_mode               = 'RGB'
        fmt.compression              = 15
        sc.render.filepath           = "//RJ_Piscicultura_3D_frames/"
        print("  Saída: sequencia PNG -> RJ_Piscicultura_3D_frames/")
        print("  Para video: VSE > Add > Image Sequence > Render Animation")

    # Descomente para preview rápido (16 samples, resolução 50%):
    # sc.cycles.samples               = 16
    # sc.render.resolution_percentage = 50
