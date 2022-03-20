from tkinter import *
#create a window
root = Tk()
root.title("CALCULATOR")
input=Entry(root,width=50)
input.grid(row=0,column=0,columnspan=3)
#defining button functions
def myclick(number):
    last=input.get()
    input.delete(0,END)
    input.insert(0, str(last)+ str(number))
def clear():
    input.delete(0,END)
def add():
    f_num=input.get()
    global first
    first=int(f_num)
    global math
    math="ADD"
    input.delete(0,END)
def sub():
    f_num=input.get()
    global first
    first=int(f_num)
    global math
    math="SUB"
    input.delete(0,END)
def mul():
    f_num=input.get()
    global first
    first=int(f_num)
    global math
    math="MUL"
    input.delete(0,END)
def div():
    f_num=input.get()
    global first
    
    first=int(f_num)
    global math
    math="DIV"
    input.delete(0,END)
def equal():
    second=input.get()
    second=int(second)
    input.delete(0,END)
    if math=="ADD":
        result=first+second
        input.insert(0,result)
    elif math=="SUB":
        result=first-second
        input.insert(0,result)
    elif math=="MUL":
        result=first*second
        input.insert(0,result)
    elif math=="DIV":
        result=first/second
        input.insert(0,result)

#defining the buutons
Button_1=Button(root,text="1",command=lambda: myclick(1),padx=40,pady=20,bg="light blue",activebackground="blue")
Button_2=Button(root,text="2",command=lambda: myclick(2),padx=40,pady=20,bg="light blue",activebackground="blue")
Button_3=Button(root,text="3",command=lambda: myclick(3),padx=40,pady=20,bg="light blue",activebackground="blue")
Button_4=Button(root,text="4",command=lambda: myclick(4),padx=40,pady=20,bg="light blue",activebackground="blue")
Button_5=Button(root,text="5",command=lambda: myclick(5),padx=40,pady=20,bg="light blue",activebackground="blue")
Button_6=Button(root,text="6",command=lambda: myclick(6),padx=40,pady=20,bg="light blue",activebackground="blue")
Button_7=Button(root,text="7",command=lambda: myclick(7),padx=40,pady=20,bg="light blue",activebackground="blue")
Button_8=Button(root,text="8",command=lambda: myclick(8),padx=40,pady=20,bg="light blue",activebackground="blue")
Button_9=Button(root,text="9",command=lambda: myclick(9),padx=40,pady=20,bg="light blue",activebackground="blue")
Button_0=Button(root,text="0",command=lambda: myclick(0),padx=40,pady=20,bg="light blue",activebackground="blue")
Button_clear=Button(root,text="Clear",command=clear,padx=80,pady=20,bg="pink",activebackground="red",fg="white")
Button_add=Button(root,text="+",command=add,padx=40,pady=20,bg="light yellow",activebackground="yellow")
Button_sub=Button(root,text="-",command=sub,padx=40,pady=20,bg="light yellow",activebackground="yellow")
Button_mul=Button(root,text="*",command=mul,padx=40,pady=20,bg="light yellow",activebackground="yellow")
Button_div=Button(root,text="/",command=div,padx=40,pady=20,bg="light yellow",activebackground="yellow")
Button_equal=Button(root,text="=",padx=80,pady=20,command=equal,bg="light green",activebackground="green")
#putting in grid view
Button_7.grid(row=1,column=0)
Button_8.grid(row=1,column=1)
Button_9.grid(row=1,column=2)

Button_4.grid(row=2,column=0)
Button_5.grid(row=2,column=1)
Button_6.grid(row=2,column=2)

Button_1.grid(row=3,column=0)
Button_2.grid(row=3,column=1)
Button_3.grid(row=3,column=2)

Button_0.grid(row=4,column=0)
Button_clear.grid(row=4,column=1,columnspan=2)

Button_add.grid(row=5,column=0)
Button_sub.grid(row=5,column=1)
Button_mul.grid(row=5,column=2)

Button_div.grid(row=6,column=0)
Button_equal.grid(row=6,column=1,columnspan=2)

root.mainloop()

