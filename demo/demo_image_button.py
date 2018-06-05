# python开发_tkinter_图片操作
# python tkinter image

from os import path
from tkinter import Button, PhotoImage, Tk, mainloop

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
    button = Button(root, image=img)
    button.pack()
    root.mainloop()


main()
