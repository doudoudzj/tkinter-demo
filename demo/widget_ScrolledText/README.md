# ScrolledText

> 滚动文本框
> 
> 自带滚动条的文本框组件
> 
> scrolledtext.ScrolledText

    参数: wrap
    说明: 换行的形式
    默认值: CHAR, 即作为字符串, 一行不够就按照字符串截取换行
    
    比如: 输入hello，he在第一行的行尾, llo在第二行的行首
    
    当:
    wrap = tk.WORD or "word"
    这个值表示在行的末尾如果有一个单词跨行，会将该单词放到下一行显示
    这时如果设置wrap=word，则表示会将 hello 这个单词挪到下一行行首显示
