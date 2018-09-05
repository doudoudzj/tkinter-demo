#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""显示系统隐藏的文件-Mac"""
import os
from tkinter import Button, Tk


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

        b1 = Button(root, text="显示隐藏文件", command=self.show)
        b1.pack(expand="yes")

        b2 = Button(root, text="不显示隐藏文件", command=self.hide)
        b2.pack(expand="yes")

        root.mainloop()  # 进入消息循环
        self.root = root

    def show(self):

        # defaults write com.apple.finder AppleShowAllFiles -bool true
        # defaults write com.apple.finder AppleShowAllFiles YES
        os.system("defaults write com.apple.finder AppleShowAllFiles YES")

    def hide(self):

        # defaults write com.apple.finder AppleShowAllFiles -bool true
        # defaults write com.apple.finder AppleShowAllFiles NO
        os.system("defaults write com.apple.finder AppleShowAllFiles NO")


if __name__ == "__main__":
    App()
