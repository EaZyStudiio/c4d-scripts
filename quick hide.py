import c4d
from c4d import gui
## THE BEER-EAZY LICENSE""By E-z5D"
# This Script is made by eazy5D. As long as you retain this notice,
# You are free to use this in any project of your work/project.
# If we meet some day and you think this stuff is worth it, you can buy me a beer in return :)


def main():
    objects = doc.GetActiveObjects(1)
    for obj in objects:
        c4d.CallCommand(100004768) # Select Children
        obj[c4d.ID_BASEOBJECT_GENERATOR_FLAG]=False
        obj[c4d.ID_BASEOBJECT_VISIBILITY_EDITOR] = 1
        obj[c4d.ID_BASEOBJECT_VISIBILITY_RENDER] = 1

    c4d.EventAdd()

if __name__=='__main__':
    main()