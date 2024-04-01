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
class StartScreen:
    def __init__(self):
        self.bgexist=0
        self.textview=tv.textview()
        font4title=self.textview.NewText()
        self.textList=[]
        self.textList.append(font4title)
        self.title_text=len(self.textList)-1
        self.buttons:button.Button=button.Button()
        self.buttonslist=[]
        #Maybe could read background image path from config.json
        #Also Move config reader into init.py
        if os.access("./res/bg.png",os.R_OK):
            self.bg=pg.image.load("./res/bg.png").convert()
            self.bgexist=1
        print("Initilization of start screen complete successfully")
    #loading texts
    def LoadTitle(self,main:init.inital):
        if main.configExist==1:
            config:list=main.GetConfig()
            #with open(main.config_path,'r') as config_reader:
            #    config=json.load(config_reader)
                #load title text properties from config.json
            self.textview.textList[self.textList[self.title_text]].SetColor(config["font_color"]) # type: ignore
            self.textview.textList[self.textList[self.title_text]].SetFont(config["font"]) # type: ignore
            self.textview.textList[self.textList[self.title_text]].SetContent(config["title"]) # type: ignore
            self.textview.textList[self.textList[self.title_text]].SetSize(config["font_size"]) # type: ignore
    def ShowTitle(self,window:pg.surface.Surface,main:init.inital):
        self.textview.textList[self.textList[self.title_text]].SetText()
        self.textview.textList[self.textList[self.title_text]].RenderSurface()
        F_width,F_height=self.textview.textList[self.textList[self.title_text]].GetDimensions()
        window.blit(self.textview.textList[self.textList[self.title_text]].GetSurface(),((main.W_width-F_width)/2,100))
        pg.display.update()
    def ShowBackground(self,window:pg.surface.Surface):
        if self.bgexist==1:
            window.blit(self.bg,(0,0))
            pg.display.update()
    def DestroyWindow(self):
        for i in self.textList:
            self.textview.DeleteText(i)
    def ShowStartExitButtonText(self,window:pg.surface.Surface,main:init.inital):
        start_button_text=self.textview.NewText()
        quit_button_text=self.textview.NewText()
        self.textList.append(start_button_text)
        self.start_button_text:int=len(self.textList)-1
        self.textList.append(quit_button_text)
        self.quit_button_text:int=len(self.textList)-1
        self.textview.textList[self.textList[self.start_button_text]].SetContent("START GAME")
        self.textview.textList[self.textList[self.quit_button_text]].SetContent("QUIT GAME")
        self.textview.textList[self.textList[self.start_button_text]].SetText()
        self.textview.textList[self.textList[self.quit_button_text]].SetText()
        self.textview.textList[self.textList[self.start_button_text]].RenderSurface()
        self.textview.textList[self.textList[self.quit_button_text]].RenderSurface()
        S_width,S_height=self.textview.textList[self.textList[self.start_button_text]].GetDimensions()
        Q_width,Q_height=self.textview.textList[self.textList[self.quit_button_text]].GetDimensions()
        window.blit(self.textview.textList[self.textList[self.start_button_text]].GetSurface(),((main.W_width-S_width)/2,(main.W_height-S_height)/2))
        window.blit(self.textview.textList[self.textList[self.quit_button_text]].GetSurface(),((main.W_width-Q_width)/2,(main.W_height-S_height)/2+100))
    def StartExitButton(self,main:init.inital):
        S_width,S_height=self.textview.textList[self.textList[self.start_button_text]].GetDimensions()
        Q_width,Q_height=self.textview.textList[self.textList[self.quit_button_text]].GetDimensions()
        start_button=self.buttons.NewButton((main.W_width-S_width)/2,(main.W_height-S_height)/2,S_width,S_height)
        quit_button=self.buttons.NewButton((main.W_width-Q_width)/2,(main.W_height-S_height)/2+100,Q_width,Q_height)
        self.buttonslist.append(start_button)
        self.start_button=len(self.buttonslist)-1
        self.buttonslist.append(quit_button)
        self.quit_button=len(self.buttonslist)-1
    def PlayMusic(self,music_path):
        self.musicplayer=music.MusicPlayer()
        self.musicplayer.SetPath(music_path)
        self.musicplayer.Play()
    def OnPress(self,mousepos,startaction,quitaction):
        return [self.buttons.buttonList[self.buttonslist[self.start_button]].OnClick(startaction,mousepos), self.buttons.buttonList[self.buttonslist[self.quit_button]].OnClick(quitaction,mousepos)]
        
       

