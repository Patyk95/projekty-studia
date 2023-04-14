import tkinter as ttk
import sqlite3
from tkinter import messagebox

class Inventory():
    def __init__(self,master=None):
        super().__init__()
        self.master=master
        master.title('Simple Inventory System')
        master.geometry('600x400')    
        master.config(background='black')
        self.create_database()
        labe1=ttk.Label(self.master,text='Please pass material name: ',font=('Arial',17),width=22,background='orange')
        labe1.grid(row=0,column=0,padx=10,pady=10)
        self.entry1=ttk.Entry(self.master,font=('Arial',17),width=18,background='white')
        self.entry1.grid(row=0,column=1,padx=10,pady=10)
        labe2=ttk.Label(self.master,text='Please scan material code: ',font=('Arial',17),width=22,background='orange')
        labe2.grid(row=1,column=0,padx=10,pady=10)
        self.entry2=ttk.Entry(self.master,font=('Arial',17),width=18,background='white')
        self.entry2.grid(row=1,column=1,padx=10,pady=10)
        labe3=ttk.Label(self.master,text='Please provide value: ',font=('Arial',17),width=22,background='orange')
        labe3.grid(row=2,column=0,padx=10,pady=10)
        self.entry3=ttk.Entry(self.master,font=('Arial',17),width=18,background='white')
        self.entry3.grid(row=2,column=1,padx=10,pady=10)
        button1=ttk.Button(self.master,text="ADD TO DATABSE",command=self.insert_db,font=('Arial',15),width=18,background='green')
        button1.grid(row=3,column=1,padx=10,pady=10)
        button2=ttk.Button(self.master,text="DISPLAY DATABASE",command=self.show_db,font=('Arial',15),width=18,background='purple')
        button2.grid(row=4,column=1,padx=10,pady=10)
        button3=ttk.Button(self.master,text="DROP DATABASE",command=self.drop_db,font=('Arial',15),width=18,background='RED')
        button3.grid(row=5,column=1,padx=10,pady=10)
        button4=ttk.Button(self.master,text="CLEAN DATABASE",command=self.clean_db,font=('Arial',15),width=18,background='ORANGE')
        button4.grid(row=6,column=1,padx=10,pady=10)
        
        
        self.master.mainloop()


    def create_database(self):
        con=sqlite3.connect('Materials_db')
        cur=con
        cur.execute('create table if not exists materials (id integer primary key autoincrement,name,scan_code,value)')

    def insert_db(self):
        con=sqlite3.connect('Materials_db')
        cur=con
        cur.execute('insert into materials(name,scan_code,value) values(:n,:s,:v)',{
                    'n':self.entry1.get(),
                    's':self.entry2.get(),
                    'v':self.entry3.get()})
        con.commit()
        messagebox.showinfo('Great','Your Product was added to database')
        self.entry1.delete(0,ttk.END)
        self.entry2.delete(0,ttk.END)
        self.entry3.delete(0,ttk.END)    

    def show_db(self):
        con=sqlite3.connect('Materials_db')
        cur=con
        search=cur.execute('select * from materials')
        for row in search:
            print(row)
        
    def drop_db(self):
        con=sqlite3.connect('Materials_db')
        cur=con
        cur.execute('drop table materials')
        con.commit()
        messagebox.showinfo('Info','Your database was dropped!')
    
    def clean_db(self):
        con=sqlite3.connect('Materials_db')
        cur=con
        cur.execute('delete from materials')
        con.commit()
        messagebox.showinfo('Info','Your database was cleaned!')


ob1=Inventory(ttk.Tk())

