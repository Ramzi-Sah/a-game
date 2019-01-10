#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
#################################################################################################################
#   Author: Ramzi Sah
#   Project: mybigdick
#   file: gameObjects.py

#   description:
#       
 
#################################################################################################################
"""
# import librarys
import random
from package.mapGrid import mapGrid

###############################################  - Main Class -  ###################################################
####################################################################################################################
class GameObjects:
    """Main Class For Holding Objects Data as ID Type Size Position."""
    
    allObjects = ()
    def __init__(self, type="None", posGrid=[0, 0], drawable=False, data={}):
        # generate random id
        self.id = ''.join(random.choice("0123456789ABCDEF") for _ in range(10))
        self.type = type
        self.drawable = drawable
        
        # set position
        self.posGrid = posGrid
        self.posWorld = [0, 0]
        self.posScreen = [0, 0]
        
        # set forces
        self.acceleration = [0, 0]
        self.speed = [0, 0]
        self.velocity = 0
        
        self.data = data
        
        
        # append new object to class vars
        GameObjects.allObjects += (self,)
    
    def setData (self, data={}):
        self.data = data
    
    def setPosGrid (self, X, Y):
        self.posGrid = [X, Y]
        
        # modify pos as posGrid
        # self.posWorld = [X, Y]
        # self.posScreen = [X, Y]
    
    def setPosWorld (self, X, Y):
        self.posWorld = [X, Y]
        self.posGrid = getPosGrid(posWorld=[X, Y])
        # self.posScreen = getPosScreen(posWorld=[X, Y])
    
    def setPosScreen (self, X, Y):
        self.posScreen = [X, Y]
    
    def setAcceleration (self, X, Y):
        self.acceleration = [X, Y]
    
    def setSpeed (self, X, Y):
        self.speed = [X, Y]
        self.velocity = (X**2 + Y**2)**.5

################################################  - functions -  ###################################################
####################################################################################################################
def getPosGrid(posWorld=[], posScreen=[]):
    # error chek
    if (posWorld == [] and posScreen == []):
        # no parameters given
        print ("[Warning] getPosGrid(posWorld=[], posScreen=[]) no parameter given.")
        return [0, 0]
    if (posWorld != [] and posScreen != []):
        # two parameter given
        print ("[Warning] getPosGrid(posWorld=[], posScreen=[]) only one parameter allowed.")
        return [0, 0]
    ####################################
    if (posScreen == []):
        # posWorld given
        GridPosX = int(posWorld[0] / mapGrid.boxSize)
        GridPosY = int(posWorld[1] / mapGrid.boxSize)
        posGrid = [GridPosX, GridPosY]
        return posGrid
    elif (posWorld == []):
        print("to do")
        # posScreen given

def getPosScreen(posWorld=[], posGrid=[]):
    # error chek
    if (posWorld == [] and posGrid == []):
        # no parameters given
        print ("[Warning] getPosScreen(posWorld=[], posGrid=[]) no parameter given.")
        return [0, 0]
    if (posWorld != [] and posGrid != []):
        # two parameter given
        print ("[Warning] getPosScreen(posWorld=[], posGrid=[]) only one parameter allowed.")
        return [0, 0]
    ####################################
    if (posGrid == []):
        # posWorld given
        for object in GameObjects.allObjects:
            if object.type == "player":
                player = object
    
        posScreenX = (posWorld[0] - player.posScreen[0])
        posScreenY = (posWorld[1] - player.posScreen[1])
        posScreen = [posScreenX, posScreenY]
        return posScreen
    
    elif (posWorld == []):
        print("to do")
        # posGrid given
    









