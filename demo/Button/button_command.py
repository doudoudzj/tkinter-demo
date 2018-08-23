#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# tkinter 模块添加一个按钮
from tkinter import *


class Window(Frame):
    def __init__(self, master=None):

        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):

        self.master.title("第一个窗体")

        self.pack(fill=BOTH, expand=1)

        # 添加一个command，进行事务处理,这里点击退出，执行退出程序
        quitButton = Button(self, text="退出", command=self.client_exit)

        quitButton.place(x=0, y=0)

    def client_exit(self):
        exit()


root = Tk()
root.geometry("400x300")
app = Window(root)
root.mainloop()
