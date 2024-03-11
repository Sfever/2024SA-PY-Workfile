'''
Start screen codes, Nothing more
'''
import pygame as pg
from . import textview as tv
import os
import json
class startscr:
    bgexist=0
    textview=""
    font4title=""
    def __init__(self):
        self.bgexist=0
        self.textview=tv.textview()
        self.font4title=self.textview.new_text()
        if os.access("../res/bg.png",os.R_OK):
            self.bg=pg.image.load("../res/bg.png").convert()
            self.bgexist=1
        print("Initilization of start screen complete successfully")
    #loading texts
    def load_title(self,main):
        if main.config_exist==1:
            config={}
            with open(main.config_path,'r') as config_reader:#read configs
                config=json.load(config_reader)
                #load title text properties from config.json
            self.textview.textlist[self.font4title].set_color(config["font_color"])
            self.textview.textlist[self.font4title].set_font(config["font"])
            self.textview.textlist[self.font4title].set_content(config["title"])
            self.textview.textlist[self.font4title].set_size(config["font_size"])
        print("Text is load successfully")
    def show_title(self,window,main):
        self.textview.textlist[self.font4title].set_text()
        self.textview.textlist[self.font4title].render_surface()
        F_width,F_height=self.textview.textlist[self.font4title].get_dimensions()
        window.blit(self.textview.textlist[self.font4title].get_surface(),((main.get_reso_horizontal()-F_width)/2,100))
        pg.display.update()
    def show_background(self,window):
        if self.bgexist==1:
            window.blit(self.bg,(0,0))
            pg.display.update()


