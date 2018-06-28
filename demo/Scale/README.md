## Scale

Scale控件允许用户通过移动滑动条来选择数值。你可以设置最小值和最大值，滚动的滑条取值在最大值和最小值之间。
你可以使用 Scale 插件来取代 Entry，特别是你需要用户输入一个特定范围内的值的时候。

创建一个在指定范围内的滑动条，需要给 Scale 类传入 from 和 to 选项。因为 from 是 Python 里面的关键字，所以规定 from 加上一个后置的下划线，即 from\_。

下面的例子我们创建了 2 个 scale,一个是垂直方向，一个是水平方向的。

移动 slider，数值会随之跟着变化。

如果要获取当前滚动条的值，可以使用 get 方法，如下所示：

```python
# 默认垂直方向, 范围从 0-100
Scale(window, from_=0, to=100).pack()
# 自定义方向等属性, 范围从 0-50
w = Scale(
	window,
    label="演示滑块",
    from_=0,
    to=50,
    orient=gui.HORIZONTAL, # 水平方向
    length=500,
    showvalue=1,
    tickinterval=3,
    resolution=0.01).pack()
print(w.get())
```

参数属性

| 属性         | 说明                                                         |
| ------------ | ------------------------------------------------------------ |
| from_         | 开始值                                                       |
| to           | 结束值                                                       |
| orient       | tkinter.HORIZONTAL 水平                                      |
| legnth       | 控件长度                                                     |
| showvalue    | 0:不显示, 1:显示                                             |
| tickinterval | 标注分成几段                                                 |
| resolution   | 最小单位/刻度值或者说保留到几位，<br />resolution 默认值 1，这意味着当你获取当前 scale 的值时，它会对当前 scale 的值自动取最接近它的整数，你可以指定 resolution 选项为-1 来取消取整功能。 |
| command      | 事件绑定回调, 回调包含有一个参数, 值为当前刻度               |

