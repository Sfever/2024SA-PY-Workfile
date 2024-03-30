'''
This file is used to display and operate any type of text in the game
All texts should use this file
Please do not use your own implentation
'''
#typehints
import pygame as pg
class _TextObject:
    def __init__(self):
        self.text:pg.font.Font
        self.surface:pg.surface.Surface
        self.color=[255,255,255]
        self.size=30
        self.font="arial"
        self.title="Fuck this world"
    def SetColor(self,color:list):
        self.color=color
    def SetFont(self, font:str):
        self.font=font
    def SetSize(self,size:int):
        self.size=size
    def SetContent(self,content:str):
        self.title=content
    def SetText(self):
        self.text=pg.font.SysFont(self.font,self.size)
    def RenderSurface(self):
        self.surface=self.text.render(self.title,True,tuple(self.color))
    def GetText(self):
        return self.text#returns the object of font
    def GetSurface(self):
        return self.surface#returns rendered surface
    def GetDimensions(self):
        return self.text.size(self.title)
    def DeleteText(self):
        self.surface.set_alpha(0)#make surface invisible
        pg.display.update()
        print("Successed to remove text")

class textview:
    def __init__(self):
        self.textList:list[_TextObject]=[]
    def NewText(self):
        newtext=_TextObject()
        self.textList.append(newtext)
        return len(self.textList)-1
    def DeleteText(self,tgt):
        self.textList[tgt].DeleteText()
        del self.textList[tgt]#remove it and make become not accessible anymore
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