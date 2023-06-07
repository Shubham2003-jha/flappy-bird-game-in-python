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
