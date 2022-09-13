from tkinter import *
from tkinter import messagebox, filedialog
from tkmacosx import *
from pytube import YouTube

# Creating Window
root = Tk()
root.geometry("897x250")
root.resizable(False, False)
root.configure(bg="black")
root.title("YouTube Video Downloader")

# Creating the browse function
def browse():
    select_destination = filedialog.askdirectory()
    download_path.set(select_destination)

# Creating the download function
def download():
    try:
        if download_path.get():
            YouTube(link.get()).streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first().download(download_path.get())

            messagebox.showinfo("YouTube", f"Video is downloaded successfully at your selected destination ({download_path.get()})")

        else:
            messagebox.showinfo("YouTube", "Please select destination")

    except Exception as e:
        messagebox.showerror("YouTube", e)

# Creating Frame
f = Frame(root, padx=250, pady=10, bg="#ff0000")
f.grid(row=0, columnspan=3)

# Creating header
header = Label(f,
               text="YouTube Video Downloader",
               font="Halvetica 30 bold",
               bg="#ff0000",          
               fg="white")

header.grid(row=0, columnspan=3)

# Creating Paste Video Link Here label
link_label = Label(root,
                   text="Paste your video link here : ",
                   font="Halvetica 18 bold",
                   bg="black",
                   fg="white")

link_label.grid(row=1, column=0, sticky="w", padx=(20, 0))

# Creating user input field
link = StringVar()
link_input = Entry(root, 
                   textvariable=link, 
                   font="Roboto-Semibold 16 bold", 
                   width=35)

link_input.grid(row=1, column=1, pady=(20, 10))

# Creating Destination label
destination_label = Label(root, 
                          text="Select Destination : ", 
                          font="Halvetica 18 bold", 
                          fg="white", 
                          bg="black")

destination_label.grid(row=2, column=0, sticky="w", padx=(20, 0))

# Creating Destination user input field
download_path = StringVar()
destination_input = Entry(root, 
                          textvariable=download_path, 
                          font="Roboto-Semibold 16 bold", 
                          width=35)

destination_input.grid(row=2, column=1, pady=10)

# Creating Browse button
browse_button = Button(root,
                       text="Browse",
                       font="Halvetica 16 bold",
                       padx=10,
                       pady=5,
                       command=browse,
                       highlightbackground="#000000",
                       bg="#4283f3",
                       fg="white",
                       activebackground="#4283f3",
                       activeforeground="white")

browse_button.grid(row=2, column=2, pady=10)

# Creating Download Button
download_button = Button(root,
                         text="Download",
                         font="Halvetica 16 bold",
                         padx=20,
                         pady=5,
                         bg="#7ed212",
                         highlightbackground="#000000",
                         fg="white",
                         command=download,
                         activebackground="#7ed212",
                         activeforeground="white")

download_button.grid(row=3, column=1, pady=10)

# Creating Mainloop
root.mainloop()
