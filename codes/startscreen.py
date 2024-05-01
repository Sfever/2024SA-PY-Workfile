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
        self.titleText=self.textview.NewText()
        #self.textList=[]
        #self.textList.append(font4title)
        #self.title_text=len(self.textList)-1
        self.buttons:button.Button=button.Button()
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
            self.textview.textList[self.titleText].SetColor(config["font_color"]) # type: ignore
            self.textview.textList[self.titleText].SetFont(config["font"]) # type: ignore
            self.textview.textList[self.titleText].SetContent(config["title"]) # type: ignore
            self.textview.textList[self.titleText].SetSize(config["font_size"]) # type: ignore
    def ShowTitle(self,window:pg.surface.Surface,main:init.inital):
        self.textview.textList[self.titleText].SetText()
        self.textview.textList[self.titleText].RenderSurface()
        F_width,F_height=self.textview.textList[self.titleText].GetDimensions()
        window.blit(self.textview.textList[self.titleText].GetSurface(),((main.W_width-F_width)/2,100))
        pg.display.update()
    def ShowBackground(self,window:pg.surface.Surface):
        if self.bgexist==1:
            window.blit(self.bg,(0,0))
            pg.display.update()
    def DestroyWindow(self):
        for i in self.textList:
            self.textview.DeleteText(i)
    def ShowStartExitButtonText(self,window:pg.surface.Surface,main:init.inital):
        self.startButtonText=self.textview.NewText()
        self.quitButtonText=self.textview.NewText()
        self.textview.textList[self.startButtonText].SetContent("START GAME")
        self.textview.textList[self.quitButtonText].SetContent("QUIT GAME")
        self.textview.textList[self.startButtonText].SetText()
        self.textview.textList[self.quitButtonText].SetText()
        self.textview.textList[self.startButtonText].RenderSurface()
        self.textview.textList[self.quitButtonText].RenderSurface()
        S_width,S_height=self.textview.textList[self.startButtonText].GetDimensions()
        Q_width,Q_height=self.textview.textList[self.quitButtonText].GetDimensions()
        window.blit(self.textview.textList[self.startButtonText].GetSurface(),((main.W_width-S_width)/2,(main.W_height-S_height)/2))
        window.blit(self.textview.textList[self.quitButtonText].GetSurface(),((main.W_width-Q_width)/2,(main.W_height-S_height)/2+100))
    def StartExitButton(self,main:init.inital):
        S_width,S_height=self.textview.textList[self.startButtonText].GetDimensions()
        Q_width,Q_height=self.textview.textList[self.quitButtonText].GetDimensions()
        self.startButton=self.buttons.NewButton((main.W_width-S_width)/2,(main.W_height-S_height)/2,S_width,S_height)
        self.quitButton=self.buttons.NewButton((main.W_width-Q_width)/2,(main.W_height-S_height)/2+100,Q_width,Q_height)
    def PlayMusic(self,music_path):
        self.musicplayer=music.MusicPlayer()
        self.musicplayer.SetPath(music_path)
        self.musicplayer.Play()
    def OnPress(self,mousepos,startaction,quitaction):
        return [self.buttons.buttonList[self.startButton].OnClick(startaction,mousepos), self.buttons.buttonList[self.buttonslist[self.quit_button]].OnClick(quitaction,mousepos)]
        
       

