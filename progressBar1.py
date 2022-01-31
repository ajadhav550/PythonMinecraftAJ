from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

pos = mc.player.getTilePos()
x = pos.x+1
y = pos.y
z = pos.z

# Add 10 glass blocks (ID 20) to this emty list
count2=0
blocks=[]

while count2<=20:
    blocks.append(20)
    count2+=1

barBlock = 22 #Lapis lazuli

count = 0
while count <= len(blocks):
    
    mc.setBlock(x,y,z,blocks[0])
    mc.setBlock(x,y+1,z,blocks[1])
    mc.setBlock(x,y+2,z,blocks[2])
    mc.setBlock(x,y+3,z,blocks[3])
    mc.setBlock(x,y+4,z,blocks[4])
    mc.setBlock(x,y+5,z,blocks[5])
    mc.setBlock(x,y+6,z,blocks[6])
    mc.setBlock(x,y+7,z,blocks[7])
    mc.setBlock(x,y+8,z,blocks[8])
    mc.setBlock(x,y+9,z,blocks[9])
    
    count+=1
    
    del blocks[9]
    blocks.insert(0,barBlock)
    
    # Insert a lapis lazuli block at the first position in the list
    
    time.sleep(2)