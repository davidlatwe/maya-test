from maya import standalone, cmds
standalone.initialize()

cmds.file(new=True, force=True)

# Should work in all version
print(cmds.workspace(fileRuleEntry="scene"))
