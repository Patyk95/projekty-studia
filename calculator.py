import tkinter
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

window = tkinter.Tk()
from tkinter import Button,Entry

window.title("CALCULATOR")
window.geometry('630x850')
window.configure(background='#001a00')


saved_values=0
saved_operator=0

text_input=StringVar()

def clear_func():
    global saved_values
    saved_values=''
    display.delete(0, tk.END)

def backspace():
    current_value = display.get()
    display.delete(len(current_value)-1,tk.END)
    
def operator_pressed(operator):
    global saved_number, saved_operator

    # odczytanie wartości z pola tekstowego
    current_value = display.get()

    if saved_operator:
        # podmiana operatora bez wykonywania obliczenia
        saved_operator = operator
        display.delete(0, tk.END)
    else:
        # zapisanie zapamiętanej liczby i operatora
        saved_number = float(current_value)
        saved_operator = operator

        # wyczyszczenie pola tekstowego
        display.delete(0, tk.END)

# funkcja do wykonania obliczenia po wciśnięciu przycisku =
def perform_calculation():
    global saved_number, saved_operator

    # odczytanie wartości z pola tekstowego
    current_value = display.get()
    new_number = float(current_value)

    # wykonanie obliczenia i wyświetlenie wyniku
    if saved_operator == '+':
        result = saved_number + new_number
    elif saved_operator == '-':
        result = saved_number - new_number
    elif saved_operator == '*':
        result = saved_number * new_number
    elif saved_operator == '/':
        result = saved_number / new_number
    else:
        result = float(new_number)
    display.delete(0, tk.END)
    display.insert(0, str(result))

    # zresetowanie zmiennych globalnych
    saved_number = result
    saved_operator = ''



display=Entry(window,width=16,border=3,font=('Arial',24),background='#00cc00')
display.grid(row=0,column=0,columnspan=7,pady=10,padx=10,sticky ='swse')

b7 = Button(window, text='7',command=lambda:display.insert(tk.END, '7'),font=('Arial', 45))
b7.grid(row=2, column=0, padx=10, pady=10)
b8 = Button(window, text='8',command=lambda:display.insert(tk.END, '8'), font=('Arial', 45))
b8.grid(row=2, column=1, padx=10, pady=10)
b9 = Button(window, text='9',command=lambda:display.insert(tk.END, '9'), font=('Arial', 45))
b9.grid(row=2, column=2, padx=10, pady=10)
b4 = Button(window, text='4',command=lambda:display.insert(tk.END, '4'), font=('Arial', 45))
b4.grid(row=3, column=0, padx=10, pady=10)
b5 = Button(window, text='5',command=lambda:display.insert(tk.END, '5'), font=('Arial', 45))
b5.grid(row=3, column=1, padx=10, pady=10)
b6 = Button(window, text='6',command=lambda:display.insert(tk.END, '6'), font=('Arial', 45))
b6.grid(row=3, column=2, padx=10, pady=10)
b1 = Button(window, text='1',command=lambda:display.insert(tk.END, '1'), font=('Arial', 45))
b1.grid(row=4, column=0, padx=10, pady=10)
b2 = Button(window, text='2',command=lambda:display.insert(tk.END, '2'), font=('Arial', 45))
b2.grid(row=4, column=1, padx=10, pady=10)
b3 = Button(window, text='3',command=lambda:display.insert(tk.END, '3'), font=('Arial', 45))
b3.grid(row=4, column=2, padx=10, pady=10)
b10 = Button(window, text='-',command=lambda:operator_pressed('-'), font=('Arial', 45),background="#b3b3b3")
b10.grid(row=4, column=3, padx=10, pady=10)
b11 = Button(window, text='/',command=lambda:operator_pressed('/'), font=('Arial', 45),width=2,background="#b3b3b3")
b11.grid(row=3, column=3, padx=10, pady=10)
b12 = Button(window, text='*',command=lambda:operator_pressed('*'), font=('Arial', 45),width=2,background="#b3b3b3")
b12.grid(row=2, column=3, padx=10, pady=10)



b13 = Button(window, text='+', font=('Arial', 45),width=2)

b13 = Button(window, text='+', command=lambda:operator_pressed('+'),font=('Arial', 45),width=2,background="#b3b3b3")

b13.grid(row=5, column=3, padx=10, pady=10)
b14 = Button(window, text='=', command=perform_calculation,font=('Arial', 45),width=2,background="#b3b3b3")
b14.grid(row=6, column=3, padx=10, pady=10)
b15 = Button(window, text='.',command=lambda:display.insert(tk.END, '.'), height=2,font=('Arial',25),width=10,background="#b3b3b3")
b15.grid(row=6, column=0, padx=10, pady=10,columnspan=3, rowspan=1, sticky ='swse')

b16= Button(window, text='0',command=lambda:display.insert(tk.END, '0'),height=2, font=('Arial', 27),width=10)
b16.grid(row=5, column=0, padx=10, pady=10,columnspan=3, rowspan=1, sticky ='swse')

b16= Button(window, text='Clear', height=6,font=('Arial', 25),command=clear_func,width=8,background='red')
b16.grid(row=1, column=6, padx=10, pady=10, rowspan=3, sticky ='swse')

b17= Button(window, text='Backspace', command=backspace,height=6,font=('Arial', 25),width=8,background='orange')
b17.grid(row=4, column=6, padx=10, pady=10, rowspan=2, sticky ='swse')

# img = ImageTk.PhotoImage(Image.open("C:\\Users\\prajt\\Desktop\wsb.jpg"))


# b18= Label(window, image=img)
# b18.grid(row=6, column=6, padx=10, pady=10)






window.mainloop()