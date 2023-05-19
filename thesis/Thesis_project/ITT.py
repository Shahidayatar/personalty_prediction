from tkinter import *
from pytesseract import image_to_string
from PIL import Image 
from tkinter import filedialog


root = Tk()
root['bg'] = "#121212"
root.title("ITT/S- Image to Text")

def extraxt(e = None , lang = 'eng'):

    result_as_a_text.delete(0.0,END)
    txt = image_to_string(img , lang = lang)
    result_as_a_text.insert(INSERT , txt)

def set_image(e = None):

    global img
    img = Image.open(filedialog.askopenfilename())
    try:
        show_case['image'] = img
        show_case.image = img
        show_case['text'] = ""
    except:
        pass
    extraxt()

show_case = Button(root , command = set_image , text = 'Open an Image ...' 
    ,bg ="#333", relief ='flat',fg ="#fff" )
show_case.pack()

result_as_a_text = Text(root,bg ="#333", relief ='flat' ,fg = "#fff" ,font = ['Vernada' , 14])
result_as_a_text.pack()

root.mainloop()


def load_file(self):
        self.pathText.delete("1.0", END)
        self.imgTxtScrolled.delete("1.0", END)
        self.file_path = askopenfilename(initialdir="home/", title="Choose Image File", filetypes=(
            ("JPEG files", "*.jpg *.jpeg"), ("PNG files", "*.png")))
        if self.file_path:
            try:
                self.progress = ttk.Progressbar(
                    self.extractTextTPane, orient=HORIZONTAL, length=100, mode='indeterminate')

                def parseImage():
                    self.progress.grid(row=1, column=0)
                    self.progress.start()
                    time.sleep(5)

                    temp = os.path.basename(self.file_path)
                    temp2 = os.path.dirname(self.file_path)
                    obj = Converter(temp, temp2)
                    v = obj.execute()

                    self.progress.stop()
                    self.progress.grid_forget()
                    if not v.isspace():
                        self.setTempText(v)
                        self.load_desc()
                    else:
                        tkinter.messagebox.showerror(
                            "OOPS!", "No Text Found!!\n")
                    self.browseTButton['state'] = 'normal'

                self.browseTButton['state'] = 'disabled'
                threading.Thread(target=parseImage).start()

                self.pathText.insert('1.0', self.file_path)

            except:
                tkinter.messagebox.showerror(
                    "Open Source File", "Failed to open file\n'%s'" % self.file_path)
        else:
            tkinter.messagebox.showerror(
                "Open Source File", "Choose a file first!!\n")





