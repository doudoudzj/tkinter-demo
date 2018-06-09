#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 绘制太阳花

import turtle

T = turtle.Turtle()

T.color('red', 'yellow')
T.begin_fill()
while True:
    T.forward(400)
    T.left(170)
    if abs(T.pos()) < 1:
        break
T.end_fill()

turtle.done()
