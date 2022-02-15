from mcpi.minecraft import Minecraft
mc=Minecraft.create()

def sortPair(val1,val2):
    if val1>val2:
        return val2,val1
    else:
        return val1,val2

def copyStructure(x1,y1,z1,x2,y2,z2):
    x1,x2=sortPair(x1,x2)
    