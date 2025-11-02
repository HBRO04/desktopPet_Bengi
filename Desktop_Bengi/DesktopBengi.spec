# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['DesktopBengi.py'],
    pathex=[],
    binaries=[],
    datas=[('cat_walking_right.gif', '.'), ('cat_walking_left.gif', '.'), ('cat_dragging.gif', '.'), ('cat_jumping.gif', '.'), ('cat_present.gif', '.'), ('cat_sleeping.gif', '.'), ('cat_idle.gif', '.')],
    hiddenimports=[],
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
    name='DesktopBengi',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['cat_icon.ico'],
)
