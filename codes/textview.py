'''
This file is used to display and operate any type of text in the game
All texts should use this file
Please do not use your own implentation
'''
import init as base
import pygame as pg
class textobj:
    def __init__(self):
        self.text=""
        self.surface=""
        self.color=[255,255,255]
        self.size=30
        self.font="arial"
        self.title="Fuck this world"
    def set_color(self,color):
        self.color=color
    def set_font(self, font):
        self.font=font
    def set_size(self,size):
        self.size=size
    def set_content(self,content):
        self.title=content
    def set_text(self):
        self.text=pg.font.SysFont(self.font,self.size)
    def render_surface(self):
        self.surface=self.text.render(self.title,True,self.color)
    def get_text(self):
        return self.text
    def get_surface(self):
        return self.surface
    def get_dimensions(self):
        return self.text.size()
    def delete_text(self):
        self.surface.set_alpha(0)
        pg.display.update()

class textview:
    def __init__(self):
        self.textlist=[]
    def new_text(self):
        newtext=textobj()
        self.textlist.append(newtext)
        return len(self.textlist)-1
    def del_text(self,tgt):
        self.textlist[tgt].delete_text()
        del self.textlist[tgt]
    '''
    self.textlist will not be provided outside the class in order to prevent losting access to textobj object accidentally
    ''' 