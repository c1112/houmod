import hou

def worldTransform(node, channel):
    source_path = node.path()
    trans = """{

    matrix src_xform = optransform("%s");
    matrix target_xform_inverted = invert(optransform(opinputpath(".", 0)));
    matrix final_xform = src_xform * target_xform_inverted;


    matrix rest_xform = identity(4);
    matrix self_xform = rest_xform * final_xform;

    float result = explodematrixpr(
            self_xform,
            vector3(ch("./px"), ch("./py"), ch("./pz")),
            vector3(ch("./prx"), ch("./pry"), ch("./prz")),
            chs("./xOrd"), chs("./rOrd"), "%s");
    return result;

    }""" % (source_path, channel)

    return trans


#Source Camera
source_camera = hou.selectedNodes()[0]
source_focalLength = source_camera.parm('focal')
source_aperture = source_camera.parm('aperture')

#Destionation Camera
dest_camera = hou.node('/obj').createNode('cam')
dest_camera.setName("renderCam")

dest_focalLength = dest_camera.parm('focal').set(source_focalLength)
dest_aperture = dest_camera.parm('aperture').set(source_aperture)
#set the world transform
for t in ["tx", "ty", "tz"]:
    dest_transform = dest_camera.parm(t).setExpression(worldTransform(source_camera, t))
#set the world rotation
for r in ["rx", "ry", "rz"]:
    dest_rot = dest_camera.parm(r).setExpression(worldTransform(source_camera, r))
