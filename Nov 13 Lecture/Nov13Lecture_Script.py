import maya.cmds as cmds

#lambda function?

#When it comes to UI in python, it actually runs the command of the UI instead of storing it
#lambda is an inline function

#any time you call a GUI you will need to use a lambda function

# if you do something '''Like this''' It'll display that message when you run the help command

def WindowMaker():
	'''Create a window.'''
	mWin = "LocWindow"
	
	if cmds.window(mWin, exists=True):
		cmds.deleteUI(mWin)
	
	mWin = cmds.window(mWin, title='Create Locator')
	mCol = cmds.columnLayout(parent=mWin, adjustableColumn=True)
	#dropCtrl = cmds.optionMenu(parent=mCol, label='Type')
	#cmds.menuItem(parent=dropCtrl, label='Bounding Box')
	#cmds.menuItem(parent=dropCtrl, label='Pivot Point')
	#cmds.button (parent=mCol, label='Create Locator')
	
	cmds.text(parent=mCol, label='Locator Type:')
	cmds.button(parent=mCol, label='Bounding Box', command=lambda x: CreateLoc(1))
	#the x is a generic thing. Sometimes you see args instead. It can be anything. We'll see more with classes
	cmds.button(parent=mCol, label='Pivot Point', command=lambda x: CreateLoc(2))	
	
	cmds.showWindow(mWin)
	
WindowMaker()
	
	
# stuff commented out is to create locator at center of objects
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
		
	
#CreateLoc()