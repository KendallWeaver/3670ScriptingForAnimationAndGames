#Make a joint chain based on a selection
# MEL script:
#joint -p -21.092602 0 2.239031 ;
#joint -p -9.624883 0 9.828197 ;
#joint -e -zso -oj xyz -sao yup joint1;
#joint -p 0.187474 0 5.762856 ;
#joint -e -zso -oj xyz -sao yup joint2;

#How it works is the joint seems to first be made, and then the next line parents it.

import maya.cmds as cmds

def MakeJoints():
	
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
	

MakeJoints()