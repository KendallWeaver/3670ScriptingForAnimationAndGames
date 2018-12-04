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
	button4 = cmds.button(parent=mainCol, label='Make Joint Chain Script', command = lambda x: jointScript.create())
	button5 = cmds.button(parent=mainCol, label='Make Controls and Change Their Color Script', command = lambda x: controlScript.create())		
	
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
		
		renameButton = cmds.button(parent=self.mainCol, label="Rename", command = lambda x: self.renaming(cmds.textField(self.inputName, q=True, text=True)))
		
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
					

class MakeJoints():
	
	def __init__(self): #Two Underscores
		self.mainWindow = 'JointWindow'
		
	def delete(self):
		if cmds.window(self.mainWindow, exists=True):
			cmds.deleteUI(self.mainWindow)
	
	def create(self):
		self.delete()
		
		self.mainWindow = "JointWindow"
	        
		self.mainWindow = cmds.window(self.mainWindow, title="Make Joint Chain")
		
		self.mainCol = cmds.columnLayout(parent=self.mainWindow, adjustableColumn=2, rowSpacing=12)
		
		self.mainRow = cmds.rowLayout(parent=self.mainCol, numberOfColumns= 2, columnAttach=[(1, "left", 45), (2, "both", 10)])
		cmds.text(parent=self.mainRow, label="Select the Objects that you want to use as a base for the joint chain.")
		
		cmds.button(parent=self.mainCol, label="Make Joint Chain", command = lambda x: self.making_chain())
		
		cmds.showWindow(self.mainWindow)

	def making_chain(self):
		#Selection location will serve as a base for where the joints will go
		sels = cmds.ls(sl=True)
		
		cmds.select(clear=True)
		
		#used for a counter in the for loop
		i=0
		for selec in sels:
			locBox = cmds.xform(sels[i], boundingBox=True, q=True)
			center = [(locBox[0]+locBox[3]) / 2, (locBox[1]+locBox[4]) / 2, (locBox[2]+locBox[5]) / 2]
			cmds.joint( p=center )
			i += 1
			
class CreateControls():
	
	def __init__(self): #Two Underscores
		self.mainWindow = 'CreateControlWindow'
		
	def delete(self):
		if cmds.window(self.mainWindow, exists=True):
			cmds.deleteUI(self.mainWindow)	
	
	def create(self):
		self.delete()

		self.mainWindow = cmds.window(self.mainWindow, title='Create Controls')
		
		self.mainCol = cmds.columnLayout(parent=self.mainWindow, adjustableColumn=2, rowSpacing=12)
		
		# Row where you can select what shape of Controls that you want
		self.shapeOptionRow = cmds.rowLayout(parent=self.mainCol, 
											 numberOfColumns=4,
											 columnAttach=[(1, "left", 45), (2, "both", 10), (3, "both", 10), (4, "both", 10)])
		cmds.text (parent=self.shapeOptionRow, label="Shape")
		self.radioButtons = cmds.radioCollection (parent=self.shapeOptionRow)
		self.circleButton = cmds.radioButton ('Circle', parent=self.shapeOptionRow, label="Circle", select=True)
		self.hourglassButton = cmds.radioButton ('Hourglass', parent=self.shapeOptionRow, label="Hourglass")
		self.squareButton = cmds.radioButton ('Square', parent=self.shapeOptionRow, label="Square")
		
		# Row where you can say what you want the controls to be named. 
		self.controlNameRow = cmds.rowLayout (parent=self.mainCol, numberOfColumns=2, columnAttach=[(1, "left", 45), (2, "both", 10)])
		cmds.text(parent=self.controlNameRow, label="Name for Controls: (ie: arm_#_control)")
		self.controlName = cmds.textField()
		
		# Button Where command will be run 
		button1 = cmds.button (parent=self.mainCol,
							   label="Create Shapes",
							   command = lambda x: self.create_controls(cmds.textField(self.controlName, q=True, text=True), cmds.radioCollection(self.radioButtons, query = True, select = True)))
		
		# Row where you can change what color the controls will be
		controlColorRow = cmds.rowLayout (parent=self.mainCol,
										  numberOfColumns=2,
										  columnAttach=[(1, "left", 45), (2, "both", 10)])
		self.colourIndex = cmds.colorIndexSliderGrp (label="Change Color To", min=0, max=20, value=14)
		
		#Button to run scripts where the controls will change color
		button2 = cmds.button (parent=self.mainCol,
							   label="Change Color",
							   command = lambda x: self.change_color(cmds.colorIndexSliderGrp(self.colourIndex, q=True, value=True)))
		
		cmds.showWindow(self.mainWindow)

	def create_controls(self, controlName, radioName):
		# Similar Code was used in the last assignment. Mainly used to help naming conventions, but now curves are created and renamed based on the input.
		selection = cmds.ls(selection=True, flatten=True)
		
		if controlName=='':
			controlName='controls'
		#xPosition, yPosition, zPosition    # apparently you can initialize multiple variables in one line
		objName = controlName.partition('#')[0] 
		#tPP = thirdPartitionPoint
		#Used to store the third partition point so we can break it apart more.
		tPP = controlName.partition('#')[2]
		
		#Partition until there are no more hashtags in the third part of the partition
		charLength = 0
		while charLength < len(tPP):
			if "#" in tPP[0]:
				tPP = tPP.partition('#')[2]
			charLength += 1
	
		numPadding = len(controlName) - (len(objName) + len(tPP))
		
		counter1 = 0
		counter2 = 0
		numHash = ''
		
		if len(selection) > 0:    # If there was a selection, it will run this code.
			i = 0
			for item in selection:
				# Taken from Previous assignment to make naming conventions easier
				while counter1<len(selection):
					# The number of #s will be subtracted by the number of digits i has, thus making room for the actual number
					
					# Gets the location of one of the objects in the selected array, learns it's position
					boxPosition = cmds.xform(selection[i], query=True, worldSpace=True, translation=True)
					
					# Sets Position
					xPosition = (boxPosition[0])    # Index 0 is the x value
					yPosition = (boxPosition[1])    # Index 1 is the y value
					zPosition = (boxPosition[2])    # Index 2 is the z value
									
					# The number of #s will be subtracted by the number of digits counter1 has, thus making room for the actual number
					sizeOfCounter1 = str(counter1)
					while counter2<(numPadding - len(sizeOfCounter1)):
						numHash += "0"
						counter2 += 1
					counter1 += 1
					counter2 = 0
					
					actualName = objName + (numHash + str(counter1)) + tPP
					
					if radioName=='Circle':
						cmds.circle(c=(0, 0, 0), d=3, nr=(0, 1, 0), r=3, s= 8, sw=360, tol=0.01, ut=0, ch=True, name=actualName)
						# following code picks a point and moves it to give the cirve a different shape
						#cmds.select((actualName + '.cv[3]'), replace=True) 
						cmds.xform(actualName, translation=(xPosition, yPosition, zPosition), worldSpace=True, absolute=True)   # Move curve to object
						#Removed Code: parents object to the curve
						#parent $selection[$i] $actualName    # Makes the nurbCurve the parent of the selected object
						#
						numHash = ""    # Reset the string so it isn't adding several 0s every time
						i+=1
						cmds.select(clear=True)
					if radioName=='Hourglass':
						cmds.circle(c=(0, 0, 0), d=3, nr=(0, 1, 0), r=3, s= 8, sw=360, tol=0.01, ut=0, ch=True, name=actualName)
						cmds.select((actualName + '.cv[3]'), replace=True) 
						cmds.select((actualName + '.cv[7]'), tgl=True)
						cmds.scale(0.244444, 1, 1, relative=True)
						cmds.xform(actualName, translation=(xPosition, yPosition, zPosition), worldSpace=True, absolute=True)   # Move curve to object
						numHash = ""    # Reset the string so it isn't adding several 0s every time
						i+=1
						cmds.select(clear=True)
					if radioName=='Square':
						cmds.circle(c=(0, 0, 0), d=3, nr=(0, 1, 0), r=3, s= 8, sw=360, tol=0.01, ut=0, ch=True, name=actualName)
						cmds.select((actualName + '.cv[3]'), replace=True)
						cmds.select((actualName + '.cv[7]'), tgl=True)
						cmds.select((actualName + '.cv[5]'), tgl=True)
						cmds.select((actualName + '.cv[1]'), tgl=True)
						cmds.scale(0.754438, 0.754438, 0.754438, relative=True)
						cmds.xform(actualName, translation=(xPosition, yPosition, zPosition), worldSpace=True, absolute=True)   # Move curve to object
						numHash = ""    # Reset the string so it isn't adding several 0s every time
						i+=1
						cmds.select(clear=True)
			print(selection)
		elif len(selection)==0:   # If there wasn't a selection, it should do this. 
			if radioName=='Circle':
				cmds.circle(c=(0, 0, 0), d=3, nr=(0, 1, 0), r=3, s= 8, sw=360, tol=0.01, ut=0, ch=True, name='C_Ctrl')
				cmds.select(clear=True)
			if radioName=='Hourglass':
				cmds.circle(c=(0, 0, 0), d=3, nr=(0, 1, 0), r=3, s= 8, sw=360, tol=0.01, ut=0, ch=True, name='H_Ctrl')
				cmds.select('H_Ctrl.cv[3]', replace=True) 
				cmds.select('H_Ctrl.cv[7]', tgl=True)
				cmds.scale(0.244444, 1, 1, relative=True)
				cmds.select(clear=True)
			if radioName=='Square':
				cmds.circle(c=(0, 0, 0), d=3, nr=(0, 1, 0), r=3, s= 8, sw=360, tol=0.01, ut=0, ch=True, name='S_Ctrl')
				cmds.select('S_Ctrl.cv[3]', replace=True)
				cmds.select('S_Ctrl.cv[7]', tgl=True)
				cmds.select('S_Ctrl.cv[5]', tgl=True)
				cmds.select('S_Ctrl.cv[1]', tgl=True)
				cmds.scale(0.754438, 0.754438, 0.754438, relative=True)
				cmds.select(clear=True)	
		
	def change_color(self, colourIndex):
		selectedControls = cmds.ls(selection=True, flatten=True)
		for controls in selectedControls:
			controlName = controls
			self.changing_official(controlName, colourIndex)
			
	def changing_official(self, controlName, colourIndex):
		shapes = cmds.listRelatives(controlName, shapes=True)
		for shape in shapes:
			if cmds.nodeType(shape)=='nurbsCurve':
				cmds.setAttr(shape + '.overrideEnabled', 1)
				cmds.setAttr(shape + '.overrideColor', (colourIndex-1))
		
randPlaceGenScript = DuplicateObject()
nameScript = Rename()										
locScript = CreateLoc()
jointScript = MakeJoints()	
controlScript = CreateControls()

CreateMainUI()