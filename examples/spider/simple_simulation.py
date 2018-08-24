#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''模拟爬虫'''
'''
界面：左侧是单选框，右侧是信息显示框，下方是按扭
功能：点击开始爬取按扭，则会自动执行函数，显示在文本框中
indicatoron = 0  改变单选框按扭样式
'''

import time
from tkinter import END, Button, Label, Radiobutton, StringVar, Tk
from tkinter.scrolledtext import ScrolledText

root = Tk()
root.title('模拟爬虫')  # 标题
text = ScrolledText(root, font=('微软雅黑'))  # 滚动框
text.grid(row=0, column=1, rowspan=4)

var = StringVar()
var.set('准备中……')

data = [('wdcs', '我的测试'), ('yylh', '一起来嗨'), ('jwbs', '今晚不睡'), ('yqtx', '一起通宵')]


# 滚动框输出项
def sl():
    for i in range(100):
        print(var.get())  # 当单选扭被按下后，可以获取其var值
        time.sleep(0.1)
        text.insert(END, str(i) + '\n')  # 向文本框写入数据
        text.see(END)  # 始终显示文本框的底部
        text.update()  # 实时显示文本框内容
    var.set('爬取完成')


# 添加按扭及标签
Button(root, text='开始爬取', font=('微软雅黑'), command=sl).grid(row=4, column=1)

# 按扭下面爬取进程说明
Label(root, fg='red', textvariable=var).grid(row=5, column=1)

# 定义多个单选框
count = 0
for each in data:
    Radiobutton(
        root, text=each[1], variable=var, value=each[0]).grid(
            row=count, column=0, sticky='w')
    count += 1

root.mainloop()
