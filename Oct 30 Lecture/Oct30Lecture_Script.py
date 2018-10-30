import maya.cmds as cmds

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
		#Previous/clear version
		#bbox = cmds.xform()
		#xPivot = (bbox[0]+bbox[3]) / 2
		#yPivot = (bbox[1]+bbox[4]) / 2
		#zPivot = (bbox[2]+bbox[5]) / 2
		
		#Condensed version
		pivot = [(bbox[0]+bbox[3]) / 2, (bbox[1]+bbox[4]) / 2, (bbox[2]+bbox[5]) / 2]
		
		cmds.delete(dups, ch=True) #Apparently we don't need it anymore; the variable still exists? or did he mean object?
		#Either way it's suppose to clean things up
		cmds.delete(dups)
		
		loc = cmds.spaceLocator() [0]
		cmds.xform(loc, translation=pivot, worldSpace=True)

	elif option is 2:
			for sel in sels:
				pivot = cmds.xform(sel, q=True, rp=True, ws=True)	#query a rotation pivot
				loc = cmds.spaceLocator() [0]
				cmds.xform(loc, translation=pivot, worldSpace=True)
		
	
CreateLoc()