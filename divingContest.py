from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time

score=0
pos=mc.player.getPos()
blockAbove = mc.getBlock(pos.x,pos.y+2,pos.z)

while blockAbove==8 or blockAbove==9:
    time.sleep(1)
    pos=mc.player.getPos()
    blockAbove=mc.getBlock(pos.x,pos.y+2,pos.z)
    score+=1
    mc.postToChat("Current score: "+str(score))
    
mc.postToChat("Final score: "+str(score))

if score>6 and score<10:
    finalPos=mc.player.getTilePos()
    mc.setBlocks(finalPos.x-5,finalPos.y+10,finalPos.x-5,finalPos.x+5,finalPos.y+10, finalPos.z+5,38)
elif score>=10 and score<18:
    finalPos=mc.player.getTilePos()
    mc.setBlocks(finalPos.x-5,finalPos.y+10,finalPos.x-5,finalPos.x+5,finalPos.y+10, finalPos.z+5,41)
elif score>=18:
    finalPos=mc.player.getTilePos()
    mc.setBlocks(finalPos.x-5,finalPos.y+10,finalPos.x-5,finalPos.x+5,finalPos.y+10, finalPos.z+5,57)