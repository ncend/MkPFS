# PyInstaller spec file for MkPFS GUI
# Build with: pyinstaller mkpfs-gui.spec

block_cipher = None

a = Analysis(
    ['mkpfs/gui/__main__.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('mkpfs/gui/theme.py', 'mkpfs/gui'),
        ('mkpfs/gui/i18n.py', 'mkpfs/gui'),
        ('mkpfs/gui/widgets.py', 'mkpfs/gui'),
        ('mkpfs/gui/panels', 'mkpfs/gui/panels'),
        ('mkpfs/pfs.py', 'mkpfs'),
        ('mkpfs/exfat.py', 'mkpfs'),
        ('mkpfs/exfat_writer.py', 'mkpfs'),
        ('mkpfs/ampr.py', 'mkpfs'),
        ('mkpfs/pbar.py', 'mkpfs'),
        ('mkpfs/utils.py', 'mkpfs'),
        ('mkpfs/consts.py', 'mkpfs'),
        ('mkpfs/_exfat_upcase.py', 'mkpfs'),
        ('mkpfs/logging.py', 'mkpfs'),
        ('mkpfs/cli.py', 'mkpfs'),
        ('assets/images/icon.png', 'assets/images'),
    ],
    hiddenimports=[
        'customtkinter',
        'PIL',
        'PIL.Image',
        'PIL.ImageTk',
        'tkinter',
        'tkinter.filedialog',
        'tkinter.messagebox',
        'tkinter.ttk',
        'multiprocessing',
        'zlib_ng',
        'isal',
        'cryptography.hazmat.primitives.ciphers',
        'cryptography.hazmat.primitives.hashes',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='mkpfs-gui',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # GUI app - no console window
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='assets/images/icon.png',
)