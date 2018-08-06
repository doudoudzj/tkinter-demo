#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import tkinter
from tkinter import ttk  #导入内部包

win = tkinter.Tk()
win.title("Treeview")

# 实例化表格
# 空白首列是显示的，设置show属性为 headings 即可隐藏首列。
tree = ttk.Treeview(win, height=18, show="headings")

def info(event):
    """详情"""
    # event.widget.selection() #获取所选的项(可能是多项，所以要for循环)
    # event.widget获取Treeview对象，调用selection获取选择所有选中的
    slct = event.widget.selection()
    for i in slct:
        print(tree.item(i))
        print(tree.item(i)["values"])
        print(tree.item(i, "values"))


# 列索引ID
tree["columns"] = ("id", "name", "age", "heigh")

# 表头设置
tree.heading("id", text="ID")
tree.heading("name", text="姓名")
tree.heading("age", text="年龄")
tree.heading("heigh", text="身高")

# 表列设置, 可设置对应列的样式等, 不显示
tree.column("id", width=100)
tree.column("name", width=100, anchor="center")
tree.column("age", width=100, anchor="center")
tree.column("heigh", width=100, anchor="center")

# 插入数据
tree.insert("", 0, text="首列显示内容", values=("135", "张三", "3", "170"))
tree.insert("", 1, text="", values=("136", "李四", "34", "171"))
tree.insert("", 2, text="", values=("137", "王五", "9", "169"))
tree.insert("", 3, text="", values=("138", "马六", "23", "175"))
tree.insert("", 3, text="", values=("138", "马六", "23", "175"))
tree.insert("", 3, text="", values=("138", "马六", "23", "175"))
tree.insert("", 3, text="", values=("138", "马六", "23", "175"))
tree.insert("", 3, text="", values=("138", "马六", "23", "175"))
tree.insert("", 3, text="", values=("138", "马六", "23", "175"))
tree.insert("", 3, text="", values=("138", "马六", "23", "175"))
tree.insert("", 3, text="", values=("138", "马六", "23", "175"))
tree.insert("", 3, text="", values=("138", "马六", "23", "175"))
tree.insert("", 3, text="", values=("138", "马六", "23", "175"))
tree.insert("", 3, text="", values=("138", "马六", "23", "175"))
tree.insert("", 3, text="", values=("138", "马六", "23", "175"))
tree.insert("", 3, text="", values=("138", "马六", "23", "175"))
tree.insert("", 3, text="", values=("138", "马六", "23", "175"))
tree.insert("", 3, text="", values=("138", "马六", "23", "175"))
tree.insert("", 3, text="", values=("138", "马六", "23", "175"))
tree.insert("", 3, text="", values=("138", "马六", "23", "175"))
tree.insert("", 3, text="", values=("138", "马六", "23", "175"))

# 加滚动条
vbar = ttk.Scrollbar(win, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=vbar.set)

# 选中事件
tree.bind("<<TreeviewSelect>>", info)


tree.grid(row=0, column=0, sticky="nswe")
vbar.grid(row=0, column=1, sticky="ns")

head_frame = tkinter.LabelFrame(win, text="操作")
head_frame.grid(row=1, column=0, columnspan=2, sticky="nswe")
left = tkinter.Label(head_frame, text="Inside the LabelFrame")
left.pack()

btn_info = tkinter.Button(head_frame, text="详情")
btn_edit = tkinter.Button(head_frame, text="编辑")
btn_delete = tkinter.Button(head_frame, text="删除")
btn_info.pack(side="left")
btn_edit.pack(side="left")
btn_delete.pack(side="left")





# tree.pack()
win.mainloop()
