from os import path
from tkinter import Tk, PhotoImage
from tkinter import ttk

root = Tk()

d = path.dirname(__file__)  #返回当前文件所在的目录
image = PhotoImage(file=d + "/demo_image.gif").subsample(10, 10)

treeview = ttk.Treeview(root)
treeview.insert("", "1", "item1", text="First Item")
treeview.insert("", "2", "item2", text="Second Item")
treeview.insert("", "end", "item3", text="Third Item")
treeview.insert("", "end", "item4", text="Fourth Item")
treeview.insert("item2", "end", "image1", text="图片", image=image)
treeview.config(height="5")
treeview.pack()

root.mainloop()
