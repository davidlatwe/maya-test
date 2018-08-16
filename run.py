from maya import standalone, cmds
standalone.initialize()

cmds.file(new=True, force=True)

# This command failed in Maya 2017 +
cmds.workspace("scene", query=True, fileRuleEntry=True)

# This works well instead.
# mel.eval("workspace -q -fileRuleEntry \"scene\"")
