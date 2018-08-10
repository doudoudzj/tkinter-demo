#!/usr/bin/env python3
#-*- coding: UTF-8 -*-
# pack几何布局管理器
"""
pack()
    Tkinter中包含的所有控件都有pack()方法，它表示调用这个方法的控件，要把自己打包到父组件容器中。
    pack()的参数包含如下六种：
    fill属性：
        说明：
            它表示某个控件在横轴方向或纵轴方向该怎么填充，到底要不要填满。
        值范围：
            X       # 表示这个控件在横轴方向填满父父组件容器，不留空白。
            Y       # 表示这个控件在纵轴方向填满父父组件容器，不留空白。
            BOTH    # 表示这个控件在横纵轴方向都填满父父组件容器，不留空白。
        其实挺抠的，如果不设置任何pack属性，Tkinter给控件的地方能少就少
        如果你看不出来某两个的现象有差别，可能是由于没有设置expand属性
    expand属性：
        说明：
            它表示某个控件在fill那个方向，要不要把空白的地方分配给它。
        值范围：
            True or 1，表示在fill那个方向，把空白处都分给这个控件，让它尽量占满。
            False or 0，表示在fill那个方向，有空也不给它。
    side属性：
        说明：
            它表示某个控件在在它可用的活动空间内，是往哪边停靠。
        值范围：
            LEFT    # 表示尽可能往左边停靠。
            RIGHT   # 表示尽可能往右边停靠。
            TOP     # 表示尽可能往顶部停靠。
            BOTTOM  # 表示尽可能往底部停靠。
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
    anchor属性：
        说明：
            它表示某个控件在容器里的摆放方式，是左还是右，是上还是下
        值范围：
            N       # 表示North，尽可能往北面/上面停靠。
            S       # 表示South，尽可能往南面/下面停靠。
            W       # 表示West，尽可能往西边/左边停靠。
            E       # 表示East，尽可能往东边/右边停靠。
            NE      # 表示NorthEast，尽可能往东北边/右上角停靠。
            NW      # 表示NorthWest，尽可能往西北边/左上角停靠。
            SE      # 表示SouthEast，尽可能往东南边/右下角停靠。
            SW      # 表示SouthWest，尽可能往西南边/左下角停靠。
            NSWE  # 表示四个方向，尽可能往东南西北方向/上下左右四个方向拉伸即铺满整个父容器。
            CENTER  # 尽可能往中心停靠。

"""

from tkinter import *  #导入tkinter模块的所有内容

root = Tk()
root.title("登录")  #窗口标题

f1 = Frame(root)
f1.pack()  #界面分为三个Frame
f2 = Frame(root)
f2.pack()
f3 = Frame(root)
f3.pack()
Label(f1, text="用户名").pack(side=LEFT)  #标签放置在f1中，左停靠
Entry(f1).pack(side=LEFT)  #单行文本框放置在f1中，左停靠
Label(f2, text="密  码").pack(side=LEFT)  #标签放置在f2中，左停靠
Entry(f2, show="*").pack(side=LEFT)  #单行文本框放置在f2中，左停靠
Button(f3, text="取消").pack(side=RIGHT)  #取消按钮放置在f3中，右停靠
Button(f3, text="登录").pack(side=RIGHT)  #登录按钮放置在f3中，右停靠

root.mainloop()
