from tkinter import *
from tkinter import ttk
import random
import tkinter.messagebox
from datetime import datetime


class Library:
    def __init__(self, root):
        self.root = root
        self.root.title("TTU Library Management System")
        self.root.geometry("1600*900+0+0")
        self.root.configure(background='powder blue')


if __name__ == '_main_':
    root = Tk()
    application = Library(root)
    root.mainloop()
