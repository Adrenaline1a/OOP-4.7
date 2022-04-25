#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from tkinter import *


def red(event):
    ent1.delete(0, END)
    l1['text'] = "Красный"
    ent1.insert(0, "#ff0000")

def orange(event):
    ent1.delete(0, END)
    l1['text'] = 'Оранжевый'
    ent1.insert(0, "#ff7d00")

def yelow(event):
    ent1.delete(0, END)
    l1['text'] = 'Жёлтый'
    ent1.insert(0, "#ffff00")

def green(event):
    ent1.delete(0, END)
    l1['text'] = 'Зелёный'
    ent1.insert(0, "#00ff00")

def gol(event):
    ent1.delete(0, END)
    l1['text'] = 'Голубой'
    ent1.insert(0, "#007dff")

def blue(event):
    ent1.delete(0, END)
    l1['text'] = 'Синий'
    ent1.insert(0, "#0000ff")

def fiol(event):
    ent1.delete(0, END)
    l1['text'] = 'Фиолетовый'
    ent1.insert(0, "#7d00ff")

if __name__ == '__main__':
    root = Tk()
    l1 = Label(font="Arial 14", width=30)
    ent1 = Entry(width=30)
    but1 = Button(bg='#ff0000', width=30, pady=5)
    but2 = Button(bg='#ff7d00', width=30, pady=5)
    but3 = Button(bg='#ffff00', width=30, pady=5)
    but4 = Button(bg='#00ff00', width=30, pady=5)
    but5 = Button(bg='#007dff', width=30, pady=5)
    but6 = Button(bg='#0000ff', width=30, pady=5)
    but7 = Button(bg='#7d00ff', width=30, pady=5)
    but1.bind('<Button-1>', red)
    but2.bind('<Button-1>', orange)
    but3.bind('<Button-1>', yelow)
    but4.bind('<Button-1>', green)
    but5.bind('<Button-1>', gol)
    but6.bind('<Button-1>', blue)
    but7.bind('<Button-1>', fiol)
    l1.pack()
    ent1.pack()
    but1.pack()
    but2.pack()
    but3.pack()
    but4.pack()
    but5.pack()
    but6.pack()
    but7.pack()
    root.mainloop()