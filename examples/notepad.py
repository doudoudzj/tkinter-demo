#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""记事本"""
# https://blog.csdn.net/mr_muli/article/details/78803842

import os
from tkinter import (Button, Checkbutton, Entry, Frame, IntVar, Label, Menu,
                     Scrollbar, StringVar, Text, Tk, Toplevel, messagebox)
from tkinter.filedialog import askopenfilename, asksaveasfilename


class NotePad():
    def __init__(self):
        root = Tk()
        self.root = root

        root.title("记事本GUI")
        root.geometry("700x500+500+100")
        # root.resizable(False, False)
        root.minsize(700, 500)
        root.attributes('-titlepath', True)

        self.note_pad = None
        self.filen_ame = ""

        self.init_menu()
        self.init_btns()
        self.line_number()
        self.init_page()

        # 绑定快捷键
        self.note_pad.bind("<Command-N>", self.op_new)
        self.note_pad.bind("<Command-n>", self.op_new)
        self.note_pad.bind("<Command-O>", self.op_open)
        self.note_pad.bind("<Command-o>", self.op_open)
        self.note_pad.bind("<Command-S>", self.op_save)
        self.note_pad.bind("<Command-s>", self.op_save)
        self.note_pad.bind("<Command-A>", self.op_select_all)
        self.note_pad.bind("<Command-a>", self.op_select_all)
        self.note_pad.bind("<Command-F>", self.op_find)
        self.note_pad.bind("<Command-f>", self.op_find)
        self.note_pad.bind("<Button-2>", self.show_context_menu)

        root.mainloop()

    def init_page(self):
        self.note_pad = Text(self.root, undo=True, highlightcolor="#ddd")
        self.note_pad.pack(expand="yes", fill="both")

        self.scroll = Scrollbar(self.note_pad)
        self.note_pad.config(yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.note_pad.yview)
        self.scroll.pack(side="right", fill="y")

    def author(self):
        messagebox.showinfo(title="作者", message="木里")

    def about(self):
        messagebox.showinfo(title="版权信息", message="2017-12-14-14:40 周四 北京邮电大学")

    def op_new(self, event=None):
        self.root.attributes('-modified', True)
        self.root.title("未命名文件")
        self.filen_ame = None
        self.note_pad.delete(1.0, "end")

    def op_open(self, event=None):
        self.filen_ame = askopenfilename(defaultextension=".txt")
        if self.filen_ame == "":
            self.filen_ame = None
        else:
            self.root.attributes('-modified', False)
            self.root.title("记事本-" + os.path.basename(self.filen_ame))
            self.note_pad.delete(1.0, "end")
            f = open(self.filen_ame, 'r')
            self.note_pad.insert(1.0, f.read())
            f.close()

    def op_save(self, event=None):
        try:
            f = open(self.filen_ame, 'w')
            msg = self.note_pad.get(1.0, 'end')
            f.write(msg)
            f.close()
            self.root.attributes('-modified', False)
        except:
            self.op_save_as()

    def op_save_as(self, event=None):
        f = asksaveasfilename(initialfile="未命名.txt", defaultextension=".txt")
        self.filen_ame = f
        fh = open(f, 'w')
        msg = self.note_pad.get(1.0, "end")
        fh.write(msg)
        fh.close()
        self.root.title("记事本" + os.path.basename(f))
        self.root.attributes('-modified', False)

    def op_cut(self, event=None):
        self.note_pad.event_generate("<<Cut>>")

    def op_copy(self, event=None):
        self.note_pad.event_generate("<<Copy>>")

    def op_paste(self, event=None):
        self.note_pad.event_generate("<<Paste>>")

    def op_undo(self, event=None):
        self.note_pad.event_generate("<<Undo>>")

    def op_redo(self, event=None):
        self.note_pad.event_generate("<<Redo>>")

    def op_select_all(self, event=None):
        self.note_pad.tag_add("sel", "1.0", "end")

    def op_find(self, event=None):
        t = Toplevel(self.root)
        t.title("查找")
        t.geometry("330x60+200+250")
        t.transient(self.root)
        Label(t, text="查找：").grid(row=0, column=0, sticky="e")
        v = StringVar()
        e = Entry(t, width=20, textvariable=v)
        e.grid(row=0, column=1, padx=2, pady=2, sticky="we")
        e.focus_set()
        c = IntVar()
        Checkbutton(
            t, text="不区分大小写", variable=c).grid(
                row=1, column=1, sticky='e')
        Button(
            t,
            text="查找所有",
            command=lambda: self.search(v.get(), c.get(), t, e)).grid(
                row=0, column=2, sticky="e" + "w", padx=2, pady=2)

        t.protocol("WM_DELETE_WINDOW", self.close_search)
        self.search_box = t

    def close_search(self):
        self.note_pad.tag_remove("match", "1.0", "end")
        self.search_box.destroy()

    def show_context_menu(self, event=None):
        self.menu_edit.tk_popup(event.x_root + 2, event.y_root + 2)

    def search(self, needle, cssnstv, t, e):
        self.note_pad.tag_remove("match", "1.0", "end")
        count = 0
        if needle:
            pos = "1.0"
            while True:
                pos = self.note_pad.search(
                    needle, pos, nocase=cssnstv, stopindex="end")
                if not pos: break
                lastpos = pos + str(len(needle))
                self.note_pad.tag_add("match", pos, lastpos)
                count += 1
                pos = lastpos
            self.note_pad.tag_config('match', fg='#f00', bg="#ddd")
            e.focus_set()
            t.title(str(count) + "个被匹配")

    def init_menu(self):
        """菜单"""

        menubar = Menu(self.root)

        # 文件菜单
        filemenu = Menu(self.root)
        filemenu.add_command(
            label="新建", accelerator="Command+N", command=self.op_new)
        filemenu.add_command(
            label="打开", accelerator="Command+O", command=self.op_open)
        filemenu.add_command(
            label="保存", accelerator="Command+S", command=self.op_save)
        filemenu.add_command(
            label="另存为",
            accelerator="Command+shift+S",
            command=self.op_save_as)
        menubar.add_cascade(label="文件", menu=filemenu)

        # 编辑菜单
        menu_edit = Menu(self.root)
        menu_edit.add_command(
            label="撤销", accelerator="Command+Z", command=self.op_undo)
        menu_edit.add_command(
            label="重做", accelerator="Command+Y", command=self.op_redo)
        menu_edit.add_separator()
        menu_edit.add_command(
            label="剪切", accelerator="Command+X", command=self.op_cut)
        menu_edit.add_command(
            label="复制", accelerator="Command+C", command=self.op_copy)
        menu_edit.add_command(
            label="粘贴", accelerator="Command+V", command=self.op_paste)
        menu_edit.add_separator()
        menu_edit.add_command(
            label="查找", accelerator="Command+F", command=self.op_find)
        menu_edit.add_command(
            label="全选", accelerator="Command+A", command=self.op_select_all)
        menubar.add_cascade(label="编辑", menu=menu_edit)
        self.menu_edit = menu_edit

        # 帮助
        menu_help = Menu(self.root)
        menu_help.add_command(label="关于我们", command=self.author)
        menu_help.add_command(label="版权", command=self.about)
        menubar.add_cascade(label="帮助", menu=menu_help)

        self.root['menu'] = menubar

    def init_btns(self):
        """快捷按钮栏"""

        shortcutbar = Frame(self.root, height=25, bg="#ddd")
        shortcutbar.pack(expand="no", fill="x")

    def line_number(self):
        """行号"""

        line_label = Label(self.root, width=2, bg='antique white')
        line_label.pack(side="left", anchor='nw', fill="y")


if __name__ == "__main__":
    NotePad()
