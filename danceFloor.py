from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time

pos=mc.player.getTilePos()
floorX=pos.x-2
#I am big sad no one loves me 
floorY=pos.y-1
floorZ=pos.z-2
width=5
length=5
block=41
mc.setBlocks(floorX, floorY, floorZ, floorX + width, floorY, floorZ+length,block)

while floorX <= pos.x <+ floorX+width and floorZ <= pos.z <= floorZ+length:
    if block == 41:
        block = 57
    else:
        block = 41
    mc.setBlocks(floorX,floorY,floorZ, floorX+width, floorY, floorZ+length, block)
    pos = mc.player.getTilePos()
    time.sleep(0.5)
mc.setBlocks(floorX, floorY, floorZ, floorX + width, floorY, floorZ+length,0)