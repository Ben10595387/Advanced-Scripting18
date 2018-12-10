import maya.cmds as cmds

class JointCreatorUI():
    def __init__(self):
        self.mWin = 'JointCreatorWindow'

    def create(self):
        self.delete()

        self.mWin = cmds.window(self.mWin, title='Joint Creator')
        mColLayoo = cmds.columnLayout(parent=self.mWin, adjustableColumn=True)
        self.dropCtrl = cmds.optionMenu(parent=mColLayoo, label='Type')
        self.UIHELP = cmds.text('REMINDER - Select objects')
        cmds.menuItem(parent=self.dropCtrl, label='Bounding Box')
        cmds.menuItem(parent=self.dropCtrl, label='Pivot Point')
        cmds.button(parent=mColLayoo, label='Create Joints',
                    c=lambda x: self.create_joints(cmds.optionMenu(self.dropCtrl, q=True, select=True)))

        cmds.showWindow(self.mWin)
        
    def delete(self):
        if cmds.window(self.mWin, exists=True):
            cmds.deleteUI(self.mWin)
    def create_joints(self, option):
        '''Creates a Joint at center of selection or pivot based on input.'''
        sels = cmds.ls(sl=True)

        # create locator at center of selections
        if option is 1:     
            
            bbox = cmds.exactWorldBoundingBox(calculateExactly = True)
            pivot = [(bbox[0] + bbox[3]) / 2, (bbox[1] + bbox[4]) / 2, (bbox[2] + bbox[5]) / 2]

            Locator = cmds.spaceLocator()
            cmds.xform(Locator, translation=pivot, worldSpace=True)
            cmds.select(cl=True)
            cmds.matchTransform(cmds.joint(), Locator)
            cmds.delete(Locator)
            

        # create locator at pivot point of each selection
        elif option is 2:
            cmds.select(cl=True)
            for sel in sels:
                cmds.matchTransform(cmds.joint(), sel)
                

                   
BensTools = JointCreatorUI()
BensTools.create()