# 使用turtle库绘制七段数码管样式的系统当前日期
# https://blog.csdn.net/Daniel960601/article/details/79152814
import turtle, datetime


def drawLine(draw):  #绘制数码管的每一段
    if (draw):
        turtle.down()
    else:
        turtle.up()

    turtle.fd(40)
    turtle.right(90)


def drawDigit(i):  #绘制数码管的每个数字
    if i in [2, 3, 4, 5, 6, 8, 9]:
        drawLine(True)
    else:
        drawLine(False)

    if i in [0, 1, 3, 4, 5, 6, 7, 8, 9]:
        drawLine(True)
    else:
        drawLine(False)

    if i in [0, 2, 3, 5, 6, 8]:
        drawLine(True)
    else:
        drawLine(False)

    if i in [0, 2, 6, 8]:
        drawLine(True)
    else:
        drawLine(False)

    turtle.left(90)

    if i in [0, 4, 5, 6, 8, 9]:
        drawLine(True)
    else:
        drawLine(False)

    if i in [0, 2, 3, 5, 6, 7, 8, 9]:
        drawLine(True)
    else:
        drawLine(False)

    if i in [0, 1, 2, 3, 4, 7, 8, 9]:
        drawLine(True)
    else:
        drawLine(False)

    turtle.right(180)
    turtle.penup()
    turtle.fd(20)


def drawData(time):  #绘制日期
    for i in time:
        drawDigit(eval(i))


def main():
    turtle.setup(800, 350, 200, 200)
    turtle.speed(100)
    turtle.pensize(5)
    turtle.penup()
    turtle.fd(-300)
    turtle.hideturtle()
    drawData(datetime.datetime.now().strftime('%Y%m%d'))
    turtle.mainloop()


main()
