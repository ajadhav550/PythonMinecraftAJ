#import all the necessary modules
from mcpi.minecraft import Minecraft
from mcpi import block
import time

#connect with the Minecraft world
mc=Minecraft.create()

# get the player's position
pos=mc.player.getTilepos()

#check if the end of the world will engulf your creation and move you if your're too close
if pos.z<-40:
    mc.postToChat('teleporting to safer distance in progress!')
    mc.player.setpos(pos.x,pos.y,-40)
    pos=mc.player.getTilePos()
    

#mark where the teleport is
zpos+pos.z-40

# create the valley by hollowing it out with air
mc.setBlocks(pos.x-1,pos.y+3,pos.z,pos.x+1,pos.y-7, pos.z-88,block.AIR.id)

#build the invisible bedrock support
mc.setBlocks(pso.x,pso.y-1,pos.z,pos.x,
pos.y-7,pos.z,block.BEDROCK_INVISIBLE.id)
mc.setBlocks(pos.x-1,pos.y-1,pos.z,pos.x,
pos,y-7,pos.z,block.BEDROCK_INVISIBLE.id)
mc.setBlocks(pos.x,pos.y-1,pos.z-88,pos.x-1,pos.y-7,pos.z-88,block.BEDROCK_INISIBLE.id)
mc.setblocks(pos.x-1,pos.y-1,
pos.z-88,pos.x,pos.y-7,pos.z-88,
block.BEDROCK_INVISIBLE.id)
mc.setBlocks(pos.x+1,