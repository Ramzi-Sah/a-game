#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
#################################################################################################################
#   Author: Ramzi Sah
#   Project: mybigdick
#   Version: 0.2

#   description:
#       Wrote Under python 3.6 Windows

#   requirements:
#       pygame => pip install pygame

#   Disclaimer :
#       * Not liable for any damage incurred from use of this software
#        Including but not limited to : temporary paralysis, spontaneous combustion and premature hair loss

#################################################################################################################
"""
# import game classes
import pygame
from package import engine, data, gameLogic

############################################# - Configuration - #################################################
#################################################################################################################

GAMETITLE = " world"

# Frames per second
FPS = 30

# Window Resolution
displayResolution = (800, 600)

# World size
worldSize = (500, 500)

# map box Size (100px = 1 box)
boxeSize = 100

################################################  - Debug -  ####################################################
#################################################################################################################




#############################################  - Main Script -  #################################################
#################################################################################################################
if __name__ == '__main__':
    gameData = data.loadData()
    gameDisplay, clock = engine.initDisplay(displayResolution, GAMETITLE)
    
    # init game logic
    gameLogic.init(gameData, worldSize, boxeSize)
    
    # main loop
    GameRuning = True
    while GameRuning:
        # update game logic
        gameLogic.update(gameDisplay, displayResolution)
        
        pygame.display.update()
        clock.tick(FPS)


