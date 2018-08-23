# Messagebox

消息对话框，共有8个类型

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

    > 询问Yes还是No
    >
    > 返回:  yes/no

5. askokcancel

    > 询问Ok还是Cancel
    >
    > 返回: True/False

6. askyesno

    > 询问Yes还是No
    >
    > 返回: True/False

7. askyesnocancel

    > 询问Yes还是No还是Cancel
    >
    > 返回: True/False/None

8. askretrycancel
    > 询问Retry还是Cancel
    > 
    > 返回: True/False

	般使用方法：	

```python
tkinter.messagebox.showinfo('提示', '消息内容')
tkinter.messagebox.showwarning('提示', '请注意：警告信息！')
tkinter.messagebox.askyesnocancel('提示', '内容已修改，是否保存并退出？')
```

高级使用方法：

```python
tkinter.messagebox.showinfo(
    title='提示',
    message='确定还是取消呢 ?',
    icon='info',
    type='okcancel')

tkinter.messagebox.showinfo(title='提示', message='确定还是取消呢 ?', parent=self.frame)

'''参数
title
	-- 参数设置标题栏的文本
message
    -- 参数设置对话框的主要内容，可以使用'\n'来进行换行

可选参数可以设置的选项和含义如下
parent
    --如果不指定该选项，那么对话框默认显示在根窗口上
    --如果想要讲对话框显示在子窗口w上，那么可以设置parent=w
    实现在父窗口顶部向下滑出的动态效果
default
    --设置默认的按钮（也就是按下回车响应的那个按钮）
    --默认是第一个按钮（像‘确定’，‘是’或‘重试’）
    --可以设置的值根据对话框的不同可以进行选择：CANCEL、IGNORE、OK、NO、RETRY或YES
icon
    --指定对话框显示的图标
    --可以指定的值有：ERROR、INFO、QUESTION或WARNING
        ERROR = "error"
        INFO = "info"
        QUESTION = "question"
        WARNING = "warning"
    --注意：不可自定义图标
'''
```

