def welcomescreen():
    playerx=int(SCREENWIDTH/5)
    playery=int(SCREENHEIGHT-GAME_SPRITES['player'].get_height())
    playery=int(playery/2)
    messagex=int((SCREENWIDTH-GAME_SPRITES['message'].get_width())/2)
    messagey=int(SCREENHEIGHT*0.10)
    
    while(True):
        for event in pygame.event.get():
            if (event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE)):
                pygame.quit()
                sys.exit()
            elif(event.type==KEYDOWN and (event.key==K_SPACE or event.key==K_UP)):
                return 4
            else:
                screen.blit(GAME_SPRITES['background'],(0,0))
                screen.blit(GAME_SPRITES['player'],(playerx,playery))
                screen.blit(GAME_SPRITES['message'],(messagex,messagey))
                screen.blit(GAME_SPRITES['base'],(basex,GROUND))
                pygame.display.update()
                FPSCLOCK.tick(FPS)
