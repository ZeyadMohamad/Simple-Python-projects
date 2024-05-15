from tkinter import *
from time import strftime

window = Tk()
window.title("Digital Clock")

def time():

    current_time = strftime("%H:%M:%S %p")
    clock.config(text= current_time)
    clock.after(1000, time)


clock = Label(window, font= ("times new roman", 40, "bold"), background= "black", foreground="white")
clock.pack(anchor="center")
time()
mainloop()