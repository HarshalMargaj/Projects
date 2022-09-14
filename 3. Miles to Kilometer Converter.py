################################################################
#         * Miles to Kilometer Converter Application *         #
################################################################

from tkinter import *
from tkmacosx import *

# The mile to km function
def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_result_label.config(text = f'{km}')

# Creating Window
root = Tk()
root.geometry('400x230')
root.resizable(False, False)
root.title('Miles to Kilometer Converter Application')
root.config(bg = 'white')

# Creating mile to km converter label
# Creating Frame
f = Frame(root, padx = 40, pady = 20, bg = '#e6005c')
f.grid(row = 0, columnspan=3)
miles_to_km_label = Label(f,
                          text = 'Miles to Kilometer Converter',
                          font = 'Halvetica 24 bold',
                          fg= 'white',
                          bg = '#e6005c')

miles_to_km_label.grid(row = 0, columnspan=3)

# Creating user input field 
miles_input = Entry(root, 
                    font = 'Roboto-Bold 18 bold', 
                    width = 9)

miles_input.grid(row = 1, column = 1, pady = 10)

# Creating Mile label
miles_label = Label(root, 
                    text = 'Mile', 
                    font = 'Roboto-Bold 18 bold', 
                    bg = 'white')

miles_label.grid(row = 1, column = 2, sticky= 'w')

# Creating = label
is_equal_to_label = Label(root, 
                          text = '=', 
                          font = 'Roboto-Bold 18 bold', 
                          bg = 'white')

is_equal_to_label.grid(row = 2, column = 0)

# Creating output label
canvas = Canvas(height=28, width=100, bg="#fff")
canvas.grid(row=2, column=1)

km_result_label = Label(root, 
                        text = '0', 
                        font = 'Roboto-Bold 18 bold', 
                        fg = 'blue', 
                        bg = 'white')

km_result_label.grid(row = 2, column = 1)

# Creating km label
km_label = Label(root, 
                 text = 'km', 
                 font = 'Roboto-Bold 18 bold', 
                 bg = 'white', 
                 pady = 10)

km_label.grid(row = 2, column = 2, sticky = 'w')

# Creating Calculate Button
calculate_button = Button(root, 
                          text = 'Calculate', 
                          command = miles_to_km, 
                          padx = 5, 
                          pady = 5, 
                          font = 'Halvetica 16 bold', 
                          bg="#ffcc00",
                          fg="white",
                          activebackground="#ffcc00",
                          activeforeground="white",
                          highlightbackground= '#ffffff')

calculate_button.grid(row = 3, column = 1, pady = 10)

# Creating mainloop
root.mainloop()





