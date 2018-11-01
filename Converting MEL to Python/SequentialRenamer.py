#Renaming Script

import maya.cmds as cmds

# This seems to work like tokenize
#'obj_#_joint'.partition('#')

def Rename(inputName='name_###_joint'):
	selection = cmds.ls(selection=True, flatten=True)
	
	#Unlike MEL when you used "tokenize", you need to use partition in this case
	
	# input has two arguments; 0 = tail_ and _joint
	
	# This creates the variable of how many #s there are
	# Create a loop that will go through and put all the hashtags in a list, leaving the last string.
	# Currently, the 3rd string with the partition is like '#_joint' if you have two hashtags or more in there. 
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
		numHash = "";    # Reset the string so it isn't adding several 0s every time

Rename()