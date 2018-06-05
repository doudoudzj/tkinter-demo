# python-tkinter-application-development

> tkinter桌面应用开发




UI: tkinter

打包工具：Pyinstaller


生成脚本

Mac系统打包发布成.app包（文件夹包形式）
```shell
pyinstaller --onedir -y -w main-script.py
pyinstaller --onedir -y main-script.spec

```

Windows系统也可以使用上述命令，这样会生成一个带各种dll和依赖文件的文件夹，可以使用-F指令把应用打包成一个独立的exe文件
```shell
pyinstaller --onedir -y -w app-script.py
```

针对Mac生成的app文字不清晰解决办法:
修改spec文件: 添加info_plist属性
设置NSHighResolutionCapable值为True

```
app = BUNDLE(coll,
             name='main.app',
             icon=None,
             bundle_identifier=None,
             info_plist={
                'CFBundleName': '应用程序',
                'CFBundleDisplayName': '应用程序',
                'CFBundleGetInfoString': "Crogram Inc.",
                'CFBundleIdentifier': "login",
                'CFBundleVersion': "0.1.0",
                'CFBundleShortVersionString': "0.1.0",
                'NSHumanReadableCopyright': "Copyright © 2018, douzhenjiang, All Rights Reserved",
                'NSHighResolutionCapable': 'True'
             })
```


