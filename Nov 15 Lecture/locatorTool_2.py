import maya.cmds as cmds

class LocatorTool():
	def __init__(self): #Two Underscores
		self.mWin = 'LocWindow'
		
	def create(self): #you don't have to pass data because python should take care of it
		self.delete()
		
		self.mWin = cmds.window(self.mWin, title='Create Locator')
		self.mCol = cmds.columnLayout(parent=self.mWin, adjustableColumn=True)
		self.dropCtrl = cmds.optionMenu(parent=self.mCol, label='Type')
		cmds.menuItem(parent=self.dropCtrl, label='Bounding Box')
		cmds.menuItem(parent=self.dropCtrl, label='Pivot Point')
		cmds.button (parent=self.mCol, label='Create Locator',
					 c=lambda x: self.create_loc(cmds.optionMenu(self.dropCtrl, q=True, value=True, select=True)))
		
		#cmds.text(parent=self.mCol, label='Locator Type:')
		#cmds.button(parent=self.mCol, label='Bounding Box', command=lambda x: CreateLoc(1))
		#the x is a generic thing. Sometimes you see args instead. It can be anything. We'll see more with classes
		#cmds.button(parent=self.mCol, label='Pivot Point', command=lambda x: CreateLoc(2))	
		
		#lambda x: CreateLoc(value of the option menu)
		#cmds.optionMenu(self.dropCtrl, q=True, value=True, select=True)
		#copy and pasted to the command value in the button above
		
		cmds.showWindow(self.mWin)
		
	def delete(self):
		#unlike before, because you defined self.mWin in the init function, self needs to be added to refer to that instances
		if cmds.window(self.mWin, exists=True):
			cmds.deleteUI(self.mWin)
			
	def create_loc(self, option=1):	#this is saying "if you don't have the option paramater when it's called out, I will put this in for it". It will always equal one
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