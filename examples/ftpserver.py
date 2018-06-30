import sys
from tkinter import *

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

import _thread

window = Tk()
window.title("FTP")
window.resizable(False, False)


def run():
    _thread.start_new_thread(ftpserver, ())


def exitftp():
    sys.exit(0)


def ftpserver():

    #实例化虚拟用户，这是FTP验证首要条件
    authorizer = DummyAuthorizer()

    #添加用户权限和路径，括号内的参数是(用户名， 密码， 用户目录， 权限)
    authorizer.add_user(var1.get(), var2.get(), '.', perm='elradfmw')

    #添加匿名用户 只需要路径
    authorizer.add_anonymous('.')

    #初始化ftp句柄
    handler = FTPHandler
    handler.authorizer = authorizer

    #监听ip 和 端口,因为linux里非root用户无法使用21端口，所以我使用了2121端口
    server = FTPServer((var3.get(), var4.get()), handler)

    #开始服务
    server.serve_forever()


# 下面这些是对最开始的时候创建的tk进行行列式填充 label为文本 entry为输入框
Label(window, text='帐号').grid(column=0, row=0)
var1 = StringVar()
Entry(window, textvariable=var1, bd=2).grid(column=1, row=0, columnspan=2)
var1.set("admin")
user = var1.get()

Label(window, text='密码:').grid(column=0, row=1)
var2 = StringVar()
Entry(window, textvariable=var2, bd=2).grid(column=1, row=1, columnspan=2)
var2.set("123456")
password = var2.get()

Label(window, text='IP 地址:').grid(column=0, row=2)
var3 = StringVar()
Entry(window, textvariable=var3, bd=2).grid(column=1, row=2, columnspan=2)
var3.set("0.0.0.0")
ipaddr = var3.get()

Label(window, text='端口号:').grid(column=0, row=3)
var4 = StringVar()
Entry(window, textvariable=var4, bd=2).grid(column=1, row=3, columnspan=2)
var4.set("2121")
port = var4.get()

Button(window, text="运行FTP", command=run).grid(column=1, row=4)
Button(window, text="退出", command=exitftp).grid(column=2, row=4, ipadx=5)

window.mainloop()
