#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 奥运五环

import turtle
p = turtle
p.pensize(6)
p.color("blue")
p.circle(30, 360)
p.pu()
p.goto(60, 0)
p.pd()
p.color("black")
p.circle(30, 360)
p.pu()
p.goto(120, 0)
p.pd()
p.color("red")
p.circle(30, 360)
p.pu()
p.goto(90, -30)
p.pd()
p.color("green")
p.circle(30, 360)
p.pu()
p.goto(30, -30)
p.pd()
p.color("yellow")
p.circle(30, 360)
p.done()
