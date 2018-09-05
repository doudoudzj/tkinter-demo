#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""显示系统隐藏的文件-Mac"""

import os
from tkinter import Button, Tk, messagebox


class App:
    def __init__(self):

        root = Tk()
        root.title("Mac显示系统隐藏的文件")
        sw = root.winfo_screenwidth()
        sh = root.winfo_screenheight()
        cw = 250
        ch = 100
        size = '%dx%d+%d+%d' % (cw, ch, (sw - cw) / 2, (sh - ch) / 2 - 50)
        root.geometry(size)
        root.resizable(False, False)
        root.update()

        b1 = Button(root, text="显示所有文件", command=self.show)
        b1.pack(expand="yes")

        b2 = Button(root, text="不显示隐藏文件", command=self.hide)
        b2.pack(expand="yes")

        root.mainloop()
        self.root = root

    def show(self):

        # defaults write com.apple.finder AppleShowAllFiles -bool true
        # defaults write com.apple.finder AppleShowAllFiles YES
        status = os.system("defaults write com.apple.finder AppleShowAllFiles YES")
        if status == 0:
            self.reload_finder()
        else:
            messagebox.showerror("提示", "设置失败")

    def hide(self):

        # defaults write com.apple.finder AppleShowAllFiles -bool true
        # defaults write com.apple.finder AppleShowAllFiles NO
        status = os.system("defaults write com.apple.finder AppleShowAllFiles NO")
        if status == 0:
            print('设置成功')
            self.reload_finder()
        else:
            messagebox.showerror("提示", "设置失败")

    def reload_finder(self):
        res = os.system("killall Finder")
        if res == 0:
            messagebox.showinfo("提示", "设置成功\n文件管理器重启成功")
        else:
            messagebox.showerror("提示", "设置成功\n但是文件管理器重启失败\n请手动重启或者再试一次")


if __name__ == "__main__":
    App()
