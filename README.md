# python-tkinter-application-development

> tkinter桌面应用开发




UI: tkinter

打包工具：Pyinstaller


生成脚本

```py
pyinstaller --onedir -y -w app-script.py
pyinstaller --onedir -y app-script.spec
```

生成的app文字不清晰解决办法:
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

参考文档：[PyGobject详解](https://blog.csdn.net/column/details/pygobject.html)、

