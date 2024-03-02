import init as base
import pygame as pg
import pygame.locals as pgl 
import os
import json
main=base.inital()
mainwindow=main.get_screen_object()
bgexist=0
font_color=[255,255,255]
font_size=30
font_type="arial"
title="Fuck this world"
if os.access("./res/bg.png",os.R_OK):
    bg=pg.image.load("./res/bg.png").convert()
    bgexist=1
if main.config_exist==1:
    config={}
    with open(main.config_path,'r') as config_reader:#read configs
        config=json.load(config_reader)
    font_color=config["font_color"]
    font_type=config["font"]
    title=config["title"]
    font_size=config["font_size"]
font4title=pg.font.SysFont(font_type,font_size)
while True:
    for event in pg.event.get():
        if event.type == pgl.QUIT:
            main.onquit()
    if bgexist==1:
        mainwindow.blit(bg,(0,0))
    main_title=font4title.render(title,True,tuple(font_color))
    F_width,F_height=font4title.size(title)
    mainwindow.blit(main_title,((main.get_reso_horizontal()-F_width)/2,100))
    pg.display.update()
