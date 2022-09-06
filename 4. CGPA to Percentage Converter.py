#!/usr/bin/env python
# coding: utf-8

# In[82]:


from tkinter import *

def CGPA_to_percentage():
    CGPA = float(cgpa_input.get())
    percentage = round((CGPA * 8.8), 2)
    percentage_output.config(text = f'{percentage}')
    
root = Tk()
root.geometry('400x200')
root.minsize(400, 200)
root.maxsize(400, 200)
root.title('CGPA to Percentage Converter')
root.config(padx = 20, pady = 20, bg = '#DCDCDC')

instr_label = Label(root, text = 'Enter your CGPA here ↓', font = 'cascadiacode 18 bold', fg = '#474747', bg = '#DCDCDC')
instr_label.grid(row = 0, column = 1)

cgpa_input = Entry(root, width = 8, font = 'opensans 18 bold')
cgpa_input.grid(row = 1, column = 1, pady = 10)

cgpa_label = Label(root, text = 'CGPA', bg = '#DCDCDC', font = 'opansans 18 bold', fg = '#474747')
cgpa_label.grid(row = 1, column = 2)

is_equal_to_label = Label(root, text = '=', bg = '#DCDCDC', fg = '#474747', font = 'opensans 18 bold')
is_equal_to_label.grid(row = 2, column = 0)

canvas = Canvas(height=28, width=80, bg="#fff")
canvas.grid(row = 2, column = 1)

percentage_output = Label(root, text = '0', bg="#fff", fg = 'blue', font = 'opensans 18 bold')
percentage_output.grid(row = 2, column = 1)

percentage_label = Label(root, text = 'Percentage(%)', bg = '#DCDCDC', font = 'opensans 18 bold', fg = '#474747')
percentage_label.grid(row = 2, column = 2)

calculate_button = Button(root, text = 'Calculate', font = 'opensans 16 bold', command = CGPA_to_percentage, padx = 5, pady = 5)
calculate_button.grid(row = 3, column = 1, pady = 10)

root.mainloop()


# In[ ]:




