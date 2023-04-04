import customtkinter as ctk


class Inventory(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Inventory System')
        self.geometry('600x400')    
        self.config(background='black')
        labe1=ctk.CTkLabel(self,text='Please provide Artikal Number: ',font=('Arial',20),width=18,bg_color='orange')
        labe1.grid(row=0,column=0,padx=10,pady=10)
        entry1=ctk.CTkEntry(self,font=('Arial',20),bg_color='green')
        entry1.grid(row=0,column=1,padx=10,pady=10)
        button1=ctk.CTkButton(self,text="CLICK",command=self.clikc,font=('Arial',15),border_width=6,bg_color='white')
        button1.grid(row=1,column=1,padx=10,pady=10)

        self.mainloop()

    def clikc(self):
        print('you have put a button')



ob1=Inventory()




