import tkinter
from tkinter import messagebox
class PopupWindow():
    def __init__(self) -> None:
        pass
    def ShowPopupWindow(self,message):
        messagebox.showinfo("Notice",message)
    def ShowWarning(self,message):
        messagebox.showwarning("Warning",message)