# -*- coding: UTF-8 -*-
# https://blog.csdn.net/weixin_41202652/article/details/78988934
#压缩软件

#设计界面
import tkinter
import tkinter.filedialog
import zipfile
import os
import tkinter.messagebox

root = tkinter.Tk()
root.title('压缩软件1.0')
root.minsize(300, 400)

#设置需要压缩路径变量
zipfilename = []


#添加文件的函数
def addfile():
    #全局化变量
    global zipfilename
    #弹出文件选框
    files = tkinter.filedialog.askopenfilenames(title='请选择需要亚索的文件')
    #将选择的文件加入列表中
    zipfilename += list(files)
    #将信息组成字符串书写
    filesstr = '\n'.join(zipfilename)
    #将文件的信息写入lable显示
    lable['text'] = filesstr


#压缩文件函数
def zip_file():
    path = './text.zip'
    #打开或者创建压缩文件
    zp = zipfile.ZipFile(path, 'w')
    #添加文件
    for filename in zipfilename:
        zp.write(filename, os.path.basename(filename))
    #关闭压缩文件
    zp.close()
    #判断压缩文件是否创建成功
    if os.path.exists(path):
        tkinter.messagebox.showinfo(title='信息', message='文件压缩成功：' + path)
    else:
        tkinter.messagebox.showerror(title='错误', message='压缩文件失败！')


#解压文件函数
def unzip_file():
    #选择需要解压的文件
    zipfilepath = tkinter.filedialog.asksaveasfilename()
    #选择解压的路径
    unzipfilepath = tkinter.filedialog.askdirectory()
    #解压操作
    zp = zipfile.ZipFile(zipfilepath)
    #解压所有
    zp.extractall(unzipfilepath)
    #关闭文件
    zp.close()


#摆放按钮
btn_add = tkinter.Button(root, text='添加文件', command=addfile)
btn_add.place(x=20, y=20)

btn_zip = tkinter.Button(root, text='压缩文件', command=zip_file)
btn_zip.place(x=110, y=20)

btn_unzip = tkinter.Button(root, text='解压文件', command=unzip_file)
btn_unzip.place(x=200, y=20)

#显示信息区域
lable = tkinter.Label(root,
                      text='没有文件信息',
                      bg='#abcdef',
                      anchor='nw',
                      justify='left')
lable.place(x=20, y=70, width=260, height=310)

root.mainloop()