import math
import tkinter
from tkinter import*
from math import*
win=Tk()

width=win.winfo_screenwidth()
height=win.winfo_screenheight()
c_x=int(width/2-570/2)
c_y=int(height/2-600/2)

win.title("Strange Calculator")
win.config(bg="#2C3E50")
win.geometry(f"650x600+{c_x}+{c_y}")
win.resizable(False,False)


equation=""
def show(value):
    global equation
    equation+=value
    lab.config(text=equation)

def clear():
    global equation
    equation=""
    lab.config(text=equation)

def expression_break(sign,expression):
    values=expression.split(sign,1)
    return values
    
def scientific(expression):
    data=expression_break("(",expression)
    if data[0]=="tan":
        result=tan(float(data[1]))
    elif data[0]=="cos":
        result=cos(float(data[1]))
    elif data[0]=="sin":
        result=sin(float(data[1]))
    elif data[0]=="sin⁻¹":
        result=degrees(asin(float(data[1])))
    elif data[0]=="cos⁻¹":
        result=degrees(acos(float(data[1])))
    elif data[0]=="tan⁻¹":
        result=degrees(atan(float(data[1])))
    elif data[0]=="log":
        result=log10(float(data[1]))
    elif data[0]=="ln":
        result=log(float(data[1]))
    return result

def calculate():
    global equation
    if ("+" or "-" or "*" or "/") in equation:
        result=eval(equation)
    else:
        result=scientific(equation)
    lab.config(text=result)
    
    
        
lab=Label(win,width=30,height=2,text="",bg="#ECF0F1",font=("Arial",30))
lab.pack()

Button(win,text="x!",width=3,height=1,cursor="hand2",font=("arial",30,"bold"),bd=3,padx=10,pady=10,fg="white",bg="Grey",activebackground="#1ABC9C",relief="raised").place(x=1,y=100)
Button(win,text="∛x",width=3,height=1,cursor="hand2",font=("arial",30,"bold"),bd=3,padx=10,pady=10,fg="white",bg="Grey",activebackground="#1ABC9C",relief="raised").place(x=100,y=100)
Button(win,text="√x",width=3,height=1,cursor="hand2",font=("arial",30,"bold"),bd=3,padx=10,pady=10,fg="white",bg="Grey",activebackground="#1ABC9C",relief="raised").place(x=190,y=100)
Button(win,text="x³",width=3,height=1,cursor="hand2",font=("arial",30,"bold"),bd=3,padx=10,pady=10,fg="white",bg="Grey",activebackground="#1ABC9C",relief="raised").place(x=280,y=100)
Button(win,text="x²",width=3,height=1,cursor="hand2",font=("arial",30,"bold"),bd=3,padx=10,pady=10,fg="white",bg="Grey",activebackground="#1ABC9C",relief="raised").place(x=370,y=100)
Button(win,text="xⁿ",width=3,height=1,cursor="hand2",font=("arial",30,"bold"),bd=3,padx=10,pady=10,fg="white",bg="Grey",activebackground="#1ABC9C",relief="raised").place(x=460,y=100)
Button(win,text="C",width=3,height=1,cursor="hand2",font=("arial",30,"bold"),bd=3,padx=10,pady=10,fg="white",bg="Orange",command=lambda: clear(),activebackground="#1ABC9C",relief="raised").place(x=550,y=100)

Button(win,text="Sin",width=3,height=1,cursor="hand2",font=("arial",30,"bold"),bd=3,padx=10,pady=10,fg="white",bg="Light Blue",command=lambda:show("sin("),activebackground="#1ABC9C",relief="raised").place(x=1,y=200)
Button(win,text="Cos",width=3,height=1,cursor="hand2",font=("arial",30,"bold"),bd=3,padx=10,pady=10,fg="white",bg="Light Blue",command=lambda:show("cos("),activebackground="#1ABC9C",relief="raised").place(x=100,y=200)
Button(win,text="Tan",width=3,height=1,cursor="hand2",font=("arial",30,"bold"),bd=3,padx=10,pady=10,fg="white",bg="Light Blue",command=lambda:show("tan("),activebackground="#1ABC9C",relief="raised").place(x=190,y=200)
Button(win,text="log",width=3,height=1,cursor="hand2",font=("arial",30,"bold"),bd=3,padx=10,pady=10,fg="white",bg="Grey",command=lambda:show("log("),activebackground="#1ABC9C",relief="raised").place(x=280,y=200)
Button(win,text="ln",width=3,height=1,cursor="hand2",font=("arial",30,"bold"),bd=3,padx=10,pady=10,fg="white",bg="Grey",command=lambda:show("ln("),activebackground="#1ABC9C",relief="raised").place(x=370,y=200)
Button(win,text="π",width=3,height=1,cursor="hand2",font=("arial",30,"bold"),bd=3,padx=10,pady=10,fg="white",bg="Grey",command=lambda:show("3.141592653"),activebackground="#1ABC9C",relief="raised").place(x=460,y=200)
Button(win,text="+",width=3,height=1,cursor="hand2",font=("arial",30,"bold"),bd=3,padx=10,pady=10,fg="white",bg="Light Blue",command=lambda:show("+"),activebackground="#1ABC9C",relief="raised").place(x=550,y=200)

Button(win,text="(",width=3,height=1,cursor="hand2",font=("arial",30,"bold"),bd=3,padx=10,pady=10,fg="white",bg="Grey",command=lambda:show("("),activebackground="#1ABC9C",relief="raised").place(x=1,y=300)
Button(win,text="sin⁻¹",width=4,height=1,cursor="hand2",font=("arial",30,"bold"),bd=3,padx=10,pady=10,fg="white",bg="Red",command=lambda:show("sin⁻¹("),activebackground="#1ABC9C",relief="raised").place(x=101,y=300)
Button(win,text="cos⁻¹",width=4,height=1,cursor="hand2",font=("arial",30,"bold"),bd=3,padx=10,pady=10,fg="white",bg="Red",command=lambda:show("cos⁻¹("),activebackground="#1ABC9C",relief="raised").place(x=225,y=300)
Button(win,text="tan⁻¹",width=4,height=1,cursor="hand2",font=("arial",30,"bold"),bd=3,padx=10,pady=10,fg="white",bg="Red",command=lambda:show("tan⁻¹("),activebackground="#1ABC9C",relief="raised").place(x=345,y=300)
Button(win,text=")",width=3,height=1,cursor="hand2",font=("arial",30,"bold"),bd=3,padx=10,pady=10,fg="white",bg="Grey",command=lambda:show(")"),activebackground="#1ABC9C",relief="raised").place(x=460,y=300)
Button(win,text="÷",width=3,height=1,cursor="hand2",font=("arial",30,"bold"),bd=3,padx=10,pady=10,fg="white",bg="Light Blue",command=lambda:show("/"),activebackground="#1ABC9C",relief="raised").place(x=550,y=300)


Button(win,text="4",width=3,height=1,cursor="hand2",font=("arial",30,"bold"),bd=3,padx=10,pady=10,fg="white",bg="Grey",command=lambda:show("4"),activebackground="#1ABC9C",relief="raised").place(x=1,y=400)
Button(win,text="5",width=3,height=1,cursor="hand2",font=("arial",30,"bold"),bd=3,padx=10,pady=10,fg="white",bg="Grey",command=lambda:show("5"),activebackground="#1ABC9C",relief="raised").place(x=100,y=400)
Button(win,text="6",width=3,height=1,cursor="hand2",font=("arial",30,"bold"),bd=3,padx=10,pady=10,fg="white",bg="Grey",command=lambda:show("6"),activebackground="#1ABC9C",relief="raised").place(x=190,y=400)
Button(win,text="7",width=3,height=1,cursor="hand2",font=("arial",30,"bold"),bd=3,padx=10,pady=10,fg="white",bg="Grey",command=lambda:show("7"),activebackground="#1ABC9C",relief="raised").place(x=280,y=400)
Button(win,text="8",width=3,height=1,cursor="hand2",font=("arial",30,"bold"),bd=3,padx=10,pady=10,fg="white",bg="Grey",command=lambda:show("8"),activebackground="#1ABC9C",relief="raised").place(x=370,y=400)
Button(win,text="9",width=3,height=1,cursor="hand2",font=("arial",30,"bold"),bd=3,padx=10,pady=10,fg="white",bg="Grey",command=lambda:show("9"),activebackground="#1ABC9C",relief="raised").place(x=460,y=400)
Button(win,text="-",width=3,height=1,cursor="hand2",font=("arial",30,"bold"),bd=3,padx=10,pady=10,fg="white",bg="Light Blue",command=lambda:show("-"),activebackground="#1ABC9C",relief="raised").place(x=550,y=400)

Button(win,text="3",width=3,height=1,cursor="hand2",font=("arial",30,"bold"),bd=3,padx=10,pady=10,fg="white",bg="Grey",command=lambda:show("3"),activebackground="#1ABC9C",relief="raised").place(x=1,y=500)
Button(win,text="2",width=3,height=1,cursor="hand2",font=("arial",30,"bold"),bd=3,padx=10,pady=10,fg="white",bg="Grey",command=lambda:show("2"),activebackground="#1ABC9C",relief="raised").place(x=100,y=500)
Button(win,text="1",width=3,height=1,cursor="hand2",font=("arial",30,"bold"),bd=3,padx=10,pady=10,fg="white",bg="Grey",command=lambda:show("1"),activebackground="#1ABC9C",relief="raised").place(x=190,y=500)
Button(win,text="0",width=3,height=1,cursor="hand2",font=("arial",30,"bold"),bd=3,padx=10,pady=10,fg="white",bg="Grey",command=lambda:show("0"),activebackground="#1ABC9C",relief="raised").place(x=280,y=500)
Button(win,text=".",width=3,height=1,cursor="hand2",font=("arial",30,"bold"),bd=3,padx=10,pady=10,fg="white",bg="Grey",command=lambda:show("."),activebackground="#1ABC9C",relief="raised").place(x=370,y=500)
Button(win,text="=",width=3,height=1,cursor="hand2",font=("arial",30,"bold"),bd=3,padx=10,pady=10,fg="white",bg="Light Blue",command=calculate,activebackground="#1ABC9C",relief="raised").place(x=460,y=500)
Button(win,text="x",width=3,height=1,cursor="hand2",font=("arial",30,"bold"),bd=3,padx=10,pady=10,fg="white",bg="Light Blue",command=lambda:show("*"),activebackground="#1ABC9C",relief="raised").place(x=550,y=500)



win.mainloop()
