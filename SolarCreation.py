import maya.cmds as cmds

cmds.polySphere( n='Sun',sx=20, sy=20, r=2)

cmds.circle(n='Murcury_Orbit' ,nr=(0, 1, 0), r=14.363608)

cmds.polySphere( n='Murcury',sx=20, sy=20, r=0.3)
cmds.move( 0, 0, 14.288922, 'Murcury',ws=True)
cmds.group( 'Murcury_Orbit', 'Murcury', n='Murcury_Grp' )

cmds.duplicate( 'Murcury_Grp' )
cmds.rename('Murcury_Grp1', 'Venus_Grp')
cmds.rename('Venus_Grp|Murcury', 'Venus')
cmds.rename('Venus_Grp|Murcury_Orbit', 'Venus_Orbit')
cmds.rotate( 0, -153.953772, 0, 'Venus_Grp' )
cmds.scale( 1.5, 1.5, 1.5, 'Venus_Grp' )
cmds.scale( .5, .5, .5, 'Venus' )

cmds.duplicate( 'Venus_Grp' )
cmds.rename('Venus_Grp1', 'Earth_Grp')
cmds.rename('Earth_Grp|Venus', 'Earth')
cmds.rename('Earth_Grp|Venus_Orbit', 'Earth_Orbit')
cmds.rotate( 0, 70, 0, 'Earth_Grp' )
cmds.scale( 2, 2, 2, 'Earth_Grp' )
cmds.scale( .7, .7, .7, 'Earth' )




