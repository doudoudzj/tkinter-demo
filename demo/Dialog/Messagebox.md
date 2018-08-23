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

一般使用方法：	

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
    icons='info',
    type='okcancel')

tkinter.messagebox.showinfo(title='提示', message='确定还是取消呢 ?', parent=self.frame)
# 参数: parent
# 说明: 实现在父窗口顶部向下滑出的动态效果

'''其他参数

参数: icons
ERROR = "error"
INFO = "info"
QUESTION = "question"
WARNING = "warning"

参数: types
ABORTRETRYIGNORE = "abortretryignore"
OK = "ok"
OKCANCEL = "okcancel"
RETRYCANCEL = "retrycancel"
YESNO = "yesno"
YESNOCANCEL = "yesnocancel"

参数: replies
ABORT = "abort"
RETRY = "retry"
IGNORE = "ignore"
OK = "ok"
CANCEL = "cancel"
YES = "yes"
NO = "no"
'''
```

