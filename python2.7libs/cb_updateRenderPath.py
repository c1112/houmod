import sgtk
#Globals
hipfile = hou.hipFile.name()
sgengine = sgtk.platform.current_engine()
tk = sgengine.tank

def buildOutPath():
    shotworkPath = tk.templates['houdini_shot_work']
    shotrenderPath = tk.templates['houdini_shot_render']

    fields = shotworkPath.get_fields(hipfile)
    customfields = { "node": "`$OS`",
                     "version": 99990,
                     "width": 99991,
                     "height": 99992,
                     "SEQ": "$F4",
                     }
    fields.update(customfields)

    tmpPath = shotrenderPath.apply_fields(fields)
    tmpPath = tmpPath.replace('v99990', """`pythonexprs("hou.hipFile.basename().split('.')[1]")`""")
    tmpPath = tmpPath.replace('99991', '`ch(chs("RS_renderCamera")+"/resx")`')
    tmpPath = tmpPath.replace('99992', '`ch(chs("RS_renderCamera")+"/resy")`')
    tmpPath = tmpPath.replace('\\','/')

    return tmpPath

#new path
newPath = buildOutPath()

#get selected nodes
for node in hou.selectedNodes():
    node.parm('RS_outputFileNamePrefix').lock(False)
    node.parm('RS_outputFileNamePrefix').set(newPath)
    node.parm('RS_outputFileNamePrefix').lock(True)
