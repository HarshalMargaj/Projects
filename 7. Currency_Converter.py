################################################################
#              * Currency Converter Application *              #
################################################################

from tkinter import *
from tkinter import ttk, messagebox
from tkmacosx import *
from currency_converter import CurrencyConverter

# Creating Window
root = Tk()
root.geometry("815x420")
root.resizable(False, False)
root.title("Currency Converter Application")
root.configure(padx = 50, pady = 240, bg = "white")

# Creating Variables
user_input_value = IntVar()
user_input_value.set(1)
output_label_value = StringVar()
output_label_value.set(0.013)
from_combobox_value = StringVar()
to_combobox_value = StringVar()

# The Convert Funtion
def convert():
    try:
        c = CurrencyConverter()
        a = c.convert(user_input_value.get(),
                      f"{from_combobox_value.get()[0:3]}",
                      f"{to_combobox_value.get()[0:3]}")
        output_label_value.set(round(a, 3))

        label1 = Label(root,
                       text = f"{user_input_value.get()} {from_combobox_value.get()} equals",
                       font = "RobotoMono 22 bold",
                       fg = "#707579",
                       bg = "white",
                       width = 100,
                       wraplength = 450,
                       justify = "center")
        
        label1.place(x = -400, y = -65)

        label2 = Label(root,
                       text = f"{output_label_value.get()} {to_combobox_value.get()}",
                       font = "PoppinsSemibold 22 bold",
                       fg = "#00cc00",
                       bg = "white",
                       width = 100,
                       wraplength = 450,
                       justify = "center")
        
        label2.place(x = -400, y = -35)

    except Exception as e:
        messagebox.showerror("Currency Converter", e)

# The Reset Funtion
def reset():
    user_input_value.set(1)
    output_label_value.set(0.013)
    from_combobox.set("INR (Indian Rupee)")
    to_combobox.set("USD (United States Dollar)")
    label1 = Label(root,
                   text = f"1 INR (Indian Rupee) equals",
                   font = "RobotoMono 22 bold",
                   fg = "#707579",
                   bg = "white",
                   width = 100,
                   wraplength = 450,
                   justify = "center")
    
    label1.place(x = -410, y = -65)

    label2 = Label(root,
                   text = f"0.013 USD (United States Dollar)",
                   font = "PoppinsSemibold 22 bold",
                   fg = "#00cc00",
                   bg = "white",
                   width = 100,
                   wraplength = 450,
                   justify = "center")
    
    label2.place(x = -410, y = -35)

# The Resetall Funtion
def resetall():
    user_input_value.set("")
    output_label_value.set(0)
    from_combobox.set("Select Currency")
    to_combobox.set("Select Currency")
    label1 = Label(root,
                   text = f"1 INR (Indian Rupee) equals",
                   font = "RobotoMono 22 bold",
                   fg = "#707579",
                   bg = "white",
                   width = 100,
                   wraplength = 450,
                   justify = "center")
    
    label1.place(x = -410, y = -65)

    label2 = Label(root,
                   text = f"0.013 USD (United States Dollar)",
                   font = "PoppinsSemibold 22 bold",
                   fg = "#00cc00",
                   bg = "white",
                   width = 100,
                   wraplength = 450,
                   justify = "center") 
    
    label2.place(x = -410, y = -35)
    label1.configure(text = "")
    label2.configure(text = "")

# Creating Labels
label1 = Label(root,
               text = f"1 INR (Indian Rupee) equals",
               font = "RobotoMono 22 bold",
               fg = "#707579",
               bg = "white",
               width = 100,
               wraplength = 450,
               justify = "center")

label1.place(x = -410, y = -65)

label2 = Label(root,
               text = f"0.013 USD (United States Dollar)",
               font = "PoppinsSemibold 22 bold",
               fg = "#00cc00",
               bg = "white",
               width = 100,
               wraplength = 450,
               justify = "center")

label2.place(x = -410, y = -35)

# From label
from_label = Label(root, 
                   text = "From : ", 
                   font = "RobotoMono 18 bold", 
                   bg = "white", 
                   padx = 5, 
                   pady = 5)

from_label.grid(row = 1, column = 0)

# To Label
to_label = Label(root, 
                 text = "To : ", 
                 font = "RobotoMono 18 bold", 
                 bg = "white", 
                 padx = 5, 
                 pady = 5)

to_label.grid(row = 2, column = 0)

# user input
user_input = Entry(root, 
                   textvariable = user_input_value, 
                   font = "RobotoMono 18 bold", 
                   fg = "#4d5156")

user_input.grid(row = 1, column = 1, padx = 10, pady = 10)

# output label
canvas = Canvas(height = 28, width = 247, bg = "#fff")
canvas.grid(row = 2, column = 1, padx = 10, pady = 10)

output_label = Label(root,
                     text = "",
                     textvariable = output_label_value,
                     font = "RobotoMono 18 bold",
                     fg = "blue",
                     bg = "white")

output_label.grid(row = 2, column = 1, padx = 10, pady = 10)

# Creating Comboboxes
# From Combobox 
from_combobox = ttk.Style()
from_combobox.configure("Blue.TCombobox", 
                        foreground = "#4d5156", 
                        background = "white", 
                        ipadx = 10, 
                        ipady = 10)

from_combobox = ttk.Combobox(root, 
                             font = "RobotoMono 16 bold", 
                             state = "readonly", 
                             textvariable = from_combobox_value,
                             width = 23)

from_combobox["values"] = ("AUD (Australian Dollar)",
                           "BRL (Brazilian Real)",
                           "BGN (Bulgarian Lev)",
                           "CAD (Canadian Dollar)",
                           "CNY (Chinese Yuan)",
                           "HRK (Croatian Kuna)",
                           "CZK (Czech Koruna)",
                           "DKK (Danish Krone)",
                           "EUR (Euro)",
                           "HKD (Hong Kong Dollar)",
                           "HUF (Hungarian Forint)",
                           "ISK (Icelandic Krona)",
                           "IDR (Indonesian Rupiah)",
                           "ILS (Israeil New Shekel)",
                           "INR (Indian Rupee)",
                           "JPY (Japanese Yen)",
                           "MYR (Malaysian Ringgit)",
                           "MXN (Mexican Peso)",
                           "NZD (New Zealand Dollar)",
                           "NOK (Norwegian Krone)",
                           "PHP (Philippine Peso)",
                           "PLN (Poland Zloty)",
                           "GBP (Pound Sterling)",
                           "RON (Romanian Leu)",
                           "RUB (Russian Ruble)",
                           "SGD (Singapore Dollar)",
                           "ZAR (South African Rand)",
                           "KRW (South Korean Won)",
                           "SEK (Swedish Krona)",
                           "CHF (Swiss Franc)",
                           "THB (Thai Baht)",
                           "TRY (Turkish Lira)",
                           "USD (United States Dollar)")

from_combobox.set("INR (Indian Rupee)")
from_combobox.grid(row = 1, column = 2, padx = 10, pady = 10)
from_combobox.config(foreground = "#4d5156")

# To Combobox
to_combobox = ttk.Style()
to_combobox.configure("Blue.TCombobox",
                      foreground = "#4d5156",
                      background = "white",
                      ipadx = 10,
                      ipady = 10,
                      width = 10)   

to_combobox = ttk.Combobox(root, 
                           font = "RobotoMono 16 bold", 
                           state = "readonly",                 
                           textvariable = to_combobox_value,
                           width = 23)

to_combobox["values"] = ("AUD (Australian Dollar)",
                         "BRL (Brazilian Real)",
                         "BGN (Bulgarian Lev)",
                         "CAD (Canadian Dollar)",
                         "CNY (Chinese Yuan)",
                         "HRK (Croatian Kuna)",
                         "CZK (Czech Koruna)",
                         "DKK (Danish Krone)",
                         "EUR (Euro)",
                         "HKD (Hong Kong Dollar)",
                         "HUF (Hungarian Forint)",
                         "ISK (Icelandic Krona)",
                         "IDR (Indonesian Rupiah)",
                         "ILS (Israeil New Shekel)",
                         "INR (Indian Rupee)",
                         "JPY (Japanese Yen)",
                         "MYR (Malaysian Ringgit)",
                         "MXN (Mexican Peso)",
                         "NZD (New Zealand Dollar)",
                         "NOK (Norwegian Krone)",
                         "PHP (Philippine Peso)",
                         "PLN (Poland Zloty)",
                         "GBP (Pound Sterling)",
                         "RON (Romanian Leu)",
                         "RUB (Russian Ruble)",
                         "SGD (Singapore Dollar)",
                         "ZAR (South African Rand)",
                         "KRW (South Korean Won)",
                         "SEK (Swedish Krona)",
                         "CHF (Swiss Franc)",
                         "THB (Thai Baht)",
                         "TRY (Turkish Lira)",
                         "USD (United States Dollar)")

to_combobox.set("USD (United States Dollar)")
to_combobox.grid(row = 2, column = 2, padx = 10, pady = 10)
to_combobox.config(foreground = "#4d5156")

# Creating Buttons
# Convert Button
convert_button = Button(root,
                        text = "CONVERT",
                        font = "RobotoMono 12 bold",
                        command = convert,
                        padx = 5,
                        pady = 5,
                        bg = '#4283f3',
                        fg = "white",
                        activebackground= '#4283f3',
                        activeforeground= 'white',
                        highlightbackground= '#ffffff')

convert_button.place(x = 175, y = 120)

# Reset Button 
reset_button = Button(root,
                      text = "RESET",
                      font = "RobotoMono 12 bold",
                      command = reset,
                      padx = 5,
                      pady = 5,
                      bg = '#ffbd03',
                      fg = "white",
                      activebackground= '#ffbd03',
                      activeforeground= 'white',
                      highlightbackground= '#ffffff')

reset_button.place(x = 295, y = 120)

# Reset All Button
reset_all_button = Button(root,
                          text = "RESET ALL",
                          font = "RobotoMono 12 bold",
                          command = resetall,
                          padx = 5,
                          pady = 5,
                          bg = '#FF3131',
                          fg = "white",
                          activebackground= '#FF3131',
                          activeforeground= 'white',
                          highlightbackground= '#ffffff')

reset_all_button.place(x = 410, y = 120)

# Currency Converter Image
currency_converter_image = PhotoImage(file = "/Users/apple/Downloads/Untitled.001 (2).png")
currency_converter_image_label = Label(root, 
                                       image = currency_converter_image, 
                                       borderwidth = 6, 
                                       relief = "ridge",
                                       bg = '#E6E2E7')

currency_converter_image_label.place(x = -30, y = -220)

root.mainloop()
