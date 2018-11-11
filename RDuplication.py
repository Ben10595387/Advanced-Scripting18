import maya.cmds as cmds
import random

def InitiateDuplication():
    Poly = cmds.ls(sl = True)
    randAmount = random.randint(1, 10)
    if len(Poly) <= 0:
        cmds.warning ("No object selected.")
    else:
        i  = 0
        while i < randAmount:
            RandX = random.randint(-50, 50)
            RandY = random.randint(-10, 10)
            RandZ = random.randint(-50, 50)
            Blocks = cmds.duplicate(Poly[0], rr=True)
            cmds.move((1*RandX), (1*RandY), (1*RandZ), Blocks, ws=True, wd=True)
            i += 1

InitiateDuplication()