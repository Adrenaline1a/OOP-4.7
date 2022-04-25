#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from tkinter import *


def save(event):
    name = ent.get()
    data = text.get(1.0, END)
    with open(name, 'w', encoding="utf-8") as f:
        f.write(data)


def opening(event):
    text.delete(1.0, END)
    name = ent.get()
    with open(name, 'r', encoding="utf-8") as f:
        data = f.read()
    text.insert(1.0, data)


if __name__ == '__main__':
    root = Tk()
    text = Text(width=25, height=5,)
    ent = Entry(width=20)
    but1 = Button(text='Открыть', width=5, pady=5)
    but2 = Button(text='Сохранить', width=5, pady=5)
    but1.bind('<Button-1>', opening)
    but2.bind('<Button-1>', save)
    ent.pack()
    but1.pack()
    but2.pack()
    text.pack()
    root.mainloop()