import c4d
from  c4d import gui
from random import randint


def randomColor():
    r = randint(0,255) / 256.0
    g = randint(0,255) / 256.0
    b = randint(0,255) / 256.0
    color = c4d.Vector(r,g,b)
    return color


def main():
    eazymat=doc.GetActiveMaterial()
    if not eazymat:
        newmat = c4d.BaseMaterial(5703)
        doc.InsertMaterial(newmat)
        doc.AddUndo(c4d.UNDOTYPE_NEW, newmat)
        c4d.EventAdd()
        newmat[c4d.MATERIAL_COLOR_COLOR]=randomColor()
        newmat.SetBit(c4d.BIT_ACTIVE)

    if eazymat:
        eazymat[c4d.MATERIAL_COLOR_COLOR]=randomColor()





if __name__=='__main__':
    main()