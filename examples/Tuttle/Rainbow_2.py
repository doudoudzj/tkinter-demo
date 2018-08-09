#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 彩虹效果 Rainbow

from turtle import *


#控制彩虹路径
def path(pen, r, g, b):
    pen.penup()
    pen.goto(-400, -300)
    pen.pendown()
    pen.pencolor(r, g, b)
    pen.circle(1000, -180)
    pen.pensize(2)
    pen.right(0.05)


#绘制彩虹控制颜色
def Rainbow():
    pen = Turtle()
    pen.right(110)
    r = 255
    g = 0
    b = 0
    interval = 5
    colormode(255)
    # 由红到黄
    while g < 256:
        path(pen, r, g, b)
        g = g + interval
    #由黄到绿
    g = 255
    while r > 0:
        r = r - interval
        path(pen, r, g, b)
    #由绿到青
    r = 0
    while (b < 255):
        b = b + interval
        path(pen, r, g, b)
    b = 255
    #由青到蓝
    while (g > 0):
        g = g - interval
        path(pen, r, g, b)
    #由蓝到紫到红
    g = 0
    while r < 255:
        r = r + interval
        path(pen, r, g, b)


#文字输出
def TextFun():
    text = Turtle()
    text.hideturtle()
    text.color("red")
    text.penup()
    text.setpos(100, -100)
    text.pendown()
    text.write(
        "Rainbow", False, align="center", font=("Script MT Bold", 80, "bold"))


def main():
    setup(800, 600, 0, 0)
    title("rainbow")
    tracer(False)
    Rainbow()
    TextFun()
    tracer(True)
    mainloop()


if __name__ == '__main__':
    main()
