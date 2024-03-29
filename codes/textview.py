'''
This file is used to display and operate any type of text in the game
All texts should use this file
Please do not use your own implentation
'''
#typehints
import pygame as pg  #Import pygame and store it as a pg library for subsequent calls.
class textobj:       #The textobj class facilitates subsequent calls
    def __init__(self):#initialisation
        self.text=""     
        self.surface=""   
        self.color=[255,255,255]  #Setting the initial colour
        self.size=30    #Setting the initial size
        self.font="arial"  #Setting the initial font
        self.title="Fuck this world"   #setting the title
    def set_color(self,color:list): #Setting up a list of colours (creating groups of variables)
        self.color=color
    def set_font(self, font:str):
        self.font=font
    def set_size(self,size:int):
        self.size=size
    def set_content(self,content:str):
        self.title=content
    def set_text(self):
        self.text=pg.font.SysFont(self.font,self.size) #Setting the value of a variable
    def render_surface(self):
        self.surface=self.text.render(self.title,True,tuple(self.color))
    def get_text(self):
        return self.text#returns the object of font
    def get_surface(self):
        return self.surface#returns rendered surface
    def get_dimensions(self):
        return self.text.size(self.title)
    def delete_text(self):
        self.surface.set_alpha(0)#make surface invisible
        pg.display.update()
        print("Successed to remove text") #print it out at the last

class textview:
    def __init__(self): #initialisation
        self.textlist=[]
    def new_text(self):  #Creating Text Object
        newtext=textobj()
        self.textlist.append(newtext)
        return len(self.textlist)-1
    def del_text(self,tgt): #Delete thw Text Object
        self.textlist[tgt].delete_text()
        del self.textlist[tgt]#remove it and make become not accessible anymore
        #print("Successed to remove text")
    '''
    self.textlist will not be provided outside the class in order to prevent losting access to textobj object accidentally
    '''
    #returns the instance of textobj for devs to work on
    '''
    def get_object(self,index):
        return self.textlist[index]
    Just for idiots, i think don't give 'em text object either
    '''