from PIL import Image
import cv2
from pytesseract import image_to_string
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk

import cv2
import pytesseract


root = tk.Tk()
root.geometry("710x600")  # Size of the window
root.title('personality prediction')

my_font1 = ('times', 18, 'bold')
my_font2 = ('times', 12, 'normal')
label1 = tk.Label(
    root, text='Upload a handwriting sample for personality detection', width=50, font=my_font1)
label1.grid(row=1, column=6, columnspan=4)
b1 = tk.Button(root, text='Upload a Image (JPG OR PNG)',
               width=20, command=lambda: upload_file())
b1.grid(row=2, column=5, columnspan=5)


def upload_file():
    f_types = [('Jpg Files', '*.jpg'),
               ('PNG Files', '*.png')]   # type of files to select
    filename = tk.filedialog.askopenfilename(multiple=True, filetypes=f_types)
    col = 1  # start from column 1
    row = 3  # start from row 3

    for f in filename:

        img = Image.open(f)  # read the image file
        img = img.resize((300, 300))  # new width & height

        def extracted():
            path_to_tesseract = r"/usr/local/Cellar/tesseract/5.0.1/bin/tesseract"
            pytesseract.tesseract_cmd = path_to_tesseract
            text = pytesseract.image_to_string(img)
            label1 = tk.Label(root, text=text, width=50, font=my_font2)
            label1.grid(row=4, column=1, columnspan=1)

            print(text[:-1])
        extracted()

        img = ImageTk.PhotoImage(img)
        e1 = tk.Label(root)
        e1.grid(row=row, column=col)
        e1.image = img
        e1['image'] = img  # garbage collection
        if(col == 3):  # start new line after third column
            row = row+1  # start wtih next row
            col = 1    # start with first column
        else:       # within the same row
            col = col+1  # increase to next column


root.mainloop()  # Keep the window open
