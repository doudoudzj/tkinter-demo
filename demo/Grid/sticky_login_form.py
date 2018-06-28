#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import tkinter as gui

master = gui.Tk()
master.resizable(False, False)
var = gui.IntVar()

gui.Label(master, text="账号").grid(row=0, sticky=gui.W, pady=5)
gui.Label(master, text="密码").grid(row=1, sticky=gui.W, pady=5)

gui.Entry(master).grid(row=0, column=1)
gui.Entry(master).grid(row=1, column=1)

gui.Button(
    master, text="登陆").grid(
        row=0,
        column=2,
        rowspan=3,
        ipadx=15,
        pady=5,
        ipady=20,
        sticky=gui.W+gui.E+gui.N+gui.S)

gui.Checkbutton(
    master, text='记住密码', variable=var).grid(
        row=2, column=1, sticky=gui.W)

gui.Button(
    master, text="登陆").grid(
        row=2,
        column=1,
        ipadx=8,
        pady=5,
        sticky=gui.E+gui.N+gui.S)

gui.mainloop()
