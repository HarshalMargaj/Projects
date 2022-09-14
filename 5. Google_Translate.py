from tkinter import *
from tkinter import ttk, messagebox
from tkmacosx import *
import googletrans
import textblob

# Creating Window
root = Tk()
root.title("Google Translate")
root.geometry("850x510")
root.resizable(False, False)
root.configure(padx=20, pady=135, bg="white")

# Fuctions
# The translate it function
def translate_it():
    # delete old translation
    to_text.delete(1.0, END)
    try:
        # Get Languages from dictionary keys
        # Get the from language key
        for key, value in languages.items():
            if value.capitalize() == from_combobox.get():
                from_language_key = key

        # Get the to language key
        for key, value in languages.items():
            if value.capitalize() == to_combobox.get():
                to_language_key = key

        # Text you want to translate
        # so I turn from_text into a textblob
        words = textblob.TextBlob(from_text.get(1.0, END))
        words = words.translate(from_lang=from_language_key, to=to_language_key)

        # output
        to_text.insert(1.0, words)

    except Exception as e:
        messagebox.showerror("Translator", e)


# The clear it function
def clear_it():
    from_text.delete(1.0, END)
    to_text.delete(1.0, END)


# Grab languages from GoogleTrans
languages = googletrans.LANGUAGES
languages_list = list(languages.values())

# Capitalize words(languages)
capitalize_languages_list = []
for i in languages_list:
    capitalize_languages_list.append(i.capitalize())

# Combo Boxes
from_combobox = ttk.Style()
from_combobox.configure("Blue.TCombobox", 
                        foreground="blue", 
                        background="white", 
                        ipadx=10, 
                        ipady=10)

from_combobox = ttk.Combobox(root,
                             values=capitalize_languages_list,
                             width=39,
                             height=10,
                             state="readonly",
                             style="Blue.TCombobox")

from_combobox.current(21)
from_combobox.grid(row=0, column=0)
from_combobox.config(foreground="blue")

to_combobox = ttk.Style()
to_combobox.configure("Blue.TCombobox", foreground="blue")
to_combobox = ttk.Combobox(root,
                           values=capitalize_languages_list,
                           width=39,
                           height=10,
                           state="readonly",
                           style="Blue.TCombobox")

to_combobox.current(38)
to_combobox.grid(row=0, column=1)
to_combobox.config(foreground="blue")

# Text Boxes
from_text = Text(root,
                 width=36,
                 height=12,
                 pady=10,
                 padx=10,
                 font=("Halvetica", 16),
                 bg="#F7F7F7",
                 highlightbackground="white")

from_text.grid(row=1, column=0, padx=10, pady=10)

to_text = Text(root,
               width=40,
               height=10,
               pady=10,
               padx=10,
               font="OpenSans 16 bold",
               bg="#E8E8E8",
               highlightbackground="white")

to_text.grid(row=1, column=1, padx=10, pady=10)

# Buttons
# Creating Translate Button
translate_button = Button(root,
                          text="Translate",
                          command=translate_it,
                          padx=5,
                          pady=5,
                          font="Halvetica 16 bold",
                          bg="#4283f3",
                          fg="white",
                          activebackground="#4283f3",
                          activeforeground="white",
                          highlightbackground="#ffffff")

translate_button.place(x=285, y=300)

# Creating Clear Button
clear_button = Button(root,
                      text="Clear",
                      command=clear_it,
                      padx=5,
                      pady=5,
                      font="Halvetica 16 bold",
                      bg="#dc3444",
                      fg="white",
                      activebackground="#dc3444",
                      activeforeground="white",
                      highlightbackground="#ffffff")

clear_button.place(x=413, y=300)

# Google Translate Image
google_translate_image = PhotoImage(file="/Users/apple/Downloads/google 3.001 (1).png")
google_translate_image_label = Label(root, image=google_translate_image, bg="white")
google_translate_image_label.place(x=100, y=-120)

root.mainloop()
