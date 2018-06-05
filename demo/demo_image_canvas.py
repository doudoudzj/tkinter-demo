#/usr/bin/env python3
#-*-coding:utf-8 -*-

# python开发_tkinter_图片操作
# python tkinter image

from os import path
from tkinter import PhotoImage, Canvas, Tk, mainloop

__author__ = {
    'name': 'name',
    'mail': 'mail@foxmail.com',
    'blog': 'http://www.blog.com/',
    'QQ': '99999999',
    'created': '2018-06-05'
}


def main():
    d = path.dirname(__file__)  #返回当前文件所在的目录
    filename = d + '/demo_image.gif'
    root = Tk()
    img = PhotoImage(file=filename)
    cv = Canvas(root, bg='white')
    cv.create_image((100, 100), image=img)
    cv.pack()
    root.mainloop()


main()
