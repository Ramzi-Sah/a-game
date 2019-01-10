#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
#################################################################################################################
#   Author: Ramzi Sah
#   Project: mybigdick
#   file: mapGrid.py

#   description:
#       

#################################################################################################################
"""
# import librarys

class mapGrid:
    """Main Class For Holding Map Data."""
    
    nbrBoxes = 0
    Boxes = ()
    boxSize = 0
    def __init__(self, GridPos=(0, 0), GridWorldPos=(0, 0)):
        self.ID = mapGrid.nbrBoxes
        self.GridPos = GridPos
        self.GridWorldPos = GridWorldPos
        
        mapGrid.nbrBoxes += 1
        mapGrid.Boxes += (self,)

def initMapGrid (worldSize, BoxSize):
    linePos = [0, 0]
    boxesGrid = [int(worldSize[0]/BoxSize), int(worldSize[1]/BoxSize)]
    mapGrid.boxSize = BoxSize
    
    for BoxX in range(boxesGrid[0]):
        linePos[0] += BoxSize
        
        BoxY = 0
        linePos[1] = 0
        for BoxY in range(boxesGrid[1]):
            linePos[1] += BoxSize
            mapGrid(GridPos=[BoxX, BoxY], GridWorldPos=[linePos[0], linePos[1]])
            
    # print(mapGrid.Boxes)
    return boxesGrid
    