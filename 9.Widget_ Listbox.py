#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
''' 控件: 标签Listbox
说明: 列表控件,可以含有一个或多个文本想,可单选也可多选
用法:
    创建: lb = ListBox(根对象, [属性列表])
    绑定变量: var=StringVar() lb=ListBox(根对象, listvariable = var)
    得到列表中的所有值: var.get()
    设置列表中的所有值: var.set((item1, item2, .....))
    添加: lb.insert(item)
    删除: lb.delete(item,...)
    绑定事件: lb.bind('<ButtonRelease-1>', 函数)
    获得所选中的选项: lbl.get(lb.curselection())
'''

from tkinter import *

root = Tk()
root.title("标签Listbox")
root.geometry()

var = StringVar()
lb = Listbox(root, listvariable=var)
list_item = [1, 2, 3, 4]  # 控件的内容为1 2 3 4
for item in list_item:
    lb.insert(END, item)
lb.delete(2, 4)  # 此时控件的内容为1 3

var.set(('a', 'ab', 'c', 'd'))  # 重新设置了，这时控件的内容就编程var的内容了
print(var.get())


def print_item(event):
    print(lb.get(lb.curselection()))


lb.bind('<ButtonRelease-1>', print_item)
lb.pack()

root.mainloop()