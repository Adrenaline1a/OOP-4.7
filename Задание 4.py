#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import Tk, Text, Button, Entry, END, filedialog


def save():
    name = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=(("Текстовый файл", "*.txt"),))
    data = text.get(1.0, END)
    with open(name, 'w', encoding="utf-8") as f:
        f.write(data)


def opening():
    text.delete(1.0, END)
    name = filedialog.askopenfilename()
    with open(name, 'r', encoding="utf-8") as f:
        data = f.read()
    text.insert(1.0, data)


if __name__ == '__main__':
    root = Tk()
    text = Text(width=100, height=80,)
    ent = Entry(width=20)
    but1 = Button(text='Открыть', width=10, pady=5, command=opening)
    but2 = Button(text='Сохранить', width=10, pady=5, command=save)
    ent.pack()
    but1.pack()
    but2.pack()
    text.pack()
    root.mainloop()
