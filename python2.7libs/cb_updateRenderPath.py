import cb_utils
import hou

def cb_update_render_path():
    #new path
    newPath = cb_utils.renders_output_path()

    #get selected nodes
    for node in hou.selectedNodes():
        node.parm('RS_outputFileNamePrefix').lock(False)
        node.parm('RS_outputFileNamePrefix').set(newPath)
        node.parm('RS_outputFileNamePrefix').lock(True)
