"""
QuickRename

Author: EAZY5d
Website: xtal3nt.xyz or eazy5dartstation.com/
Name-US: QuickRename
Description-US: Quickly Rename's your tag &/or texture with any Object selected
Written for Maxon Cinema 4D R20.057
"""
import c4d

def main():
    doc.StartUndo()
    sel=doc.GetSelection()

    tag=doc.GetActiveTag()

    material=doc.GetActiveMaterial()

    for obj in sel:
        doc.AddUndo(c4d.UNDOTYPE_CHANGE, obj)
        name=obj.GetName()
        tag()[c4d.ID_BASELIST_NAME] = name
        c4d.EventAdd()
        try:# try and execute this code
            material()[c4d.ID_BASELIST_NAME] = name+str("_tex")
            c4d.EventAdd()

        except: # If something went wrong
            pass # Do nothing

    doc.EndUndo()
    c4d.EventAdd()

if __name__=='__main__':
    main()