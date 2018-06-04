#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# https://blog.csdn.net/happen23/article/details/78763530

import tkinter as tk
from PIL import Image, ImageTk


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, width=400, height=300)
        self.pack()
        self.pilImage = Image.open("20170507214352664.png")
        self.tkImage = ImageTk.PhotoImage(image=self.pilImage)
        self.label = tk.Label(self, image=self.tkImage)
        self.label.pack()

    def processEvent(self, event):
        pass


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()