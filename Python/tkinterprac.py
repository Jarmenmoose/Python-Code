import tkinter as tk
window = tk.Tk()
greeting = tk.Label(text="Hello, Tkinter")
label = tk.Label(text="Hello, Tkinteer")





display_text = tk.StringVar()
display = tk.Label(window, textvariable=display_text)
display.pack()

def add_one():
    s = display_text.get()
    s += '1'
    display_text.set(s)

one = tk.Button(window, text="1", height=10, width=10, command=add_one)
one.pack()









def submit():
    entry.delete(0)
    yahello = entry.get()
    print (yahello)





button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
    command = submit
)

entry = tk.Entry()
submit()

entry.pack()
greeting.pack()
label.pack()
button.pack()
window.mainloop()
