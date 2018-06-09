#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 向列表框添加滚动条

from tkinter import *
window = Tk()
window.title("New England")
yscroll = Scrollbar(window, orient=VERTICAL)
yscroll.grid(row=0, column=2, rowspan=4, padx=(0, 100), pady=5, sticky=NS)
statesList = [
    "Connecticut", "Maine", "Masssachusetts", "New Hampshired",
    "Rhode ISsland", "Vermont"
]
conOFlstNE = StringVar()
lstNE = Listbox(
    window,
    width=14,
    height=4,
    listvariable=conOFlstNE,
    yscrollcommand=yscroll.set)
lstNE.grid(row=0, column=1, rowspan=4, padx=(100, 0), pady=5, sticky=E)
conOFlstNE.set(tuple(statesList))
yscroll["command"] = lstNE.yview
window.mainloop()