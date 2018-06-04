#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 创建一个窗口

import tkinter  # 引用Tk模块
mainWindow = tkinter.Tk()  # 初始化Tk(), 实例化
mainWindow.title('测试程序')  # 设置窗口标题
mainWindow.geometry('200x300')  # 默认窗口尺寸, 是字母x不是符号*
# 现有个问题, 必须width和height同时false时才会生效
mainWindow.resizable(width=False, height=False)  # 宽不可变, 高可变, 默认为True
mainWindow.mainloop()  # 进入消息循环
