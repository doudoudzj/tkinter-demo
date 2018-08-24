#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""加载jpg图片"""

import os
from tkinter import Tk, Button, Entry, Label

from PIL import Image, ImageTk

root = Tk()
root.title("加载jpg图片")

image_file = os.path.join(os.path.dirname(__file__), "doudou.jpg")

img = Image.open(image_file)  # 打开图片
photo = ImageTk.PhotoImage(img)  # 用PIL模块的PhotoImage打开
imglabel = Label(root, image=photo)
imglabel.grid(row=0, column=0, columnspan=4)

Label(root, text="输入:").grid(row=1, column=0, sticky='sn')

Entry(root).grid(row=1, column=1, columnspan=2)

Button(root, text="确定").grid(row=1, column=3)

root.mainloop()
