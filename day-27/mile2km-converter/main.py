from tkinter import *


# conversion function
def m2km():
    m = float(mile_entry.get())
    value_label.config(text=round(m * 1.609, 2))


# Set up the window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(pady=20, padx=20)

# create components
mile_entry = Entry(width=10)
mile_entry.insert(END, string="0")
mile_label = Label(text="Miles")
equal_label = Label(text="is equal to")
value_label = Label(text=0)
km_label = Label(text="km")
calc_btn = Button(text="Calculate", command=m2km)

# position components
mile_entry.grid(column=1, row=0)
mile_label.grid(column=2, row=0)
equal_label.grid(column=0, row=1)
value_label.grid(column=1, row=1)
km_label.grid(column=2, row=1)
calc_btn.grid(column=1, row=2)

window.mainloop()
