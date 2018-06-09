#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# 首先等边三角形：
# 等边三角形刚开始用的是这种比较暴力的方式：
# 使得程序非常的冗长。

import turtle
'''
turtle.seth(0)
turtle.fd(100)
turtle.seth(120)
turtle.fd(100)
turtle.seth(240)
turtle.fd(100)
'''
# 然后细看代码可以发现重复的地方，阅读了下文档，发现有left()这么个好东西。
# 然后就有了以下的代码：

p = turtle
p.pensize(5)  # 画笔的粗为10
# 循环语句，循环三次
for i in range(3):
    p.forward(100)  # 向前走100默认方向为x轴正方向
    p.left(120)  # 左转120°

turtle.done()
