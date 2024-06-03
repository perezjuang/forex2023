import tkinter as tk
from tkinter import *
from tkinter import ttk

class MyWindow:
    def __init__(self, win):
        self.lbl1=Label(win, text='First number')
        self.lbl1.place(x=100, y=50)
        
        self.lbl2=Label(win, text='Second number')
        self.lbl2.place(x=100, y=100)


        self.lbl3=Label(win, text='Result')
        self.lbl3.place(x=100, y=200)

        self.t1=Entry(bd=3)
        self.t1.place(x=200, y=50)

        self.t2=Entry()
        self.t2.place(x=200, y=100)

        self.t3=Entry()
        self.t3.place(x=200, y=200)


        self.btn1 = Button(win, text='Add')
        self.btn2=Button(win, text='Subtract')
      
        
        
        self.b1=Button(win, text='Add', command=self.add)
        self.b2=Button(win, text='Subtract')
        self.b2.bind('<Button-1>', self.sub)
        self.b1.place(x=100, y=150)
        self.b2.place(x=200, y=150)
        
        



        self.langs = ["C", "C++", "Java",  "Python", "PHP"]
        self.Combo = ttk.Combobox(win, values = self.langs)
        self.Combo.bind('<<ComboboxSelected>>', self.selectionChanged) 
        self.Combo.set("Pick an Option")
        self.Combo.place(x=300, y=300)


 
















    def selectionChanged(self, event) :
        print(self.Combo.get())


    def add(self):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1+num2
        self.t3.insert(END, str(result))
    def sub(self, event):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1-num2
        self.t3.insert(END, str(result))

window=Tk()
mywin=MyWindow(window)
window.title('Hello Python')
window.geometry("800x600+10+10")
window.mainloop()





