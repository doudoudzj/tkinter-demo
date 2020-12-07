#/usr/bin/env python3
#-*-coding:utf-8 -*-

# python开发_tkinter_图片操作
# python tkinter image
# 注意: PhotoImage只支持的格式为: GIF, PPM/PGM

from os import path
import tkinter


def main():
    d = path.dirname(__file__)  #返回当前文件所在的目录
    filename = d + '/image.gif'
    root = tkinter.Tk()
    img = tkinter.PhotoImage(file=filename)
    button = tkinter.Button(root, image=img)
    button.pack()
    root.mainloop()


main()
