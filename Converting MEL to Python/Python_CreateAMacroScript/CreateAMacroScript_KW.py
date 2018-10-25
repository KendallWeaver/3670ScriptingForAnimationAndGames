#Creates The Left Part of the Monolith 

import maya.cmds as cmds

cmds.polyCube (n="Monolith_Left", 
			   sx=1, 
			   sy=1, 
			   sz=1)
#Selects the Monolith and adjusts it by resizing it and moving it
cmds.select ("Monolith_Left")
# When you want to select something with a specific name, put it in quotes
# Also, future note, the string can be in single quotation marks instead of double
cmds.scale (3.22, 10.886, 3.22, r=True)
#Personal Note: the -r command for these instances is "relative". The flags (-r, for example) depend on the substrings (move, scale, polySphere, etc).
cmds.move (-4.994, 5.255, 0, r=True)
#Selects the bottom portion of the slab and expands it
# tgl is the same as the -toggle command in the previous script
# In the following script, you replace what is selected, add it to an active list, and then toggle/make an additional selection that is added to the list
cmds.select ('Monolith_Left.e[0]', replace=True) 
cmds.select ('Monolith_Left.e[0]', add=True)
cmds.select ('Monolith_Left.e[11]', tgl=True) 
cmds.select ('Monolith_Left.e[11]', add=True) 
cmds.select ('Monolith_Left.e[3]', tgl=True)
cmds.select ('Monolith_Left.e[3]', add=True) 
cmds.select ('Monolith_Left.e[10]', tgl=True) 
cmds.select ('Monolith_Left.e[10]', add=True) 
cmds.scale (1.455422, 1.455422, 1.455422, pivot=(-0.994, -0.188, 0), r=True)
cmds.move (1.602612, 0, 0, r=True)

#One thing I've noticed is that usually the main arguments, or like the main thing you want to do, is at the beginning of the command.

#Creates the Right Part of the Monolith
cmds.polyCube (n="Monolith_Right", 
			   sx=1, 
			   sy=1, 
			   sz=1)
#Selects the bottom of this slab and resizes and moves it
cmds.select ("Monolith_Right") 
cmds.scale (3.22, 10.886, 3.22, r=True) 
cmds.move (4.994, 5.255, 0, r=True) 
#Selects the bottom portion again and expands it slightly
cmds.select ('Monolith_Right.e[0]', replace=True)
cmds.select ('Monolith_Right.e[0]', add=True) 
cmds.select ('Monolith_Right.e[11]', tgl=True)
cmds.select ('Monolith_Right.e[11]', add=True)
cmds.select ('Monolith_Right.e[3]', tgl=True)
cmds.select ('Monolith_Right.e[3]', add=True) 
cmds.select ('Monolith_Right.e[10]', tgl=True) 
cmds.select ('Monolith_Right.e[10]', add=True) 
cmds.scale (1.255422, 1.255422, 1.255422, pivot=(5.148401, -0.188, 0), r=True)
#Creates the Middle, Top Slab
cmds.polyCube (n="Monolith_Top", 
			   sx=1, 
			   sy=1, 
			   sz=1)
#Selects the Top Part and resizes it
cmds.select ('Monolith_Top') 
cmds.scale (16.19, 3.312, 4.986, r=True)
cmds.move (0, 12.237, 0, r=True) 
#Selects portions of edges of the top slab and moves it
cmds.select ('Monolith_Top')
cmds.select ('Monolith_Top.e[6]', replace=True)
cmds.move (0, 0.546549, 0, r=True) 
cmds.select ('Monolith_Top.e[11]', replace=True) 
cmds.move (0.397275, 0, 0, r=True)
cmds.select ('Monolith_Top.e[11]', add=True)
cmds.select ('Monolith_Top.e[2]', replace=True)
cmds.select ('Monolith_Top.e[1]', tgl=True)
cmds.scale (1, 1, 0.867012, pivot=(0, 14.166275, 0), r=True) 
#Selects inner edge of left slab and moves it
cmds.select ('Monolith_Left', replace=True)
cmds.select ('Monolith_Left.e[5]', replace=True)
cmds.move (-0.47427, 0, 0, r=True) 
#Selects all the objects created
cmds.select ('Monolith_Right', 'Monolith_Left', 'Monolith_Top', replace=True)
#Add Division Command
cmds.polySubdivideFacet ("Monolith_Right", ch=True, divisions=1, mode=0)
cmds.polySubdivideFacet ("Monolith_Left", ch=True, divisions=1, mode=0)
cmds.polySubdivideFacet ("Monolith_Top", ch=True, divisions=1, mode=0)
#Extruding a particular face, moving it, scaling it, and relatively moving it again
cmds.select ('Monolith_Right.f[0]', replace=True)
cmds.hilite ('Monolith_Right.f[0]')
cmds.selectMode (component=True)
cmds.select ('Monolith_Right.f[0]', replace=True)
cmds.polyExtrudeFacet ('Monolith_Right.f[0]', 
					   pivotX=3.95256825,
					   pivotY=2.5335,
					   pivotZ=1.918422108,
					   divisions=1,
					   smoothingAngle=30)
cmds.setAttr ("polyExtrudeFace1.localTranslate", 0, 0, 0.808428, type="double3")
cmds.scale (0.899733, 0.899733, 0.899733, pivot=(3.952568, 2.564018, 2.726274), r=True)
cmds.move (0, -0.238607, 0, r=True) 
#Clearing the selection
cmds.select (clear=True)
#Performing the same operation again on a different face
cmds.select ('Monolith_Top', replace=True)
cmds.select ('Monolith_Top.f[10]', replace=True)
cmds.hilite ('Monolith_Top.f[10]')
cmds.selectMode (component=True)
cmds.select ('Monolith_Top.f[10]', replace=True)
cmds.polyExtrudeFacet ('Monolith_Top.f[10]',
					   pivotX=4.0475,
					   pivotY=14.02963734,
					   pivotZ=1.080730488,
					   divisions=1,
					   smoothingAngle=30)
cmds.setAttr ("polyExtrudeFace2.localTranslate", 0, 0, 0.452993, type="double3") 
cmds.scale (1, 1, 0.687206, pivot=(4.062784, 14.482373, -1.080731), r=True)
cmds.move (0, 0, -0.13514, r=True)
cmds.select (clear=True)
#Selecting the Left Slab and rotating it
cmds.select ('Monolith_Left', replace=True) 
cmds.rotate (0, 8.359451, 0, os=True, r=True) 
#Selecting All Slabs and Creating a Group
cmds.group ('Monolith_Top', 'Monolith_Left', 'Monolith_Right')
#Renaming the group
cmds.rename ("group1", "MonolithGroup1")
#Creating a base square to parent the Monolith to
cmds.polyCube (n="Altar",
			   sx=1, 
			   sy=1, 
			   sz=1)
cmds.move (0, 0, 9.29538, r=True)
#Parenting the Monolith to the Altar
cmds.parent ('MonolithGroup1', 'Altar')