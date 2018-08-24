## filedialog

### 文件对话框 filedialog

可以实现打开文件或保存文件的功能。

##### 函数

filedialog 模块提供了两个函数：

```python
askopenfilename(**options) # 用于打开文件
asksaveasfilename(**options) # 用于保存文件
```

##### 使用

```python
from tkinter import filedialog
filedialog.askopenfilename(title='打开文件', filetypes=[('Python', '*.py *.pyw'), ('All Files', '*')])
filedialog.asksaveasfilename(title='保存文件', initialdir='/', initialfile='hello.py')
```

##### 参数

两个函数可供设置的选项是一样的，下面列举了可用选项及含义：

- title

    说明：指定文件对话框的标题栏文本

- defaultextension

    说明：指定文件的后缀
    例如：defaultextension='.jpg'，那么当用户输入一个文件名'Python'的时候，文件名会自动添加后缀为'Python.jpg'
    注意：如果用户输入文件名包含后缀，那么该选项不生效

- filetypes

    说明：指定筛选文件类型的下拉菜单选项
    值格式：该选项的值是由二元组构成的列表，每个二元组是由（类型名，后缀）构成
    例如：filetypes=[('PNG', '.png'), ('JPG', '.jpg'), ('GIF', '.gif')]

- initialdir

    说明：指定打开保存文件的默认路径
    默认值：默认路径是当前文件夹

- parent

    说明：如果不指定该选项，那么对话框默认显示在根窗口上

    值：如果想要将对话框显示在子窗口 w 上，那么可以设置 parent=w

##### 返回值

1. 如果用户选择了一个文件，那么返回值是该文件的完整路径

2. 如果用户点击了取消按钮，那么返回值是空字符串
