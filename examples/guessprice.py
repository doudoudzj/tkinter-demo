#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# python学习——tkinter实战（猜价格）
# https://www.cnblogs.com/xiaobingbing/p/8017010.html

import tkinter
import tkinter.messagebox
import random


class guessprice:
    # 界面布局方法
    def __init__(self):
        # 创建主界面，并且保存到成员属性中
        self.root = tkinter.Tk()
        self.root.minsize(240, 200)
        self.root.maxsize(240, 200)
        self.root.title('价格竞猜小游戏1.0版')
        # 设置显示面板的变量
        self.result = tkinter.IntVar()
        self.result.set('')
        self.truenum = random.randint(1, 100)  # 随机一个数字作为答案
        # 界面布局
        self.menus()
        self.layout()
        self.root.mainloop()

    # 菜单界面的摆放
    def menus(self):
        # 添加菜单
        # 创建总菜单
        allmenu = tkinter.Menu(self.root)
        # 添加子菜单1
        filemenu = tkinter.Menu(allmenu, tearoff=0)
        allmenu.add_cascade(label='开始', menu=filemenu)
        filemenu.add_command(label='并没有啥', command=self.bmys)
        self.root.config(menu=allmenu)
        # 添加子菜单2
        filemenu = tkinter.Menu(allmenu, tearoff=0)
        allmenu.add_cascade(label='查看', menu=filemenu)
        filemenu.add_command(label='作者', command=self.zz)
        filemenu.add_command(label='联系方式', command=self.lxfs)
        # 添加分割线
        filemenu.add_separator()
        filemenu.add_command(label='版本号', command=self.bbh)

        self.root.config(menu=allmenu)

    # 主界面的摆放
    def layout(self):
        # 描述标签1
        label1 = tkinter.Label(self.root, text='请输入要\n竞猜的价格：')
        label1.place(x=5, y=0, height=80, width=80)
        # 输入文本框1
        entry1 = tkinter.Entry(self.root,
                               bd=3,
                               font=('宋体', 15),
                               textvariable=self.result)
        entry1.place(x=90, y=20, height=40, width=115)
        # 单位标签2
        label2 = tkinter.Label(self.root, text='元', font=('宋体', 15))
        label2.place(x=210, y=0, height=80, width=30)
        # 说明标签3
        label3 = tkinter.Label(self.root, text='(正确的价格在1-100之间，少侠努力呦～)')
        label3.place(x=5, y=65, height=30, width=230)
        # 确定按钮1
        btn1 = tkinter.Button(self.root, text='确定', bd=3, command=self.queding)
        btn1.place(x=10, y=105, height=40, width=100)
        # 查看正确答案按钮2
        btn2 = tkinter.Button(self.root,
                              text='查看正确答案',
                              bd=3,
                              command=self.ckda)
        btn2.place(x=130, y=105, height=40, width=100)

    # 操作函数
    # 菜单部分
    # 版本号设置
    def bbh(self):
        tkinter.messagebox.showinfo('', '上面明明写着1.0，还问。。。')

    # 联系方式设置
    def lxfs(self):
        tkinter.messagebox.showinfo('', '这么想要作者的联系方式啊= =')

    # 作者设置
    def zz(self):
        tkinter.messagebox.showinfo('', '小饼饼～是不是萌萌哒')

    # 并没有啥设置
    def bmys(self):
        tkinter.messagebox.showinfo('', '0.0真的没啥,棒棒糖也没有')

    # 功能部分
    # 确定按钮的设置
    def queding(self):
        guess = self.result.get()  # 获取输入框中的数字，以备稍后的对比之用
        # 对输入的数字和随机选取的数字进行大小比对
        if guess == self.truenum:
            tkinter.messagebox.showinfo('', '哎呦不错哦，猜对了')
            self.truenum = random.randint(1, 100)
            self.result.set('')  # 清空之前在输入框中输入过的数字
        else:
            if guess > self.truenum:
                tkinter.messagebox.showinfo('', '猜的大了')
                self.result.set('')  # 清空之前在输入框中输入过的数字
            else:
                tkinter.messagebox.showinfo('', '猜的小了')
                self.result.set('')  # 清空之前在输入框中输入过的数字

    # 查看答案按钮的设置
    def ckda(self):
        global truenum
        tkinter.messagebox.showinfo('', self.truenum)
        self.truenum = random.randint(1, 100)  # 保证在查看完答案之后直接开启随机数字并可以进行下一次游戏


if __name__ == "__main__":
    myguessprice = guessprice()
