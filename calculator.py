
from tkinter import *

root=Tk()
root.title("Simple Calculator")
root.iconbitmap("D:\SDE\Py\Calc1.ico")
input=Entry(root, width=35, borderwidth=5)
input.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def button_click(number):
    current=input.get()
     #deletes the entered string
    input.delete(0,END)
    input.insert(0,str(current)+str(number))
    
def button_clear():
    input.delete(0, END)


def button_add():
    global first_number
    global operation
    operation="+"
    first_number=int(input.get()) 
    input.delete(0,END)

def button_equal():
    second_number=input.get()
    input.delete(0, END)
    if(operation=="+"):
        sum=first_number+int(second_number)
        input.insert(0, sum)
    elif(operation=="-"):
        sub=first_number-int(second_number)
        input.insert(0, sub)
    elif(operation=="*"):
        mul=first_number*int(second_number)
        input.insert(0, mul)
    elif(operation=="/"):
        div=first_number/int(second_number)
        input.insert(0, div)
    elif(operation=="%"):
        mod=first_number%int(second_number)
        input.insert(0, mod)
    

def button_mul():
    global first_number
    global operation
    operation="*"
    first_number=int(input.get()) 
    input.delete(0,END)

def button_div():
    global first_number
    global operation
    operation="/"
    first_number=int(input.get()) 
    input.delete(0,END)

def button_sub():
    global first_number
    global operation
    operation="-"
    first_number=int(input.get()) 
    input.delete(0,END)
button_1=Button(root, text="1",padx=40,pady=20, command=lambda: button_click(1))
button_2=Button(root, text="2",padx=40,pady=20, command=lambda: button_click(2))
button_3=Button(root, text="3",padx=40,pady=20, command=lambda: button_click(3))
button_4=Button(root, text="4",padx=40,pady=20, command=lambda: button_click(4))
button_5=Button(root, text="5",padx=40,pady=20, command=lambda: button_click(5))
button_6=Button(root, text="6",padx=40,pady=20, command=lambda: button_click(6))
button_7=Button(root, text="7",padx=40,pady=20, command=lambda: button_click(7))
button_8=Button(root, text="8",padx=40,pady=20, command=lambda: button_click(8))
button_9=Button(root, text="9",padx=40,pady=20, command=lambda: button_click(9))
button_0=Button(root, text="0",padx=40,pady=20, command=lambda: button_click(0))
button_clear=Button(root, text=" AC ",padx=80,pady=20, command=button_clear,bg="Red")
button_add=Button(root, text="+",padx=39,pady=20, command=button_add,bg="yellow")
button_equal=Button(root, text="=",padx=87,pady=20, command=button_equal,bg="blue")
button_mul=Button(root, text="*",padx=40,pady=20, command=button_mul,bg="pink")
button_div=Button(root, text="/",padx=40,pady=20, command=button_div,bg="lightblue")
button_sub=Button(root, text="-",padx=40,pady=20, command=button_sub,bg="yellow")

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_0.grid(row=4,column=0)
button_clear.grid(row=6,column=1, columnspan=2)
button_add.grid(row=5,column=0)
button_equal.grid(row=5,column=1, columnspan=2)
button_sub.grid(row=6, column=0)
button_mul.grid(row=4,column=1)
button_div.grid(row=4,column=2)





#button=Button(root, text="Submit",state=ACTIVE,padx=50, pady=50,  fg="black", bg="green")
#button.pack() 

root.mainloop()