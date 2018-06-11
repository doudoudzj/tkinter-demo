#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from tkinter import *
import search

root = Tk()  # 创建窗口对象的背景色


# mp3 = search.searchMusic(searchInputKey)


# 搜索框
searchInputKey = StringVar()
searchInput = Entry(root, textvariable=searchInputKey)
searchInput.pack()

# 搜索指令
def searchCommand():
    mp3 = search.searchMusic(searchInputKey.get())
    for item in mp3:  # 第二个小部件插入数据
        searchList.insert(0, item)

# 点击搜索
searchButton = Button(root, text="搜索", command=searchCommand)
searchButton.pack()

# 搜到的列表
searchList = Listbox(root)
# for item in mp3:  # 第二个小部件插入数据
#     searchList.insert(0, item)
searchList.pack()









# print(search.searchMusic('我们不一样'))


root.mainloop()  # 进入消息循环
