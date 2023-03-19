import tkinter
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

window = tkinter.Tk()
from tkinter import Button,Label,Entry

window.title("CALCULATOR")
window.geometry('630x850')
window.configure(background='#001a00')

calculation=''

text_input=StringVar()


def clear_func():
    global calculation
    calculation=''
    display.delete(1.0,'end')


def evaluate_calculation():
    global calculation
    try:
        calculation=str(eval(calculation))
        display.delete(1.0,'end')
        display.insert(1.0,calculation)
        print (calculation)
    except:
        clear_func()
        display.insert(1.0,'ERROR')


def  add_to_calculator(symbol):
    global calculation
    calculation+= str(symbol)
    display.delete(1.0,'end')
    display.insert(1.0,calculation)
   

def backspace():
    global calculation
    global calculation
    calculation= calculation[0:len(calculation)-1]
    display.delete(1.0,'end')
    display.insert(1.0,calculation)
    
    


display=Text(window,width=16,height=2,border=3,font=('Arial',24),background='#00cc00')
display.grid(row=0,column=0,columnspan=7,pady=10,padx=10,sticky ='swse')

b7 = Button(window, text='7',command=lambda:add_to_calculator(7),font=('Arial', 45))
b7.grid(row=2, column=0, padx=10, pady=10)
b8 = Button(window, text='8',command=lambda:add_to_calculator(8), font=('Arial', 45))
b8.grid(row=2, column=1, padx=10, pady=10)
b9 = Button(window, text='9',command=lambda:add_to_calculator(9), font=('Arial', 45))
b9.grid(row=2, column=2, padx=10, pady=10)
b4 = Button(window, text='4',command=lambda:add_to_calculator(4), font=('Arial', 45))
b4.grid(row=3, column=0, padx=10, pady=10)
b5 = Button(window, text='5',command=lambda:add_to_calculator(5), font=('Arial', 45))
b5.grid(row=3, column=1, padx=10, pady=10)
b6 = Button(window, text='6',command=lambda:add_to_calculator(6), font=('Arial', 45))
b6.grid(row=3, column=2, padx=10, pady=10)
b1 = Button(window, text='1',command=lambda:add_to_calculator(1), font=('Arial', 45))
b1.grid(row=4, column=0, padx=10, pady=10)
b2 = Button(window, text='2',command=lambda:add_to_calculator(2), font=('Arial', 45))
b2.grid(row=4, column=1, padx=10, pady=10)
b3 = Button(window, text='3',command=lambda:add_to_calculator(3), font=('Arial', 45))
b3.grid(row=4, column=2, padx=10, pady=10)
b10 = Button(window, text='-',command=lambda:add_to_calculator('-'), font=('Arial', 45),background="#b3b3b3")
b10.grid(row=4, column=3, padx=10, pady=10)
b11 = Button(window, text='/',command=lambda:add_to_calculator('/'), font=('Arial', 45),width=2,background="#b3b3b3")
b11.grid(row=3, column=3, padx=10, pady=10)
b12 = Button(window, text='*',command=lambda:add_to_calculator('*'), font=('Arial', 45),width=2,background="#b3b3b3")
b12.grid(row=2, column=3, padx=10, pady=10)
b13 = Button(window, text='+', command=lambda:add_to_calculator('+'),font=('Arial', 45),width=2,background="#b3b3b3")
b13.grid(row=5, column=3, padx=10, pady=10)
b14 = Button(window, text='=', command=evaluate_calculation,font=('Arial', 45),width=2,background="#b3b3b3")
b14.grid(row=6, column=3, padx=10, pady=10)
b15 = Button(window, text='.',command=lambda:add_to_calculator('.'), height=2,font=('Arial',25),width=10,background="#b3b3b3")
b15.grid(row=6, column=0, padx=10, pady=10,columnspan=3, rowspan=1, sticky ='swse')

b16= Button(window, text='0',height=2, font=('Arial', 27),width=10)
b16.grid(row=5, column=0, padx=10, pady=10,columnspan=3, rowspan=1, sticky ='swse')

b16= Button(window, text='Clear', height=6,font=('Arial', 25),command=clear_func,width=8,background='red')
b16.grid(row=1, column=6, padx=10, pady=10, rowspan=3, sticky ='swse')

b17= Button(window, text='Backspace', command=backspace,height=6,font=('Arial', 25),width=8,background='orange')
b17.grid(row=4, column=6, padx=10, pady=10, rowspan=2, sticky ='swse')

img = ImageTk.PhotoImage(Image.open("C:\\Users\\prajt\\Desktop\wsb.jpg"))


b18= Label(window, image=img)
b18.grid(row=6, column=6, padx=10, pady=10)




        










window.mainloop()