########################################################
#           * Unit Converter Application *             #
########################################################

from tkinter import *
from tkinter import ttk, messagebox
from tkmacosx import *
from unitconvert import (lengthunits,
                         volumeunits,
                         massunits,
                         digitalunits,
                         timeunits,
                         temperatureunits)

# Creating Window
root = Tk()
root.title("Unit Converter Application")
root.geometry("550x300")
root.resizable(False, False)
root.configure(padx=43, pady=90)

# Creating Variables
user_input_value = IntVar()
user_input_value.set("")
output_label_value = IntVar()
unit_combobox_value = StringVar()
from_combobox_value = StringVar()
to_combobox_value = StringVar()

# Creating Functions
# The Convert Function
def convert():
    try:
        if unit_combobox_value.get() == "Length":
            a = lengthunits.LengthUnit(
                user_input_value.get(),
                f"{from_combobox_value.get()}",
                f"{to_combobox_value.get()}",
            ).doconvert()
            output_label_value.set(a)

        elif unit_combobox_value.get() == "Volume":
            a = volumeunits.VolumeUnit(
                user_input_value.get(),
                f"{from_combobox_value.get()}",
                f"{to_combobox_value.get()}",
            ).doconvert()
            output_label_value.set(a)

        elif unit_combobox_value.get() == "Mass":
            a = massunits.MassUnit(
                user_input_value.get(),
                f"{from_combobox_value.get()}",
                f"{to_combobox_value.get()}",
            ).doconvert()
            output_label_value.set(a)

        elif unit_combobox_value.get() == "Time":
            a = timeunits.TimeUnit(
                user_input_value.get(),
                f"{from_combobox_value.get()}",
                f"{to_combobox_value.get()}",
            ).doconvert()
            output_label_value.set(a)

        elif unit_combobox_value.get() == "Digital":
            a = digitalunits.DigitalUnit(
                user_input_value.get(),
                f"{from_combobox_value.get()}",
                f"{to_combobox_value.get()}",
            ).doconvert()
            output_label_value.set(a)

        elif unit_combobox_value.get() == "Temperature":
            a = temperatureunits.TemperatureUnit(
                user_input_value.get(),
                f"{from_combobox_value.get()}",
                f"{to_combobox_value.get()}",
            ).doconvert()
            output_label_value.set(a)

    except Exception as e:
        messagebox.showerror("Error", str(e))


# The Reset Function
def reset():
    user_input_value.set("")
    output_label_value.set(0)


# The Reset All Function
def resetall():
    user_input_value.set("")
    output_label_value.set(0)
    unit_combobox.set("Length")
    from_combobox.set("cm")
    to_combobox.set("m")


#  The Selected Function
def selected(event):

    unit_label = event.widget.get()

    if unit_label == "Length":
        from_combobox["values"] = ( "mm", 
                                    "cm", 
                                    "in", 
                                    "ft", 
                                    "yd", 
                                    "m", 
                                    "km", 
                                    "mi")

        to_combobox["values"] = ( "mm", 
                                  "cm", 
                                  "in", 
                                  "ft", 
                                  "yd", 
                                  "m", 
                                  "km", 
                                  "mi")

    elif unit_label == "Volume":
        from_combobox["values"] = ( "ml",
                                    "l",
                                    "tsp",
                                    "tbsp",
                                    "floz",
                                    "cup",
                                    "pt",
                                    "qt",
                                    "gal",
                                    "lcup",
                                    "in3",
                                    "ft3")

        to_combobox["values"] = ( "ml",
                                  "l",
                                  "tsp",
                                  "tbsp",
                                  "floz",
                                  "cup",
                                  "pt",
                                  "qt",
                                  "gal",
                                  "lcup",
                                  "in3",
                                  "ft3")

    elif unit_label == "Mass":
        from_combobox["values"] = ( "mg", 
                                    "g", 
                                    "oz", 
                                    "lb", 
                                    "kg")

        to_combobox["values"] = ( "mg", 
                                  "g", 
                                  "oz", 
                                  "lb", 
                                  "kg")

    elif unit_label == "Time":
        from_combobox["values"] = ( "ms",
                                    "sec",
                                    "min",
                                    "hr",
                                    "day",
                                    "wk",
                                    "mo",
                                    "yr")

        to_combobox["values"] = ( "ms", 
                                  "sec", 
                                  "min", 
                                  "hr", 
                                  "day", 
                                  "wk", 
                                  "mo", 
                                  "yr")

    elif unit_label == "Digital":
        from_combobox["values"] = ( "B",
                                    "kB",
                                    "MB",
                                    "GB",
                                    "TB",
                                    "PB",
                                    "EB",
                                    "ZB",
                                    "YB",
                                    "KiB",
                                    "MiB",
                                    "GiB",
                                    "TiB",
                                    "PiB",
                                    "EiB",
                                    "ZiB",
                                    "YiB")

        to_combobox["values"] = ( "B",
                                  "kB",
                                  "MB",
                                  "GB",
                                  "TB",
                                  "PB",
                                  "EB",
                                  "ZB",
                                  "YB",
                                  "KiB",
                                  "MiB",
                                  "GiB",
                                  "TiB",
                                  "PiB",
                                  "EiB",
                                  "ZiB",
                                  "YiB")

    elif unit_label == "Temperature":
        from_combobox["values"] = ( "F", 
                                    "C", 
                                    "K")

        to_combobox["values"] = ( "F", 
                                  "C", 
                                  "K")


# Creating Labels
# Unit label
unit_label = Label(root, text="Unit : ", font="Halvetica 18 bold")

# From label
from_label = Label(root, text="From : ", font="Halvetica 18 bold")

# To label
to_label = Label(root, text="To : ", font="Halvetica 18 bold")

# User Input Field
user_input = Entry(root, textvariable=user_input_value, font="Halvetica 18 bold")

# Output label
output_label = Label(root,
                     textvariable=output_label_value,
                     font="Halvetica 18 bold",
                     width=20,
                     bg="white",
                     fg="blue",)

# Creating Comboboxes
# Unit Combobox
unit_combobox = ttk.Combobox(root, 
                             textvariable=unit_combobox_value, 
                             font="Halvetica 16 bold", 
                             state="readonly")

unit_combobox["values"] = ("Length", 
                            "Volume", 
                            "Mass", 
                            "Time", 
                            "Digital", 
                            "Temperature")
unit_combobox.set("Length")
unit_combobox.bind("<<ComboboxSelected>>", selected)

# from combobox

from_combobox = ttk.Combobox(root,
                             state="readonly",
                             textvariable=from_combobox_value,
                             font="Halvetica 16 bold",
                             width=10)

from_combobox.set("cm")
from_combobox.bind("<<ComboboxSelected>>", selected)


# to combobox
to_combobox = ttk.Combobox(root,
                           state="readonly",
                           textvariable=to_combobox_value,
                           font="Halvetica 16 bold",
                           width=10)

to_combobox.set("m")
to_combobox.bind("<<ComboboxSelected>>", selected)

# Creating Buttons
# Convert Button
convert_button = Button(root, 
                        text="CONVERT", 
                        font="RobotoMono 12 bold", 
                        command=convert,
                        padx=10, 
                        pady=5,
                        bg="#4283f3",
                        fg="white",
                        activebackground="#4283f3",
                        activeforeground="white")
              
# Reset Button
reset_button = Button(root,
                      text="RESET",
                      font="RobotoMono 12 bold",
                      command=reset,
                      padx=10,
                      pady=5,
                      bg = '#ffbd03',
                      fg = "white",
                      activebackground= '#ffbd03',
                      activeforeground= 'white')

# Reset All Button
reset_all_button = Button(root,
                          text="RESET ALL",
                          font="RobotoMono 12 bold",
                          command=resetall,
                          padx=10,
                          pady=5,
                          bg = '#FF3131',
                          fg = "white",
                          activebackground= '#FF3131',
                          activeforeground= 'white')

# packing
# Labels
unit_label.grid(row=0, column=0)
from_label.place(x=-8, y=55)
to_label.place(x=14, y=100)
user_input.grid(row=1, column=1)
output_label.grid(row=2, column=1, padx=10, pady=10)

# Buttons
convert_button.place(x=43, y=150)
reset_button.place(x=174, y=150)
reset_all_button.place(x=299, y=150)

# Comboboxes
unit_combobox.grid(row=0, column=1, padx=10, pady=10)
from_combobox.grid(row=1, column=2, padx=10, pady=10)
to_combobox.grid(row=2, column=2, padx=10, pady=10)

# Unit Converter Image
unit_converter_image = PhotoImage(file="/Users/apple/Downloads/Untitled 3.001.png")
label = Label(root, image=unit_converter_image)
label.place(x=0, y=-75)

# Creating Mainloop
root.mainloop()
