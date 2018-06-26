# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 画布，使用Canvas小构件
# http://www.cnblogs.com/libra-yong/p/6368816.html
# http://www.cnblogs.com/gao241/p/3522155.html

import tkinter as gui


class demo:
    def __init__(self):
        window = gui.Tk()
        window.title("Canvas Demo")

        # 在窗口画布
        self.canvas = gui.Canvas(window, width=200, height=200, bg="white")
        self.canvas.pack()

        # 创建frame的框架，窗口window为这个框架的父容器
        frame = gui.Frame(window)
        frame.pack()

        # frame框架作为Button的父容器
        btRectangle = gui.Button(frame, text="矩形", command=self.displayRect)
        btOval = gui.Button(frame, text="椭圆", command=self.displayOval)
        btArc = gui.Button(frame, text="圆弧", command=self.displayArc)
        btPolygon = gui.Button(frame, text="多边形", command=self.displayPolygon)
        btLine = gui.Button(frame, text="线段", command=self.displayLine)
        btString = gui.Button(frame, text="文本", command=self.displayString)
        btClear = gui.Button(frame, text="清空", command=self.displayClear)

        # Button在画布上布局
        # btRectangle.grid(row=1, column=1)
        # btOval.grid(row=1, column=2)
        # btArc.grid(row=1, column=3)
        # btPolygon.grid(row=1, column=4)
        # btLine.grid(row=1, column=5)
        # btString.grid(row=1, column=6)
        # btClear.grid(row=1, column=7)

        # Button可以循环处理做布局
        clu = 0
        but = [btRectangle, btOval, btArc, btPolygon, btLine, btString, btClear]
        for i in but:
            clu += 1
            i.grid(row=1, column=clu)

        # 创建事件循环直到关闭主窗口
        window.mainloop()

    # 画个矩形, 正方形
    def displayRect(self):
        self.canvas.create_rectangle(10, 10, 190, 190, tags="rect")

    # fill填充oval的颜色
    def displayOval(self):
        self.canvas.create_oval(10, 10, 190, 190, fill="red", tags="oval")

    # start为开始的度数，extent为要转的度数.全部以逆时针为正方向，0为x轴正方向
    def displayArc(self):
        self.canvas.create_arc(
            10,
            10,
            190,
            190,
            start=0,
            extent=90,
            width=8,
            fill="red",
            tags="arc")

    def displayPolygon(self):
        self.canvas.create_polygon(10, 10, 190, 90, 10, 90, tags="polygon")

    # arrow表示line指向，activefill：当鼠标在line上时出现的特定风格，本例中鼠标移动到第二个line上时line变蓝
    def displayLine(self):
        self.canvas.create_line(10, 10, 190, 190, fill="red", tags="line")
        self.canvas.create_line(
            10,
            90,
            190,
            10,
            width=9,
            arrow="first",
            activefill="blue",
            tags="line")

    # font定义字体（字体名，大小，风格）
    def displayString(self):
        self.canvas.create_text(
            100,
            40,
            text="crogram.com",
            font="time 10 bold underline",
            tags="string")

    # delete方法通过tags参数从画布上删除图形
    def displayClear(self):
        self.canvas.delete("rect", "oval", "arc", "polygon", "line", "string")


demo()