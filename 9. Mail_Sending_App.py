###################################################################
#                   * Mail Sending Application *                  #
###################################################################
from tkinter import *
from tkinter import ttk, messagebox
import smtplib

# Creating Window
root = Tk()
root.geometry("560x480")
root.minsize(560, 480)
root.maxsize(560, 480)
root.title("Mail Sender using Python")
root.configure(padx=20, pady=10)

# Fuctions
smtp_object = smtplib.SMTP("smtp.gmail.com", 587)
smtp_object.ehlo()
smtp_object.starttls()

# The Login Function
def login():
    try:
        email = mail_input.get()
        password = pass_input.get()
        smtp_object.login(email, password)

        succes_label = Label(f0,
                             text="Login Successful",
                             font="RobotoMono 16 bold",
                             fg="#00cc00",
                             bg="white",
                             pady=10)
        
        succes_label.grid(row=5, column=0)

    except Exception as e:
        messagebox.showerror("Mail", e)

# The Send Function
def send():
    try:
        from_email = email_from_input.get()
        to_email = email_to_input.get()
        subject = subject_input.get()
        message = message_input.get()
        msg = "Subject : " + subject + "\n" + message

        smtp_object.sendmail(from_email, to_email, msg)

        sent_label = Label(f1,
                           text="Message Sent",
                           font="RobotoMono 16 bold",
                           fg="#00cc00",
                           bg="white",
                           pady=10)
        
        sent_label.grid(row=5, column=1)

    except Exception as e:
        messagebox.showerror("Mail", e)

# Creating Frame
f = Frame(root)
f.grid(row=0, columnspan=2)
# Creating Header
gmail_image = PhotoImage(file="/Users/apple/Desktop/logo_gmail_lockup_default_2x_r5.png")
gmail_image_label = Label(f, image=gmail_image)
gmail_image_label.grid(row=0, columnspan=2, padx=160)

# Creating Notebook
my_notebook = ttk.Notebook(root)
my_notebook.grid()

###################################################################
#                        * Login Section *                        #
###################################################################

# Creating Frame
f0 = Frame(my_notebook, bg="white")
my_notebook.add(f0, text="Login")

# Creating Sing to continue to Gmail label
signin_label = Label(f0,
                     text="Sign In to continue to Gmail",
                     font="OpenSans-Semibold 16 bold",
                     fg="black",
                     bg="white")

signin_label.place(x=115, y=10)

# Creating Enter your Email label
mail_label = Label(f0,
                   text="Enter your Email",
                   font="RobotoMono 18 bold",
                   bg="white",
                   fg="#1b72e8",
                   padx=150)

mail_label.grid(row=0, column=0, pady=(50, 0))

# Creating user input for email
mail_input = Entry(f0, 
                   width=30, 
                   font="OpenSans-Semibold 18 bold", 
                   fg="black")

mail_input.grid(row=1, column=0, pady=10)

# Creating Enter your password label
pass_label = Label(f0, 
                   text="Enter your password", 
                   font="RobotoMono 18 bold", 
                   bg="white", 
                   fg="#1b72e8")

pass_label.grid(row=2, column=0)

# Creating user input for password
pass_input = Entry(f0, 
                   width=30, 
                   font="OpenSans-Semibold 18 bold", 
                   fg="black")

pass_input.grid(row=3, column=0, pady=10)

# Creating Login Button
login_button = Button(f0, 
                      text="Login", 
                      font="RobotoMono 12 bold", 
                      padx=5, 
                      pady=5, 
                      command=login)

login_button.grid(row=4, column=0)

###################################################################
#                        * Compose Section *                      #
###################################################################

# Creating Frame
f1 = Frame(my_notebook, bg="white")
my_notebook.add(f1, text="Compose")

# Creating From label
from_label = Label(f1,
                   text="From : ",
                   font="Roboto-Bold 18 bold",
                   fg="#4d5156",
                   bg="white",
                   justify="right")

from_label.grid(row=0, column=0, sticky="e", padx=(60, 0))

# Creating email from user input
email_from_input = Entry(f1, 
                         font="OpenSans-Semibold 18 bold", 
                         width=25, 
                         fg="black")

email_from_input.grid(row=0, column=1, pady=10)

# Creating To label
to_label = Label(f1,
                 text="To : ",
                 font="Roboto-Bold 18 bold",
                 fg="#4d5156",
                 bg="white",
                 justify="right")

to_label.grid(row=1, column=0, sticky="e")

# Creating email to user input
email_to_input = Entry(f1, 
                       font="OpenSans-Semibold 18 bold", 
                       width=25, 
                       fg="black")

email_to_input.grid(row=1, column=1, pady=10)

# Creating Subject label
subject_label = Label(f1,
                      text="Subject : ",
                      font="Roboto-Bold 18 bold",
                      fg="#4d5156",
                      bg="white",
                      justify="right")

subject_label.grid(row=2, column=0, sticky="e")

# Creating Subject user input
subject_input = Entry(f1, 
                      font="OpenSans-Semibold 18 bold", 
                      width=25, 
                      fg="black")

subject_input.grid(row=2, column=1, pady=10)

# Creating Message label
message_label = Label(f1,
                      text="Message : ",
                      font="Roboto-Bold 18 bold",
                      fg="#4d5156",
                      bg="white",
                      justify="right")

message_label.grid(row=3, column=0, sticky="e")

# Creating Message user input
message_input = Entry(f1, 
                      font="OpenSans-Semibold 18 bold", 
                      width=25, 
                      fg="black")

message_input.grid(row=3, column=1, pady=10)

# Creating Send Button
send_button = Button(f1, 
                     text="Send", 
                     font="RobotoMono 12 bold", 
                     padx=5, 
                     pady=5, 
                     command=send)

send_button.grid(row=4, column=1, pady=(5, 5))

# Creating Mainloop
root.mainloop()
