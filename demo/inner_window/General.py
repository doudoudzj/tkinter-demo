#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 创建一个基本窗口
'''
几个常用属性:
    title: 设置窗口标题
    geometry: 设置窗口大小
    resizable(): 设置窗口是否可以变化长 宽
'''

import tkinter  # 引用Tk模块

# 初始化Tk(), 实例化
mainWindow = tkinter.Tk()

# 设置窗口标题
mainWindow.title('测试程序')

# 默认窗口尺寸, 是字母x, 不是符号*
mainWindow.geometry('200x200')

# 现有个问题, 必须width和height同时false时才会生效
mainWindow.resizable(width=False, height=False)  # 宽不可变, 高可变, 默认为True

mainWindow.mainloop()  # 进入消息循环
