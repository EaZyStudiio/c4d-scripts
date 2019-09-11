import c4d
#Welcome to the world of Python

def main():
    def tool():
        return c4d.plugins.FindPlugin(doc.GetAction(), c4d.PLUGINTYPE_TOOL)

    def object():
        return doc.GetActiveObject()

    def tag():
        return doc.GetActiveTag()

    def renderdata():
        return doc.GetActiveRenderData()

    def prefs(id):
        return c4d.plugins.FindPlugin(id, c4d.PLUGINTYPE_PREFS)
    
    name=c4d.gui.InputDialog("What's tha Name ")

    c4d.CallCommand(100004772) # Group Objects
    object()[c4d.ID_BASELIST_NAME] = name


if __name__=='__main__':
    main()
    c4d.EventAdd()