import maya.cmds as cmds

def CreateJoints():
    SelectedObject = cmds.ls(sl = True)
    for item in SelectedObject:
        bbox = cmds.exactWorldBoundingBox(calculateExactly=True)
        cmds.joint()
        cmds.parent( 'SelectedObject|joint', removeObject=True)
        cmds.joint()
        #for joint hierarchy use index? 
        
        
