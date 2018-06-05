# python-tkinter-application-development

> tkinter桌面应用开发


UI: tkinter

打包工具：pyinstaller
生成脚本

```shell
pyinstaller -F -w app.py # -F等同于--onedir
pyinstaller -D -w app.py # -D等同于 --onefile
```

-F 选项可以打出一个exe文件，默认是 -D，意思是打成一个文件夹
-w 直接发布的exe应用带命令行调试窗口，在指令内加入-w命令可以屏蔽

对打包有特殊需求的可以通过修改生成的spec文件, 然后打包spec文件

Mac系统打包发布成.app包（文件夹包形式）

```shell
pyinstaller --onedir -y -w app.py # 生成文件app.spec
pyinstaller --onedir -y app.spec # 生成.app文件夹, Mac特有的应用形式
```

Windows系统也可以使用上述命令，这样会生成一个带各种dll和依赖文件的文件夹，可以使用-F指令把应用打包成一个独立的exe文件
-F指令等同于--onefile

```shell
pyinstaller --onefile -y -w app.py #生成app.spec
pyinstaller --onefile -y -w app.spec
# 或者
pyinstaller -F -y -w app.py
pyinstaller -F -y -w app.spec
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
                'CFBundleName': '应用程序名称',
                'CFBundleDisplayName': '应用程序名称',
                'CFBundleGetInfoString': "Crogram Inc.",
                'CFBundleIdentifier': "login",
                'CFBundleVersion': "0.1.0",
                'CFBundleShortVersionString': "0.1.0",
                'NSHumanReadableCopyright': "Copyright © 2018, Crogram Inc., All Rights Reserved",
                'NSHighResolutionCapable': 'True'
             })
```


