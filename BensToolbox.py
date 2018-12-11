import maya.cmds as cmds


class Toolbox():
    def __init__(self):
        self.mWindow = 'ToolboxWindow'

    def create(self):
        self.delete()

        cmds.window(self.mWindow, title='Toolbox')
        self.mCoLayoo = cmds.columnLayout(parent=self.mWindow, adjustableColumn=True)
        self.InfoTextR = cmds.text('Rename selected objects.')
        cmds.button(parent=self.mCoLayoo, label='Renamer', command=lambda x: self.renamerUI())
        self.InfoTextL = cmds.text('Create Locators using one selection or multiple.')
        cmds.button(parent=self.mCoLayoo, label='Locator', command=lambda x: self.locatorUI())
        self.InfoTextRD = cmds.text('Duplicate selected object using randomness.')
        cmds.button(parent=self.mCoLayoo, label='Random Duplicator', command=lambda x: self.randomDupUI())
        self.InfoTextJ = cmds.text('Create Joints using one selection or multiple.')
        cmds.button(parent=self.mCoLayoo, label='Joint Creator', command=lambda x: self.jointUI())
        self.InfoTextL = cmds.text('Create controls and control grps using selected objects.')
        cmds.button(parent=self.mCoLayoo, label='Control Creator', command=lambda x: self.controlCreatorUI())

        cmds.showWindow(self.mWindow)

    def delete(self):
        if cmds.window(self.mWindow, q=True, exists=True):
            cmds.deleteUI(self.mWindow)

    def renameWin(self):
        import Renamer
        reload(Renamer)
        renameTool = Renamer.RenamerUI()
        renameTool.create()

    def randomDupUI(self):
        import RDuplication
        reload(RDuplication)
        randomTool = RDuplication.RandomDuplicationUI()
        randomTool.create()

    def locatorUI(self):
        import Locator
        reload(Locator)
        locatorTool = Locator.LocatorUI()
        locatorTool.create()

    def jointUI(self):
        import JntCreator
        reload(JntCreator)
        jointsTool = JntCreator.JointCreatorUI()
        jointsTool.create()

    def controlCreatorUI(self):
        import ControllerCreator
        reload(ControllerCreator)
        controlTool = ControllerCreator.ControllerCreatorUI()
        controlTool.create()


BensToolBox = Toolbox()
BensToolBox.create()