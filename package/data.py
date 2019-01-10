#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
#################################################################################################################
#   Author: Ramzi Sah
#   Project: mybigdick
#   file: data.py

#   description:
#       

#################################################################################################################
"""
# import librarys
import pygame
import json

# functions
def loadData():
    """ import data files and parse them for pygame """
    
    print ("loading data ...")
    gameobjectsData = {}
    folders = ("map/", "objects/", "ui/")
    cfg = ()
    
    for folder in folders:
        try:
            with open("data/"+folder+"config.json", "r") as cfgFile:
                cfg += (json.load(cfgFile),)
        except Exception as error:
            print("[ERROR] error while loading game data: " + str(error))
    
    for folder in cfg:
        for folderClass in folder:
            # get objects data
            if (folderClass == "objects"):
                for object in folder["objects"]:
                    gameobjectsData[object] = folder["objects"][object]
                    
                    # parse image and append it to gameobjectsData dict
                    dataLoader = pygame.image.load(gameobjectsData[object]['file'])
                    gameobjectsData[object]['pygame.image'] = dataLoader
                
            # get ui data
            # if (folderClass == "ui"):
    
    print ('Data loaded Successfully  : '+ str(gameobjectsData))
    return gameobjectsData

