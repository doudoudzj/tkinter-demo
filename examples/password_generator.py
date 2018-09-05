#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""密码生成程序"""

import random
import sys
from tkinter import Button, Entry, Frame, IntVar, Label, Radiobutton, StringVar, Tk

import clipboard


class PasswordGenerator():
    def __init__(self):
        root = Tk()
        root.title('密码生成器')
        root.update()

        self.root = root
        self.ps_length = IntVar(value=8)
        self.ps_level = IntVar(value=3)
        self.password = StringVar()

        self.load_view()
        root.mainloop()

    def load_view(self):

        f1 = Frame(self.root)
        f1.pack(padx=10, pady=5)

        Label(f1, text="密码长度：").grid(row=0, column=0)

        f1r = Frame(f1)
        f1r.grid(row=0, column=1)

        Entry(
            f1r,
            textvariable=self.ps_length,
            width=5,
            validate="key",
            validatecommand=(self.test, '%P')).grid(
                row=0, column=1)

        Button(f1r, text="+", command=self.calcPlus).grid(row=0, column=2)
        Button(f1r, text="-", command=self.calcSubt).grid(row=0, column=3)

        Label(f1, text="密码强度：").grid(row=1, column=0)

        f1rb = Frame(f1)
        f1rb.grid(row=1, column=1)

        Radiobutton(
            f1rb, text="简单", variable=self.ps_level, value=1).grid(
                row=1, column=1)
        Radiobutton(
            f1rb, text="一般", variable=self.ps_level, value=3).grid(
                row=1, column=2)
        Radiobutton(
            f1rb, text="复杂", variable=self.ps_level, value=4).grid(
                row=1, column=3)

        Entry(self.root, textvariable=self.password, state="readonly").pack()

        submit = Button(self.root, text="生成密码并复制到剪切板", command=self.getPw)
        submit.pack()

    def cutLength(self):
        res = []
        for i in range(self.ps_level.get(), 1, -1):
            res.append(
                random.randint(1,
                               self.ps_length.get() - sum(res) - i + 1))
        res.append(self.ps_length.get() - sum(res))
        random.shuffle(res)
        return res

    def makePassword(self, dists, arr):
        res = []
        for i in range(len(arr)):
            for j in range(arr[i]):
                res += random.choice(dists[i])
        random.shuffle(res)
        return ''.join(res)

    def getPassword(self):
        arr = self.cutLength()
        str1 = '01'
        str2 = '23456789'
        str3 = 'abcdefghijkmnpqrstuvwxyz'
        str4 = 'ABCDEFGHJKMNPQRSTUVWXYZ'
        str5 = '_@!,.:;-=+/?'

        dists = {
            1: [str1 + str2],
            3: [str2, str3, str4],
            4: [str2, str3, str4, str5]
        }
        return self.makePassword(dists[self.ps_level.get()], arr)

    def test(self, res):
        if res.isdigit():
            return int(res) > 4
        else:
            return False

    def calcPlus(self):
        self.ps_length.set(self.ps_length.get() + 1)

    def calcSubt(self):
        lengVal = self.ps_length.get()
        if lengVal > 4:
            self.ps_length.set(lengVal - 1)

    def getPw(self):
        res = self.getPassword()
        clipboard.copy(res)
        self.password.set(res)


if __name__ == "__main__":
    PasswordGenerator()
