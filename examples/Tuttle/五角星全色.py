from random import *
from math import *
from turtle import *


def main():
    p = Turtle()
    p.speed(3)
    p.pensize(5)
    p.pencolor("black")
    p.fillcolor("yellow")
    p.begin_fill()
    for i in range(5):
        p.forward(200)
        p.right(144)
    p.end_fill()
    done()


main()