# Toplevel

> 容器控件: 用来提供一个单独的对话框(窗口)

> Toplevel（顶级窗口）组件类似于Frame组件，但Toplevel组件是一个独立的顶级窗口，这种窗口通常拥有标题栏、边框等部件，和Tk()创建出来的根窗口是一样的，共享着一样的方法。
> 何时使用Toplevel组件？
> Toplevel组件通常用在显示额外的窗口、对话框或者其他弹出窗口上。

Tk（根窗口）和Toplevel（顶级窗口）的方法：

下边这一系列方法用于与窗口管理器进行交互。他们可以被Tk（根窗口）调用，同时也适用于Toplevel（顶级窗口）

注意：并非所有操作系统均完全支持下方所有方法的实现。

| 方法                                                         | 含义                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| aspect(minNumber=None, minDenom=None, maxNumber=None, maxDenom=None,) | --控制该窗口的宽高比(width:height)<br/>--宽高比限制在：minNumber/minDenom~maxNumber/maxDenom--如果忽略参数，则返回一个4元组表示当前的限制（如果有的话） |
| attribute(*args)                                             | --设置和获取窗口属性--如果你只给出选项名，将返回当前窗口该选项的值<br/>--注意：以下选项不支持关键字参数，你需要在选项前加横岗（-）并用字符串的方式表示，用逗号（,）隔开选项和值。）<br/>--例如你希望设置窗口的透明度为50%，你应该使用attribute("-alpha", 0.5)代替attribute(alpha=0.5)<br/>--args选项列表见文末 |
| client(name=None)                                            | --设置和获取WM_CLIENT_MACHINE属性<br/>--如果要删除WM_CLIENT_MACHINE属性，赋值为空字符串即可<br/>--该属性仅支持X窗口系统的窗口管理器，其他系统均忽略 |
| colormapwindows(*wlist)                                      | --设置和获取WM_COLORMAP_WINDOWS属性<br/>--该属性仅支持X窗口系统的窗口管理器，其他系统均忽略 |
| command(value=None)                                          | --设置和获取WM_COMMAND属性<br/>--该属性仅支持X窗口系统的窗口管理器，其他系统均忽略 |
| deiconify()                                                  | --显示窗口<br/>--默认情况下新创建的窗口都会显示在屏幕上，但是用iconify()或withdraw()方法可以在屏幕上移除窗口 |
| focusmodel(model=None)                                       | --设置和获取焦点模式                                         |
| frame()                                                      | --返回一个字符串表示当前系统特征<br/>--对于类Unix系统，返回值是X窗口标识符<br/>--对于Windows系统，返回值是HWND强制转换为长整形的结果 |
| geometry(geometry=None)                                      | --设置和获取窗口的尺寸<br/>--geometry的参数格式为："%dx%d%+d%+d"%(width, height, xoffset, yoffset) |
| (wm_)grid(baseWidth=None, baseHeight=None, widthInc=None, heightInc=None) | --通知窗口管理器该窗口将以网格的形式重新调整尺寸<br/>--baseWidth和baseHeight指定Tk_GeometryRequest要求的网格单元数<br/>--widthInc和heightInc指定单元的高度和宽度 |
| (wm_)group(window=None)                                      | --将窗口添加到窗口群中<br/>--window参数指定控制窗口群的主窗口<br/>--如果忽略该选项，将返回当前窗口群的主窗口 |
| (wm_)iconbitmap(bitmap=None, default=None)                   | --设置和获取窗口的图标--例如root.iconbitmap(bitmap="python.ico")<br/>--default参数可以用于指定由该窗口创建的子窗口的默认图标 |
| (wm_)iconify()                                               | --将窗口图标化（最小化）<br/>--需要重新显示窗口，用deiconify()方法<br/>--该方法会使得state()返回"iconic" |
| (wm_)iconmask(bitmap=None)                                   | --设置和获取位图编码                                         |
| (wm_)iconname(newName=None)                                  | --设置和获取当前窗口图标化（最小化）时的图标名字             |
| (wm_)iconposition(x=None, y=None)                            | --设置和获取当前窗口图标化（最小化）时的图标位置             |
| (wm_)iconwindow(pathName=None)                               | --设置和获取当前窗口图标化（最小化）时的组件窗口<br/>--该方法会使得state()返回“icon” |
| (wm_)maxsize(width=None, height=None)                        | --设置和获取该窗口的最大尺寸                                 |
| (wm_)minsize(width=None, height=None)                        | --设置和获取该窗口的最小尺寸                                 |
| (wm_)overrideredirect(boolean=None)                          | --如果参数为True，该窗口忽略所有的小部件（也就是说该窗口将没有传统的标题栏、边框等部件） |
| (wm_)positionfrom(who=None)                                  | --指定窗口位置由“谁决定<br/>--如果who参数是“user”，窗口位置由用户决定<br/>--如果who参数是“program”，窗口位置由系统决定 |
| (wm_)protocol(name=None, func=None)                          | --将回调函数func与相应的规则name绑定<br/>--name参数可以是“WM_DELETE_WINDOW”：窗口被关闭的时候<br/>--name参数可以是“WM_SAVE_YOURSELF”：窗口被保存的时候<br/>--name参数可以是“WM_TAKE_FOCUS”：窗口获得焦点的时候 |
| (wm_)resizable(width=None, height=None)                      | --指定是否可以改变该窗口的尺寸<br/>--width为True说明允许调整窗口的水平尺寸<br/>--height为True说明允许调整窗口的垂直尺寸 |
| (wm_)sizefrom(who=None)                                      | --指定窗口尺寸由“谁决定<br/>--如果who参数是“user”，窗口尺寸由用户决定<br/>--如果who参数是“program”，窗口尺寸由系统决定 |
| (wm_)state(newstate=None)                                    | --设置和获得当前窗口的状态<br/>--newstate的只可以是'normal', 'iconoc'(见iconify), 'withdraw'(见withdraw), 'icon'(见iconwindow)和'zoomed'(放大，Windows特有) |
| (wm_)title(string=None)                                      | --设置窗口的标题                                             |
| (wm_)transient(master=None)                                  | --指定为master的临时窗口                                     |
| (wm_)withdraw()                                              | --将窗口从屏幕上移除（并没有销毁）<br/>--需要重新显示窗口，使用deiconify()方法<br/>--该方法会使得state()返回"withdraw" |
| wm_aspect(minNumber=None, minDenom=None, maxNumber=None, manDenom=None) | --见上方aspect()                                             |
| wm_attributes(*args)                                         | --见上方attributes()                                         |
| wm_client(name=None)                                         | --见上方client()                                             |
| wm_colormapwindows(*wlist)                                   | --见上方colormapwindows()                                    |
| wm_command(value=None)                                       | --见上方command()                                            |
| wm_deiconify()                                               | --见上方deiconify()                                          |
| wm_focusmodel(model=None)                                    | --见上方focusmodel()                                         |
| wm_frame()                                                   | --见上方frame()                                              |
| wm_geometry(geometry=None)                                   | --见上方geometry()                                           |

 

attribute(*args)之args参数

| 选项       | 含义                                                         |
| ---------- | ------------------------------------------------------------ |
| alpha      | （Windows，Mac）控制窗口的透明度1.0表示不透明，0.0表示完全透明该选项并不支持所有的系统，对于不支持的系统，Tkinter绘制一个不透明（1.0）的窗口 |
| disabled   | （Windows）禁用整个窗口（这时候你只能从任务管理器中关闭它）  |
| fullscreen | （Windows，Mac）如果设置为True，则全屏显示窗口               |
| modified   | （Mac）如果设置为True，该窗口被标记为改动过                  |
| titlepath  | （Mac）设置窗口代理图标的路径                                |
| toolwindow | （Windows）如果设置为True，该窗口采用工具窗口的样式          |
| topmost    | （Windows，Mac）如果设置为True，该窗口将永远置顶             |