import maya.cmds as cmds

class LocatorUI():
    def __init__(self):
        self.mWin = 'LocatorWindow'

    def create(self):
        self.delete()

        self.mWin = cmds.window(self.mWin, title='Locator Creation')
        mColLayoo = cmds.columnLayout(parent=self.mWin, adjustableColumn=True)
        self.dropCtrl = cmds.optionMenu(parent=mColLayoo, label='Type')
        self.UIHELP = cmds.text('REMINDER - Select objects')
        cmds.menuItem(parent=self.dropCtrl, label='Bounding Box')
        cmds.menuItem(parent=self.dropCtrl, label='Pivot Point')
        cmds.button(parent=mColLayoo, label='Locator Creator',
                    c=lambda x: self.create_loc(cmds.optionMenu(self.dropCtrl, q=True, select=True)))

        cmds.showWindow(self.mWin)
        
    def delete(self):
        if cmds.window(self.mWin, exists=True):
            cmds.deleteUI(self.mWin)
            
    def create_loc(self, option):
        '''Creates a locator at center of selection or pivot based on input.'''
        sels = cmds.ls(sl=True)

        # create locator at center of selections
        if option is 1:
            
            bbox = cmds.exactWorldBoundingBox(calculateExactly = True)
            pivot = [(bbox[0] + bbox[3]) / 2, (bbox[1] + bbox[4]) / 2, (bbox[2] + bbox[5]) / 2]

            Locator = cmds.spaceLocator()[0]
            cmds.xform(Locator, translation=pivot, worldSpace=True)

        # create locator at pivot point of each selection
        elif option is 2:
            for sel in sels:
                pivot = cmds.xform(sel, q=True, rp=True, ws=True)
                Locator = cmds.spaceLocator()[0]
                cmds.xform(Locator, translation=pivot, worldSpace=True)       
    

BensTools = LocatorUI()
BensTools.create()