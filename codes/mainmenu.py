import init as base
import pygame as pg
import pygame.locals as pgl 
main=base.inital()
mainwindow=main.get_screen_object()
while True:
    for event in pg.event.get():
        if event.type == pgl.QUIT:
            main.onquit()


