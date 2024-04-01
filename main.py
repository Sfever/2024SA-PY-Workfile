def main():
    from codes import init as base
    from codes import startscreen as ss
    from codes import popup
    import pygame as pg
    import pygame.locals as pgl 
    import time
    #intialize objects
    main=base.inital()
    main.InitializeWindow()
    mainwindow=main.screen
    start_screen=ss.StartScreen()
    start_screen.LoadTitle(main)
    #easter_egg_quit_button=button.button(10,10,100,100)
    is_start_screen=1
    is_game_screen=0
    windowManger=popup.PopupWindow()
    def Hello():
        return 0

    clock=pg.time.Clock()
    while 1:
        clock.tick(60)
        #print("4")
        for event in pg.event.get():
            if event.type == pgl.QUIT:
                main.OnQuit()
            if event.type==pgl.MOUSEBUTTONDOWN:
                mousepos=pg.mouse.get_pos()
                if is_start_screen==2:
                    button_result=start_screen.OnPress(mousepos,Hello,main.OnQuit)
                    print(button_result)
                    if button_result[0]!=None:
                        is_start_screen=button_result[0]
                        is_game_screen=button_result[0]+1
                    #easter_egg_quit_button.onclick(main.onquit(),mousepos)
        #print("5")
        if is_start_screen==1:
            #show background if it's there
            start_screen.ShowBackground(mainwindow)
            start_screen.ShowStartExitButtonText(mainwindow,main)
            start_screen.StartExitButton(main)
            #show title text
            start_screen.ShowTitle(mainwindow,main)
            start_screen.PlayMusic("./res/bgm_start.m4a")
            music_player_ss=start_screen.musicplayer
            is_start_screen=2
        elif is_game_screen==1:
            music_player_ss.Stop()
            main.InitializeWindow()
            is_game_screen=2
        #print("3")
        elif is_game_screen==2:
            #print("7")
            pass
        #Update display
        pg.display.update()
        #print("6")

if __name__=="__main__":
    main()