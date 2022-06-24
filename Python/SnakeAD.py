import tkinter as tk
from functools import partial
import random
from tkinter import ttk


window = tk.Tk()
window.geometry("700x700")


#Creating the board
def create_board():
    c= 0
    r = 0
    while c<20:
        while r<20:
            board = tk.Canvas(window, height =20, width = 20, highlightthickness=1, highlightbackground="black")
            board.grid(row = r, column = c)
            r+=1
        r=0
        c+=1



bod1 = tk.Canvas(window)





movements = {"a": (-0.1, 0), "d": (0.1, 0), "w": (0, -0.1), "s": (0, 0.1)}

def move_snake():
    global after_id

    if previous_key not in movements.keys():
        canvas.after_cancel(after_id)
        after_id = None

    else:
        canvas.move(bod1, *movements[previous_key])
        after_id = canvas.after(50, move_snake)




def key_press(event):
    global previous_key, after_id

    if event.char == previous_key:
        return

    elif after_id:
        canvas.after_cancel(after_id)

    previous_key = event.char
    move_snake()




create_board()

window.bind("<Key>", key_press)
window.mainloop()
