#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Menu

import tkinter as gui

window = gui.Tk()
window.title("菜单演示")
window.option_add('*tearOff', False)

menuBar = gui.Menu(window)  # 创建菜单栏

window.config(menu=menuBar)  # 设置窗体的菜单栏

File = gui.Menu(menuBar)  # 创建菜单: '文件'
Edit = gui.Menu(menuBar)  # 创建菜单: '编辑'
Help_ = gui.Menu(menuBar)  # 创建菜单: 'Help'
test = gui.Menu(menuBar)  # 创建菜单: '测试菜单'

# 添加菜单到菜单栏, 作为下拉根菜单的标题, 也可以用作子级菜单入口标签
menuBar.add_cascade(menu=File, label='文件')  # 添加菜单: '文件'
menuBar.add_cascade(menu=Edit, label='编辑')  # 添加菜单: '编辑'
menuBar.add_cascade(menu=test, label='测试菜单')  # 添加菜单: '测试菜单'
menuBar.add_cascade(menu=Help_, label='Help')  # 添加菜单: 'Help'

# 在'文件' 菜单里, 添加命令菜单项 '新建'
File.add_command(label='新建', command=lambda: print("新建菜单"))
# 在'文件' 菜单里, 添加分割线
File.add_separator()  # 分割线
# 在'文件' 菜单里, 添加命令菜单项 '打开'
File.add_command(label='打开', command=lambda: print("Open File"))
File.add_separator()  # 分割线

# 将 '文件' 菜单作为父菜单, 创建菜单: '保存'
SAVE = gui.Menu(File)  # 在父菜单 '文件' 里添加子菜单 '保存'
File.add_cascade(menu=SAVE, label='保存')  # 设置菜单标签名
SAVE.add_command(label='保存为', command=lambda: print(" Save as"))
SAVE.add_command(label='保存所有', command=lambda: print(" Save all"))


# 创建窗口
def createWindow():
    w = gui.Toplevel()
    w.title("新建窗口")


# 退出窗口
def exitWindow():
    exit()


# 设置窗体默认菜单栏
def defaultMenu():
    window.config(menu=menuBar)


# 设置测试菜单栏
def switchMenu():
    # 切换菜单功能可以用在权限控制方面
    menuBar1 = gui.Menu(window)  # 创建菜单栏
    window.config(menu=menuBar1)  # 设置窗体菜单
    test1 = gui.Menu(menuBar1)  # 创建菜单
    menuBar1.add_cascade(menu=test1, label='文件')  # 放置test菜单到menuBar1
    test1.add_command(label='切换到默认菜单', command=defaultMenu)  # 放置命令菜单项到test菜单里


test.add_command(label='新建', command=lambda: print("新建菜单"))  # 添加命令菜单项
test.add_command(label='退出', command=exitWindow)
test.add_separator()  # 分割线
test.add_command(label='新建窗口', command=createWindow)
test.add_command(label='切换菜单', command=switchMenu)

window.mainloop()
