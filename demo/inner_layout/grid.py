#!/usr/bin/env python3
#-*- coding: UTF-8 -*-
# grid 几何布局管理器
"""
grid()
    pack()固然有它的优势和用武之地，但是它需要借助诸如Frame（或者ttk.Frame），PanedWindow等等这样的容器来实现对齐、排版、布局等等。
    注：ttk，theme tkinter，继承了Tkinter并覆盖了一些方法，比自带的Tkinter具有更美观的效果。用法几乎是一样的。
    老版的Tkinter没有集成，需要自己pip install，8.x之后的Tkinter都自带ttk了。

    相比之下，Tkinter每一个控件都有的grid()方法就是一个神器了。布局排版很简单，不需要借助Frame什么的，只通过设置row和column属性，即可让它自动对齐到网格。
    当然，其他属性可以帮助设置的更好看。
    注意！！！在同一个主窗口中，要么就都用pack()，要么就都用grid()！！混着用，grid()无效！！
    grid()的参数包含如下五种：
    row和column属性：
        说明：
            它表示某个控件要放在第几行网格或第几列网格。
        值范围：
            整数，当然，都是从0开始计的。
    rowspan和columnspan属性：
        说明：
            它表示某个控件将会竖着跨几行或横着跨几列。
        值范围：
            整数，默认都是1，最小值为1
    padx和pady属性：
        说明：
            表示某个控件的外边距，即控件边缘和这个控件所在容器之间的间距
            padx是X轴方向，即左右外边距
            pady是Y轴方向，即上线外边距
        单位：
            像素
    ipadx和ipady属性：
        说明：
            它表示某个控件的内边距，即控件边缘和此控件内显示的内容(文字图片什么的)之间的间距
            ipadx是X轴方向，即左右内边距
            ipady是Y轴方向，即上线内边距
        单位：
            像素
    sticky属性（这个有点类似pack()的anchor）：
        说明：
            它表示某个控件在网格里的摆放方式，是左还是右，是上还是下
        值范围：
            "N"         # 表示North，尽可能往北面/上面停靠。
            "S"         # 表示South，尽可能往南面/下面停靠。
            "W"         # 表示West，尽可能往西边/左边停靠。
            "E"         # 表示East，尽可能往东边/右边停靠。
            "NS"        # 表示NorthSouth，尽可能往南北方向/上下拉伸。
            "EW"        # 表示EastWest，尽可能往东西方向/左右拉伸。
            "NSWE"      # 表示四个方向，尽可能往东南西北方向/上下左右拉伸即铺满整个父容器。
            "CENTER"    # 尽可能往中心停靠。
        例子：
            Button(text="1行1列").grid(row=0, column=0)
            Button(text="1行2列").grid(row=0, column=1)
            Button(text="1行3列横跨两列靠右").grid(row=0, column=2, columnspan=2, sticky=E)
            Label(text="空白").grid(row=0, column=4)
            Button(text="2行1列").grid(row=1, column=0)
            Button(text="2行2列").grid(row=1, column=1, sticky=W)
            Button(text="2行2列").grid(row=1, column=1, sticky=E)
            Button(text="2行3列").grid(row=1, column=2)
            Button(text="2行4列").grid(row=1, column=3)
            Button(text="2行5列").grid(row=1, column=4)
"""

from tkinter import Tk, Button, Label

root = Tk()
root.title("grid布局")


Button(root, text="1").grid(row=0, column=0, padx=2, ipadx=20)  # 按钮1放置于1行1列
Button(root, text="2").grid(row=0, column=1, padx=2, ipadx=20)  # 按钮2放置于1行2列
Button(root, text="3").grid(row=0, column=2, padx=2, ipadx=20)  # 按钮3放置于1行3列
Button(root, text="4").grid(row=1, column=0, padx=2, ipadx=20)  # 按钮4放置于2行1列
Button(root, text="5").grid(row=1, column=1, padx=2, ipadx=20)  # 按钮5放置于2行2列
Button(root, text="6").grid(row=1, column=2, padx=2, ipadx=20)  # 按钮6放置于2行3列
Button(root, text="7").grid(row=2, column=0, padx=2, ipadx=20)  # 按钮7放置于3行1列
Button(root, text="8").grid(row=2, column=1, padx=2, ipadx=20)  # 按钮8放置于3行2列
Button(root, text="9").grid(row=2, column=2, padx=2, ipadx=20)  # 按钮9放置于3行3列
Button(root, text="0").grid(row=3, column=0, padx=2, ipadx=20, columnspan=2, sticky="ew")  # 跨两列，左右紧贴
Button(root, text=".").grid(row=3, column=2, padx=2, ipadx=20, sticky="ew")  # 左右紧贴
Label(root, text="grid布局").grid(row=4, column=0, padx=2, ipadx=20, columnspan=3, sticky="ew")  # 左右紧贴


root.mainloop()
