import c4d
#Welcome to the world of Python

def main():
    c4d.CallCommand(100004766, 100004766) # Select All
    c4d.CallCommand(100004787, 100004787) # Delete
    c4d.CallCommand(100004797, 100004797) # Select All
    c4d.CallCommand(100004735, 100004735) # Delete
    c4d.CallCommand(300001025, 300001025) # Select All
    c4d.CallCommand(300001024, 300001024) # Delete
    c4d.CallCommand(12149, 12149) # Frame Default
    c4d.CallCommand(12091, 12091) # Gouraud Shading
    c4d.CallCommand(12093, 12093) # Wireframe


if __name__=='__main__':
    main()
    c4d.EventAdd()