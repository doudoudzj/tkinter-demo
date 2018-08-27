#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 创建一个基本窗口
'''
常用属性:
    title: 设置窗口标题
    geometry: 设置窗口大小
    resizable(): 设置窗口是否可以变化长 宽
'''

from tkinter import Tk, Button

window = Tk()  # 初始化Tk(), 实例化

window.title('测试程序')  # 设置窗口标题

# 设置窗口尺寸, 是字母x, 不是符号*, +100 +100 定义窗口弹出时的默认展示位置
# window.geometry("200x200+100+100")

# 现有个问题, 必须width和height同时false时才会生效
# window.resizable(False, False)  # 宽不可变, 高可变, 默认为True

window["bg"] = "pink"  # 窗口背景色

# window.attributes("-alpha", 0.8)  # 窗口透明度, 值越小透明度越高

Button(window, text="你好你好").pack()

window.attributes("-disabled", True)

window.mainloop()  # 进入消息循环
