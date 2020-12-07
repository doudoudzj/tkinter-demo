# /usr/bin/env python3
# -*-coding:utf-8 -*-

# python开发_tkinter_图片操作
# python tkinter image
# 注意: PhotoImage只支持的格式为: GIF, PPM/PGM

from os import path
from tkinter import Label, PhotoImage, Tk, mainloop


def main():
    d = path.dirname(__file__)  # 返回当前文件所在的目录
    filename = path.join(path.dirname(__file__), 'image.gif')
    root = Tk()
    img = PhotoImage(file=filename)
    label = Label(root, image=img)
    label.pack()
    root.mainloop()


main()
