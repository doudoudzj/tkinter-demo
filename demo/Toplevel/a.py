# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 顶级窗口 Toplevel
# TopLevel与Frame类似，但它包含窗体属性（如Title）
'''1.创建简单的Toplevel'''

import tkinter

root = tkinter.Tk()
root.title('主窗体')

tl = tkinter.Toplevel()
tl.title('子窗体')

# 在子窗体中，添加了一个Label
tkinter.Label(tl, text='子窗体子窗体子窗体子窗体子窗体').pack()
tkinter.Label(tl, text='hello label').pack()
tkinter.Label(tl, text='hello label').pack()

root.mainloop()

# 运行结果生成了两个窗体，一个是root启动的，另一个则是Toplevel创建的，它包含有一个label;
# 关闭子窗体，没有退出程序，Tk仍旧工作
# 关闭主窗体，整个Tk结束子窗体也结束，它不能单独存在。
