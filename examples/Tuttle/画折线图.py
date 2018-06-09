#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 画折线图

import turtle
yValues = [10.0, 7.4, 6.4, 5.3, 4.4, 3.7, 2.6]


def main():
    t = turtle.Turtle()
    t.hideturtle()
    drawLine(t, 0, 0, 300, 0)  #画x轴
    drawLine(t, 0, 0, 0, 175)  #画y轴
    #画折线
    for i in range(6):
        drawLineWithDots(t, 40 + (40 * i), 15 * yValues[i],
                         40 + (40 * (i + 1)), 15 * (yValues[i + 1]), "blue")
    drawTickMarks(t)
    #给图上x y 轴上的间距点表上值
    displayText(t)
    turtle.done()


def drawLine(t, x1, y1, x2, y2, colorP="black"):
    t.up()
    t.goto(x1, y1)
    t.down()
    t.pencolor(colorP)
    t.goto(x2, y2)


def drawLineWithDots(t, x1, y1, x2, y2, colorP="black"):
    t.pencolor(colorP)
    t.up()
    t.goto(x1, y1)
    t.dot(5)
    t.down()
    t.goto(x2, y2)
    t.dot(5)


def drawTickMarks(t):
    for i in range(1, 8):
        drawLine(t, 40 * i, 0, 40 * i, 10)  #画x轴上的间距点
    drawLine(t, 0, 15 * max(yValues), 10, 15 * max(yValues))  #画出y轴最上面的那一个点
    drawLine(t, 0, 15 * min(yValues), 10, 15 * min(yValues))  #画出y轴最下面的那一个点


def displayText(t):
    t.pencolor("blue")
    t.up()
    #在对应的位置标出10.0
    t.goto(-10, (15 * max(yValues)) - 8)
    t.write(max(yValues), align="center")
    #再对应的位置标出2.6
    t.goto(-10, (15 * min(yValues)) - 8)
    t.write(min(yValues), align="center")
    #标出x轴上对应的点
    x = 40
    for i in range(2000, 2013, 2):
        t.goto(x, -20)
        t.write(str(i), align="center")
        x += 40
    #在这张折线图下方给点说明
    t.goto(0, -50)
    t.write("大学生吸烟率情况分析图", font=("Arial", 16, "normal"))


main()
