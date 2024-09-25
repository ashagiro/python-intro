from tkinter import *

window = Tk()
# window.minsize(width=300, height=200)
window.config(padx=20, pady=20)
window.title("mile to km converter")

def miles_to_km(n):
# The formula to convert miles to km: kilometers = miles × 1.609344. 
    return n*1.609344

# Entry
entry = Entry(width=15)
entry.grid(column=1, row=0)

# Result
result = Label(text="")
result.grid(column=1, row=1)

# Button
def action():
    mile_entry = float(entry.get())
    km_result = miles_to_km(mile_entry)
    result.config(text=str(km_result))
    pass
button = Button(text="Calculate", command=action)
button.grid(column=1, row=3)

# labels: miles, km, equals to
miles_label = Label(text = "miles")
miles_label.grid(column=2, row=0)

km_label = Label(text="km")
km_label.grid(column=2, row=1)

equals_label = Label(text="equals to")
equals_label.grid(column=0, row=1)

window.mainloop()