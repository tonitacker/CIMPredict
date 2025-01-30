# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('icon.icns', '.'),  # Icon-Datei
	('fav256x256.ico', '.'),
        ('portableR', 'portableR'),
        ('R-Skripte', 'R-Skripte')
    ],
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
    name='CIMPredict',
    debug=True,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=True
)

app = BUNDLE(
    exe,  
    name='CIMPredict.app',
    icon='icon.icns',
    bundle_identifier='com.tonitacker.CIMPredict'
)