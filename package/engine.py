#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
#################################################################################################################
#   Author: Ramzi Sah
#   Project: mybigdick
#   file: engine.py

#   description:
#       

#################################################################################################################
"""
# import librarys
import pygame

def initDisplay (Resolution=(800, 600), displayTitle="my wonderful title"):
    """launch a pygame display."""
    
    pygame.init()
    pygame.font.init()
    gameDisplay = pygame.display.set_mode(Resolution, 0, 0)
    clock = pygame.time.Clock()
    
    # pygameoptions
    pygame.display.set_caption(displayTitle)
    
    # pygame.display.set_icon(...)
    #   set_icon(Surface) -> None
    #    Change the system image for the display window

    return gameDisplay, clock

def closeGame ():
    """ properly Close pygame & python """
    
    print("Closing Game...")
    GameRuning = False
    pygame.quit()
    quit() # error with pyinstaller ?
