from mcpi.minecraft import Minecraft
mc=Minecraft.create()

import time

blocks=[]

while True:
    hits=mc.events.pollBlockHits()
    if len(hits)>0:
        hit=hits[0]
        hitX,hitY,hitZ=hit.pos.x,hit.pos.y,hit.pos.z
        block=mc.getBlock(hitX,hitY,hitZ)
        blocks.append(block)
        
    #Add the if statement here
    if 57 in blocks:
        mc.postToChat("You have found Diamond!")
        break
        



    time.sleep(0.2)
