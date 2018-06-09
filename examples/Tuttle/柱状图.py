#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 柱状图

import turtle
heights = [856, 420, 360, 260, 205]


def main():
    t = turtle.Turtle()
    t.hideturtle()
    for i in range(5):
        drawFilledRectangle(t, -200 + (76 * i), 0, 76, heights[i] / 4, "black",
                            "light blue")
    displayText(t)
    turtle.done()


def drawFilledRectangle(t, x, y, w, h, colorP="black", colorF="white"):
    t.pencolor(colorP)
    t.fillcolor(colorF)
    t.up()
    t.goto(x, y)
    t.down()
    t.begin_fill()
    t.goto(x + w, y)
    t.goto(x + w, y + h)
    t.goto(x, y + h)
    t.goto(x, y)
    t.end_fill()


def displayText(t):
    languages = ["haha1", "haha2", "haha3", "haha4", "haha5"]
    t.pencolor("blue")
    t.up()
    for i in range(5):
        t.goto((-162 + 76 * i), heights[i] / 4)
        t.write(str(heights[i]), align="center", font=("Arial", 10, "normal"))
        t.goto((-162 + 76 * i), 10)
        t.write(languages[i], align="center", font=("Arial", 10, "normal"))
        t.goto(-200, -25)
        t.write("haha 统计图", font=("Arial", 10, "normal"))
        t.goto(-200, -45)
        t.write('(哈哈哈哈哈啊哈哈)', font=("Arial", 10, "normal"))


main()