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
# 窗口透明度, 值越小透明度越高
window.attributes("-alpha", 0.8)
# 设置窗口图标
window.iconbitmap('icon.ico')
# 刷新窗口
window.update()
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