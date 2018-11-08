import maya.cmds as cmds

def RenameSelectedObject(input):
    SelectedObject = cmds.ls(sl = True)
    newarray = input.split('#')
    begnumber = 1
    newarray = [newarray[0], newarray[len(newarray)-1]]
    recount = len(input) - (len(newarray[0]) + len(newarray[1]))
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
        
RenameSelectedObject("shape_##_Geo")           

