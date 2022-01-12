from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random
def growTree(x, y, z):
    mc.setBlocks(x,y,z,x,y+5,z,17)
    mc.setBlocks(x-3,y+7,z-3,x+3,y+6,z+3,18)
    mc.setBlocks(x-2,y+8,z-2,x+2,y+7,z+2,18)
    mc.setBlocks(x-1,y+9,z-1,x+1,y+8,z+1,18)
  
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

growTree(x+1, y, z)
growTree(x+random.randint(0,5),y,z)
growTree(x+random.randint(6,10),y,z)