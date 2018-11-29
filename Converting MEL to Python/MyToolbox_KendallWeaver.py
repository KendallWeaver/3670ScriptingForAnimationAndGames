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
	button1 = cmds.button(parent=mainCol, label='Random Placement Generator Script', command = lambda x: randPlaceGenScript.create())
	button2 = cmds.button(parent=mainCol, label='Renamer Script', command = lambda x: nameScript.create())
	#commented out in case the python Toolbox won't include this
	#button3 = cmds.button(parent=self.mainCol, label='Create Control Script', command = lambda x: CreateControlUI())
	button3 = cmds.button(parent=mainCol, label='Create Locator Script', command = lambda x: locScript.create())
	
	cmds.showWindow(mainWindow)

#Renaming Script
# This seems to work like tokenize
#'obj_#_joint'.partition('#')

class Rename():
	def __init__(self): #Two Underscores
		self.mainWindow = 'RenamerWindow'
		
	def delete(self):
		if cmds.window(self.mainWindow, exists=True):
			cmds.deleteUI(self.mainWindow)	
	
	def create(self):
		self.delete()
		
		self.mainWindow = "RenamerWindow"
	        
		self.mainWindow = cmds.window(self.mainWindow, title="Rename Object(s)")
		
		self.mainCol = cmds.columnLayout(parent=self.mainWindow, adjustableColumn=2, rowSpacing=12)
		
		# Row where user can input the name they want the selected objects/joints to change to
		self.nameRow = cmds.rowLayout(parent=self.mainCol, numberOfColumns= 2, columnAttach=[(1, "left", 45), (2, "both", 10)])
		cmds.text(parent=self.nameRow, label="Name (ie: arm_#_joint)")
		self.inputName = cmds.textField()
		
		#I wonder if there's a way to have 3 cmds.text fields that can be converted into 1 
		
		cmds.button(parent=self.mainCol, label="Rename", command = lambda x: self.renaming(cmds.textField(self.inputName, q=True, text=True)))
		
		cmds.showWindow(self.mainWindow)
			
	def renaming(self, inputName):

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
class DuplicateObject():
	def __init__(self): #Two Underscores
		self.mainWindow = 'RandomPlacementWindow'
		
	def delete(self):
		if cmds.window(self.mainWindow, exists=True):
			cmds.deleteUI(self.mainWindow)
	
	def create(self):

		self.delete()
		
		self.mainWindow = "RandomPlacementWindow"
		
		self.mainWindow = cmds.window(self.mainWindow, title = "Random Placement Generator")
		
		# create a window, have a label with "number of duplicates, a field that accepts an Int,
		# a range of floats, and a button to do it
		
		# Important parts:
		#Window, Layout, Field (controls: intField, FloatField, buttons)
		#Range values, 
		#command to call the function
		
		self.mainCol = cmds.columnLayout(parent=self.mainWindow, adjustableColumn=True, rowSpacing=12)
		
		#first row
		self.dupRowLayout = cmds.rowLayout(parent=self.mainCol, numberOfColumns= 3, columnAlign=(1, "right"), columnAttach=[(1, "left", 30), (2, "left", 10), (3, "both", 10)])
		cmds.text(parent=self.dupRowLayout, label="Duplicate")
		self.dupIntField = cmds.intField(parent=self.dupRowLayout, minValue=1, maxValue=25, value=7)    # catching the name of the control so we can query later	
		#Range Row Layout
		self.rangeRowLayout = cmds.rowLayout(parent=self.mainCol, numberOfColumns= 4, columnAlign=(1, "right"), columnAttach=[(1, "left", 45), (2, "left", 10), (3, "both", 10), (4, "both", 10)])
		cmds.text(parent=self.rangeRowLayout, label="Range")
		#In my random generator script, I actually used int values instead of float values. I will change it accordingly
		self.xRange = cmds.intField(parent=self.rangeRowLayout, value=0)
		#In the orginal number generator script I made, i didn't use y values, because they were dominos.
		# yRange = `floatField(parent=self.rangeRowLayout, value=0`
		self.zRange = cmds.intField(parent=self.rangeRowLayout, value=0)
		
		#create button
		button = cmds.button(parent=self.mainCol, label="Generate",
								command =lambda x: self.dup_rand(cmds.intField(self.dupIntField, q=True, v=True), cmds.intField(self.xRange, q=True, v=True), cmds.intField(self.zRange, q=True, v=True)))
		
		cmds.showWindow(self.mainWindow)
			
	def dup_rand(self, dupIntField, xRange, zRange):
		selection = cmds.ls(sl=True)
		#this will duplicate the object a number of times compared to the random number that was given as a parameter
		
		i = 0
		
		while i<dupIntField:
			cmds.select (selection)
			cmds.duplicate (selection)
			xPosition = rand.uniform(-(xRange), xRange)
			zPosition = rand.uniform(-(zRange), zRange)
			cmds.move (xPosition, 0, zPosition, r=True)
			i+=1

#CreateLocator Script
class CreateLoc():	#this is saying "if you don't have the option paramater when it's called out, I will put this in for it". It will always equal one
	def __init__(self): #Two Underscores
		self.mainWindow = 'LocWindow'
	
	def create(self): #you don't have to pass data because python should take care of it
		self.delete()
	
		self.mainWindow = cmds.window(self.mainWindow, title='Create Locator')
		self.mainCol = cmds.columnLayout(parent=self.mainWindow, adjustableColumn=True, rowSpacing=12)
		#dropCtrl = cmds.optionMenu(parent=self.mainCol, label='Type')
		#cmds.menuItem(parent=dropCtrl, label='Bounding Box')
		#cmds.menuItem(parent=dropCtrl, label='Pivot Point')
		#cmds.button (parent=self.mainCol, label='Create Locator')
		
		cmds.text(parent=self.mainCol, label='Locator Type:')
		cmds.button(parent=self.mainCol, label='Bounding Box', command=lambda x: self.create_loc(option=1))
		#the x is a generic thing. Sometimes you see args instead. It can be anything. We'll see more with classes
		cmds.button(parent=self.mainCol, label='Pivot Point', command=lambda x: self.create_loc(option=2))	
		
		cmds.showWindow(self.mainWindow)
		
		sels = cmds.ls(sl=True)
		
	def delete(self):
		#unlike before, because you defined self.mainWindow in the init function, self needs to be added to refer to that instances
		if cmds.window(self.mainWindow, exists=True):
			cmds.deleteUI(self.mainWindow)
	
	def create_loc(self, option=1):
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
					
randPlaceGenScript = DuplicateObject()
nameScript = Rename()										
locScript = CreateLoc()
				
CreateMainUI()