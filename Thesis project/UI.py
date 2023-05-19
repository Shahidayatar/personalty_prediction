

import string
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
from pytesseract import Output

root = tk.Tk()
root.geometry("1280x900")  # Size of the window
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
        img = img.resize((400, 400))  # new width & height

        def get_grayscale(): # to Increase the accuracy of the image we convert it 
            return img.convert('L')
        get_grayscale()
      
        
        def TextExtracted():
            path_to_tesseract = r"/usr/local/Cellar/tesseract/5.0.1/bin/tesseract"
            pytesseract.tesseract_cmd = path_to_tesseract
            text = pytesseract.image_to_string(img)
            label1 = tk.Label(root, text="the text extracted from the handwritng sample is :"+text, width=50, font=my_font2)
            label1.grid(row=4, column=1, columnspan=1)

            print(text[:-1])

        TextExtracted()
        strs = ''.join(filename)
      #  print(type(strs))


        def PersonalityPrediction():# deeectionof space
            img = cv2.imread(strs)
            d = pytesseract.image_to_data(img, output_type=Output.DICT)# this extracts text from the handwritng sample
            n_boxes = len(d['level'])# we get the size of the hamdwriting 
        
            for i in range(n_boxes):
                (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            if(i > 0 and i<=2):
                xy= "the person is an introvert"
            elif(i > 2 and i <= 4):
                xy= "the person is social"
            elif(i > 4 ):
                xy = "the person is an extrovert"
            label3 = tk.Label(root, text="personality predicted :"+xy, width=50, font=my_font1)
            label3.grid(row=3, column=6, columnspan=6)


           # cv2.imshow('img', img)
           # cv2.waitKey(0)
        PersonalityPrediction()
 

   
      
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

       

root.mainloop()  #this is to  Keep the window open




