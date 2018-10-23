import maya.cdms as cdms

sels = cdms.ls(sl=True)

for sel in sels:
    print sel
    cdms.connectAttr(`Tail_IK_Jnt_Scale_MD.outputX`, `%s.translateX` % sel, f=True)