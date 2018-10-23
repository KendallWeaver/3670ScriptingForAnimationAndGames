#Arrays in python are called lists
#Variables don't require a special character ($)
#Python is dynamic typing; variables can be changed to a new type at any time
#No more semi colons, no curly braces. I think you can still you them?
#Python relies on spacing an organization to help define code blocks
#Loops will end with :     IE> if(2>x): The next code in the loop should be indented (like you usually do)

#if():
	#New Code
    
#in python, you need to tell the script you need to use the Maya library for code
	#import maya.cmds
	#or is it impart ? cure you eye sight
	#import maya.cmds as cmds
	
	#then later when using the ls command, you can do cmds.ls
		#banana = cmds.ls(sl=True)[0]
	

#Maya:   polySphere -r 1 -sx 20 -sy 20 -ax 0 1 0 -cuv 2 -ch 1	
#Python: cmds.polySphere(r=1, sx=20, sy=20, ax=[0, 1, 0], cuv=2, ch=1)

# obj = cmds.polySphere(r=1, sx=20, sy=20, ax=[0, 1, 0], cuv=2, ch=1)
# obj = ["ball", "polySphere1"]

#Approaching Arrays
#If you just want access to one part of the array 
#obj = obj[0]
#now obj is just a string instead of a list

# obj = cmds.polySphere(r=1, sx=20, sy=20, ax=[0, 1, 0], cuv=2, ch=1)[0]
#if you do that, obj == "pSphere1", becoming just a string
# you can add the [0] after the other alternative code as well

import maya.cmds as cmds

obj = cmds.polySphere(r=3, sx=20, sy=20, ax=[0,1,0], cuv=2, ch=1)[0]
cmds.move(0, 3, 0, obj, ws=True)

#he was able to do something like r=2
								 #sx+20
#maybe ask him later?
obj = cmds.polySphere(r=2, 
				      sx=20,
				      sy=20,
				      ax=[0,1,0],
				      cuv=2,
				      ch=1)[0]
cmds.move(0, 7, 0, obj, ws=True)

obj = cmds.polySphere(r=1, sx=20, sy=20, ax=[0,1,0], cuv=2, ch=1)[0]
cmds.move(0, 9.5, 0, obj, ws=True)