import pygame as pg
import warnings
import json
import os
import tqdm.rich as tr
import time
import sys
import random
#This files is used to intialize only
#No actual function
class inital:
    config_exist=0
    config_path="./settings/config.json"
    W_width=0
    W_height=0
    caption="Pending"
    screen=""
    start_time=0
    def __init__(self):
        self.start_time=time.time()
        pg.init()
        if os.path.exists(self.config_path):
            if os.access(self.config_path,os.R_OK):
                self.config_exist=1
        if self.config_exist==0:
            warnings.warn("config.json can not be read,loading defaults...")
            for i in tr.trange(100):
                time.sleep(round(random.uniform(0.01,0.2),2))#absolutely weird, this progress bar indicates nothing
                self.W_width=720
                self.W_height=480
            time.sleep(1)
#config detection
        else:
            print("Loading config from config.json...")
            config={}
            with open(self.config_path,'r') as config_reader:#read configs
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
    def get_screen_object(self):
        return self.screen
    #get config exist or not
    def get_config_status(self):
        return self.config_exist
    #get resolutions
    def get_reso_horizontal(self):
        return self.W_width
    def get_reso_vertical(self):
        return self.W_height
    def get_window_size(self):
        return [self.get_reso_horizontal(),self.get_reso_vertical()]
    def init_window(self):
        self.screen=pg.display.set_mode([self.W_width,self.W_height],pg.RESIZABLE)
        pg.display.set_caption(self.caption)#initializing window
    def onquit(self):
        pg.quit()
        end_time=time.time()
        print("quit success, run time",(end_time-self.start_time),"seconds")
        sys.exit()
        
