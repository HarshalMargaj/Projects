################################################################
#        * CGPA TO Percentage Converter Application *          #
################################################################

from tkinter import *
from tkmacosx import *

# The cgpa to percentage function
def CGPA_to_percentage():
    CGPA = float(cgpa_input.get())
    percentage = round((CGPA * 8.8), 2)
    percentage_output.config(text=f"{percentage}")

# Creating window
root = Tk()
root.geometry("400x230")
root.resizable(False, False)
root.title("CGPA to Percentage Converter Application")
root.config(bg="white")

# Creating cgpa to percentage converter label
f = Frame(root, padx = 25, pady = 20, bg = '#cc0000')
f.grid(row = 0, columnspan= 3)

instr_label = Label(f,
                    text="CGPA to Percentage Converter",
                    font="Halvetica 24 bold",
                    fg="white",
                    bg="#cc0000")

instr_label.grid(row=0, columnspan=3)


cgpa_input = Entry(root, 
                   width=8, 
                   font="opensans 18 bold")

cgpa_input.grid(row=1, column=1, pady=10)

# Creating CGPA label
cgpa_label = Label(root, 
                   text="CGPA", 
                   bg="white", 
                   font="Roboto-Bold 18 bold", 
                   fg="#474747")

cgpa_label.grid(row=1, column=2, sticky= 'w')

# Creating = label
is_equal_to_label = Label(root, 
                          text="=", 
                          bg="white", 
                          fg="#474747", 
                          font="Roboto-Bold 18 bold")

is_equal_to_label.grid(row=2, column=0)

canvas = Canvas(height=28, width=100, bg="#fff")
canvas.grid(row=2, column=1)

# Creating output label
percentage_output = Label(root, 
                          text="0", 
                          bg="#fff", 
                          fg="blue", 
                          font="Roboto-Bold 18 bold")

percentage_output.grid(row=2, column=1)

# Creating percentage label
percentage_label = Label(root, 
                         text="Percentage(%)", 
                         bg="white", 
                         font="Roboto-Bold 18 bold", 
                         fg="#474747")

percentage_label.grid(row=2, column=2, sticky = 'w')

# Creating Calculate Button
calculate_button = Button(root,
                          text="Calculate",
                          font="OpenSans-Bold 16 bold",
                          command=CGPA_to_percentage,
                          padx=5,
                          pady=5,
                          bg="#4283f3",
                          fg="white",
                          activebackground="#4283f3",
                          activeforeground="white",
                          highlightbackground= '#ffffff')

calculate_button.grid(row=3, column=1, pady=10)

# Creating mainloop
root.mainloop()
