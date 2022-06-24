import tkinter as tk
from functools import partial


window = tk.Tk()
window.geometry("250x150")
name = tk.Label(text="Alex Instruments LI-84")
name.pack()


#On Screen Output

display_text = tk.StringVar()
display = tk.Label(window, textvariable=display_text)
display.pack()



#functions


#Submit entry
dothedo = []
res = []
def subnum(numbah):
    printbut(numbah+10)
    dothedo.append(numbah)
    print (numbah)
    print (dothedo)


#Convert to multiple digits
def numcon(dothetwo):

    # Converting integer list to string list
    s = [str(i) for i in dothetwo]

    # Join list items using join()
    res.append(int("".join(s)))

    return(res)



print(res)


y = 0
def Operation(value):
    printbut(value)
    global y
    y = value
    print (dothedo)
    numcon(dothedo)
    dothedo.clear()
    print(res)


#Calculating result
def Equals():
    numcon(dothedo)
    if y == 0:
        print (res[0] + res[1])
        print (res[0], res[1])
        print (j)
        display_text.set(res[0] + res[1])

    elif y == 1:
        print (res[0] - res[1])
        print (res[0], res[1])
        print (j)
        display_text.set(res[0] - res[1])
    elif y == 2:
        print (res[0] * res[1])
        print (res[0], res[1])
        print (j)
        display_text.set(res[0] * res[1])
    elif y == 3:
        print (res[0] / res[1])
        print (res[0], res[1])
        print (j)
        display_text.set(res[0] / res[1])





#Number Buttons
k= 0
numbut = []
for j in range(10):

    b = tk.Button(window, text = j, command = partial(subnum,j))
    b.place(x=(-150*k)+30+30*j, y=60 + 30*k, width=30, anchor='ne')
    numbut.append(b)
    if j >= 4:
        k = 1

#Operation Buttons

add = tk.Button(text="+", command = partial(Operation,0))
sub = tk.Button(text="-", command = partial(Operation,1))
mult = tk.Button(text="X", command = partial(Operation,2))
div = tk.Button(text="/", command = partial(Operation,3))
eqs = tk.Button(text="=", command = Equals)





#Displaying the current inputs

def printbut(value):
    global printcal
    printcal = display_text.get()


    if value == 0:
        printcal += "+"
        display_text.set(printcal)
    elif value == 1:
        printcal += "-"
        display_text.set(printcal)
    elif value == 2:
        printcal += "X"
        display_text.set(printcal)
    elif value == 3:
        printcal += "/"
        display_text.set(printcal)
    elif value == 10:
        printcal += "0"
        display_text.set(printcal)
    elif value == 11:
        printcal += "1"
        display_text.set(printcal)
    elif value == 12:
        printcal += "2"
        display_text.set(printcal)
    elif value == 13:
        printcal += "3"
        display_text.set(printcal)
    elif value == 14:
        printcal += "4"
        display_text.set(printcal)
    elif value == 15:
        printcal += "5"
        display_text.set(printcal)
    elif value == 16:
        printcal += "6"
        display_text.set(printcal)
    elif value == 17:
        printcal += "7"
        display_text.set(printcal)
    elif value == 18:
        printcal += "8"
        display_text.set(printcal)
    elif value == 19:
        printcal += "9"
        display_text.set(printcal)


#Clear operations

def clr():
    numbut.clear()
    dothedo.clear()
    res.clear()
    display_text.set("")

clr = tk.Button(text="Clear", command = clr)







add.place(x=30, y=120, width = 30, anchor='ne')
sub.place(x=60, y=120, width = 30, anchor='ne')
mult.place(x=90, y=120, width = 30, anchor='ne')
div.place(x=120, y=120, width = 30, anchor='ne')
eqs.place(x=150, y=120, width = 30, anchor='ne')
clr.place(x=200, y=120, width = 50, anchor='ne')
print (dothedo)
window.mainloop()
