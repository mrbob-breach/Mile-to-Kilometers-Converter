from tkinter import *

FONT = "Arial"
FONT_SIZE = 12


def button_clicked():
    km_converted = int(input.get()) * 1.609
    km_amount.config(text=km_converted)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(250, 120)
window.config(padx=20, pady=20)

my_label_miles = Label(text="Miles", font=(FONT, FONT_SIZE))
my_label_miles.grid(column=2, row=0)

my_label_km = Label(text="Km",font=(FONT, FONT_SIZE))
my_label_km.grid(column=2, row=1)

my_label_equal = Label(text="is equal to", font=(FONT, FONT_SIZE))
my_label_equal.grid(column=0, row=1)

km_amount = Label(text="0", font=(FONT, FONT_SIZE))
km_amount.grid(column=1, row=1)

input = Entry(width=10)
input.insert(END, "0")
input.grid(column=1, row=0)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()
