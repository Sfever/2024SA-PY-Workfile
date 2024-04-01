'''
Codes used to initalize pygame and config
'''
import pygame as pg
import warnings
import json
import os
import tqdm.rich as tr
import time
import sys
import random
from . import popup
#This files is used to intialize only
#No actual function
#typehints
class inital:
    def __init__(self):
        self.start_time=time.time()
        self.popupManager=popup.PopupWindow()
        self.configPath="./settings/config.json"
        self.configExist=0
        self.caption="Just a Title"
        pg.init()
        if os.path.exists(self.configPath):
            if os.access(self.configPath,os.R_OK):
                self.configExist=1
        if self.configExist==0:
            warnings.warn("config.json can not be read,loading defaults...")
            self.popupManager.ShowWarning("Config Not found!")
            for i in tr.trange(100):
                time.sleep(round(random.uniform(0.01,0.2),2))#absolutely weird, this progress bar indicates nothing
                self.W_width=720
                self.W_height=480
            time.sleep(1)
#config detection
        else:
            print("Loading config from config.json...")
            config={}
            with open(self.configPath,'r') as config_reader:#read configs
                config=json.load(config_reader)
            jump_bar=config["jumpbar"]
            if jump_bar!=True:
                for i in tr.trange(100):
                    time.sleep(round(random.uniform(0.0001,0.2),5))#absolutely weird, this progress bar indicates nothing
            time.sleep(1)
            print("config.json loaded as",config)
            self.W_width=config["resolution_horizontal"]
            self.W_height=config["resolution_vertical"]#load configs
            self.caption=config["caption"]
        end_time=time.time()
        print("Intialize suceess with time",(end_time-self.start_time),"seconds")
    #get screen object for other files to draw
    '''
    def GetScreenObject(self):
        return self.screen
    #get config exist or not
    def GetConfigStatus(self):
        return self.configExist
    #get resolutions
    def GetResolutionH(self):
        return self.W_width
    def GetResolutionV(self):
        return self.W_height
    You can always access with . 
    '''
    def GetWindowSize (self):
        return [self.W_width,self.W_height]
    def InitializeWindow(self):
        self.screen=pg.display.set_mode([self.W_width,self.W_height],pg.RESIZABLE)
        #print(type(self.screen))
        pg.display.set_caption(self.caption)#initializing window
        print("Init Success")
    def OnQuit(self):
        pg.quit()
        end_time=time.time()
        print("quit success, run time",(end_time-self.start_time),"seconds")
        sys.exit()
    def GetConfig(self)->list:
        if self.configExist==1:
            with open(self.configPath,'r') as config_reader:
                config=json.load(config_reader)
                return config
        else:
            return []
        
