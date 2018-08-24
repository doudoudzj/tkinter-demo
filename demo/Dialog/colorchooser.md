## colorchooser

#### 颜色对话框 colorchooser

可以实现让用户选择需要的颜色的功能。

##### 模块提供了一个函数

askcolor(color, option=value, ...)

##### 使用

```python
from tkinter import Tk, colorchooser
root = Tk()
colorchooser.askcolor(title='选择颜色', color='#333', parent=root)
```

##### 参数

-   title

    说明：指定颜色选择器标题栏的文本
    默认值：默认标题是“颜色”

-   color

    说明：要显示的初始的颜色(下图四个红箭头指的地方)
    默认值：默认颜色是浅灰色（light gray）

-   parent

    说明：如果不指定该选项，那么对话框默认显示在根窗口上
    值：如果想要将对话框显示在子窗口 w 上，那么可以设置 parent=w

##### 返回值

1. 如果用户点击的‘确定’按钮，返回值是一个二元组(triple, color)，其中的 triple 是一个三元组(R, G, B)--其中 R, G, B 的范围是[0, 255]（就是该颜色的 RGB 颜色），第二个参数选中颜色的 16 进制的值

2. 如果用户点击的‘取消’按钮，返回值是（None, None）
