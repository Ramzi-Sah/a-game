# -*- mode: python -*-
ProjectPath = r'C:\Users\Ramzi\Documents\Ramzi\Dev\py\Projects\PyGame\P2'

a = Analysis(['main.py'],
    pathex=[ProjectPath+r'\build'],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None)

pyz = PYZ(a.pure, a.zipped_data,cipher=None)

EXE(pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='Future Project',
    debug=False,
    strip=False,
    upx=False,
    runtime_tmpdir=None,
    console=True,
    icon=ProjectPath+r'\icon.ico'
    )
