'''
Start screen codes, Nothing more
'''
#typehints are needed
import pygame as pg
from . import textview as tv
from . import button
from . import init
from . import music
import os
import json
from threading import Thread
class startscr:
    def __init__(self):
        self.bgexist=0
        self.textview=tv.textview()
        font4title=self.textview.new_text()
        self.textlist=[]
        self.textlist.append(font4title)
        self.title_text=len(self.textlist)-1
        self.buttons:button.button=button.button()
        self.buttonslist=[]
        #Maybe could read background image path from config.json
        #Also Move config reader into init.py
        if os.access("./res/bg.png",os.R_OK):
            self.bg=pg.image.load("./res/bg.png").convert()
            self.bgexist=1
        print("Initilization of start screen complete successfully")
    #loading texts
    def load_title(self,main:init.inital):
        if main.configExist==1:
            config=main.get_config()
            #with open(main.config_path,'r') as config_reader:
            #    config=json.load(config_reader)
                #load title text properties from config.json
            self.textview.textlist[self.textlist[self.title_text]].set_color(config["font_color"])
            self.textview.textlist[self.textlist[self.title_text]].set_font(config["font"])
            self.textview.textlist[self.textlist[self.title_text]].set_content(config["title"])
            self.textview.textlist[self.textlist[self.title_text]].set_size(config["font_size"])
    def show_title(self,window:pg.surface.Surface,main:init.inital):
        self.textview.textlist[self.textlist[self.title_text]].set_text()
        self.textview.textlist[self.textlist[self.title_text]].render_surface()
        F_width,F_height=self.textview.textlist[self.textlist[self.title_text]].get_dimensions()
        window.blit(self.textview.textlist[self.textlist[self.title_text]].get_surface(),((main.get_reso_horizontal()-F_width)/2,100))
        pg.display.update()
    def show_background(self,window:pg.surface.Surface):
        if self.bgexist==1:
            window.blit(self.bg,(0,0))
            pg.display.update()
    def destroy_window(self):
        for i in self.textlist:
            self.textview.del_text(i)
    def show_start_exit_button_text(self,window:pg.surface.Surface,main:init.inital):
        start_button_text:tv.textobj=self.textview.new_text()
        quit_button_text:tv.textobj=self.textview.new_text()
        self.textlist.append(start_button_text)
        self.start_button_text:int=len(self.textlist)-1
        self.textlist.append(quit_button_text)
        self.quit_button_text:int=len(self.textlist)-1
        self.textview.textlist[self.textlist[self.start_button_text]].set_content("START GAME")
        self.textview.textlist[self.textlist[self.quit_button_text]].set_content("QUIT GAME")
        self.textview.textlist[self.textlist[self.start_button_text]].set_text()
        self.textview.textlist[self.textlist[self.quit_button_text]].set_text()
        self.textview.textlist[self.textlist[self.start_button_text]].render_surface()
        self.textview.textlist[self.textlist[self.quit_button_text]].render_surface()
        S_width,S_height=self.textview.textlist[self.textlist[self.start_button_text]].get_dimensions()
        Q_width,Q_height=self.textview.textlist[self.textlist[self.quit_button_text]].get_dimensions()
        window.blit(self.textview.textlist[self.textlist[self.start_button_text]].get_surface(),((main.get_reso_horizontal()-S_width)/2,(main.get_reso_vertical()-S_height)/2))
        window.blit(self.textview.textlist[self.textlist[self.quit_button_text]].get_surface(),((main.get_reso_horizontal()-Q_width)/2,(main.get_reso_vertical()-S_height)/2+100))
    def start_exit_button(self,main:init.inital):
        S_width,S_height=self.textview.textlist[self.textlist[self.start_button_text]].get_dimensions()
        Q_width,Q_height=self.textview.textlist[self.textlist[self.quit_button_text]].get_dimensions()
        start_button=self.buttons.new_button((main.get_reso_horizontal()-S_width)/2,(main.get_reso_vertical()-S_height)/2,S_width,S_height)
        quit_button=self.buttons.new_button((main.get_reso_horizontal()-Q_width)/2,(main.get_reso_vertical()-S_height)/2+100,Q_width,Q_height)
        self.buttonslist.append(start_button)
        self.start_button=len(self.buttonslist)-1
        self.buttonslist.append(quit_button)
        self.quit_button=len(self.buttonslist)-1
    def play_music(self,music_path):
        self.musicplayer=music.MusicPlayer()
        self.musicplayer.set_path(music_path)
        self.musicplayer.play()
    def get_player(self):
        return self.musicplayer
    def onpress_start_screen(self,mousepos,startaction,quitaction):
        return [self.buttons.buttonlist[self.buttonslist[self.start_button]].onclick(startaction,mousepos), self.buttons.buttonlist[self.buttonslist[self.quit_button]].onclick(quitaction,mousepos)]
        
       

