# -*- mode: python -*-

block_cipher = None


a = Analysis(['MainWindow.py'],
             pathex=['C:\\Users\\deanl\\Desktop\\ConvertCVTSToExcel'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

for d in a.datas:
    if 'pyconfig' in d[0]:
        a.datas.remove(d)
        break

a.datas += [('safranlogo.png','C:\\Users\\deanl\\Desktop\\ConvertCVTSToExcel\\safranlogo.png', 'Data'),
            ('dataTemplate.xlsx','C:\\Users\\deanl\\Desktop\\ConvertCVTSToExcel\\dataTemplate.xlsx', 'Data'),
            ('safranico.ico','C:\\Users\\deanl\\Desktop\\ConvertCVTSToExcel\\safranico.ico', 'Data')]

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='MainWindow',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False, icon='C:\\Users\\deanl\\Desktop\\ConvertCVTSToExcel\\safranico.ico' )
