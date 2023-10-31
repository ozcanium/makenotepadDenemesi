import tkinter as tk
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

class Notepad_file:

    __root = tk.Tk()

    # default window width and height
    __thisWidth = 650
    __thisHeight = 450
    __thisTextArea = Text(__root)
    __thisMenuBar = Menu(__root)
    __thisFileMenu = Menu(__thisMenuBar, tearoff=0)
    __thisEditMenu = Menu(__thisMenuBar, tearoff=0)
    __thisHelpMenu = Menu(__thisMenuBar, tearoff=0)

    # For adding the scrollbar
    __thisScrollBar = Scrollbar(__thisTextArea)
    __file = None

    def __init__(self, **kwargs):

        # Here, we will Set the icon
        try:
            self.__root.wm_iconbitmap("Notepad.ico")
        except:
            pass

        # here, we will set the window text
        self.__root.title("Untitled- Notepad File")

        # here, we will set the center the window
        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()

        # For left-align
        left = (screenWidth - self.__thisWidth) / 2

        # For top-align
        top = (screenHeight - self.__thisHeight) / 2

        # For top and bottom
        self.__root.geometry(f'{self.__thisWidth}x{self.__thisHeight}+{int(left)}+{int(top)}')

        # Here, we are making the text-area auto resizable
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)

        # Here, we will add the controls such as widgets
        self.__thisTextArea.grid(sticky=N + E + S + W)

        # For opening the new file
        self.__thisFileMenu.add_command(label="New File",
                                        command=self.__newFile)

        # For opening the already existing file from the menu
        self.__thisFileMenu.add_command(label="Open File",
                                        command=self.__openFile)

        # For saving the current working file
        self.__thisFileMenu.add_command(label="Save File",
                                        command=self.__saveFile)

        # For creating the line in the dialog Box
        self.__thisFileMenu.add_separator()
        self.__thisFileMenu.add_command(label="Exit",
                                        command=self.__quitApplication)
        self.__thisMenuBar.add_cascade(label="File",
                                      menu=self.__thisFileMenu)

        # for giving the feature of cutting in Files
        self.__thisEditMenu.add_command(label="Cut",
                                        command=self.__cut)

        # For giving the feature of copying in file
        self.__thisEditMenu.add_command(label="Copy",
                                        command=self.__copy)

        # for giving the feature of pasting in file
        self.__thisEditMenu.add_command(label="Paste",
                                        command=self.__paste)

        # for giving the feature of editing in file
        self.__thisMenuBar.add_cascade(label="Edit",
                                      menu=self.__thisEditMenu)

        # For creating the feature of description of the notepad File
        self.__thisHelpMenu.add_command(label="About Notepad",
                                        command=self.__showAbout)
        self.__thisMenuBar.add_cascade(label="Help",
                                      menu=self.__thisHelpMenu)

        self.__root.config(menu=self.__thisMenuBar)

        self.__thisScrollBar.pack(side=RIGHT, fill=Y)
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)

        self.__thisTextArea.focus_set()

    def __quitApplication(self):
        self.__root.destroy()

    def __showAbout(self):
        showinfo("Notepad", "A simple notepad app")

    def __openFile(self):

        self.__file = askopenfilename(defaultextension=".txt",
                                     filetypes=[("All Files", "*.*"),
                                                ("Text Documents", "*.txt")])

        if self.__file == "":
            self.__file = None
        else:
            self.__root.title(os.path.basename(self.__file) + " - Notepad")
            self.__thisTextArea.delete(1.0, END)

            file = open(self.__file, "r")

            self.__thisTextArea.insert(1.0, file.read())

            file.close()

    def __newFile(self):
        self.__root.title("Untitled - Notepad")
        self.__file = None
        self.__thisTextArea.delete(1.0, END)

    def __saveFile(self):

        if self.__file is None:
            self.__file = asksaveasfilename(initialfile='Untitled.txt',
                                           defaultextension=".txt",
                                           filetypes=[("All Files", "*.*"),
                                                      ("Text Documents", "*.txt")])

            if self.__file == "":
                self.__file = None
            else:
                file = open(self.__file, "w")
                file.write(self.__thisTextArea.get(1.0, END))
                file.close()

                self.__root.title(os.path.basename(self.__file) + " - Notepad")

        else:
            file = open(self.__file, "w")
            file.write(self.__thisTextArea.get(1.0, END))
            file.close()

    def __cut(self):
        self.__thisTextArea.event_generate("<<Cut>>")

    def __copy(self):
        self.__thisTextArea.event_generate("<<Copy>>")

    def __paste(self):
        self.__thisTextArea.event_generate("<<Paste>>")

    def run(self):
        self.__root.mainloop()


# For running the main application
notepad = Notepad_file()
notepad.run()
