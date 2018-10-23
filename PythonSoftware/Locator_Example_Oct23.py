import maya.cmds as cmds

obj = cmds.polySphere(r=1, sx=20, sy=20, ax=[0,1,0], cuv=2, ch=1)[0]
cmds.move(3, 5, 6, obj, ws=True)