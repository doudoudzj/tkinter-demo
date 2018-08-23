#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 对话框

from tkinter import Tk, Button
import tkinter.messagebox


class MainWindow():
    def __init__(self):
        self.frame = Tk()
        self.frame.title('对话框')
        self.frame.geometry('300x200')

        self.button1 = Button(self.frame, text="button1")
        self.button2 = Button(self.frame, text="button2")
        self.button3 = Button(self.frame, text="显示错误")
        self.button4 = Button(
            self.frame, text="按钮4", command=self.buttonListener4)

        self.button1.pack()
        self.button2.pack()
        self.button3.pack()
        self.button4.pack()

        self.button1.bind("<ButtonRelease-1>", self.buttonListener1)
        self.button2.bind("<ButtonRelease-1>", self.buttonListener2)
        self.button3.bind("<ButtonRelease-1>", self.buttonListener3)

        self.frame.mainloop()

    def buttonListener1(self, event):
        tkinter.messagebox.showinfo("标题", "第一个弹出消息窗口")

    def buttonListener2(self, event):
        tkinter.messagebox.showwarning("警告消息", "this is button 2 dialog")

    def buttonListener3(self, event):
        tkinter.messagebox.showerror("错误消息", "this is button 3 dialog")

    def buttonListener4(self):
        tkinter.messagebox.showinfo("messagebox", "按钮4的消息窗口")


window = MainWindow()
