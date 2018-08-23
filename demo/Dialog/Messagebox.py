#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''消息对话框'''

from tkinter import Tk, Button, Message
import tkinter.messagebox


class MainWindow():
    def __init__(self):
        self.frame = Tk()
        self.frame.title('消息对话框')
        self.frame.geometry('300x0')

        self.button1 = Button(self.frame, text='提示信息')
        self.button2 = Button(self.frame, text='警告信息')
        self.button3 = Button(self.frame, text='显示错误')

        self.button1.pack()
        self.button2.pack()
        self.button3.pack()

        # 使用bind绑定单击事件来触发函数
        self.button1.bind('<ButtonRelease-1>', self.buttonListener1)
        self.button2.bind('<ButtonRelease-1>', self.buttonListener2)
        self.button3.bind('<ButtonRelease-1>', self.buttonListener3)

        # 使用command属性绑定触发函数
        Button(self.frame, text='是否处理数据', command=self.buttonListener4).pack()
        Button(self.frame, text='确定取消', command=self.buttonListener5).pack()
        Button(self.frame, text='你是傻子吗', command=self.buttonListener6).pack()
        Button(self.frame, text='退出操作', command=self.buttonListener7).pack()
        Button(self.frame, text='是否重试操作', command=self.buttonListener8).pack()
        Button(self.frame, text='设定了父组件', command=self.buttonListener9).pack()
        Button(self.frame, text='另外一种用法', command=self.buttonListener10).pack()

        self.frame.mainloop()

    def buttonListener1(self, event):
        res = tkinter.messagebox.showinfo('提示', '第一个弹出消息窗口')
        print(res)

    def buttonListener2(self, event):
        res = tkinter.messagebox.showwarning('警告消息', '请注意：警告信息！')
        print(res)

    def buttonListener3(self, event):
        res = tkinter.messagebox.showerror('错误消息', '出错啦！')
        print(res)

    def buttonListener4(self):
        res = tkinter.messagebox.askquestion('提示', '是否处理数据 ?')
        if res == 'yes':
            tkinter.messagebox.showinfo('提示', '好的, 马上去处理')
        elif res == 'no':
            tkinter.messagebox.showinfo('提示', '好的, 不处理')

    def buttonListener5(self):
        res = tkinter.messagebox.askokcancel('提示', '确定还是取消呢？')
        if res == True:
            tkinter.messagebox.showinfo('提示', '确定')
        elif res == False:
            tkinter.messagebox.showinfo('提示', '取消')

    def buttonListener6(self):
        res = tkinter.messagebox.askyesno('提示', '你是傻子吗 ?')
        if res == True:
            tkinter.messagebox.showinfo('提示', '哈哈, 你是傻子呀 !')
        elif res == False:
            tkinter.messagebox.showinfo('提示', '哦, 你不是傻子啊 ！')

    def buttonListener7(self):
        res = tkinter.messagebox.askyesnocancel('提示', '内容已修改，是否保存并退出？')
        if res == True:
            tkinter.messagebox.showinfo('提示', '好的, 保存并退出 !')
        elif res == False:
            tkinter.messagebox.showinfo('提示', '好的, 不保存直接退出 ！')
        elif res == None:
            tkinter.messagebox.showinfo('提示', '哦, 取消操作 ！')

    def buttonListener8(self):
        res = tkinter.messagebox.askretrycancel('提示', '操作失败，是否重试？', parent=self.frame)
        if res == True:
            tkinter.messagebox.showinfo('提示', '好的, 我再试试 !', parent=self.frame)
        elif res == False:
            tkinter.messagebox.showinfo('提示', '好的, 不试了 ！', parent=self.frame)

    def buttonListener9(self):
        tkinter.messagebox.showinfo(title='提示', message='哈哈', parent=self.frame)

    def buttonListener10(self):
        tkinter.messagebox.showinfo(title='提示', message='确定还是取消呢 ?')


window = MainWindow()
