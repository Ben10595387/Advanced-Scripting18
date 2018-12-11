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
        self.UIHELP = cmds.text('REMINDER - Select objects')
        self.UIHELP = cmds.text('Selected objects must have a _Suffix')  
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
        NewName = item.rpartition('_')[0] 
        #i  = 0
        #while(i < len(Number) - 1):
            #NewName += (Number[i]+"_")
            #i += 1
        CtrlStuff = (NewName + "_Ctrl")
        cmds.rename(Ctrl, CtrlStuff)
        cmds.select(CtrlStuff)
        cmds.group (name = (CtrlStuff + "_Grp"))
        cmds.matchTransform ((CtrlStuff + "_Grp"), item)


    def CreateControls(self):
        SelectedObject = cmds.ls(sl = True)
        shape = cmds.optionMenu(self.OpMenu, q=True, v=True)
       
        if (shape == "Circle"):
            for item in SelectedObject:
                CircleShape = []
                CircleShape = cmds.circle(center = [0, 0, 0], normal = [0, 1, 0,], sw = 360, radius = 1, degree = 3, sections = 8)
                self.ColorControl(CircleShape[0])
                self.Rename(CircleShape[0], item)
                if(len(SelectedObject) <= 0):
                    cmds.circle(center(0, 0, 0), normal (0, 1, 0,), sw = 360, radius = 1, degree = 3, sections = 8)
       
        elif (shape == "Square"):
            for item in SelectedObject:
                points = [[-1, 0, 1], [-1, 0, 1], [-1, 0, -1], [-1, 0, -1], [-1, 0, -1], [1, 0, -1], [1, 0, -1], [1, 0, -1], [1, 0, 1], [1, 0, 1], [1, 0, 1], [-1, 0, 1], [-1, 0, 1]]
                knots = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4] 
                BezierShape = cmds.curve(bezier = True, d = 3, p = points, k = knots)
                self.ColorControl(BezierShape)
                self.Rename(BezierShape, item)
                
                if(len(SelectedObject) <= 0):
                    cmds.curve(bezier = True, d = 3, p = points, k = knots)

        elif (shape == "Corner"):
            for item in SelectedObject:
                points = [[0, 0, -1], [0, 0, -1], [-1, 0, 0], [-1, 0, 0], [-1, 0, 0], [0, 0, 1], [0, 0, 1]]
                knots = [0, 0, 0, 1, 1, 1, 2, 2, 2] 
                BezierShape = cmds.curve(bezier = True, d = 3, p = points, k = knots)
                self.ColorControl(BezierShape)
                self.Rename(BezierShape, item)
                if(len(SelectedObject) <= 0):
                    cmds.curve(bezier = True, d = 3, p = points, k = knots)
                    
                    
        elif (shape == "Arc"):
            for item in SelectedObject:
                CircleShape = []
                CircleShape = cmds.circle(center = [0, 0, 0], normal = [0, 1, 0,], sw = 180, radius = 1, degree = 3, sections = 8)
                self.ColorControl(CircleShape[0])
                self.Rename(CircleShape[0], item)
                if(len(SelectedObject) <= 0):
                    cmds.circle(center(0, 0, 0), normal (0, 1, 0,), sw = 180, radius = 1, degree = 3, sections = 8)
                    
        elif (shape == "Diamond"):
            for item in SelectedObject:
                points = [-1, 0, 0], [-1, 0, 0], [-0.590989, 0, -0.202351], [-0.394499, 0, -0.398796], [-0.198009, 0, -0.595242], [0, 0, -1], [0, 0, -1], [0, 0, -1], [0.210344, 0, -0.597296], [0.412258, 0, -0.39169], [0.614172, 0, -0.186084], [1, 0, 0], [1, 0, 0], [1, 0, 0], [0.631462, 0, 0.174426], [0.40628, 0, 0.40159], [0.181098, 0, 0.628753], [0, 0, 1], [0, 0, 1], [0, 0, 1], [-0.203337, 0, 0.582577], [-0.39392, 0, 0.389832], [-0.584502, 0, 0.197086], [-1, 0, 0], [-1, 0, 0]
                knots = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8] 
                BezierShape = cmds.curve(bezier = True, d = 3, p = points, k = knots)
                self.ColorControl(BezierShape)
                self.Rename(BezierShape, item)
                if(len(SelectedObject) <= 0):
                    cmds.curve(bezier = True, d = 3, p = points, k = knots)
                    
        elif(shape == "Assign Shape"):
            print "No Shape Selected" 
            
                                                            
BensTools = ControllerCreatorUI()
BensTools.create()

