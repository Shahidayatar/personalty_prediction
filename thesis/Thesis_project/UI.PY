
import sys
import os
import tkinter.messagebox
from PIL import ImageTk
import PIL.Image
import time
import threading
from tkinter.filedialog import askopenfilename

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1




def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel_1(root)
    UI_support.init(root, top)
    root.mainloop()


w = None


def create_New_Toplevel_1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel(root)
    top = New_Toplevel_1(w)
    UI_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_New_Toplevel_1():
    global w
    w.destroy()
    w = None


class New_Toplevel_1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        self.file_path = ""
        self.text = ""
        self.imgLabel = Label(top)

        _bgcolor = '#000080'  # X11 color: 'gray85'
        _fgcolor = '#FFFFFF'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#d9d9d9'  # X11 color: 'gray85'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=[
                       ('selected', _compcolor), ('active', _ana2color)])

        top.geometry("600x550+387+131")
        top.title("Heisenberg OCR")
        top.configure(highlightcolor="blue")

        self.TPanedwindow1 = ttk.Panedwindow(top, orient="vertical")
        self.TPanedwindow1.place(relx=0.02, rely=0.02,
                                 relheight=0.97, relwidth=0.97)
        self.TPanedwindow1.configure(width=200)
        self.extractTextTPane = ttk.Labelframe(height=200, text='Extract Text')
        self.TPanedwindow1.add(self.extractTextTPane)
        self.imageSearchTPane = ttk.Labelframe(text='Search Image')
        self.TPanedwindow1.add(self.imageSearchTPane)
        self.__funcid0 = self.TPanedwindow1.bind('<Map>', self.__adjust_sash0)

        self.imgPathFrame = Frame(self.extractTextTPane)
        self.imgPathFrame.place(relx=0.05, rely=0.15,
                                relheight=0.25, relwidth=0.9)
        self.imgPathFrame.configure(relief=GROOVE)
        self.imgPathFrame.configure(borderwidth="5")
        self.imgPathFrame.configure(relief=GROOVE)
        self.imgPathFrame.configure(width=225)
        self.imgPathFrame.configure(background="#000080")

        self.pathTLabel = ttk.Label(self.imgPathFrame)
        self.pathTLabel.place(relx=0.04, rely=0.2, height=25, width=37)
        self.pathTLabel.configure(background="#000080")
        self.pathTLabel.configure(foreground="#FFFFFF")
        self.pathTLabel.configure(relief=FLAT)
        self.pathTLabel.configure(text='''Path:''')

        self.pathText = Text(self.imgPathFrame)
        self.pathText.place(relx=0.11, rely=0.22, relheight=0.6, relwidth=0.7)
        self.pathText.configure(background="white")
        self.pathText.configure(font="TkTextFont")
      #  self.pathText.configure(background="#000080")
        self.pathText.configure(width=10)
        self.pathText.configure(wrap=WORD)

        self.browseTButton = ttk.Button(
            self.imgPathFrame, command=self.load_file)
        self.browseTButton.place(relx=0.82, rely=0.24, height=25, width=83)
        self.browseTButton.configure(takefocus="")
        self.browseTButton.configure(text='''Browse''')
        self.browseTButton.configure(compound="center")

        self.imgTxtScrolled = ScrolledText(self.extractTextTPane)
        self.imgTxtScrolled.place(
            relx=0.05, rely=0.43, relheight=0.5, relwidth=0.9)
        self.imgTxtScrolled.configure(background="white")
        self.imgTxtScrolled.configure(font="TkTextFont")
        self.imgTxtScrolled.configure(insertborderwidth="3")
       # self.imgTxtScrolled.configure(selectbackground="#c4c4c4")
        self.imgTxtScrolled.configure(width=10)
        self.imgTxtScrolled.configure(wrap=NONE)
        self.imgTxtScrolled.configure(background="grey")

        self.getImgFrame = Frame(self.imageSearchTPane)
        self.getImgFrame.place(relx=0.05, rely=0.09,
                               relheight=0.17, relwidth=0.9)
        self.getImgFrame.configure(relief=GROOVE)
        self.getImgFrame.configure(borderwidth="5")
        self.getImgFrame.configure(relief=GROOVE)
        self.getImgFrame.configure(width=125)
        self.getImgFrame.configure(background="#000080")

        self.typeTLabel = ttk.Label(self.getImgFrame)
        self.typeTLabel.place(relx=0.04, rely=0.25, height=28, width=68)
        self.typeTLabel.configure(background="#000080")
        self.typeTLabel.configure(foreground="#FFFFFF")
        self.typeTLabel.configure(relief=FLAT)
        self.typeTLabel.configure(text='''Enter Text:''')

        self.searchText = Entry(self.getImgFrame)
        self.searchText.place(relx=0.19, rely=0.25,
                              relheight=0.5, relwidth=0.63)
        self.searchText.configure(background="white")
        self.searchText.configure(font="TkTextFont")
        self.searchText.configure(selectbackground="#c4c4c4")
        self.searchText.configure(width=10)

        self.searchTButton = ttk.Button(
            self.getImgFrame, command=self.searchImg)
        self.searchTButton.place(relx=0.84, rely=0.25, height=28, width=73)
        self.searchTButton.configure(takefocus="")
        self.searchTButton.configure(text='''Search''')

        self.searchImgFrame = Frame(self.imageSearchTPane)
        self.searchImgFrame.place(
            relx=0.05, rely=0.3, relheight=0.64, relwidth=0.9)
        self.searchImgFrame.configure(relief=GROOVE)
        self.searchImgFrame.configure(borderwidth="5")
        self.searchImgFrame.configure(relief=GROOVE)
        self.searchImgFrame.configure(width=125)

        self.imgCanvas = Canvas(self.searchImgFrame,
                                scrollregion=(0, 0, 3000, 3000))
        self.imgCanvas.place(relx=0, rely=0, relheight=1, relwidth=1)
        self.imgCanvas.configure(background="grey")
        self.imgCanvas.configure(borderwidth="2")
        self.imgCanvas.configure(relief=RIDGE)
        self.imgCanvas.configure(selectbackground="#c4c4c4")
        self.imgCanvas.configure(width=378)

        self.hbar = Scrollbar(self.searchImgFrame, orient=HORIZONTAL)
        self.hbar.pack(side=BOTTOM, fill=X)
        self.hbar.config(command=self.imgCanvas.xview)
        self.vbar = Scrollbar(self.searchImgFrame, orient=VERTICAL)
        self.vbar.pack(side=RIGHT, fill=Y)
        self.vbar.config(command=self.imgCanvas.yview)
        self.imgCanvas.config(xscrollcommand=self.hbar.set,
                              yscrollcommand=self.vbar.set)
        self.imgCanvas.pack(side=LEFT, expand=True, fill=BOTH)

    def __adjust_sash0(self, event):
        paned = event.widget
        pos = [200, ]
        i = 0
        for sash in pos:
            paned.sashpos(i, sash)
            i += 1
        paned.unbind('<map>', self.__funcid0)
        del self.__funcid0

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

    def searchImg(self):
        self.progress = ttk.Progressbar(
            self.imageSearchTPane, orient=HORIZONTAL, length=100, mode='indeterminate')

        def findImage():
            self.progress.grid(row=1, column=0)
            self.progress.start()
            # time.sleep(5)

            self.progress.stop()
            self.progress.grid_forget()
            temp2 = os.path.dirname(self.file_path)
            obj1 = TextToImage(temp2, self.getSearchText())
            obj1.textDict()
            list1 = obj1.search()
            if len(list1) != 0:
                self.load_image(list1)
            else:
                tkinter.messagebox.showerror(
                    "OOPS!", "No Image Found. Try searching with other keyword!!\n")
            self.searchTButton['state'] = 'normal'

        self.searchTButton['state'] = 'disabled'
        threading.Thread(target=findImage).start()

    def load_desc(self):
        self.imgTxtScrolled.insert('1.0', self.getTempText())

    def getSearchText(self):
        return self.searchText.get()

    def setTempText(self, desc):
        self.text = desc

    def getTempText(self):
        return self.text

    def load_image(self, images=None):
        if images is None:
            images = []
        self.imgCanvas.delete("all")
        if not self.file_path:
            tkinter.messagebox.showerror("Error", "Input Image First!!!\n")
        else:
            dirpath = os.path.dirname(self.file_path)
            for i, img_path in enumerate(images):
                path = os.path.join(dirpath, img_path)
                img = PIL.Image.open(path)
                resized = img.resize((150, 150), PIL.Image.ANTIALIAS)
                tkimage = ImageTk.PhotoImage(resized)
                label = Label(self.imgCanvas, image=tkimage)
                label.image = tkimage
                self.imgCanvas.create_image(
                    i*165, 0, image=tkimage, anchor="nw")
                self.imgCanvas.create_text(
                    50+i*165, 160, text=img_path, anchor="nw")

    """        
    def openFile(self,path):
        print("hi")
        os.chdir(os.path.dirname(path))
        img12=os.open(path,'r')
        jpg=img12.read()
    """

# The following code is added to facilitate the Scrolled widgets you specified.


class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
       
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        # self.configure(yscrollcommand=_autoscroll(vsb),
        #    xscrollcommand=_autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        
        if py3:
            methods = Pack.__dict__.keys() | Grid.__dict__.keys() \
                | Place.__dict__.keys()
        else:
            methods = Pack.__dict__.keys() + Grid.__dict__.keys() \
                + Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)


def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        return func(cls, container, **kw)
    return wrapped


class ScrolledText(AutoScroll, Text):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        Text.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)


class ScrolledListBox(AutoScroll, Listbox):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)


if __name__ == '__main__':
    vp_start_gui()
