#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Tkinter 登陆成功并跳转到主界面
# 主函数main.py
# https://blog.csdn.net/tiandawangliang/article/details/54969746

from tkinter import *
from LoginPage import *

root = Tk()
root.title('程序')
LoginPage(root)
root.mainloop()
