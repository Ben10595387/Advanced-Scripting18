import maya.cmds as cmds

class RenamerUI():
    def __init__(self):
        self.mWindow = "Rename Selected Objects"
    
    def create(self):
        self.delete()

        self.mWindow = cmds.window(self.mWindow, widthHeight = [200, 100], title='Rename Selected Objects')
        self.mCol = cmds.columnLayout(parent=self.mWindow, adjustableColumn=True)
        self.mainInput = cmds.textField(placeholderText='Input Name')
        self.suffix = cmds.textField(placeholderText='Suffix')
        self.UIHELP = cmds.text('REMINDER - Select objects')
        cmds.button(label = 'Go', command=lambda x: self.RenameSelectedObject(cmds.textField(self.mainInput, query = True, text = True) + '**' + cmds.textField(self.suffix, query = True, text = True)))
        cmds.showWindow(self.mWindow)


    def delete(self):
        if cmds.window(self.mWindow, q=True, exists=True):
            cmds.deleteUI(self.mWindow)
     
    def RenameSelectedObject(self, input):
        SelectedObject = cmds.ls(sl = True)
        newarray = input.split('**')
        begnumber = 1
        newarray = [newarray[0], newarray[len(newarray)-1]]
        recount = len(input) - (len(newarray[0]) + len(newarray[1]))
        print('newarray:/n')
        print(newarray)  
        for item in SelectedObject:
            SelectedAmount = 0
            i  = 0
            while i <= begnumber:
                SelectedAmount += 1
                i += 10
            print(recount)
            AmountRecount = recount - SelectedAmount
            i  = 0
            Paddingnum = str(begnumber)
            while i < AmountRecount:
                Paddingnum = '0' + Paddingnum
                i += 1
            Reorder = newarray[0] + "_" + Paddingnum + "_" + newarray[len(newarray)-1]
            cmds.rename(item, Reorder)
            begnumber += 1 
        
#BensTools = RenamerUI()
#BensTools.create()   
                   

