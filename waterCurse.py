from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()

count=0
while count<60:
    pos =mc.player.getPos()
    mc.setBlock(pos.x,pos.y,pos.z,8)
    count+=1
    time.sleep(0.5)