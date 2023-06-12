import sys
import random
import pygame
from pygame.locals import *
FPS=32
SCREENHEIGHT=500
SCREENWIDTH=300
screen=pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
GROUND=SCREENHEIGHT*0.8
GAME_SPRITES={}
GAME_SOUNDS={}
PLAYER='sprites/flappy.png'
BACKGROUND='sprites/backgorund.png'
PIPE='sprites/pipe.png'
basex=0
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




#--------------------------------------------------------------------------------
def getrandompipe():
    pipeheight=GAME_SPRITES['pipe'][0].get_height()
    offset=SCREENHEIGHT/3
    pipex=SCREENWIDTH+10
    y2=offset+random.randrange(0,SCREENHEIGHT-basex-1.2*offset)
    y1=pipeheight-y2+offset
    lst=[{'x':pipex,'y':-y1},{'x':pipex,'y':y2}]
    return lst

#---------------------------------------------------------------------
def iscollide(playerx, playery, upperPipes, lowerPipes):
    if playery> GROUND - 25  or playery<0:
        GAME_SOUNDS['hit'].play()
        return True
    
    for pipe in upperPipes:
        pipeHeight = GAME_SPRITES['pipe'][0].get_height()
        if playery < pipeHeight + pipe['y'] and abs(playerx - pipe['x']) < (int(GAME_SPRITES['pipe'][0].get_width())+int(GAME_SPRITES['player'].get_width()))/2:
            GAME_SOUNDS['hit'].play()
            return True

    for pipe in lowerPipes:
        if (playery + GAME_SPRITES['player'].get_height() > pipe['y']) and abs(playerx - pipe['x']) < (int(GAME_SPRITES['pipe'][0].get_width())+int(GAME_SPRITES['player'].get_width()))/2:
            GAME_SOUNDS['hit'].play()
            return True

    return False


#-----------------------------------------------------------------------
def maingame():
    score=0
    playerx=SCREENWIDTH/5
    playery=SCREENHEIGHT/2
    basex=0
    newpipe1=getrandompipe()
    newpipe2=getrandompipe()
    upperpipes=[{'x':SCREENWIDTH+200,'y':newpipe1[0]['y']},
                {'x':1.5*SCREENWIDTH+200,'y':newpipe2[0]['y']}]
    lowerpipes=[{'x':SCREENWIDTH+200,'y':newpipe1[1]['y']},
                {'x':1.5*SCREENWIDTH+200,'y':newpipe2[1]['y']}]
    pipevelx=-4
    flappyvely=-9
    maxv=10
    minv=-8
    flappyacc=1
    playerflapv=-8
    isflapped=False
    

    while(True):
        for event in pygame.event.get():
            if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN and (event.key==K_SPACE or event.key==K_UP):
                if playery>0:
                    flappyvely=playerflapv
                    isflapped=True
                    GAME_SOUNDS['wing'].play()
        crashtest=iscollide(playerx,playery,upperpipes,lowerpipes)
        if crashtest:
            return
        playermidpos=playerx+GAME_SPRITES['player'].get_width()/2
        for pipe in upperpipes:
            pipemidpos=pipe['x']+GAME_SPRITES['pipe'][0].get_width()/2
            if pipemidpos<=playermidpos<pipemidpos+4:
                score+=1
                print("your score is ",score)
                GAME_SOUNDS['point'].play()


        if flappyvely<maxv and not isflapped:
            flappyvely+=flappyacc
        
        if isflapped:
            isflapped=False
        
        playerHeight = GAME_SPRITES['player'].get_height()
        playery = playery + min(flappyvely, GROUND - playery - playerHeight)

        for upperPipe , lowerPipe in zip(upperpipes, lowerpipes):
            upperPipe['x'] += pipevelx
            lowerPipe['x'] += pipevelx
        

        if 0<upperpipes[0]['x']<5:
            newpipe = getrandompipe()
            upperpipes.append(newpipe[0])
            lowerpipes.append(newpipe[1])

        if upperpipes[0]['x'] < -GAME_SPRITES['pipe'][0].get_width():
            upperpipes.pop(0)
            lowerpipes.pop(0)
        
        screen.blit(GAME_SPRITES['background'], (0, 0))
        for upperPipe, lowerPipe in zip(upperpipes, lowerpipes):
            screen.blit(GAME_SPRITES['pipe'][0], (upperPipe['x'], upperPipe['y']))
            screen.blit(GAME_SPRITES['pipe'][1], (lowerPipe['x'], lowerPipe['y']))

        screen.blit(GAME_SPRITES['base'], (basex, GROUND))
        screen.blit(GAME_SPRITES['player'], (playerx, playery))
        myDigits = [int(x) for x in list(str(score))]
        width = 0
        for digit in myDigits:
            width += GAME_SPRITES['numbers'][digit].get_width()
        Xoffset = (SCREENWIDTH - width)/2

        for digit in myDigits:
            screen.blit(GAME_SPRITES['numbers'][digit], (Xoffset, SCREENHEIGHT*0.12))
            Xoffset += GAME_SPRITES['numbers'][digit].get_width()
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        

        


        

            



        pass
    
    

    


#----------------------------------------------------------------------------- 
if __name__=="__main__":
    pygame.init()
    FPSCLOCK=pygame.time.Clock()
    GAME_SPRITES['numbers']=(pygame.image.load('sprites/0.png').convert_alpha(),
                             pygame.image.load('sprites/1.png').convert_alpha(),
                             pygame.image.load('sprites/2.png').convert_alpha(),
                             pygame.image.load('sprites/3.png').convert_alpha(),
                             pygame.image.load('sprites/4.png').convert_alpha(),
                             pygame.image.load('sprites/5.png').convert_alpha(),
                             pygame.image.load('sprites/6.png').convert_alpha(),
                             pygame.image.load('sprites/7.png').convert_alpha(),
                             pygame.image.load('sprites/8.png').convert_alpha(),
                             pygame.image.load('sprites/9.png').convert_alpha())
    #images used in game
    GAME_SPRITES['message']=pygame.image.load('sprites/intro.png').convert_alpha()
    GAME_SPRITES['base']=pygame.image.load('sprites/base.png').convert_alpha()
    GAME_SPRITES['pipe']=(pygame.transform.rotate(pygame.image.load('sprites/pipe.png').convert_alpha(),180),pygame.image.load('sprites/pipe.png').convert_alpha())
    GAME_SPRITES['background']=pygame.image.load('sprites/background.png').convert()
    GAME_SPRITES['player']=pygame.image.load('sprites/flappy.png').convert_alpha()
    #game sounds
    GAME_SOUNDS['hit']=pygame.mixer.Sound('audio/hit.wav')
    GAME_SOUNDS['die']=pygame.mixer.Sound('audio/die.wav')
    GAME_SOUNDS['point']=pygame.mixer.Sound('audio/point.wav')
    GAME_SOUNDS['swoosh']=pygame.mixer.Sound('audio/swoosh.wav')
    GAME_SOUNDS['wing']=pygame.mixer.Sound('audio/wing.wav')

    while(True):
        welcomescreen()
        maingame()









