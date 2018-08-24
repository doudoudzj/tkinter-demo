# ScrolledText

#### 滚动文本框 ScrolledText

可以实现自带滚动条的文本框组件

##### 使用

```python
from tkinter import scrolledtext

# 实例化一个文本框
text = scrolledtext.ScrolledText()

# or
from tkinter.scrolledtext import ScrolledText

# 实例化一个文本框
text = ScrolledText(root)
```

##### 参数

-   第一个参数

    说明：无指定参数名称的第一个参数

    默认：无

    值：可以设置为父容器

-   width

    说明：宽度

    注意：宽度单位为一个字符

    例如：宽度值为 10，那么文本框默认显示的宽度是 10 个字符的宽度

-   height

    说明：高度

    注意：宽度单位为一个字符

-   bg or background

    说明：背景色

    值：

-   fg or foreground

    说明：字体颜色

    值范围：

-   highlightcolor

    说明：激活文本框时边框的高亮色

-   font

    说明：字体格式

    值格式：('Courier New', 25)

-   wrap

    说明: 换行的形式

    默认值: CHAR or 'char', 即作为字符串, 一行不够就按照字符串截取换行

    比如: 输入 hello，he 在第一行的行尾, llo 在第二行的行首

    取值:

    wrap = tk.WORD or 'word"

    这个值表示在行的末尾如果有一个单词跨行，会将该单词放到下一行显示

    这时如果设置 wrap=word，则表示会将 hello 这个单词挪到下一行行首显示
