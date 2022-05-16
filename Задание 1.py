#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from tkinter import *


def summ(event):
    try:
        s1 = float(ent1.get())
        s2 = float(ent2.get())
        l1['text'] = s1+s2
    except ValueError:
        l1['text'] = 'Ошибка'


def raz(event):
    try:
        s1 = float(ent1.get())
        s2 = float(ent2.get())
        l1['text'] = s1-s2
    except ValueError:
        l1['text'] = 'Ошибка'


def mul(event):
    try:
        s1 = float(ent1.get())
        s2 = float(ent2.get())
        l1['text'] = s1*s2
    except ValueError:
        l1['text'] = 'Ошибка'


def dele(event):
    try:
        s1 = float(ent1.get())
        s2 = float(ent2.get())
        l1['text'] = s1/s2
    except ValueError:
        l1['text'] = 'Ошибка'
    except ZeroDivisionError:
        l1['text'] = 'Деление на 0!'


if __name__ == '__main__':
    root = Tk()
    ent1 = Entry(width=20)
    ent2 = Entry(width=20)
    but1 = Button(text='+')
    but2 = Button(text='-')
    but3 = Button(text='*')
    but4 = Button(text='/')
    l1 = Label(font="Arial 14")
    but1.bind('<Button-1>', summ)
    but2.bind('<Button-1>', raz)
    but3.bind('<Button-1>', mul)
    but4.bind('<Button-1>', dele)
    l1.config(bd=10)
    ent1.pack()
    ent2.pack()
    but1.pack()
    but2.pack()
    but3.pack()
    but4.pack()
    l1.pack()
    root.mainloop()