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

    Toggle = doc.SearchObject("E-Z DEFULT CAM")

    if not Toggle:
        ToggleNew=c4d.BaseObject(c4d.Ocamera)
        ToggleNew[c4d.ID_BASELIST_NAME]="E-Z DEFULT CAM"
        ToggleNew()[c4d.ID_BASEOBJECT_REL_POSITION,c4d.VECTOR_X] = 600
        ToggleNew()[c4d.ID_BASEOBJECT_REL_POSITION,c4d.VECTOR_Y] = 300
        ToggleNew()[c4d.ID_BASEOBJECT_REL_POSITION,c4d.VECTOR_Z] = -600
        ToggleNew()[c4d.ID_BASEOBJECT_REL_ROTATION,c4d.VECTOR_X] = 0.785
        ToggleNew()[c4d.ID_BASEOBJECT_REL_ROTATION,c4d.VECTOR_Y] = -0.339
        doc.InsertObject(ToggleNew)

    if Toggle:
        Toggle()[c4d.ID_BASEOBJECT_REL_POSITION,c4d.VECTOR_X] = 600
        Toggle()[c4d.ID_BASEOBJECT_REL_POSITION,c4d.VECTOR_Y] = 300
        Toggle()[c4d.ID_BASEOBJECT_REL_POSITION,c4d.VECTOR_Z] = -600
        Toggle()[c4d.ID_BASEOBJECT_REL_ROTATION,c4d.VECTOR_X] = 0.785
        Toggle()[c4d.ID_BASEOBJECT_REL_ROTATION,c4d.VECTOR_Y] = -0.339

if __name__=='__main__':
    main()
    c4d.EventAdd()