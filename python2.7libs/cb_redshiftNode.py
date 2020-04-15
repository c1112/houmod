import sgtk
#Globals
hipfile = hou.hipFile.name()
sgengine = sgtk.platform.current_engine()
context = sgengine.context.entity.get('type')
tk = sgengine.tank

def buildOutPath():
    if context == 'Shot':
        shotworkPath = tk.templates['houdini_shot_work']
        shotrenderPath = tk.templates['houdini_shot_render']
    if context == 'Asset':
        shotworkPath = tk.templates['houdini_asset_work']
        shotrenderPath = tk.templates['houdini_asset_render']

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

#get the current tab path for placing the cb_redshift node in the current context
def getcurtabpath():
    try:
        curtab = hou.ui.paneTabUnderCursor().name()
        return hou.ui.findPaneTab(curtab).pwd().path()
    except:
        return "/out"


outnet = getcurtabpath()
outpath = buildOutPath()

cb_rop = hou.node(outnet).createNode('Redshift_ROP', 'CB-Redshift')


cb_rop.parm('RS_outputFileNamePrefix').set(outpath)
cb_rop.parm('RS_outputFileNamePrefix').lock(True)
cb_rop.parm('RS_renderCamera').set('/obj/renderCam')
cb_rop.parm('BlockSize').set(256)
cb_rop.parm('RS_renderAOVsToMPlay').set(True)

#redshift archive
cb_rop.parm('RS_archive_enable').set(1)
cb_rop.parm('RS_archive_file').set("$HIP/../data/rs/tmp/$HIPNAME`_`$OS.$F4.rs")
