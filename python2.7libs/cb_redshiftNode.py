import xyz_utils
import cb_utils
import hou

def create_cb_redshift_node():
    outnet = xyz_utils.getcurtabpath()
    outpath = cb_utils.renders_output_path()

    cb_rop = hou.node(outnet).createNode('Redshift_ROP', 'CB-Redshift')


    cb_rop.parm('RS_outputFileNamePrefix').set(outpath)
    cb_rop.parm('RS_outputFileNamePrefix').lock(True)
    cb_rop.parm('RS_renderCamera').set('/obj/renderCam')
    cb_rop.parm('BlockSize').set(256)
    cb_rop.parm('RS_renderAOVsToMPlay').set(True)

    #redshift archive
    cb_rop.parm('RS_archive_enable').set(1)
    cb_rop.parm('RS_archive_file').set("$HIP/../data/rs/tmp/$HIPNAME`_`$OS.$F4.rs")
