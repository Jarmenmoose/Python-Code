import tkinter as tk
from functools import partial


window = tk.Tk()
name = tk.Label(text="Ligma Instruments LI-84")
name.pack()
#x=0

#functions

#operations = [operator.add, operator.sub, operator.mul, operator.truediv]
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

#dothetwo = [1, 2, 3]
#print(numcon(dothetwo))
print(res)


#def subopadd():
    #chakras = "entry.get()"

#doing the do
#chakras = [range(0,5)]
#def opthedo():
    #if chakras[i] == 0:
        #print(dothedo[0] + dothedo[1])

#Operations
#def Addition(y):
    #print (y)
#def Multiplication(y):
    #print(y)
#def Operation(y):
    #global x
    #x = y

#    print(x)

y = 0
def Operation(value):
    printbut(value)
    global y
    y = value
    print (dothedo)
    numcon(dothedo)
    dothedo.clear()
    print(res)
#def Subtraction():
    #x = lambda a , b : a - b
#def Division ():
    #x = lambda a , b : a / b

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





#print(Addition(2,3))

#Number Buttons

numbut = []
for j in range(10):

    b = tk.Button(window, text = j, command = partial(subnum,j))
    b.pack()
    numbut.append(b)


#Operation Buttons

add = tk.Button(text="+", command = partial(Operation,0))
sub = tk.Button(text="-", command = partial(Operation,1))
mult = tk.Button(text="X", command = partial(Operation,2))
div = tk.Button(text="/", command = partial(Operation,3))
eqs = tk.Button(text="=", command = Equals)
    #command = submit

#On Screen Output

display_text = tk.StringVar()
display = tk.Label(window, textvariable=display_text)
display.pack()


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





#opbut =[]
#for j in range(4):
    #b = tk.Button(window, text = )
    #b.pack()
    #opbut.append(b)

#doing the do
#print(Addition())



add.pack()
sub.pack()
mult.pack()
div.pack()
eqs.pack()
clr.pack()
#outbox.pack()
print (dothedo)
window.mainloop()
