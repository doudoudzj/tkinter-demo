#!/usr/bin/env python3
#-*- coding: UTF-8 -*-
from tkinter import Tk, Button

root = Tk()

Button(root, text='A').pack(side='left', expand='yes', fill='y')
Button(root, text='B').pack(side='top', expand='yes', fill='both')
Button(root, text='C').pack(side='right', expand='yes', fill='none')
Button(root, text='D').pack(side='left', expand='no', fill='y')
Button(root, text='E').pack(side='top', expand='yes', fill='both')
Button(root, text='F').pack(side='bottom', expand='yes')
Button(root, text='G').pack(anchor='se')

root.mainloop()