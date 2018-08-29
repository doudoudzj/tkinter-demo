#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""FTP客户端GUI"""

import os
from ftplib import FTP
from tkinter import (Button, Entry, IntVar, Label, Listbox, Menu, StringVar,
                     Tk, filedialog)


class ftp_client():
    def __init__(self):
        self.root = Tk()
        self.root.title("FTP客户端GUI")
        self.root.geometry("500x400+500+100")
        self.root.resizable(False, False)

        self.default_port = IntVar()
        self.default_timeout = IntVar()
        self.path = StringVar()
        self.inputFileName = ""

        self.entry_ip = Entry(self.root)
        self.entry_port = Entry(self.root, textvariable=self.default_port)
        self.entry_user = Entry(self.root)
        self.entry_passwd = Entry(self.root, show="*")
        self.listbox = Listbox(self.root)

        self.default_port.set(21)
        self.default_timeout.set(-999)
        self.path_ = " "

        self.ftp = FTP()
        self.init_menu()
        self.init_page()

    def init_page(self):
        """界面"""

        label_ip = Label(self.root, text="地址:")
        label_ip.grid(row=0, column=0, sticky="e")
        self.entry_ip.grid(row=0, column=1, sticky="w")

        label_port = Label(self.root, text="端口:")
        label_port.grid(row=1, column=0, sticky="e")
        self.entry_port.grid(row=1, column=1, sticky="w")

        label_user = Label(self.root, text="账号:")
        label_user.grid(row=2, column=0, sticky="e")
        self.entry_user.grid(row=2, column=1, sticky="w")

        label_passwd = Label(self.root, text="密码:")
        label_passwd.grid(row=3, column=0, sticky="e")
        self.entry_passwd.grid(row=3, column=1, sticky="w")

        button_connect = Button(self.root, text="连接", command=self.login)
        button_connect.grid(row=4, column=1, sticky="w")

        button_disconnect = Button(self.root, text="断开", command=self.ftp_quit)
        button_disconnect.grid(row=4, column=2)

        button_reflash = Button(self.root, text="刷新", command=self.reflash)
        button_reflash.grid(row=4, column=3)

        label_file_list = Label(self.root, text="文件列表:")
        label_file_list.grid(row=5, column=1, sticky="w")

        self.listbox.bind("<Double-Button-1>", self.click_db)
        self.listbox.grid(row=6, column=1, sticky="w")

        Label(self.root, text="目标路径:").grid(row=7, column=0)
        Entry(self.root, textvariable=self.path).grid(row=7, column=1)
        Button(
            self.root, text="路径选择", command=self.selectPath).grid(
                row=7, column=2)

        Label(self.root, text="双击可下载文件!").grid(row=8, column=1, sticky="w")

        self.root.mainloop()

    def init_menu(self):

        self.menubar = Menu(self.root)
        self.fmenu = Menu(self.menubar, tearoff=0)
        for each in ["打开", "保存", "另存为", "关闭"]:
            self.fmenu.add_command(label=each)
        self.fmenu.add_separator()
        self.fmenu.add_command(label="退出", command=self.quit)
        self.menubar.add_cascade(label="文件", menu=self.fmenu)

        self.emenu = Menu(self.menubar, tearoff=0)
        for each in ["复制", "剪切", "粘贴"]:
            self.emenu.add_command(label=each)
        self.menubar.add_cascade(label="编辑", menu=self.emenu)

        self.vmenu = Menu(self.menubar, tearoff=0)
        self.vmenu.add_command(label="状态")
        self.menubar.add_cascade(label="视图", menu=self.vmenu)

        self.amenu = Menu(self.menubar, tearoff=0)
        self.amenu.add_command(label="版本信息")
        self.menubar.add_cascade(label="关于", menu=self.amenu)
        self.root["menu"] = self.menubar

    def login(self):
        self.ftp.connect(
            self.entry_ip.get().strip(),
            int(self.entry_port.get().strip()),
            #  self.default_timeout
        )
        self.ftp.login(self.entry_user.get(), self.entry_passwd.get())

    def ftp_quit(self):
        if self.ftp is not None:
            self.ftp.quit()

    def ftp_close(self):
        if self.ftp is not None:
            self.ftp.close()

    def reflash(self):
        filelist = self.ftp.nlst()
        if self.listbox.size() > 0:
            self.listbox.delete(0, "end")

        for i in range(len(filelist)):
            self.listbox.insert("end", filelist[i])

    def click_db(self, event):
        self.download()

    def download(self):
        inputFileName = self.listbox.get(self.listbox.curselection())
        file_handler = open(self.path.get() + "/" + inputFileName, "wb").write
        self.ftp.retrbinary("RETR %s" % os.path.basename(inputFileName),
                            file_handler, 1024)

    def selectPath(self):
        self.path_ = filedialog.askdirectory()
        self.path.set(self.path_)

    def quit(self):
        self.root.quit()


# def main():
#     ftp_client()

if __name__ == "__main__":
    ftp_client()
