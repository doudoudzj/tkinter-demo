# -*- coding: utf-8 -*-
# https://blog.csdn.net/Tifficial/article/details/78116862

import os
import time
import tkinter.messagebox
from tkinter import *
from tkinter.filedialog import *

from PIL import Image, ImageTk

import pygame


class create_UI():
    def __init__(self):
        pass

    def create_button(self, app):
        button_functions = [
            self.picSelect, self.writePoet, self.showPoet, quit
        ]
        button_texts = ['选\n择\n图\n片', '为\n你\n写\n诗', '查\n看', '退\n出']
        column_index = 3
        button_num = len(button_functions)
        for index in range(button_num):
            button = Button(
                app,
                text=button_texts[index],
                font=('方正舒体', 25),
                bd=0,
                bg='white',
                command=button_functions[index])
            button.grid(row=0, column=column_index, sticky='n')
            column_index += 1

    def ui(self):
        app = Tk()
        app.title("为你写诗")
        app.resizable(0, 0)  #禁止调整窗口大小
        image = Image.open(r'9668839.jpeg')
        background_image = ImageTk.PhotoImage(image)
        w = background_image.width()
        h = background_image.height()
        app.geometry('%dx%d+0+0' % (w, h))

        background_label = Label(app, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.create_button(app)
        app.mainloop()

    def set_button_sound(self):

        water_drop_pwd = r"SarahBrightman-ScarboroughFair.mp3"
        pygame.mixer.init()
        pygame.mixer.music.load(water_drop_pwd)
        pygame.mixer.music.play()
        time.sleep(200.5)
        pygame.mixer.music.stop()

    def picSelect(self):
        self.set_button_sound()
        default_dir = r"C:\Users\lenovon\Desktop"  # 设置默认打开目录
        fns = askopenfilename(
            filetypes=[("all", "*.*"), ("text file", "*.txt")],
            title=u"选择图片",
            initialdir=(os.path.expanduser(default_dir)))
        fns_list = list(fns)
        print("fns list:", fns_list)

    def writePoet(self):
        self.set_button_sound()
        tkinter.messagebox.showinfo('Message', '查看')

    def showPoet(self):
        self.set_button_sound()
        tkinter.messagebox.showinfo('Message', '展示结果')


if __name__ == "__main__":
    demo = create_UI()

    demo.ui()
