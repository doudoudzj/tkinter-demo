#!/usr/bin/env python3
#-*- coding: UTF-8 -*-
# place几何布局管理器
# 用此方法时，需要提前设计好窗口的大小，以及各组件的位置大小。

from tkinter import *

root=Tk();root.title("登录")

root['width']=200;root['height']=80  #窗口宽度高度
Label(root,text="用户名",width=6).place(x=1,y=1) #绝对坐标(1,1)
Entry(root,width=20).place(x=45,y=1)
Label(root,text="密  码",width=6).place(x=1,y=20)
Entry(root,width=20,show='*').place(x=45,y=20)
Button(root,text="登录",width=8).place(x=40,y=40)
Button(root,text="取消",width=8).place(x=110,y=40)

root.mainloop()
