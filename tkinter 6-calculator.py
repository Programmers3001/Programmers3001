from tkinter import *

#screen and input
root=Tk()
root.title('Calculator')
e=Entry(root, width=37, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

#what button do?
def buttonclick(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))
def buttonclear():
    e.delete(0,END)
def buttonadd():
    stnum=e.get()
    global fnum
    global math
    math='add'
    fnum=int(stnum)
    e.delete(0, END)
def buttonequal():
    ndnum=e.get()
    e.delete(0, END)
    if math=='add':
        e.insert(0, fnum + int(ndnum))
    elif math=='subtract':
        e.insert(0, fnum - int(ndnum))
    elif math=='multiply':
        e.insert(0, fnum * int(ndnum))
    elif math=='devide':
        e.insert(0, fnum / int(ndnum))
def buttonsubtract():
    stnum=e.get()
    global fnum
    global math
    math='subtract'
    fnum=int(stnum)
    e.delete(0, END)
def buttonmultiply():
    stnum=e.get()
    global fnum
    global math
    math='multiply'
    fnum=int(stnum)
    e.delete(0, END)
def buttondevide():
    stnum=e.get()
    global fnum
    global math
    math='devide'
    fnum=int(stnum)
    e.delete(0, END)
    
    
    
#define buttons
button1=Button(root, text='1', padx=40, pady=20, command=lambda: buttonclick(1))
button2=Button(root, text='2', padx=40, pady=20, command=lambda:buttonclick(2))
button3=Button(root, text='3', padx=40, pady=20, command=lambda:buttonclick(3))
button4=Button(root, text='4', padx=40, pady=20, command=lambda:buttonclick(4))
button5=Button(root, text='5', padx=40, pady=20, command=lambda:buttonclick(5))
button6=Button(root, text='6', padx=40, pady=20, command=lambda:buttonclick(6))
button7=Button(root, text='7', padx=40, pady=20, command=lambda:buttonclick(7))
button8=Button(root, text='8', padx=40, pady=20, command=lambda:buttonclick(8))
button9=Button(root, text='9', padx=40, pady=20, command=lambda:buttonclick(9))
button0=Button(root, text='0', padx=40, pady=20, command=lambda:buttonclick(0))
buttonadd=Button(root, text='+', padx=39, pady=20, command=buttonadd)
buttonequal=Button(root, text='=', padx=91, pady=20, command=buttonequal)
buttonc=Button(root, text='C', padx=91, pady=20, command=buttonclear)
buttonsubtract=Button(root, text='-', padx=41, pady=20, command=buttonsubtract)
buttonmultiply=Button(root, text='*', padx=39, pady=20, command=buttonmultiply)
buttondevide=Button(root, text='/', padx=45, pady=20, command=buttondevide)


#put buttons on the screen
button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)

button0.grid(row=4,column=0)
buttonadd.grid(row=5,column=0)
buttonequal.grid(row=5,column=1, columnspan=2)
buttonc.grid(row=4,column=1,columnspan=2)

buttonsubtract.grid(row=6,column=0)
buttonmultiply.grid(row=6,column=1)
buttondevide.grid(row=6,column=2)




#running file
root.mainloop()
