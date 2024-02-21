import tkinter as tk
from tkinter import ttk

def convert():
    value = float(entry_value.get())
    conv_type = optiontype.get()

    if conv_type == "Centimeter to Meter":
        result = value / 100
        result_label.config(text="{} cm is equal to {:.4f} m.".format(value, result))
    elif conv_type == "Meter to Centimeter":
        result = value * 100
        result_label.config(text="{} m is equal to {:.4f} cm.".format(value, result))
    elif conv_type == "Centimeter to Feet":
        result = value / 30.48
        result_label.config(text="{} cm is equal to {:.4f} feet.".format(value, result))
    elif conv_type == "Feet to Inches":
        result = value * 12
        result_label.config(text="{} feet is equal to {:.4f} inches.".format(value, result))
    elif conv_type == "Mile to Kilometer":
        result = value * 1.60934
        result_label.config(text="{} mile is equal to {:.4f} km.".format(value, result))
    elif conv_type == "Square Feet to Square Meters":
        result = value * 0.092903
        result_label.config(text="{} sqft is equal to {:.4f} sqm.".format(value, result))
    elif conv_type == "Square Feet to Acres":
        result = value * 0.0000229568
        result_label.config(text="{} sqft is equal to {:.4f} acres.".format(value, result))

root = tk.Tk()
root.title("Unit Converter")

label_type = ttk.Label(root, text="Conversion Type:")
label_type.grid(row=0, column=0)

types = ["Centimeter to Meter", "Meter to Centimeter", "Centimeter to Feet", "Feet to Inches", "Mile to Kilometer", "Square Feet to Square Meters", "Square Feet to Acres"]
optiontype = ttk.Combobox(root, values=types)
optiontype.grid(row=0, column=1)

label_value = ttk.Label(root, text="Enter Value:")
label_value.grid(row=1, column=0, padx=10, pady=10)

entry_value = ttk.Entry(root)
entry_value.grid(row=1, column=1, padx=10, pady=10)

convert_button = ttk.Button(root, text="Convert", command=convert)
convert_button.grid(row=2, columnspan=2, padx=10, pady=10)

result_label = ttk.Label(root, text="Result: ")
result_label.grid(row=3, columnspan=2, padx=10, pady=10)

root.mainloop()
