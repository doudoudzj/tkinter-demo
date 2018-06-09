#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 分形图形

import turtle



def main():
    T = turtle.Turtle()
    T.hideturtle()
    T.speed(10)
    level = 12
    fract(T, -80, 60, 80, 60, level)
    turtle.done()


def fract(T, x1, y1, x2, y2, level):
    newX = 0
    newY = 0
    if level == 0:
        drawLine(T, x1, y1, x2, y2)
    else:
        newX = (x1 + x2) / 2 + (y2 - y1) / 2
        newY = (y1 + y2) / 2 - (x2 - x1) / 2
        fract(T, x1, y1, newX, newY, level - 1)
        fract(T, newX, newY, x2, y2, level - 1)


def drawLine(T, x1, y1, x2, y2):
    T.up()
    T.goto(x1, y1)
    T.down()
    T.goto(x2, y2)


main()