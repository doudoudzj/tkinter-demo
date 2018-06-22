#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 使用Turtle库绘制三角形开始到圆形各个图案

import turtle


def main():
    # pensize()  画笔大小
    turtle.pensize(3)
    # penup/down()   提起笔/放下
    turtle.penup()
    # goto()   画笔至（x,y）点
    turtle.goto(-200, -50)
    turtle.pendown()
    # begin/end_fill()   开始/结束填充
    turtle.begin_fill()
    turtle.color("red")
    # circle()   绘制图形，其中steps=n，n边形，若steps缺省则为圆
    turtle.circle(40, steps=3)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(-100, -50)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("blue")
    turtle.circle(40, steps=4)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(0, -50)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("green")
    turtle.circle(40, steps=5)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(100, -50)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("yellow")
    turtle.circle(40, steps=6)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(200, -50)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("purple")
    turtle.circle(40)
    turtle.end_fill()

    turtle.color("green")
    turtle.penup()
    turtle.goto(-100, 50)
    turtle.pendown()
    turtle.write(
        ("Cool Colorful shapes"),
        # font()   文本参数：字体，大小，样式
        font=("Times", 18, "bold"))
    turtle.hideturtle()

    turtle.done()


if __name__ == '__main__':
    main()
