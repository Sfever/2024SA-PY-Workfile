from tkinter import messagebox
import sys
import os
class PopupWindow():
    def __init__(self,nativepath="./x64/Debug") -> None:
        self.allownative=False
        if os.path.exists(nativepath):
            sys.path.append(nativepath)
            from nativepopup import PopWin
            self.allownative=True
    def ShowPopupWindow(self,title,message):
        messagebox.showinfo(title,message)
    def ShowWarning(self,message):
        messagebox.showwarning("Warning",message)
    def ShowNativePop(self,title,message):
        if self.allownative==False:
            self.ShowPopupWindow(title,message)
        from nativepopup import PopWin    
        PopWin("test","test114")