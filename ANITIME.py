import c4d
from c4d import gui
from c4d import documents

###########################################################################
#Turns off all Subdivision Surfaces. Turn them back on with CTRL modifier.#
###########################################################################
#Written by Andrew Runyon
#Icon by Can Erduman

def GetNextObject(op):
    """
    This function loops through every object in the scene
    """
    if op==None: return None

    if op.GetDown(): return op.GetDown()

    while not op.GetNext() and op.GetUp():
      op = op.GetUp()

    return op.GetNext()

def getNextLayer(layer):
    if layer.GetDown():
         return layer.GetDown()
    while layer.GetUp() and not layer.GetNext():
         layer = layer.GetUp()
    return layer.GetNext()


def main():
    doc.StartUndo()
    c4dVersion= c4d.GetC4DVersion()

    CTRL=False
    bc = c4d.BaseContainer()
    c4d.gui.GetInputState(c4d.BFM_INPUT_KEYBOARD,c4d.BFM_INPUT_CHANNEL,bc)

    if bc[c4d.BFM_INPUT_QUALIFIER] ==2 :
        CTRL=True

    obj = doc.GetActiveObjects(1)
    if not obj:
        gui.MessageDialog("Select your mesh will you")
        return True

    bc = c4d.BaseContainer()
    root = doc.GetLayerObjectRoot()
    layer = root.GetDown()
    toggled = 0

    Toggle = doc.SearchObject("Anitime is Active")
    myobject = doc.GetFirstObject()
    while myobject:
      doc.AddUndo(c4d.UNDOTYPE_CHANGE_SMALL, myobject)
      myobject = GetNextObject(myobject)
    #If Control key is depressed turn on all Subdivision Surfaces
    if not Toggle:
      c4d.CallCommand(100004809, 100004809) # Add to New Layer
      ToggleNew=c4d.BaseObject(c4d.Onull)
      ToggleNew[c4d.ID_BASELIST_NAME]="Anitime is Active"
      doc.InsertObject(ToggleNew)
      myobject = doc.GetFirstObject()
      while myobject:
        if myobject.GetTypeName() == "Subdivision Surface":
          myobject[c4d.ID_BASEOBJECT_GENERATOR_FLAG] = 1
        myobject = GetNextObject(myobject)

      c4d.EventAdd()
      return

    #Else turn off all Subdivision Surfaces
    if Toggle:
      myobject = doc.GetFirstObject()
      while myobject:
        if myobject.GetTypeName() == "Subdivision Surface":
          myobject[c4d.ID_BASEOBJECT_GENERATOR_FLAG] = 0
        myobject = GetNextObject(myobject)

    if c4d.gui.GetInputState(c4d.BFM_INPUT_KEYBOARD,c4d.BFM_INPUT_CHANNEL,bc):
        if not bc[c4d.BFM_INPUT_QUALIFIER] & c4d.QSHIFT:
            # Mute Selected Layers
            while layer:
                if layer.GetBit(c4d.BIT_ACTIVE):
                    layer_data = layer.GetLayerData(doc)
                    layer_data['locked'] = not layer_data['locked']
                    layer.SetLayerData(doc,layer_data)
                    toggled = 1

                if not layer.GetBit(c4d.BIT_ACTIVE):
                    toggled = 1

                layer = getNextLayer(layer)
        else:
            return


    if toggled == 0:
        gui.MessageDialog("Make sure ur mesh has a layer /n attached to it")
        return False

    c4d.EventAdd()

    if CTRL == True:
        saver=c4d.BaseObject(c4d.Onull)
        doc.InsertObject(saver)
        Toggle = doc.SearchObject("Anitime is Active")
        Toggle.SetBit(c4d.BIT_ACTIVE)
        c4d.CallCommand(100004787, 100004787) # Delete





    c4d.EventAdd()
    doc.EndUndo()

if __name__=='__main__':
    main()