import maya.cmds as cmds

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
		
controlScript = CreateControls()
controlScript.create()