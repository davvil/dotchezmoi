#!/usr/bin/env python3

import i3ipc
import os
import sys

i3 = i3ipc.Connection()

outputs = [o for o in i3.get_outputs() if o.active]
if len(outputs) != 2:
    sys.exit(0)

focusedWindow = i3.get_tree().find_focused()
focusedWSName = focusedWindow.workspace().name
focusedOutput = [o for o in outputs if o.current_workspace == focusedWSName][0]
# workspaces() is a function of a container, somwhat strange...
workspaces = focusedWindow.workspaces()
actions = [
    (outputs[0].current_workspace, outputs[1].name),
    (outputs[1].current_workspace, outputs[0].name)
]
print(actions)
for wsName, output in actions:
    i3.command("[workspace=\"%s\"]move workspace to output %s" % (wsName, output))
    i3.command("focus output %s" % output)
    i3.command("workspace %s" % wsName)
i3.command("focus output %s" % focusedOutput.name)
