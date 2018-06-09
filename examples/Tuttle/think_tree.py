#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 利用广度优先遍历思想画树

from random import *
from math import *
from turtle import *


def tree(plist, l, a, f):
    if l > 2:
        nextlist = []
        for p in plist:
            p.forward(l)
            q = p.clone()
            p.left(a)
            q.right(a)
            nextlist.append(p)
            nextlist.append(q)
        tree(nextlist, l * f, a, f)


def main():
    p = Turtle()
    p.color("green")
    p.speed(10)
    p.pensize(1)
    p.left(90)
    p.hideturtle()  #隐藏箭头
    p.penup()  #抬笔
    p.goto(-100, -100)
    p.pendown()  #落笔
    tree([p], 90, 60, 0.65)
    done()


main()