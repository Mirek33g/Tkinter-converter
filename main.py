from tkinter import *

window = Tk()
window.title("Miles to kilometer Converter")
window.config(padx= 25, pady= 25)


def calculation():
  number = float(input.get())
  result = number * 1.609
  fourth_label(text=f"{result}")


input = Entry(width= 10)
input.grid(column= 1, row= 0)


second_label = Label(text= "Miles")
second_label.grid(column=2, row= 0)

third_label = Label(text= "is equal to")
third_label.grid(column= 0, row= 1)

fourth_label = Label(text= "0")
fourth_label.grid(column= 1, row= 1)

fifth_label = Label(text= "Km")
fifth_label.grid(column= 2, row= 1)

button = Button(text="Calculate", command=calculation)
button.grid(column= 1, row= 2)


