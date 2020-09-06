#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Brownian motion

'''Brownian motion -- an example of a multi-threaded Tkinter program.
python开发_thread_布朗运动
https://www.cnblogs.com/hongten/p/hongten_python_thread_tkinter_brownian.html

注意：bug, 退出异常, 不能退出
下面我将给大家介绍有关python中thread来实现布朗运动的一个例子
'''

import random
import sys
import threading
import time
from tkinter import Tk, Canvas

# 画布大小
WIDTH = 500
HEIGHT = 500
SIGMA = 50
BUZZ = 2
RADIUS = 3
LAMBDA = 10
FILL = 'red'

stop = 0  # Set when main loop exits


def particle(canvas):
    r = RADIUS
    x = random.gauss(WIDTH / 2.0, SIGMA)
    y = random.gauss(HEIGHT / 2.0, SIGMA)
    p = canvas.create_oval(x - r, y - r, x + r, y + r, fill=FILL)
    while not stop:
        dx = random.gauss(0, BUZZ)
        dy = random.gauss(0, BUZZ)
        dt = random.expovariate(LAMBDA)
        try:
            canvas.move(p, dx, dy)
        except TclError:
            break
        time.sleep(dt)


def main():
    global stop
    root = Tk()
    root.title('布朗运动')
    canvas = Canvas(root, width=WIDTH, height=HEIGHT)
    canvas.pack(fill='both', expand=1)
    # 粒子数目
    np = 30
    if sys.argv[1:]:
        np = int(sys.argv[1])
    for i in range(np):
        t = threading.Thread(target=particle, args=(canvas, ))
        t.start()
    try:
        root.mainloop()
    finally:
        stop = 1


main()
