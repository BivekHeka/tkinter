from tkinter import *

def meter_to_km():
    meter= float(meter_input.get())
    km = meter /1000
    km_result_label.config(text=f"{km}")


window = Tk()
window.title("Meter to Kilometer Converter")
window.config(padx=20,pady=20)

meter_input = Entry(width=7)
meter_input.grid(column=1, row=0)

meter_label = Label(text="meter")
meter_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate",command=meter_to_km)
calculate_button.grid(column=1, row=2)


window.mainloop()