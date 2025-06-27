# -*- mode: python -*-

block_cipher = None


a = Analysis(['aw_notify/main.py'],
             pathex=[],
             binaries=None,
             datas=None,
             hiddenimports=[
                'desktop_notifier.resources',
                'winrt',
                'winrt.windows.ui.notifications',
                'winrt.windows.data.xml.dom',
                'winrt.windows.foundation',
                'winrt.windows.foundation.collections',
                'winrt.windows.system.userprofile',
                'winrt.windows.storage.streams',
                'winrt.windows.ui.notifications.management',
                'desktop_notifier.sync'
             ],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='aw-notify',
          contents_directory=".",
          debug=False,
          strip=False,
          upx=True,
          console=True)
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='aw-notify')
