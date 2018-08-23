#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''标签Label'''

from tkinter import Tk, Label

root = Tk()
root.title('Label')

Label(
    root, anchor='e', bg='blue', fg='red', text='Python', width=30,
    height=5).pack()

Label(
    root,
    bg='red',
    fg='#ddd',
    text='Python GUI\nTkinter',
    justify='left',
    width=30,
    height=5).pack()

Label(
    root,
    bg='green',
    text='Python GUI\nTkinter',
    justify='right',
    width=30,
    height=5).pack()

Label(
    root,
    bg='black',
    fg='white',
    text='Python GUI\nTkinter',
    justify='center',
    width=30,
    height=5).pack()

root.mainloop()