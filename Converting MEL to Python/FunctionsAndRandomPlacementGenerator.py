#Duplicate and Random Generator Script

import maya.cmds as cmds

#to use rand, do this

import random as rand

def DuplicateObject(duplicateNumber=10, xRange = 15, zRange = 25):
	    
    selection = cmds.ls(sl=True)

    #this will duplicate the object a number of times compared to the random number that was given as a parameter
    
    i = 0
    
    while i<duplicateNumber:
        cmds.select (selection)
        cmds.duplicate (selection)
        xPosition = rand.uniform(-(xRange), xRange)
        zPosition = rand.uniform(-(zRange), zRange)
        cmds.move (xPosition, 0, zPosition, r=True)
        i+=1
        
        
DuplicateObject()