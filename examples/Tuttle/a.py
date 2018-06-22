#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 画矩形立方体
# 楼梯, 笑脸：）

import turtle
# 画矩形立方体


def draw_cube(i):
    turtle.begin_fill()
    turtle.color("red")
    turtle.goto(i, i * 3)
    turtle.goto(100 + i, i * 3)
    turtle.goto(100 + i, 20 + i * 3)
    turtle.goto(i, 20 + i * 3)
    turtle.goto(i, i * 3)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(i, 20 + i * 3)
    turtle.pendown()
    turtle.goto(10 + i, 30 + i * 3)
    turtle.goto(110 + i, 30 + i * 3)
    turtle.goto(110 + i, 10 + i * 3)
    turtle.goto(100 + i, i * 3)
    turtle.penup()
    turtle.goto(100 + i, 20 + i * 3)
    turtle.pendown()
    turtle.goto(110 + i, 30 + i * 3)
# 画笑脸


def draw_smile_face(x, y):
    turtle.goto(x + 50, y)
    turtle.pensize(1.5)
 # 脸部
    turtle.circle(20)
    turtle.penup()
# 眼睛
    turtle.goto(x + 40, y + 20)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("red")
    turtle.circle(3)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(x + 60, y + 20)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("red")
    turtle.circle(3)
    turtle.end_fill()
    turtle.penup()
 # 嘴巴
    turtle.goto(x + 45, y + 10)
    turtle.pendown()
    turtle.right(90)
    turtle.pensize(2)
    turtle.circle(5, 180)


def main():
    turtle.speed(2)
    for i in range(0, 100, 10):
        draw_cube(i)
        draw_smile_face(100, 300)
        turtle.hideturtle()


main()
