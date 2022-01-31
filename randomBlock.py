from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import random
blockIDs=[1,22,41,57]
block=random.choice(blockIDs)
pos=mc.player.getTilePos()
mc.setBlock(pos.x,pos.y,pos.z+1,block)