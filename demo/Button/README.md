# Button

> 按钮控件: 在程序中显示按钮; 响应消息

##### 使用

```python
tkinter.Button(
    parent,
    text='确定还是取消呢 ?',
    width=20,
    height=5,
    command=dowhat_function)

```
##### 参数

-   parent

    说明：父组件

-   text

    说明：按钮显示的名称

-   command

    说明：按钮点击时回调事件

-   width

    说明：按钮宽度
    单位：一个字符

-   height

    说明：按钮高度
    单位：一个字符

-   background
    
    说明：按钮背景颜色

-   foreground
    
    说明：按钮字颜色

_可选参数可以设置的选项和含义如下_


##### 函数

-   flash

        说明：按钮刷新
        注意：当按钮的状态为disabled时，则忽略

-   invoke

        说明：按钮反射函数
        注意：当按钮的状态为disabled时，则忽略
