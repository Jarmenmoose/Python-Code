import tkinter as tk

# Main Window
window = tk.Tk()
window.geometry("700x700")


# Creating snake body
canvas = tk.Canvas(window, width=700, height=700)
canvas.pack()
bod1 = canvas.create_rectangle(0, 0, 25, 25, fill='red')


previous_key = None
after_id = None

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


window.bind("<Key>", key_press)
window.mainloop()
