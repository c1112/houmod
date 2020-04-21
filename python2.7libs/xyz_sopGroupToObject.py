import hou

def extract_groups(selected_nodes):
    '''Create objects using target object primitive groups.'''

    if len(selected_nodes) != 1:
        return

    with hou.undos.group('Separate Objects'):
        node = selected_nodes[0]
        node.setDisplayFlag(False)

        groups = node.displayNode().geometry().primGroups()

        for group in groups:
            obj = node.createOutputNode('geo', group.name(), run_init_scripts=True)

            merge = obj.createNode('object_merge')
            merge.parm('objpath1').set("%s/%s" % (node.path(), "OUT"))
            merge.parm('group1').set(group.name())

            null = merge.createOutputNode('null')
            null.setDisplayFlag(True)
            null.setRenderFlag(True)
            
