# -*- mode: python ; coding: utf-8 -*-

from pathlib import Path

a = Analysis(
    ['../fancy-runner.py'],
    pathex=[],
    binaries=[],
    datas=[('/Users/Zhisen/PycharmProjects/fancy/fancy/assets/*.icns', 'fancy/assets'), ('/Users/Zhisen/PycharmProjects/fancy/fancy/assets/*.png', 'fancy/assets')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='fancy-runner-mac',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='fancy-runner-mac',
)
