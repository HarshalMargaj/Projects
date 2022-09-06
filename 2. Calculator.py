#!/usr/bin/env python
# coding: utf-8

# In[3]:


from tkinter import *

root = Tk()
root.geometry('300x375')
root.minsize(300, 375)
root.maxsize(300, 375)
root.title('Calculator')
root.configure(bg = 'black')
root.wm_iconbitmap('/Users/apple/Documents/Screenshots/Screenshot 2022-09-03 at 4.02.27 PM.png')

def click(event):
    text = event.widget.cget('text')
    print(text)
    if text == '=':
        if screen_value.get().isdigit():
            value = int(screen_value.get())
        else:
            try:
                value = eval(screen_value.get())
            except:
                value = 'ERROR'
                
        screen_value.set(value)
        screen.update()
        
    elif text == 'AC':
        screen_value.set('')
        screen.update()
    else:
        screen_value.set(screen_value.get() + text)
        screen.update()

screen_value = StringVar()
screen_value.set('')
screen = Entry(root, textvariable = screen_value, font = 'Digital-7 50 bold', bg = '#CDCD33')
screen.pack(fill = 'x', ipadx = 5, padx = 5, pady = 5)

f = Frame(root, bg = 'Black')
button = Button(f, text = 'AC', font = 'opensans 16 bold', padx = 10, pady = 12)
button.pack(side = 'left', padx = 5, pady = 5, ipadx = 32)
button.bind("<Button-1>", click)

button = Button(f, text = '%', font = 'opensans 16 bold', padx = 7, pady = 12)
button.pack(side = 'left', padx = 5, pady = 5)
button.bind("<Button-1>", click)

button = Button(f, text = '/', font = 'opensans 16 bold', padx = 10, pady = 12)
button.pack(side = 'left', padx = 5, pady = 5, ipadx = 2)
button.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg = 'Black')
button = Button(f, text = '7', font = 'opensans 16 bold', padx = 10, pady = 12)
button.pack(side = 'left', padx = 5, pady = 5)
button.bind("<Button-1>", click)

button = Button(f, text = '8', font = 'opensans 16 bold', padx = 10, pady = 12)
button.pack(side = 'left', padx = 5, pady = 5)
button.bind("<Button-1>", click)

button = Button(f, text = '9', font = 'opensans 16 bold', padx = 10, pady = 12)
button.pack(side = 'left', padx = 5, pady = 5)
button.bind("<Button-1>", click)

button = Button(f, text = '*', bg = 'Yellow', font = 'opensans 16 bold', padx = 10, pady = 12)
button.pack(side = 'left', padx = 5, pady = 5, ipadx = 2)
button.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg = 'Black')
button = Button(f, text = '4', font = 'opensans 16 bold', padx = 10, pady = 12)
button.pack(side = 'left', padx = 5, pady = 5)
button.bind("<Button-1>", click)

button = Button(f, text = '5', font = 'opensans 16 bold', padx = 10, pady = 12)
button.pack(side = 'left', padx = 5, pady = 5)
button.bind("<Button-1>", click)

button = Button(f, text = '6', font = 'opensans 16 bold', padx = 10, pady = 12)
button.pack(side = 'left', padx = 5, pady = 5)
button.bind("<Button-1>", click)

button = Button(f, text = '-', bg = 'Yellow', font = 'opensans 16 bold', padx = 11, pady = 12)
button.pack(side = 'left', padx = 5, pady = 5, ipadx = 1)
button.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg = 'Black')
button = Button(f, text = '1', bg = 'blue', font = 'opensans 16 bold', padx = 10, pady = 12)
button.pack(side = 'left', padx = 5, pady = 5)
button.bind("<Button-1>", click)

button = Button(f, text = '2', font = 'opensans 16 bold', padx = 10, pady = 12)
button.pack(side = 'left', padx = 5, pady = 5)
button.bind("<Button-1>", click)

button = Button(f, text = '3', font = 'opensans 16 bold', padx = 10, pady = 12)
button.pack(side = 'left', padx = 5, pady = 5)
button.bind("<Button-1>", click)

button = Button(f, text = '+', font = 'opensans 16 bold', padx = 10, pady = 12)
button.pack(side = 'left', padx = 5, pady = 5)
button.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg = 'Black')
button = Button(f, text = '0', font = 'opensans 16 bold', padx = 10, pady = 12)
button.pack(side = 'left', padx = 5, pady = 5, ipadx = 37)
button.bind("<Button-1>", click)

button = Button(f, text = '.', font = 'opensans 16 bold', padx = 10, pady = 12)
button.pack(side = 'left', padx = 5, pady = 5, ipadx = 3)
button.bind("<Button-1>", click)

button = Button(f, text = '=', font = 'opensans 16 bold', padx = 10, pady = 12)
button.pack(side = 'left', padx = 5, pady = 5)
button.bind("<Button-1>", click)
f.pack()

root.mainloop()


# In[ ]:




