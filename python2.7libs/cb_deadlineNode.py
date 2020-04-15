#get the current tab path for placing the cb_redshift node in the current context
def getcurtabpath():
    try:
        curtab = hou.ui.paneTabUnderCursor().name()
        return hou.ui.findPaneTab(curtab).pwd().path()
    except:
        return "/out"


outnet = getcurtabpath()
cb_rop = hou.node(outnet).createNode('deadline', 'CB-Deadline')

#set some parms
jobname = cb_rop.parm('dl_job_name')
jobname.deleteAllKeyframes()
jobname.set("`pythonexprs(\"hou.hipFile.path().split('/')[4]\")` | $HIPNAME`_``pythonexprs(\"hou.node('.').inputAncestors()[0].name()\")`")
jobname.lock(True)

cb_rop.parm('trange').set(1)
cb_rop.parm('dl_limit_frames_to_node').set(True)
cb_rop.parm('dl_pool').set("3d")
cb_rop.parm('dl_secondary_pool').set("all")
cb_rop.parm('dl_group').set("houdini")
cb_rop.parm('dl_concurrent_tasks').set(3)
cb_rop.parm('dl_slave_task_limit').set(0)
cb_rop.parm('dl_chunk_size').set(20)
cb_rop.parm('dl_redshift_job').set(1)
cb_rop.parm('dl_redshift_pool').set("3d")
cb_rop.parm('dl_redshift_secondary_pool').set("all")
cb_rop.parm('dl_redshift_group').set("redshift")
