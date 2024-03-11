import pygame as pg
class button:
    def __init__(self,posx,posy,width,height):
        self.x=posx
        self.y=posy
        self.width=width
        self.height=height
    def onclick(self,action,mousepos):
        if mousepos[0] > self.x:
            if mousepos[1] > self.y:
                if mousepos[0] < self.x+self.width:
                    if mousepos[1] < self.y+self.height:
                        action()

