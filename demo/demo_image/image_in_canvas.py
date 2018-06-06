#/usr/bin/env python3
#-*-coding:utf-8 -*-
# python开发_tkinter_图片操作
# 注意: PhotoImage只支持的格式为: GIF, PPM/PGM

from os import path
from tkinter import PhotoImage, Canvas, Tk, mainloop


def main():
    d = path.dirname(__file__)  #返回当前文件所在的目录
    filename = d + '/image.gif'
    root = Tk()
    img = PhotoImage(file=filename)
    cv = Canvas(root, bg='white')
    cv.create_image((100, 100), image=img)
    cv.pack()
    root.mainloop()


main()
