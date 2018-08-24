# Messagebox

#### 消息对话框 Messagebox

共有 8 中消息类型，对应函数如下：

##### 函数

1. showinfo

    > 提示信息
    > 返回: ok

2. showwarning

    > 警告提示
    >
    > 返回: ok

3. showerror

    > 错误提示
    >
    > 返回: ok

4. askquestion

    > 询问 Yes 还是 No
    >
    > 返回: yes/no

5. askokcancel

    > 询问 Ok 还是 Cancel
    >
    > 返回: True/False

6. askyesno

    > 询问 Yes 还是 No
    >
    > 返回: True/False

7. askyesnocancel

    > 询问 Yes 还是 No 还是 Cancel
    >
    > 返回: True/False/None

8. askretrycancel
    > 询问 Retry 还是 Cancel
    >
    > 返回: True/False

##### 使用

```python
tkinter.messagebox.showinfo('提示', '消息内容')
tkinter.messagebox.showwarning('提示', '请注意：警告信息！')
tkinter.messagebox.askyesnocancel('提示', '内容已修改，是否保存并退出？')

tkinter.messagebox.showinfo(
    title='提示',
    message='确定还是取消呢 ?',
    icon='info',
    type='okcancel')

tkinter.messagebox.showinfo(title='提示', message='确定还是取消呢 ?', parent=self.frame)
```

##### 参数

-   title

    说明：设置对话框窗口标题栏的文本

-   message

    说明：设置对话框的主要内容，可以使用'\n'来进行换行

_可选参数可以设置的选项和含义如下_

- parent

    说明：如果不指定该选项，那么对话框默认显示在根窗口上

    默认值：如果想要讲对话框显示在子窗口 w 上，那么可以设置 parent=w

    效果：在父窗口顶部向下滑出的动态效果

- default

    说明：默认的相应按钮（也就是按下回车时响应的那个按钮）

    默认值：默认是第一个按钮（像‘确定’，‘是’或‘重试’）

    范围：可以设置的值根据对话框的不同可以进行选择：CANCEL、IGNORE、OK、NO、RETRY 或 YES

- icon

    说明：指定对话框窗口标题栏显示的图标

    值范围：可以指定的值有：ERROR、INFO、QUESTION 或 WARNING

    ​ ERROR = "error"

    ​ INFO = "info"

    ​ QUESTION = "question"

    ​ WARNING = "warning"
    注意：不可自定义图标

##### 返回值

askokcancel()、askretrycancel()和 askyesno()返回布尔类型的值：

返回 True 表示用户点击了‘确定’或‘是’按钮
返回 False 表示用户点击了‘取消’或‘否’按钮

askquestion()返回‘yes’或‘no’字符串表示用户点击了‘是’或‘否’按钮

showerror()、showinfo()和 showwarning()返回‘ok’表示用户按下了‘是’按钮
