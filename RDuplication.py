import maya.cmds as cmds

def InitiateDuplication():
    Poly[] = cmds.ls(sl = True)
    Blocks[] = 1
    randAmount = random.randint(1, 10)
    RandX = random.randint(0, 10)
    RandY = random.randint(0, 10)
    RandZ = random.randint(0, 10)
    print(RandX, RandY, RandZ)
    if len(Poly) <= 0:
        cmds.warning "No object selected."
    else:
        i  = 0
        while i < randAmount:
            cmds.duplicate(rr=True) 
            cmds.move(0+RandX, 0+RandY, 0+RandZ, Blocks ws=True wd=True)
            i += 1