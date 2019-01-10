#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
#################################################################################################################
#   Author: Ramzi Sah
#   Project: mybigdick
#   file: gameLogic.py

#   description:
#       

#################################################################################################################
"""
# import librarys
import pygame
from package.gameObjects import GameObjects
from package import mapGrid

###########################################  - Pre defined vars -  ##############################################
#################################################################################################################
# Some RGB Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

PLAYER_SPD = 5

#############################################  - Main functions -  #################################################
####################################################################################################################

def init (gameobjectsData, worldSize, BoxeSize):
    global player
    Cursor = GameObjects(type="cursor")
    player = GameObjects(type="player", data=gameobjectsData['player'], drawable=True)
    
    # recovered from server
    object = GameObjects(type="bot", data=gameobjectsData['Tank'], drawable=True)
    
    # init map grid
    mapGrid.initMapGrid (worldSize, BoxeSize)

def update (gameDisplay, displayResolution):
    gameLogicCheckEvents()
    reCalculatePositions()
    DrawFrame(gameDisplay, displayResolution)
    
    return

#############################################  - Other functions -  #################################################
#####################################################################################################################
def reCalculatePositions():
    
    for gameObject in GameObjects.allObjects:
        # reallocate speed
        gameObject.setSpeed(gameObject.speed[0] + gameObject.acceleration[0], gameObject.speed[1] + gameObject.acceleration[1])
        
        gameObject.setPosWorld(gameObject.posWorld[0] + gameObject.speed[0], gameObject.posWorld[1] + gameObject.speed[1])
        
        # reallocate Position
        if gameObject.type != "player":
            gameObject.setPosScreen(gameObject.posWorld[0] - player.posWorld[0], gameObject.posWorld[1] - player.posWorld[1])
        

def DrawFrame(gameDisplay, displayResolution):
    """Clear screen and redraw all objects."""
    
    # Clear Screen
    gameDisplay.fill(WHITE)
    
    # Draw UI
    # BLACK = (0, 0, 0)
    # WHITE = (255, 255, 255)
    # RED = (255, 0, 0)
    # GREEN = (0, 255, 0)
    # BLUE = (0, 0, 255)
    DrawRectWorld (gameDisplay, 0, 0, 500, 500, GREEN, 50)

    # Display Objects
    for gameObject in GameObjects.allObjects:
        if gameObject.drawable == True:
            pos = (displayResolution[0]/2 - gameObject.posScreen[0] - gameObject.data['size'][0]/2, displayResolution[1]/2 - gameObject.posScreen[1] - gameObject.data['size'][1]/2)
            gameDisplay.blit(gameObject.data['pygame.image'], pos)
            
            # Add some text
            Text = pygame.font.SysFont('Arial', 20)
            textsurface = Text.render(str(gameObject.posGrid), False, (0, 0, 0))
            gameDisplay.blit(textsurface, [pos[0] + 100, pos[1]])
    
    DrawRectWorld (gameDisplay, -player.posWorld[0], -player.posWorld[1], 5, 5, RED, 255)

def DrawRectWorld (gameDisplay, x_world, y_world, Hight, Width, COLOR, Alpha):
    """Draw rectangle based on world position."""
    
    # calculating UI position
    RectX = x_world + player.posWorld[0] + 800/2
    RectY = y_world + player.posWorld[1] + 600/2
    
    Rect = pygame.Surface((Hight, Width))
    Rect.set_alpha(Alpha) # alpha level {min 0, max 255}
    Rect.fill(COLOR)
    gameDisplay.blit(Rect, (RectX, RectY))
    
    return

def gameLogicCheckEvents():
    """check for pygame events."""
    
    for event in pygame.event.get():
        
        # QUIT event
        if event.type == pygame.QUIT:
            closeGame ()
        
        # chek for keyboard KEYDOWN input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.setSpeed(player.speed[0]+PLAYER_SPD, player.speed[1])
            elif event.key == pygame.K_RIGHT:
                player.setSpeed(player.speed[0]-PLAYER_SPD, player.speed[1])
            elif event.key == pygame.K_UP:
                player.setSpeed(player.speed[0], player.speed[1]+PLAYER_SPD)
            elif event.key == pygame.K_DOWN:
                player.setSpeed(player.speed[0], player.speed[1]-PLAYER_SPD)
        
        # chek for keyboard KEYDOWN input
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.setSpeed(player.speed[0]-PLAYER_SPD, player.speed[1])
            elif event.key == pygame.K_RIGHT:
                player.setSpeed(player.speed[0]+PLAYER_SPD, player.speed[1])
            elif event.key == pygame.K_UP:
                player.setSpeed(player.speed[0], player.speed[1]-PLAYER_SPD)
            elif event.key == pygame.K_DOWN:
                player.setSpeed(player.speed[0], player.speed[1]+PLAYER_SPD)
