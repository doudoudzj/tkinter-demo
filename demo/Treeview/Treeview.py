#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
ttk.Treeview 控件展示了tree中项的层级集合关系。
    每一个项都有一个文字描述的标签，一个可选的图属性及可选的数据集列表。数据集元素在树的标签后显示在连续列中。
    数据集的显示顺序可以通过控件的displaycolumns选项设置。
    树控件同样可以显示列头。列可以通过数值或者通过在控件列选项中列出的符号名来访问。
    每一个项由唯一的名字标识。如果调用项时没有给项分配ID，（树）控件会为每一个项生成一个ID。
    名为“{ }”的根项很好认。根项本身是不显示的；它的子节点会展示在层级的顶层。
    每个项也包含若干标签（tags）列表，用于把事件绑定和某个单独的项结合起来，以控制项的外观。

Treeview控件根据可滚动控件选项(Scrollable Widget Option)中的描述，以及Treeview.xview()方法和Treeview.yview()，可以支持横向和纵向滚动。

一、Treeview(options)中的options：
    先声明实例化
        tree = ttk.Treeview(root)
    columns
        说明：
            值应该是一个列表(list)。
        例子：
            tree["columns"] = ["title","content"]
            # 可以声明两个列，分别用title和content这两个标识符来表示（但它们的名称不一定叫这两个）
    displaycolumns
        说明：
            值应该是一个列表(list)。既可以用columns选项中声明的符号标识符来表示，也可以用整形列序号来表示。
            displaycolumns的目的在于指明要显示哪些列，以及它显示的位置顺序。
        例子：
            tree["displaycolumns"] = ["content", "title"]
            # 这样在GUI界面，就会先显示content列，后显示title列。
    height
        说明：
            值应该是一个整形数值。用来表示GUI界面上可见的行有多少。
        例子：
            tree["height"] = 15
            # 那么加载的Treeview就会显示15行
    width
        说明：
            没有这个选项。Treeview的宽度，取决于所有列宽之和。要设置列宽去。
    padding
        说明：
            值应该是一个列表(list)。用来表示这个控件的内边界。顺序“左、上、右、下”。
        例子：
            tree["padding"] = [1, 2, 3, 4]
            # 这里设置了内左边界为1，内上边距为2，内右边距为3，内...不写了。
    selectmode
        说明：
            值是以下三选一："extended"(默认)，"browse"，"none"。用来表示加载Treeview后是否可以点选多行。
        例子：
            tree["selectmode"] = "extended"     # 按Ctrl可以高亮选中多行；
            tree["selectmode"] = "browse"       # 按啥都只能同时高亮一行；
            tree["selectmode"] = "none"         # 按啥都不高亮。
    show
        说明：
            值应该是一个列表(list)，可以包含"tree"，"headings"中的0到多个。表示是否要显示tree元素（放在#0的列）和headings（表头）元素。默认是两个都显示。
        例子：
            tree["show"] = "tree"               # 只显示#0的列；
            tree["show"] = "headings"           # 只显示表头对应的列；
            tree["show"] = ["tree","headings"]  # 两个都显示(即所有列)。
    yscrollcommand和xscrollcommand
        说明：
            这两个是前面提到的可滚动控件选项(Scrollable Widget Option)中的设置。所有可滚动的(scrollable)的控件都可以设置这两个通用选项。
            首先要有个scrbar = Scrollbar(root)，然后设置可滚动控件的这两个属性为scrbar.set即可。这有点像button的command属性传递事件一样。
        例子：
        tree["yscrollcommand"] = scrbar.set

二、item的options
    一些Treeview的方法，例如Treeview.get_children([item])方法，会返回item的子节点，这样可以对这些结点进行设置。这就涉及到item的options。

    查看item的方法
        children = tree.get_children()          # 返回了一大帮children
        for child in children:                  # 可以通过这样的方式查看tree包含的那些children崽子们
            print child                         # 对于tree给生成的那些itemID，他们都是string类型，比如“I001”“I002”...
        print tree.item("I001")                 # 可以查看I001那一项到底是个啥。应该是个dictionary！！
        print tree.item("I001")["values"][0]    # 可以拿到“《利用Python进行数据分析》”这个title
    输出结果如下，即为ID为“I001”的item结构
        {
            "text": "",
            "image": "",
            "values": ["第一个字段值", "第二个字段值"],
            "open": 0,
            "tags": ""
        }
    可以看到，这个项目中包含五个key：text、image、values、open、tags，于是可以对他们进行设置。（这个例子来自于http://www.cnblogs.com/wumac/p/5816764.html 有改动）
        children = tree.get_children()
        for num in range(len(children)):
            if (num % 2 == 0):
                tree.item(children[num], *item options*)
    text
        说明：设置item的标签文字。如果用Treeview模拟Listview，这一项看不到效果。
    image
        说明：为item设置一个image。如果用Treeview模拟Listview，这一项看不到效果。
    values
        说明：
            如果用Treeview模拟Listview，tree.get_children()相当于返回了表格的总行数。每一个行相当于一个item，那么values就是这一行的全部内容。
            values应该是个list，list的元素个数应该和你设置的列数相同。不够的会被空白填充，超过的会被截掉。
        例子：
            tree.item(children[num], values = ["A_TITLE", "SOME_CONTENTS"])
    open
        说明：
            这是一个布尔值。为True时，这个item的子节点会显示。为False时，它的子节点被隐藏。
    tags
        说明：
            这是一个列表list。列表里为某个item的标签集合，以string表示。具体参见“三、tag的options”

三、tag的options
    对于Treeview的崽子节点们，可以为他们每个人都打上一个tag，然后配合Treeview.tag_configure()对于不同的tag做不同的处理。
    这有点像html中被赋予了id和class的标签，可以在css样式表中对他们统一润色一样。
    例子（这个例子来自于http://www.cnblogs.com/wumac/p/5816764.html 有改动）
        children = tree.get_children()
        for num in range(len(children)):
            if (num % 2 == 0):
                tree.item(children[num], tags = ["evenLine"])
        tree.tag_configure("evenLine", *tag config*)
    foreground
        说明：定义文字颜色。
    background
        说明：定义背景色。
    font
        说明：定义文字字体。
    image
        说明：定义item的图像

四、列标识符
    列标识符可以是如下三种形式的：

    符号名称。
        说明：类似于上文定义的“title”、“content”
    整形数n。
        说明：表示第n列。
    字符串型 #n。
        说明：表示第n列。#0总是分配给树根节点的。其他的从#1开始计算。

五、Treeview可接受的事件
    坑！勿踩！这里的事件，都是“<<”和“>>”的。两个左右尖括号！！！

    <<TreeviewSelect>>
    说明：
        当某个item被选中时会触发这个事件。
        这和<Button-1>的效果是不一样的。<Button-1>首先会选中这个Treeview，导致首次Treeview.selection()时返回空tuple。
    <<TreeviewOpen>>
    说明：
        将一个item的open改为True之前会触发这个事件。
        想象一下，open=True就是展开。类似于，先触发事件，后展开这个项。
    <<TreeviewClose>>
    说明：
        将一个item的open改为False之后会触发这个事件。
        想象一下，open=False就是折叠。类似于，先折叠这个项，后触发这个事件。

六、Treeview的方法API
    bbox(item, [column])
        说明：
            该方法会返回一个指定item的边界信息，用tuple形式表示：(x, y, width, column)。
        参数：
            item——指明一个item，可以用tree.focus()方法返回。
            column——可选，默认是None，假如传入"#2"，将会返回#2这个单元的边界信息。
        返回值：
            tuple类型，例如(301, 25, 401, 20)。如果指定的column是不可见的(invisible)，将会返回空字符串。
    get_children([item])
        说明：
            该方法会返回指定item的子节点们。用tuple表示。
        参数：
            item——可选，指明一个item。不指明，将会返回root结点的崽子们。
        返回值：
            tuple类型，例如('I001', 'I002', 'I003', 'I004', 'I005', 'I006', 'I007', 'I008', 'I009', 'I00A', 'I00B', 'I00C', 'I00D')。
    set_children(item, *newchildren)
        说明：
            该方法会将item的子节点们设置为newchildren。
            按照API文档的说法，这个方法会引起item中包含，但newchildren中不包含的节点从tree中分离。此外，newchildren中的元素，不能是item的祖先。
            newchildren用tuple表示。
        参数：
            item——指明一个item。
            newchildren——用tuple表示的item的新崽子们。
        返回值：
            None。
    column(column, [option], [*keyword])*
        说明:
            该方法用于返回或设置某一列的信息。如果设置keyword参数，这个方法用于设置列；如果没设置，用于返回列。
        参数:
            column——指明一个column。可以用"#2"指定第二列，也可以用"content"这种文字标识符指定。"#0"表示树根。
            option——可选，默认None。对于一个column来说，它一共有五个性质，option可以从这五种中取值，包含哪些参数，这个方法就会返回它对应的值:
                {
                    "id": "title",              # 返回列名。id是只读的，从初始化Treeview空间时就设置好了，不能通过keyword设置。
                    "anchor": u"w",             # 返回列内容的对齐方式。图中"w"表示west，左对齐。
                    "minwidth": 20,             # 返回列的最小宽度（像素）。拖拽改变列宽时的最小限制。
                    "stretch": 1,               # 布尔值或者1/0，表示列是否可以拖动改变列宽。
                    "width": 300                # 返回列的设置宽度（像素）。
                }
            keyword——可选，需要传入dict类型，key就是上面的option，value自己设置。
        返回值：
            dict类型，或者string类型，或者int类型。
        例子：
            可以这样设置：
                myOption = {} # 初始化一个option dict，不然会报错：myOption is not defined
                myOption["minwidth"] = 50 # 添加一个设置
                myOption["width"] = 280 # 添加一个设置
            应该这样传值：
                tree.column("#2", myOption) # 一定要带上，表示传入的是dict
    delete(*items)
        说明：
            该方法会删除指定的items和他们的崽子们。树根不能删。
        参数：
            items——指明items，用tuple形式。
        返回值：
            None。
    detach(*items)
        说明：
            该方法会使指定的items和树脱离亲子关系。树根不能和任何人脱离关系。
            脱离关系的items和他的崽子们都还在，可以重新插入别的树中，但是显示不出来了。
        参数：
            items——指明items，用tuple形式。
        返回值：
            None。
    exists(item)
        说明：
            该方法会返回指定的item是否存在。存在返回True。
        参数：
            items——指明item。
        返回值：
            布尔值。
    focus([item])
        说明：
            如果设置了item，会定位到那个item；如果没有设置，返回正获得焦点的那个；如果没有人有焦点，返回空字符串。
            友情提示：多选items也只是返回第一个item的ID
        参数：
            items——可选，指明想要高亮的item。
        返回值：
            string类型，或者None。
    heading(column, [option], [*keyword])*
        说明：
            该方法用于返回或设置某一列的表头信息。如果设置keyword参数，这个方法用于设置表头；如果没设置，用于返回表头信息。
        参数：
            column——指明一个column。可以用"#2"指定第二列，也可以用"content"这种文字标识符指定。"#0"表示树根。
            option——可选，默认None。对于一个column来说，它一共有五个性质，option可以从这五种中取值，包含哪些参数，这个方法就会返回它对应的值：
                {
                    "text"："",                 # 返回列表头名。
                    "anchor"："center",         # 返回列内容的对齐方式。图中"center"表示居中对齐。
                    "image"："",                # 可以设置表头的图像。
                    "command"：""               # 点击这列表头时可以触发一个操作，比如递增排序操作。
                }
            keyword——可选，需要传入dict类型，key就是上面的option，value自己设置。
        返回值：
            dict类型，或者string类型。
        例子：
            参考前面column()方法
    identify(component, x, y)
        说明：
            （不太会用这一项，总报错，说我传入的component应该是“区域、项、列、行或元素”，难道传入"#2"不可以吗？）
            文档中说这个方法会返回一个在指明的x y坐标下指定组件的详细说明，如果组件不显示，返回空字符串。
        参数：
            component——应该传入区域、项、列、行或元素。
            x/y——x/y坐标。
        返回值：
            （我猜想是一个dict描述，或者是空字符串）。

    identify_row(y)
        说明：
            这里会返回被选中的是哪一个item，打印item的ID。
            友情提示：绑定事件就该改成鼠标事件<Button-1>了，Treeview自己的事件无法传入x和y，除非在Treeview绑定事件的回调函数里，自己再通过Button获取x/y
        参数：
            y——y坐标。
        返回值：
            string类型的item ID。
    identify_column(x)
        说明：
            这里会返回被选中的是哪一个column，打印column的名称。
            友情提示：绑定事件就该改成鼠标事件<Button-1>了，Treeview自己的事件无法传入x和y，除非在Treeview绑定事件的回调函数里，自己再通过Button获取x/y
        参数：
            x——x坐标。
        返回值：
            string类型的column名。树根是"#0"。
    identify_region(x,y)
        说明：
            这里会返回被选中的是哪一个区域，打印区域名称。
            友情提示：绑定事件就该改成鼠标事件<Button-1>了，Treeview自己的事件无法传入x和y，除非在Treeview绑定事件的回调函数里，自己再通过Button获取x/y
        参数：
            x/y——x/y坐标。
        返回值：
            string类型的区域名：
                "heading"表示表头区域；
                "tree"表示树根区域；
                "separator"表示列分割线区域；
                "cell"表示单元格区域。
    identify_element(x,y)
        说明：
            这里会返回被选中的是哪一个元素，打印元素名称。
            友情提示：绑定事件就该改成鼠标事件<Button-1>了，Treeview自己的事件无法传入x和y，除非在Treeview绑定事件的回调函数里，自己再通过Button获取x/y
        参数：
            x/y——x/y坐标。
        返回值：
            string类型的元素名。比方说单击了单元格元素，会返回"text"。
    index(item)
        说明：
            这里会返回被选中item的索引。
            友情提示：如果想通过绑定事件来获取当前item，然后再返回它的index(item)，还是要绑定鼠标事件<Button-1>因为要获取y
        参数：
            item——求索引的item。
        返回值：
            int类型。
    insert(parent, index, [iid], *keyword)*
        说明：
            用来创建一个新节点，并且返回这个节点的标识符。
        参数：
            parent——string类型。指明时，将在这个节点下创建新节点；否则将创建一个孤点。
            index——integer类型或者直接写"end"。表示创建的节点将会在什么位置，如果传入了一个非正数，会在崽子队列的头部插入这个节点，如果是传入"end"，或者是一个超过了总崽子数量的正数，会追加到结尾。
            iid——可选，是否传入这个值，决定了创建这个节点时是否为他赋予了一个标识符。
            keyword——新建的节点本身的信息，以键值对表示。
        返回值：
            string类型的新节点标识符。
    item(item, [option], [*keyword])*
        说明：
            查询某一个项，或者修改某一个项。
        参数：
            item——传入一个项，用标识符表示。
            option——可选，取值参考前面item options，如果传入，将修改item项；如果不传入，则只查询这个项。
            keyword——可选，和option一起传入。
        返回值：
            string类型或None。
    move(item, parent, index)
        说明：
            把一个item从parent的崽子们中，移到index那个位置。
        参数：
            item——传入一个项，用标识符表示。
            parent——指明父节点。
            index——integer类型。要移动到的位置。
        返回值：
            None。
    next(item)
        说明：
            返回item的索引中下一个孩子。如果没有就返回空字符串。
        参数：
            item——传入一个项，用标识符表示。
        返回值：
            string类型。
    parent(item)
        说明：
            返回item的父节点。如果没有就返回空字符串。
        参数：
            item——传入一个项，用标识符表示。
        返回值：
            string类型。
    prev(item)
        说明：
            返回item的索引中前一个孩子。如果没有就返回空字符串。
        参数：
            item——传入一个项，用标识符表示。
        返回值：
            string类型。
    reattach(item, parent, index)
        说明：
            移动节点。和前面提到的Tree.move(item, parent, index)是一样的
        参数：
            item——传入一个项，用标识符表示。
            parent——指明父节点。
            index——integer类型。要移动到的位置。
        返回值：
            None。
    see(item)
        说明：
            这个方法可以保证指明的那个item的可见性一定为True
        参数：
            item——传入一个项，用标识符表示。
            parent——指明父节点。
            index——integer类型。要移动到的位置。
        返回值：
            None。
    selection([option], [items])
        说明：
            这个方法用来返回当前被选中的那一项，或者为某一item设置option
        参数：
            option——可选，如果传入，则表示为item设置对应option。
            items——可选，和option同时传入，指明哪一个item。
        返回值：
            string类型或None。
    selection_set(items)
        说明：
            指明的items将会被集体选中。
        参数：
            items——指明哪些items。
        返回值：
            None。
    selection_add(items)
        说明：
            再选中队列中，添加某些items。
        参数：
            items——指明哪些items。
        返回值：
            None。
    selection_remove(items)
        说明：
            再选中队列中，删除某些items。
        参数：
            items——指明哪些items。
        返回值：
            None。
    selection_toggle(items)
        说明：
            toggle一般表示开关，也就是说这个方法会反选指定的items。从选中(开)改成未选中(关)状态。
        参数：
            items——指明哪些items。
        返回值：
            None。
    set(item, [column], [value])
        说明：
            这个方法会返回或设置指定项或指定项的某一列的值。
            如果只传入item，该方法会以dict类型返回所有列的键值对情况的集合；
            如果传入item和column，该方法会直接返回某项中指定列的值，类型就要看这个值本身了；
            如果传入item、column、value，该方法将会为指定项的指定列设置value值。
        参数：
            item——指明一个item。
            column——可选，传入一个列名。
            value——传入一个要设置的键值对的值。
        返回值：
            基本数据类型或None。
    tag_bind(tagname, [sequence], [callback])
        说明：
            这个方法会为特定的那个tag，在发生某个事件时，调用callback的回调函数。
        参数：
            tagname——指明一个tag。
            sequence——可选，传入事件，比如"<Button-1>"，表示某个tag在点击鼠标左键时，会调用callback回调函数。
            callback——相应事件的回调函数，可能需要配合lambda用。
        返回值：
            None。
    tag_configure(tagname, [option], [*keyword])*
        说明：
            这个方法会返回或为指定的那个tag设置option。参见前面tag option那里。
            只传入tagname时，会返回这个tag的option情况，用dict表示；
            只传入tagname和option时，会返回这个tag指明的option的情况；
            传入tagname、option、keyword时，会为tag的option属性设置keyword。
        参数：
            tagname——指明一个tag。
            option——可选，指定一个option。
            keyword——可选，传入一个要设置的option的keyword。
        返回值：
            None。
    tag_has(tagname, [item])
        说明：
            这个方法会列出具有tagname的所有item或查询指定的item是否有名为tagname的tag。
        参数：
            tagname——指明一个tag。
            item——可选，指定一个item。
        返回值：
            list类型或Boolean类型。
    xview([*args])
        说明：
            查询或修改Treeview控件的水平位置。
        参数：
            args——可选，传入时修改；否则查询。
        返回值：
            数值型或None。
    yview([*args])
        说明：
            查询或修改Treeview控件的垂直位置。
        参数：
            args——可选，传入时修改；否则查询。
        返回值：
            数值型或None。
"""

import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.title("Treeview")

# 实例化表格
# 空白首列是显示的，设置show属性为 headings 即可隐藏首列。
tree = ttk.Treeview(win, height=18, show="headings")


def info(event):
    """详情"""
    # event.widget.selection() #获取所选的项(可能是多项，所以要for循环)
    # event.widget获取Treeview对象，调用selection获取选择所有选中的
    slct = event.widget.selection()
    for i in slct:
        print(tree.item(i))
        print(tree.item(i)["values"])
        print(tree.item(i, "values"))


# 列索引ID
tree["columns"] = ("id", "name", "age", "heigh")

# 表头设置
tree.heading("id", text="ID")
tree.heading("name", text="姓名")
tree.heading("age", text="年龄")
tree.heading("heigh", text="身高")

# 表列设置, 可设置对应列的样式等, 不显示
tree.column("id", width=100)
tree.column("name", width=100, anchor="center")
tree.column("age", width=100, anchor="center")
tree.column("heigh", width=100, anchor="center")

# 插入数据
tree.insert("", 0, text="首列显示内容", values=("135", "张三", "3", "170"))
tree.insert("", 1, text="", values=("136", "李四", "34", "171"))
tree.insert("", 2, text="", values=("137", "王五", "9", "169"))
tree.insert("", 3, text="", values=("138", "马六", "23", "175"))
tree.insert("", 3, text="", values=("138", "马六", "23", "175"))
tree.insert("", 3, text="", values=("138", "马六", "23", "175"))
tree.insert("", 3, text="", values=("138", "马六", "23", "175"))
tree.insert("", 3, text="", values=("138", "马六", "23", "175"))
tree.insert("", 3, text="", values=("138", "马六", "23", "175"))
tree.insert("", 3, text="", values=("138", "马六", "23", "175"))
tree.insert("", 3, text="", values=("138", "马六", "23", "175"))
tree.insert("", 3, text="", values=("138", "马六", "23", "175"))
tree.insert("", 3, text="", values=("138", "马六", "23", "175"))
tree.insert("", 3, text="", values=("138", "马六", "23", "175"))
tree.insert("", 3, text="", values=("138", "马六", "23", "175"))
tree.insert("", 3, text="", values=("138", "马六", "23", "175"))
tree.insert("", 3, text="", values=("138", "马六", "23", "175"))
tree.insert("", 3, text="", values=("138", "马六", "23", "175"))
tree.insert("", 3, text="", values=("138", "马六", "23", "175"))
tree.insert("", 3, text="", values=("138", "马六", "23", "175"))
tree.insert("", 3, text="", values=("138", "马六", "23", "175"))

# 加滚动条
vbar = ttk.Scrollbar(win, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=vbar.set)

# 选中事件
tree.bind("<<TreeviewSelect>>", info)

tree.grid(row=0, column=0, sticky="nswe")
vbar.grid(row=0, column=1, sticky="ns")

head_frame = tkinter.LabelFrame(win, text="操作")
head_frame.grid(row=1, column=0, columnspan=2, sticky="nswe")
left = tkinter.Label(head_frame, text="Inside the LabelFrame")
left.pack()

btn_info = tkinter.Button(head_frame, text="详情")
btn_edit = tkinter.Button(head_frame, text="编辑")
btn_delete = tkinter.Button(head_frame, text="删除")
btn_info.pack(side="left")
btn_edit.pack(side="left")
btn_delete.pack(side="left")

# tree.pack()
win.mainloop()
