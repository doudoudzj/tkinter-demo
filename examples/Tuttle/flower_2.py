# Turtle 库绘制一棵西兰花
'''
Turtle库是Python中一个强大的绘制图像的函数库，灵活使用Turtle库可以绘制各种好看的图像。 
下面介绍使用Turtle库绘制一棵西兰花。

绘制一棵西兰花，从主干出发以一定的角度向左向右生成对称的枝干，再从每个枝干出发向左向右生成对称的枝干，循环此动作，并最终绘制出一棵漂亮的西兰花。
'''
'''首先导入Turtle库，并设置画笔大小、画笔速度及颜色，并隐藏画笔

p = Turtle()
p.pensize(5)
# p.color(clr)
p.hideturtle()
p.getscreen().tracer(30, 0)

设置起始方向以及位置（屏幕中心为坐标原点）
p.left(90)
p.penup()
p.goto(x, y)
p.pendown()

设置画笔完成之后，开始绘制西兰花，首先绘制从开始画位置向着预定的方向前进一段距离，并向左向右分成两个对称的分支
p.forward(l)
q = p.clone()
p.left(a)
q.right(a)
'''

from turtle import Turtle
# 每完成一次分支后就将两个分支对象添加到list中，并通过遍历list完成整个图像的绘制
def tree(plist, l, a, f):
    if l > 5:
        lst = []
        for p in plist:
            p.forward(l)
            q = p.clone()
            p.left(a)
            q.right(a)
            lst.append(p)
            lst.append(q)
        tree(lst, l * f, a, f)


# 在程序中通过递归调用完成了一棵西兰花的绘制。
# 程序剩余代码如下：
def maketree(x, y, clr):
    p = Turtle()
    p.pensize(5)
    p.color(clr)
    p.hideturtle()
    p.getscreen().tracer(30, 0)
    #p.speed(10)
    p.left(90)
    p.penup()
    p.goto(x, y)
    p.pendown()
    t = tree([p], 200, 20, 0.6375)
    #print(len(p.getscreen().turtles()))


def main():
    maketree(0, -300, "green")
    


main()
