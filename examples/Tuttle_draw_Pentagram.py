#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 画五角星Pentagram

from turtle import *


def draw():
    fillcolor("red")  #设置填充颜色
    speed(8)
    pensize(2)  # 画笔粗细
    begin_fill()
    while True:
        forward(200)  #设置五角星的大小
        right(144)
        if abs(pos()) < 1:
            break
    end_fill()


# 主程序
def main():
    draw()
    done()


if __name__ == '__main__':
    main()
