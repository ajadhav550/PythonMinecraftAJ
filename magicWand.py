from mcpi.minecraft import Minecraft
mc=Minecraft.create()

import time
count=0
while count<61:
    time.sleep(1)
    mc.postToChat(count)
    count+=1

hits=mc.events.pollBlockHits()
block=103

for hit in hits:
    x,y,z=hit.pos.x,hit.pos.y,hit.pos.z
    mc.setBlock(x,y,z,147)