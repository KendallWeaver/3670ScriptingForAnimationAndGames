#Classes
#Other Classes can inherit attributes from other classes. 
#dot operator can access components from other classes to use.

import maya.cmds as cmds

#you have class variables and instance variables
#self is a special work to create an instance
#its referring back to the template itself
#so feet = 4 is the template for everything. doing self. indicates that one instance is different, while chaning the
#feet will make it change everything.
#at least I think that's what's happening


class Animal():
	#every class should start with this. it's to initialize an object and how it's constructed
	#everyone function should have the sself in front of it, so python knows you are talking about the method in that
	#instance. 
	def __init__(self, colour, name):	#this is a constructor
		#this is where you can define the variables for the object
		#these attributes have to be assigned
		self.colour = colour
		self.name = name
		
	#look at locatorTool_2 for more details regarding it.
	#but when creating attributes inside a class, you should proceed most variables with self. 
		
		
#Animal('brown', 'charley')

mytool = LocatorTool()
help(mytool)
mytool.create()	
