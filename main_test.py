from codes import init as base
import pygame as pg
import pygame.locals as pgl 
import os
import json
from codes import textview
#intialize objects
main=base.inital()
mainwindow=main.get_screen_object()
bgexist=0
textlist=textview.textview()
font4title_index=textlist.new_text()
font4title=textlist.get_object(font4title_index)

if os.access("./res/bg.png",os.R_OK):
    bg=pg.image.load("./res/bg.png").convert()
    bgexist=1

if main.config_exist==1:
    config={}
    with open(main.config_path,'r') as config_reader:#read configs
        config=json.load(config_reader)
    #load title text properties from config.json
    font4title.set_color(config["font_color"])
    font4title.set_font(config["font"])
    font4title.set_content(config["title"])
    font4title.set_size(config["font_size"])

font4title.set_text()


    #show background if it's ther

    #get title text size for show it in center
F_width,F_height=font4title.get_dimensions()
    #show title text
    #Update display
main.onquit()
