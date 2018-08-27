## Window

##### 基础：


```python
# 实例化一个窗口
window = tkinter.Tk()
# 主消息循环
window.mainloop()
# 设置窗口标题
window.title("Hello World")
# 设置窗口尺寸, "宽度300x高度200"，中间的符号是字母x，不是符号*，也不是乘号
window.geometry("300x200")
# 设置窗口尺寸及位置偏移量，"+X坐标+Y坐标"，坐标点位置在窗口左上角
# window.geometry("宽度x高度+X+Y")
window.geometry("200x200+100+100")
# 禁止窗口尺寸变动
window.resizable(False, False)
# 窗口最大尺寸
window.maxsize(1000, 400)
# 窗口最小尺寸
window.minsize(1000, 400)
# 窗口背景色
window["bg"] = "pink"
# 设置窗口图标
window.iconbitmap('icon.ico')
# 刷新窗口
window.update()
```

##### 设置窗口函数:
attributes()

可取字段类型: -alpha, -fullscreen, -modified, -notify, -titlepath, -topmost, or -transparent

```python
# 透明度, 值越小透明度越高
window.attributes("-alpha", 0.8)
# 全屏, 没有标题栏及上面的窗口控件: 隐藏、显示和最大化
# 注意: 此时maxsize的设置必须是最大化的尺寸, 否则会报错
window.attributes("-fullscreen", True)
# 已编辑未保存状态, 关闭按钮提示已有内容修改
window.attributes('-modified', True or 1)
# 
window.attributes('-notify', True or 1)
# 标题栏的标题处可以选择地址
window.attributes('-titlepath', True or 1)
# 一直置顶显示
window.attributes('-topmost', True or 1)
# 无边框
window.attributes('-transparent', True or 1)
```

##### 可调用函数：

```python
# 获取窗口左上角X坐标
window.winfo_x()
# 获取窗口左上角Y坐标
window.winfo_y()
# 获取窗口当前宽度
window.winfo_width()
# 获取当前窗口高度
window.winfo_height()
# 获取当前屏幕宽度
window.winfo_screenwidth()
# 获取当前屏幕高度
window.winfo_screenheight()
```