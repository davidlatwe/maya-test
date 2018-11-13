import os
from maya import standalone, cmds
standalone.initialize()

os.environ["project"] = "/Path/To/My/Project"

cmds.file(new=True, force=True)
file_node = cmds.createNode("file")
cmds.setAttr(file_node + ".fileTextureName",
             "$project/img/pic.jpg",
             type="string")
file_path = cmds.getAttr(file_node + ".fileTextureName",
                         expandEnvironmentVariables=True)

assert file_path == "/Path/To/My/Project/img/pic.jpg"
