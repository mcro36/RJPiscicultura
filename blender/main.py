"""
RJ Piscicultura — Modelo 3D Blender 4.x
========================================
Piscicultura intensiva de tilápia (360 m³ + 60 m³ buffer)
Localização: Belo Horizonte, MG

Sistema de coordenadas
  X : 0 = Oeste   →  30.00 = Leste
  Y : 0 = Sul     →  68.37 = Norte (cota mais alta)
  Z : elevação em metros (Norte Z=10, Sul Z=0)

Como usar
  1. Abra o Blender 4.x
  2. Menu superior → Scripting
  3. Open → selecione este arquivo (main.py)
  4. Clique em "Run Script"
  5. Render → Animation (Ctrl+F12) para gerar RJ_Piscicultura_3D.mp4

  Para preview rápido: descomente as linhas de preview em scene.py
"""

import sys
import os
import importlib
import importlib.util
import bpy

# ── Caminho da pasta blender/ — ajuste se mover o projeto ────────────────────
SCRIPT_DIR = r"C:\Code\RJ_piscicultura\blender"


def _load(name):
    """Carrega (ou recarrega) um módulo pelo caminho absoluto.
    Funciona no Blender Text Editor, linha de comando e addons."""
    path = os.path.join(SCRIPT_DIR, f"{name}.py")
    if name in sys.modules:
        # Força reload para refletir edições sem reiniciar o Blender
        spec = importlib.util.spec_from_file_location(name, path)
        mod  = importlib.util.module_from_spec(spec)
        sys.modules[name] = mod
        spec.loader.exec_module(mod)
        return mod
    spec = importlib.util.spec_from_file_location(name, path)
    mod  = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


# ── Carrega módulos em ordem de dependência ───────────────────────────────────
_load("constants")
_load("utils")
_load("terrain")
_load("tanks")
_load("ras")
_load("pipes")
_load("galpao")
_load("infra")
_load("scene")

import utils   as _u
import terrain as _terrain
import tanks   as _tanks
import ras     as _ras
import pipes   as _pipes
import galpao  as _galpao
import infra   as _infra
import scene   as _scene


def main():
    print()
    print("=" * 60)
    print("  RJ Piscicultura — construindo modelo 3D")
    print("=" * 60)

    print("  [1/9] Limpando cena e inicializando materiais...")
    _u.clear_scene()
    _u.init_materials()

    print("  [2/9] Terreno — Relevo SRTM30m + Patamares + Entorno...")
    _terrain.build_natural_terrain()
    _terrain.build_road()
    _terrain.build_nat_grading()
    _terrain.build_lote15h2()
    _terrain.build_lote15h1()

    print("  [3/9] Tanques T1–T7 (Ø 7,40 m, geomembrana HDPE)...")
    _tanks.build_all_tanks()

    print("  [4/9] Sistema RAS (decantador + percolador + UV + reserv.)...")
    _ras.build_ras()

    print("  [5/9] Tubulações enterradas (drenagem, retorno, aeração, poço)...")
    _pipes.build_pipes()

    print("  [6/9] Galpão compartilhado (filetagem + ração + depósito + graxaria)...")
    _galpao.build_galpao()

    print("  [7/9] Infraestrutura (sopradores, CLP, gerador, poço, acessos)...")
    _infra.build_infra()

    print("  [8/9] Iluminação e câmera flythrough...")
    _scene.build_lighting()
    _scene.build_camera()

    print("  [9/9] Configuração de render (Cycles 1080p H264)...")
    _scene.setup_render()

    print()
    print("=" * 60)
    print("  MODELO CONCLUÍDO!")
    print("  ► NUMPAD-0    : câmera ativa")
    print("  ► SPACE       : prévia da animação na timeline")
    print("  ► Ctrl+F12    : renderizar vídeo  →  RJ_Piscicultura_3D.mp4")
    print("=" * 60)
    print()


main()
