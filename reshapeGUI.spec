# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_data_files, collect_submodules

# Collect all PyQt6 submodules and resources (e.g., Qt plugins)
hiddenimports = collect_submodules('PyQt6')
datas = collect_data_files('PyQt6')

a = Analysis(
    ['reshapeGUI.py'],
    pathex=[],
    binaries=[],
    datas=datas,  # Include PyQt6 data files (e.g., Qt plugins)
    hiddenimports=hiddenimports,  # Ensure PyQt6 submodules are included
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='reshapeGUI',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # This will ensure the app is windowed
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
