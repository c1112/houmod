import hou

def getcurtabpath():
    ''' get current context in houdini '''
    try:
        curtab = hou.ui.paneTabUnderCursor().name()
        return hou.ui.findPaneTab(curtab).pwd().path()
    except:
        return "/out"
