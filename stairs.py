from mcpi.minecraft import Minecraft
mc=Minecraft.create()

pos=mc.player.getTilePos()
x,y,z=pos.x,pos.y,pos.z

stairBlock=156

for step in range(1000):
    mc.setBlock(x+step,y+step,z,stairBlock)
    