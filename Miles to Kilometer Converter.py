#!/usr/bin/env python
# coding: utf-8

# In[7]:


from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_result_label.config(text = f'{km}')

root = Tk()
root.geometry('300x140')
root.title('Miles to Kilometer Converter')
root.config(padx = 20, pady = 20, bg = '#C1C1CD')
    
miles_input = Entry(root, font = 'opensans 18 bold', width = 6)
miles_input.grid(row = 1, column = 2)

miles_label = Label(root, text = 'Mile', font = 'cascadiacode 18 bold', bg = '#C1C1CD')
miles_label.grid(row = 1, column = 3)

is_equal_to_label = Label(root, text = 'is equal to', font = 'opensans 18 bold', bg = '#C1C1CD')
is_equal_to_label.grid(row = 2, column = 1)

km_result_label = Label(root, text = '0', font = 'cascadiacode 18 bold', fg = 'blue', bg = '#C1C1CD', pady = 10)
km_result_label.grid(row = 2, column = 2)

km_label = Label(root, text = 'km', font = 'cascadiacode 18 bold', bg = '#C1C1CD', pady = 10)
km_label.grid(row = 2, column = 3)

calculate_button = Button(root, text = 'Calculate', command = miles_to_km, bg = '#C1C1CD', padx = 5, pady = 5, font = 'cascadiacode 0 bold', fg = '#595959')
calculate_button.grid(row = 3, column = 2, pady = 10)

root.mainloop()


# In[ ]:




