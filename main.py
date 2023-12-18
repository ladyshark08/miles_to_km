from tkinter import *

window = Tk()
window.title("Miles To KM Converter")
window.minsize(width=300, height=100)
window.config(padx=30, pady=30)

miles_entry = Entry(width=10)
miles_entry.grid(column=1, row=0)

Miles = Label(text="Miles")
Miles.grid(column=2, row=0)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

conversion = Label(text=0)
conversion.grid(column=1, row=1)

KM = Label(text="Km")
KM.grid(column=2, row=1)


def conv():
    a = float(miles_entry.get()) * 1.609
    conversion.config(text=a)


calculate = Button(text="Calculate", command=conv)
calculate.grid(column=1, row=2)

window.mainloop()