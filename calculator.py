import tkinter
import tkinter as tk
from tkinter import *

window = tkinter.Tk()
from tkinter import Button,Label,Entry

window.title("CALCULATOR")
window.geometry('630x850')
window.configure(background='#00CCFF')



text_input=StringVar()

display=Entry(window,width=15,textvariable=text_input,font=('Arial',45),background='white')
display.grid(row=0,column=0,columnspan=7,pady=10,padx=10,sticky ='swse')

b7 = Button(window, text='7',command=lambda:button_clik(7),font=('Arial', 45))
b7.grid(row=2, column=0, padx=10, pady=10)
b8 = Button(window, text='8', font=('Arial', 45))
b8.grid(row=2, column=1, padx=10, pady=10)
b9 = Button(window, text='9', font=('Arial', 45))
b9.grid(row=2, column=2, padx=10, pady=10)
b4 = Button(window, text='4', font=('Arial', 45))
b4.grid(row=3, column=0, padx=10, pady=10)
b5 = Button(window, text='5', font=('Arial', 45))
b5.grid(row=3, column=1, padx=10, pady=10)
b6 = Button(window, text='6', font=('Arial', 45))
b6.grid(row=3, column=2, padx=10, pady=10)
b1 = Button(window, text='1', font=('Arial', 45))
b1.grid(row=4, column=0, padx=10, pady=10)
b2 = Button(window, text='2', font=('Arial', 45))
b2.grid(row=4, column=1, padx=10, pady=10)
b3 = Button(window, text='3', font=('Arial', 45))
b3.grid(row=4, column=2, padx=10, pady=10)
b10 = Button(window, text='-', font=('Arial', 45))
b10.grid(row=4, column=3, padx=10, pady=10)
b11 = Button(window, text='/', font=('Arial', 45),width=2)
b11.grid(row=3, column=3, padx=10, pady=10)
b12 = Button(window, text='x', font=('Arial', 45),width=2)
b12.grid(row=2, column=3, padx=10, pady=10)


b13 = Button(window, text='+', font=('Arial', 45),width=2)
b13.grid(row=5, column=3, padx=10, pady=10)

b14 = Button(window, text='=', font=('Arial', 45),width=2)
b14.grid(row=6, column=3, padx=10, pady=10)

b15 = Button(window, text='.', height=2,font=('Arial',25),width=10)
b15.grid(row=6, column=0, padx=10, pady=10,columnspan=3, rowspan=1, sticky ='swse')

b16= Button(window, text='0',height=2, font=('Arial', 27),width=10)
b16.grid(row=5, column=0, padx=10, pady=10,columnspan=3, rowspan=1, sticky ='swse')

b16= Button(window, text='Clear', height=6,font=('Arial', 25),width=8,background='red')
b16.grid(row=1, column=6, padx=10, pady=10, rowspan=3, sticky ='swse')

b17= Button(window, text='Backspace', height=6,font=('Arial', 25),width=8,background='orange')
b17.grid(row=4, column=6, padx=10, pady=10, rowspan=3, sticky ='swse')


def button_clik(number):
    global  operator
    operator = operator + str(number)
    text_input.set(operator)

window.mainloop()