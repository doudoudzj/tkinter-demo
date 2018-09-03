# Menu

> 菜单控件: 显示菜单栏, 下拉菜单和弹出菜单

##### 使用：

```python
#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# demo.py
"""菜单 demo"""

from tkinter import Tk, Menu
root = Tk()

# 创建菜单
menubar = Menu(root)

# 创建菜单，作为下拉菜单列表，是menubar的下一级
filemenu = Menu(menubar)

# 将下拉菜单filemenu放入菜单栏menubar上，直接依次显示
menubar.add_cascade(label="文件", menu=filemenu)

# 将菜单项添加到下拉菜单里，是filemenu的下一级
filemenu.add_command(label="文件打开")
filemenu.add_command(label="文件保存")
filemenu.add_command(label="文件关闭")

# 将菜单menubar放到窗口上，成为窗口菜单栏
root.config(menu=menubar)
# or
root["menu"] = menubar
root.mainloop()
```

##### 参数

-   command

    说明：设置回调函数
    注意：在窗口菜单栏上的根节点菜单不生效

##### 函数

-   add_cascade()

    说明：添加级联菜单，主要用作下拉菜单的父节点，用于承载下级菜单的，可以认为是一个label
    用途：
        1. 可以作为一级菜单项显示在根节点上，同时需要在此菜单内添加add_command以作为下拉菜单里的菜单项
        2. 亦可以添加add_cascade以增加一个下一级的下拉级联菜单

-   add_checkbutton()

    说明：添加可选按钮项

-   add_command()

    说明：添加命令菜单项，参数command用来执行回调函数

    用途：

        1. 作为最终菜单项显示在菜单下拉列表内
        2. 也可以作为一级菜单项添加到根节点上，但是在窗口菜单栏里是不生效的！

    参数：

        -   accelerator，用于添加菜单的快捷键，该选项仅显示，并没有实现加速键的功能，添加功能需按键绑定
        -   command，绑定事件
        例如：
        filemenu.add_command(label="打开", command=callback, accelerator='Ctrl+N')
        root.bind_all("<Control-n>", lambda event: print('快捷键Ctrl+N'))
    注意：
        不能直接作为一级菜单显示在窗口菜单栏的根节点上

-   add_radiobutton()

    说明：添加单选菜单项

-   add_separator()

    说明：添加分割线

-   post(x, y)

    说明：在指定位置弹出菜单
    参数：(x, y)，两个参数，即 x 和 y 坐标

