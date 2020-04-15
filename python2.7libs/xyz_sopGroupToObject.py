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

            #xform = merge.createOutputNode('xform')
            #xform.setDisplayFlag(True)
            #xform.setRenderFlag(True)

            #t = xform.parmTuple('t')
            #t[0].setExpression('-centroid(opinputpath(".", 0), 0)')
            #t[1].setExpression('-centroid(opinputpath(".", 0), 1)')
            #t[2].setExpression('-centroid(opinputpath(".", 0), 2)')

            #obj.parmTuple('t').set([-x for x in t.eval()])

extract_groups(hou.selectedNodes())
