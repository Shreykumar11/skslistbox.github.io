from tkinter import *
from tkinter import messagebox

def add():
    a=s1.get()
    if k.get()==1:
        lb1.insert(END, a)
    elif k.get()==2:
        lb2.insert(END, a)
    s1.set(a)

def delete():
    a=s1.get()
    lb1.delete(ANCHOR)
    lb2.delete(ANCHOR)

def display():
    k.set(0)
    a1=""
    a2=""
    a1=lb1.get(ANCHOR)
    a2=lb2.get(ANCHOR)
    if a1 !="":
        messagebox.showinfo("MALE", a1)
    if a2 !="":
        messagebox.showinfo("FEMALE", a2)

def clear():
    s1.set("")
    k.set(0)

def reset():
    s1.set("")
    k.set(0)
    lb1.delete(0,END)
    lb2.delete(0, END)

root=Tk()
root.title("WINDOWS")
root.geometry("500x500")
root.configure(bg="yellow")

k=IntVar()
s1=StringVar()
s1.set("")

l1=Label(root, text="Name", font="Cambria 18 bold", bg="pink")
l1.place(x=100, y=50)
e1=Entry(root, textvariable=s1, width=30, bg="cyan")
e1.place(x=200, y=55)

r1=Radiobutton(root, text="Male", variable=k, value=1)
r1.place(x=130, y=100)
r2=Radiobutton(root, text="Female", variable=k, value=2)
r2.place(x=330, y=100)

lb1=Listbox(root, height=15, width=35, bg="cyan")
lb1.place(x=50, y=150)
lb2=Listbox(root, height=15, width=35, bg="cyan")
lb2.place(x=270, y=150)

b1=Button(root, text="ADD", bg="black", fg="white", command=add)
b1.place(x=50, y= 420)
b2=Button(root, text="DELETE", bg="black", fg="white", command=delete)
b2.place(x=100, y= 420)
b3=Button(root, text="DISPLAY", bg="black", fg="white", command=display)
b3.place(x=170, y= 420)
b4=Button(root, text="CLEAR", bg="black", fg="white", command=clear)
b4.place(x=240, y= 420)
b5=Button(root, text="RESET", bg="black", fg="white", command=reset)
b5.place(x=300, y= 420)
b6=Button(root, text="EXIT", bg="red", fg="white", command=root.destroy)
b6.place(x=370, y= 420)

root.mainloop()
