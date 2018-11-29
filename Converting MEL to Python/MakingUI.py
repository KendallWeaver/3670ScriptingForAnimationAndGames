import maya.cmds as cmds
#to use rand, do this
import random as rand


#Main UI
def CreateMainUI():
	mainWindow = "CreateUIWindow"
	if cmds.window(mainWindow, exists=True):
		cmds.deleteUI(mainWindow)
	    
	mainWindow = cmds.window(mainWindow, title = 'Toolbox')
	
	mainCol = cmds.columnLayout(parent=mainWindow, adjustableColumn=True, rowSpacing=12)
	
	#Add Text Field to Explain Available Scripts
	cmds.text(parent=mainCol, label='Scripts (Python)')
	
	#Button Where command will be run 
	button1 = cmds.button(parent=mainCol, label='Random Placement Generator Script', command = lambda x: RandomGeneratorUI())
	button2 = cmds.button(parent=mainCol, label='Renamer Script', command = lambda x: RenamerUI())
	#commented out in case the python Toolbox won't include this
	#button3 = cmds.button(parent=mainCol, label='Create Control Script', command = lambda x: CreateControlUI())
	button3 = cmds.button(parent=mainCol, label='Create Locator Script', command = lambda x: CreateLocatorUI())
	
	cmds.showWindow(mainWindow)
	
CreateMainUI()

def RandomGeneratorUI():
	mainWindow = "RandomPlacementWindow"
	#deletes UI if it already exists
	if cmds.window(mainWindow, exists=True):
		cmds.deleteUI(mainWindow)
	
	mainWindow = cmds.window(mainWindow, title = "Random Placement Generator")
	
	# create a window, have a label with "number of duplicates, a field that accepts an Int,
	# a range of floats, and a button to do it
	
	# Important parts:
	#Window, Layout, Field (controls: intField, FloatField, buttons)
	#Range values, 
	#command to call the function
	
	mainCol = cmds.columnLayout(parent=mainWindow, adjustableColumn=True, rowSpacing=12)
	
	#first row
	dupRowLayout = cmds.rowLayout(parent=mainCol, numberOfColumns= 3, columnAlign=(1, "right"), columnAttach=[(1, "left", 30), (2, "left", 10), (3, "both", 10)])
	cmds.text(parent=dupRowLayout, label="Duplicate")
	dupIntField = cmds.intField(parent=dupRowLayout, minValue=1, maxValue=25, value=7)    # catching the name of the control so we can query later	
	#Range Row Layout
	rangeRowLayout = cmds.rowLayout(parent=mainCol, numberOfColumns= 4, columnAlign=(1, "right"), columnAttach=[(1, "left", 45), (2, "left", 10), (3, "both", 10), (4, "both", 10)])
	cmds.text(parent=rangeRowLayout, label="Range")
	#In my random generator script, I actually used int values instead of float values. I will change it accordingly
	xRange = cmds.intField(parent=rangeRowLayout, value=0)
	#In the orginal number generator script I made, i didn't use y values, because they were dominos.
	# yRange = `floatField(parent=rangeRowLayout, value=0`
	zRange = cmds.intField(parent=rangeRowLayout, value=0)
	
	#create button
	button = cmds.button(parent=mainCol, label="Generate")
	
	cmds.showWindow(mainWindow)

def RenamerUI():
	mainWindow = "RenamerWindow"
	if cmds.window(mainWindow, exists=True):
		cmds.deleteUI(mainWindow)
        
	mainWindow = cmds.window(mainWindow, title="Rename Object(s)")
	
	mainCol = cmds.columnLayout(parent=mainWindow, adjustableColumn=2, rowSpacing=12)
	
	# Row where user can input the name they want the selected objects/joints to change to
	nameRow = cmds.rowLayout(parent=mainCol, numberOfColumns= 2, columnAttach=[(1, "left", 45), (2, "both", 10)])
	cmds.text(parent=nameRow, label="Name (ie: arm_#_joint)")
	rename = cmds.textField()
	
	#I wonder if there's a way to have 3 cmds.text fields that can be converted into 1 
	
	button = cmds.button(parent=mainCol, label="Rename", command = lambda x: Rename())
	
	cmds.showWindow(mainWindow)

def CreateLocatorUI():
	'''Create a window.'''
	mainWindow = "LocWindow"
	
	if cmds.window(mainWindow, exists=True):
		cmds.deleteUI(mainWindow)
	
	mainWindow = cmds.window(mainWindow, title='Create Locator')
	mainCol = cmds.columnLayout(parent=mainWindow, adjustableColumn=True, rowSpacing=12)
	#dropCtrl = cmds.optionMenu(parent=mainCol, label='Type')
	#cmds.menuItem(parent=dropCtrl, label='Bounding Box')
	#cmds.menuItem(parent=dropCtrl, label='Pivot Point')
	#cmds.button (parent=mainCol, label='Create Locator')
	
	cmds.text(parent=mainCol, label='Locator Type:')
	cmds.button(parent=mainCol, label='Bounding Box', command=lambda x: CreateLoc(1))
	#the x is a generic thing. Sometimes you see args instead. It can be anything. We'll see more with classes
	cmds.button(parent=mainCol, label='Pivot Point', command=lambda x: CreateLoc(2))	
	
	cmds.showWindow(mainWindow)

#Renaming Script
# This seems to work like tokenize
#'obj_#_joint'.partition('#')

def Rename(inputName='name_#_joint'):
	selection = cmds.ls(selection=True, flatten=True)
	
	#Unlike MEL when you used "tokenize", you need to use partition in this case
	
	# input has two arguments 0 = tail_ and _joint
	
	# This creates the variable of how many #s there are
	# Create a loop that will go through and put all the hashtags in a list, leaving the last .
	# Currently, the 3rd  with the partition is like '#_joint' if you have two hashtags or more in there. 
	objName = inputName.partition('#')[0]
	#tPP = thirdPartitionPoint
	#Used to store the third partition point so we can break it apart more.
	tPP = inputName.partition('#')[2]
	
	#Partition until there are no more hashtags in the third part of the partition
	charLength = 0
	while charLength < len(tPP):
		if "#" in tPP[0]:
			tPP = tPP.partition('#')[2]
		charLength += 1

	numPadding = len(inputName) - (len(objName) + len(tPP))

	#initializing counters for the loops
	counter1 = 0
	counter2 = 0
	numHash = ''
	
	while counter1<len(selection):
		# The number of #s will be subtracted by the number of digits counter1 has, thus making room for the actual number
		sizeOfCounter1 = str(counter1)
		while counter2<(numPadding - len(sizeOfCounter1)):
			numHash += "0"
			counter2 += 1 
		actualName = objName + (numHash + str(counter1)) + tPP
		cmds.rename(selection[counter1], actualName)
		counter1 += 1
		counter2 = 0
		numHash = ""    # Reset the  so it isn't adding several 0s every time
		
		
#Duplicate and Random Generator Script
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

#CreateLocator Script
def CreateLoc(option=1):	#this is saying "if you don't have the option paramater when it's called out, I will put this in for it". It will always equal one
	sels = cmds.ls(sl=True)
	
	if option is 1:
		dups = cmds.duplicate(sels, rr=True)
		dups = cmds.polyUnite(dups,
							  ch=True,
							  mergeUVSets=True,
							  centerPivot=True)[0]	
		bbox = cmds.xform(dups, boundingBox=True, q=True)
		
		#Condensed version
		pivot = [(bbox[0]+bbox[3]) / 2, (bbox[1]+bbox[4]) / 2, (bbox[2]+bbox[5]) / 2]
		
		cmds.delete(dups, ch=True) 
		cmds.delete(dups)
		
		loc = cmds.spaceLocator() [0]
		cmds.xform(loc, translation=pivot, worldSpace=True)

	elif option is 2:
			for sel in sels:
				pivot = cmds.xform(sel, q=True, rp=True, ws=True)	#query a rotation pivot
				loc = cmds.spaceLocator() [0]
				cmds.xform(loc, translation=pivot, worldSpace=True)