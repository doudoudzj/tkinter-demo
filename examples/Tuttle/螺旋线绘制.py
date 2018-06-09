#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 螺旋线绘制

import turtle
import time

turtle.speed("fastest")
turtle.pensize(2)
for x in range(100):
    turtle.forward(2 * x)
    # 角度的控制
    # 不同的值不同, 绘制的图像会不同
    turtle.left(90)
time.sleep(3)

turtle.done()
