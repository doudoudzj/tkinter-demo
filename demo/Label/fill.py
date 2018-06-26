#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 控件: 标签Label

import tkinter

root = tkinter.Tk()
root.title('填充形式')

lb = tkinter.Label(root, text="一个测试用的标签", bg="red", fg="#fff")
lb2 = tkinter.Label(root, text="另一个测试用的标签", bg="#ddd")

# X方向填充
# lb.pack(fill=tkinter.X)

# Y方向填充
# lb.pack(fill=tkinter.Y)

# 想要高度100%, 需要设置属性expand=True
# lb.pack(fill=tkinter.Y, expand=True)

# 两个方向都填充
# lb.pack(fill=tkinter.BOTH, expand=True)

# fill填充会自动按照比例来等分空间
# lb.pack(fill=tkinter.BOTH, expand=True)
# lb2.pack(fill=tkinter.BOTH, expand=True)

# fill填充会自动按照比例来充分空间
lb.pack(fill=tkinter.BOTH, expand=True)
lb2.pack()

root.mainloop()
