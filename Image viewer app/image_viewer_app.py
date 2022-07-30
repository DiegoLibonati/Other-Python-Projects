from email.mime import image
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import os
from win32api import GetSystemMetrics

root = Tk()
root.title("Image Viewer APP")
root.geometry("1280x720")
root.config(bg="#100720")
root.minsize(1280, 720)

frame = Frame(root)
frame.pack(side=BOTTOM, padx=15, pady=15)

label_image = Label(frame, bg="#100720")
label_image.pack(fill="both", expand=True)

# Menu
menu_bar = Menu(root)
root.config(menu=menu_bar)
filemenu = Menu(menu_bar, tearoff=0)

menu_bar.add_cascade(label = "Archivo", menu=filemenu)

filemenu.add_command(label="Open Image", command=lambda:open_image())
filemenu.add_command(label="Exit", command=lambda:exit())

def open_image():
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select image file", filetype=(("JPG File", "*.jpg"), ("PNG file", "*.png"),("All file", "name.txt")))
    img = Image.open(filename)
    img = img.resize((1280,720))
    img = ImageTk.PhotoImage(img)
    label_image.configure(image=img)
    label_image.image=img
root.mainloop()