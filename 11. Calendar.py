from tkinter import *
from tkcalendar import Calendar
from tkinter import ttk
from tkmacosx import *

# Creating Window
root = Tk()
root.geometry('400x230')
root.title('Calendar')
root.configure(bg = 'white')
# Changing Theme
style = ttk.Style(root)
style.theme_use('clam')

# The select date function
def selectdate():
  date_label.configure(text = f'Selected Date is {cal.get_date()}')

cal = Calendar(root, 
               selectmode = 'day', 
               year = 2022, 
               month = 9, 
               day = 22,
               background = '#4283f3',
               headersbackground = '#C8E0F7',
               bordercolor = '#C8E0F7',
               normalforeground = '#012AC7',
               weekendbackground = '#F2D3DD',
               weekendforeground = '#E10021',
               othermonthforeground = '#818181',
               othermonthbackground = '#E1E1E1',
               othermonthweforeground = '#818181',
               othermonthwebackground = '#E1E1E1',
               selectbackground = '#F8F593',
               selectforeground = 'black')

cal.pack(fill = 'both', expand = True)

# Creating Select Date Button
sel_date_button = Button(root, 
                         text = 'Select Date', 
                         bg = '#4283f3', 
                         command = selectdate, 
                         fg = '#FFFFFF',
                         activebackground= '#4283f3',
                         activeforeground= '#FFFFFF',
                         highlightbackground= '#ffffff')

sel_date_button.pack(pady = 10)

# Creating Selected Date label
date_label = Label(root, 
                   text = '', 
                   font = 'Halvetica 16 bold', 
                   fg = '#707579', 
                   bg = 'white')

date_label.pack()

# Creating mainloop
root.mainloop()