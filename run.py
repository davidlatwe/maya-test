from maya import standalone, cmds
standalone.initialize()

cmds.file(new=True, force=True)
location = cmds.camera("persp", query=True, worldCenterOfInterest=True)
print(location)
