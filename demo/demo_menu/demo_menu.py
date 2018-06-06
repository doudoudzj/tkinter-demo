from tkinter import *

ROOT = Tk()
ROOT.option_add('*tearOff', False)

MENUBAR = Menu(ROOT)
ROOT.config(menu=MENUBAR)

File = Menu(MENUBAR)
Edit = Menu(MENUBAR)
Help_ = Menu(MENUBAR)

MENUBAR.add_cascade(menu=File, label='File')
MENUBAR.add_cascade(menu=Edit, label='Edit')
MENUBAR.add_cascade(menu=Help_, label='Help')

File.add_command(label='新建', command=lambda: print(" New File"))
File.add_separator()
File.add_command(label='打开', command=lambda: print("Open File"))
File.add_separator()
SAVE = Menu(File)
File.add_cascade(menu=SAVE, label='保存')
SAVE.add_command(label='保存为', command=lambda: print(" Save as"))
SAVE.add_command(label='保存所有', command=lambda: print(" Save all"))

ROOT.mainloop()
