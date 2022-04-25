#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from tkinter import *


def name():
    label['text'] = 'Игорь'


def number():
    label['text'] = '+4 821 222-11-23'


def adress():
    label['text'] = 'Россия, г. Ставрополь'


if __name__ == '__main__':
    root = Tk()
    var = IntVar()
    var.set(-1)
    Radiobutton(indicatoron=0, text="Имя", command=name,
    variable=var, value=0).pack()
    Radiobutton(indicatoron=0, text="Номер", command=number,
    variable=var, value=1).pack()
    Radiobutton(indicatoron=0, text="Адресс", command=adress,
    variable=var, value=2).pack()
    label = Label(width=40, height=25)
    label.pack()
    root.mainloop()