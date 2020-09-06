#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from PIL import Image, ImageTk
import tkinter
import tkinter.filedialog
top = tkinter.Tk()
top.title = 'new'
top.geometry('640x480')


def choose_fiel():
    selectFileName = tkinter.filedialog.askopenfilename(title='选择文件')  # 选择文件
    e.set(selectFileName)


e = tkinter.StringVar()
e_entry = tkinter.Entry(top, width=68, textvariable=e)
e_entry.pack()


def upload_func(a):
    '''
    要自己写个方法，ftp等方法，上传文件到服务器

    '''
    print(a)
    pass


submit_button = tkinter.Button(top, text="选择文件", command=choose_fiel)
submit_button.pack()
submit_button = tkinter.Button(
    top, text="上传", command=lambda: upload_func(e_entry.get()))
submit_button.pack()


def showImg(img1):
    load = Image.open(img1)
    render = ImageTk.PhotoImage(load)

    img = tkinter.Label(image=render)
    img.image = render
    img.place(x=200, y=100)


submit_button = tkinter.Button(
    top, text="显示图片", command=lambda: showImg(showImg('服务器上的pic路径')))
submit_button.pack()

top.mainloop()
