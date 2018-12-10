import maya.cmds as cmds

class ControllerCreatorUI():
    def __init__(self):
        self.RGBValues = []
        self.mWindow = "CCreatorWindow"

    def create(self):
        self.delete()

        self.mWindow = cmds.window(self.mWindow, title='Controller Creator', widthHeight = (400, 200))
        self.mCol = cmds.columnLayout(parent=self.mWindow, adjustableColumn=True)
        self.OpMenu = cmds.optionMenu(width = 100, label = "Shape Selection")
        self.AS = cmds.menuItem(label = "Assign Shape")
        self.CIR = cmds.menuItem(label = "Circle")
        self.S = cmds.menuItem(label = "Square")
        self.COR = cmds.menuItem(label = "Corner")
        self.ARC = cmds.menuItem(label = "Arc")
        self.DIAM = cmds.menuItem(label = "Diamond")
        
        self.SC = cmds.button(label = "Select Color", command=lambda x: self.SelectColor())
        self.CC = cmds.button(label = "Create Controls", command=lambda x: self.CreateControls())


        cmds.showWindow(self.mWindow)


    def delete(self):
        if cmds.window(self.mWindow, q=True, exists=True):
            cmds.deleteUI(self.mWindow)
            

    def SelectColor(self):
        cmds.colorEditor()
        if cmds.colorEditor(query = True, result = True):
            self.RGBValues = cmds.colorEditor(query = True, rgb = True)
            print(self.RGBValues)

    def ColorControl(self, item):
        cmds.setAttr ((item + ".overrideEnabled"), 1)
        cmds.setAttr ((item + ".overrideRGBColors"), 1)
        cmds.setAttr ((item + ".overrideColorRGB"), self.RGBValues[0], self.RGBValues[1], self.RGBValues[2])
        
    def Rename(self, Ctrl, item):
        sels = cmds.ls(sl=True)
        cmds.select(cl=True)
        Number = item.split(' ')
        NewName = '' 
        i  = 0
        while(i < len(Number) - 1):
            NewName += (Number[i]+"_")
            i += 1
        CtrlStuff = (NewName + "Ctrl")
        cmds.rename(Ctrl, CtrlStuff)
        cmds.group (name = (CtrlStuff + "_Grp"))
        cmds.matchTransform ((CtrlStuff + "_Grp"), item)


    def CreateControls(self):
        SelectedObject = cmds.ls(sl = True)
        shape = cmds.optionMenu(self.OpMenu, q=True, v=True)
        
        for item in SelectedObject:
            CircleShape = []
            CircleShape = cmds.circle(center = [0, 0, 0], normal = [0, 1, 0,], sw = 360, radius = 1, degree = 3, sections = 8)
            self.ColorControl(CircleShape[0])
            self.Rename(CircleShape[0], item)
            
            if (shape == "Circle"):
                if(len(SelectedObject) <= 0):
                    cmds.circle(center(0, 0, 0), normal (0, 1, 0,), sw = 360, radius = 1, degree = 3, sections = 8) 

BensTools = ControllerCreatorUI()
BensTools.create()
