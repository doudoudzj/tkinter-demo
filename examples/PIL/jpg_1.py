#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""加载jpg图片"""

import os
from tkinter import Tk, Label

from PIL import Image, ImageTk

root = Tk()
root.title("加载jpg图片")

image_file = os.path.join(os.path.dirname(__file__), "doudou.jpg")

img = Image.open(image_file)  # 打开图片
photo = ImageTk.PhotoImage(img)  # 用PIL模块的PhotoImage打开
imglabel = Label(root, image=photo)
imglabel.pack()

root.mainloop()
