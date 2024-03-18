from codes import init as base
from codes import startscreen as ss
from codes import button
import pygame as pg
import pygame.locals as pgl 
#intialize objects
main=base.inital()
main.init_window()
mainwindow=main.get_screen_object()
start_screen=ss.startscr()
start_screen.load_title(main)
#easter_egg_quit_button=button.button(10,10,100,100)
def hello():
    print("hello")
while True:
    for event in pg.event.get():
        if event.type == pgl.QUIT:
            main.onquit()
        if event.type==pgl.MOUSEBUTTONDOWN:
            mousepos=pg.mouse.get_pos()
            start_screen.onpress_start_screen(mousepos,hello,main.onquit)
            #easter_egg_quit_button.onclick(main.onquit(),mousepos)

    #show background if it's there
    start_screen.show_background(mainwindow)
    start_screen.show_start_exit_button_text(mainwindow,main)
    start_screen.start_exit_button(main)
    #show title text
    start_screen.show_title(mainwindow,main)
    #Update display
    pg.display.update()
