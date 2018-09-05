#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""Python实现计算器"""

from functools import partial
from tkinter import Tk, Button, Entry
from tkinter.font import Font

from PIL import Image, ImageTk


def get_input(entry, argu):
    entry.insert("end", argu)


def backspace(entry):
    input_len = len(entry.get())
    entry.delete(input_len - 1)


def clear(entry):
    entry.delete(0, "end")


def calc(entry):
    input = entry.get()
    output = str(eval(input.strip()))
    clear(entry)
    entry.insert("end", output)


def App():
    root = Tk()
    root.title("Calculate")
    root.resizable(0, 0)
    root.update()

    entry = Entry(root, justify="right")
    entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

    button_font = Font(size=10)
    button_bg = "#333"
    button_active_bg = "#eee"

    btn = partial(
        Button,
        root,
        bg=button_bg,
        padx=10,
        pady=3,
        font=button_font,
        activeforeground="#fff",
        activebackground=button_active_bg)

    button7 = btn(text="7", command=lambda: get_input(entry, "7"))
    button7.grid(row=1, column=0, pady=5)

    button8 = btn(text="8", command=lambda: get_input(entry, "8"))
    button8.grid(row=1, column=1, pady=5)

    button9 = btn(text="9", command=lambda: get_input(entry, "9"))
    button9.grid(row=1, column=2, pady=5)

    button10 = btn(text="+", command=lambda: get_input(entry, "+"))
    button10.grid(row=1, column=3, pady=5)

    button4 = btn(text="4", command=lambda: get_input(entry, "4"))
    button4.grid(row=2, column=0, pady=5)

    button5 = btn(text="5", command=lambda: get_input(entry, "5"))
    button5.grid(row=2, column=1, pady=5)

    button6 = btn(text="6", command=lambda: get_input(entry, "6"))
    button6.grid(row=2, column=2, pady=5)

    button11 = btn(text="-", command=lambda: get_input(entry, "-"))
    button11.grid(row=2, column=3, pady=5)

    button1 = btn(text="1", command=lambda: get_input(entry, "1"))
    button1.grid(row=3, column=0, pady=5)

    button2 = btn(text="2", command=lambda: get_input(entry, "2"))
    button2.grid(row=3, column=1, pady=5)

    button3 = btn(text="3", command=lambda: get_input(entry, "3"))
    button3.grid(row=3, column=2, pady=5)

    button12 = btn(text="*", command=lambda: get_input(entry, "*"))
    button12.grid(row=3, column=3, pady=5)

    button0 = btn(text="0", command=lambda: get_input(entry, "0"))
    button0.grid(row=4, column=0, columnspan=2, padx=3, pady=5, sticky="nsew")

    button13 = btn(text=".", command=lambda: get_input(entry, "."))
    button13.grid(row=4, column=2, pady=5)

    button14 = btn(text="÷", command=lambda: get_input(entry, "/"))
    button14.grid(row=4, column=3, pady=5)

    button15 = btn(text="<-", command=lambda: backspace(entry))
    button15.grid(row=5, column=0, pady=5)

    button16 = btn(text="C", command=lambda: clear(entry))
    button16.grid(row=5, column=1, pady=5)

    button17 = btn(text="=", command=lambda: calc(entry))
    button17.grid(row=5, column=2, columnspan=2, padx=3, pady=5, sticky="nsew")

    root.mainloop()


if __name__ == "__main__":
    App()
