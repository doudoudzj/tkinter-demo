#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""FTP服务器GUI"""

import sys
from tkinter import Tk, Label, Button, Entry, StringVar

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

import _thread


class FTP(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("FTP服务器GUI")
        self.set_window_center(self, 300, 180)
        self.resizable(False, False)

        self.server = None
        self.var1 = StringVar()
        self.var2 = StringVar()
        self.var3 = StringVar()
        self.var4 = StringVar()

        self.load_view()

    def run(self):
        _thread.start_new_thread(self.ftpserver, ())

    def exitftp(self):
        self.server.close_all()

    def ftpserver(self):

        # 实例化虚拟用户，这是FTP验证首要条件
        authorizer = DummyAuthorizer()

        # 添加用户权限和路径，括号内的参数是(用户名， 密码， 用户目录， 权限)
        authorizer.add_user(
            self.var1.get(), self.var2.get(), '.', perm='elradfmw')

        # 添加匿名用户，任何人都可以访问，否则需要输入用户名和密码才能访问
        # 匿名用户只需要配置路径
        authorizer.add_anonymous('.', msg_login="Welcome")

        # 初始化ftp句柄
        handler = FTPHandler
        handler.authorizer = authorizer

        # 监听ip 和 端口,因为linux里非root用户无法使用21端口，所以我使用了2121端口
        self.server = FTPServer((self.var3.get(), self.var4.get()), handler)

        # 开始服务
        self.server.serve_forever()

    def load_view(self):
        """界面"""
        Label(self, text='账号:').grid(column=0, row=0)
        Entry(self, textvariable=self.var1, bd=2).grid(column=1, row=0)
        self.var1.set("admin")
        user = self.var1.get()

        Label(self, text="密码:").grid(column=0, row=1)

        Entry(self, textvariable=self.var2, bd=2).grid(column=1, row=1)
        self.var2.set("123456")
        password = self.var2.get()

        Label(self, text="地址:").grid(column=0, row=2)
        Entry(self, textvariable=self.var3, bd=2).grid(column=1, row=2)
        self.var3.set("0.0.0.0")
        ipaddr = self.var3.get()

        Label(self, text="端口:").grid(column=0, row=3)

        Entry(self, textvariable=self.var4, bd=2).grid(column=1, row=3)
        self.var4.set("2121")
        port = self.var4.get()

        Button(self, text="启动", command=self.run).grid(column=0, row=4)
        Button(self, text="停止", command=self.exitftp).grid(column=1, row=4)

    def set_window_center(self, window, width, height):
        """设置窗口宽高及居中"""
        # 获取屏幕 宽、高
        w_s = window.winfo_screenwidth()
        h_s = window.winfo_screenheight()
        # 计算 x, y 位置
        x_co = (w_s - width) / 2
        y_co = (h_s - height) / 2 - 50
        window.geometry("%dx%d+%d+%d" % (width, height, x_co, y_co))
        window.minsize(width, height)


if __name__ == "__main__":
    ftp = FTP()
    ftp.mainloop()
