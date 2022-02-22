from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def sortPair(val1, val2):
    if val1 >  val2:
        return val2, val1
    else:
        return val1, val2
    
def copyStructure(x1, y1, z1, x2, y2, z2):
    x1, x2 = sortPair(x1, x2)
    y1, y2 = sortPair(y1, y2)
    z2, z2 = sortPair(z1, z2)
    
    structure = []
    stack = []
    wall =[]
    
    
    print('Please wait...')
    for z in range(z1, z2+1):
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                print(x,y,z)
                block = mc.getBlock(x,y,z)
                stack.append(block)
            wall.append(stack)
            stack = []
        structure.append(wall)
        wall=[]
    print(structure)
                                    
    
    
    return structure

def buildStructure(x, y, z, structure):
    xStart = x
    yStart = y
    zStart = z
    
    for wall in structure:
        for stack in wall:
            for block in stack:
                mc.setBlock(x,y,z,block)
                y+=1
            x+=1
            y=yStart
        z+=1
        x=xStart
                               
    
    

input('Move to the first corner and press enter in this window')
pos = mc.player.getTilePos()
x1, y1, z1 = pos.x, pos.y, pos.z


input('Move tot he opposite corner and press enter in this window')
pos = mc.player.getTilePos()
x2, y2, z2 = pos.x, pos.y, pos.z


structure = copyStructure(x1, y1, z1, x2, y2, z2)


input('Move to the posittion you want to create the structure and press ENTER in this window')
pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z
buildStructure(x,y,z,structure)