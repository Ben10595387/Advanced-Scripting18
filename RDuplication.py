import maya.cmds as cmds
import random

class RandomDuplicationUI():
    
    def __init__(self):
        self.mWindow = "RandomDuplicator"

    def create(self):
        self.delete()

        self.mWindow = cmds.window(self.mWindow, widthHeight = (800, 100), title='Random Duplicator')
        self.mCol = cmds.columnLayout(parent=self.mWindow, adjustableColumn=True)
        self.DupText = cmds.text(label = 'Duplication Amount')
        DuplicationAmount = cmds.floatFieldGrp( numberOfFields=2, label='(Lowest, Highest)')            
        RangeX = cmds.floatFieldGrp( numberOfFields=2, label='X Range (Lowest, Highest)')
        RangeY = cmds.floatFieldGrp( numberOfFields=2, label='Y Range (Lowest, Highest)')
        RangeZ = cmds.floatFieldGrp( numberOfFields=2, label='Z Range (Lowest, Highest)')
        self.UIHELP = cmds.text('REMINDER - Select objects')
        cmds.button(label = 'Run', command=lambda x: self.InitiateDuplication(DuplicationAmount, RangeX, RangeY, RangeZ))
           
        
        cmds.showWindow(self.mWindow)
    
    def delete(self):
        if cmds.window(self.mWindow, exists=True):
            cmds.deleteUI(self.mWindow)    

    def InitiateDuplication(self, DuplicationAmount, RangeX, RangeY, RangeZ):
        Poly = cmds.ls(sl = True)
        randAmount = random.randint(cmds.floatFieldGrp(DuplicationAmount, q=True, v=True)[0], 
        cmds.floatFieldGrp(DuplicationAmount, q=True, v=True)[1])
        if len(Poly) <= 0:
            cmds.warning ("No object selected.")
        else:
            i  = 0
            while i < randAmount:
                RandX = random.randint(cmds.floatFieldGrp(RangeX, q=True, v=True)[0], 
                cmds.floatFieldGrp(RangeX, q=True, v=True)[1])
                RandY = random.randint(cmds.floatFieldGrp(RangeY, q=True, v=True)[0], 
                cmds.floatFieldGrp(RangeY, q=True, v=True)[1])
                RandZ = random.randint(cmds.floatFieldGrp(RangeZ, q=True, v=True)[0], 
                cmds.floatFieldGrp(RangeZ, q=True, v=True)[1])
                Blocks = cmds.duplicate(Poly[0], rr=True)
                cmds.move((1*RandX), (1*RandY), (1*RandZ), Blocks, ws=True, wd=True)
                i += 1
                

BensTools = RandomDuplicationUI()
BensTools.create()

