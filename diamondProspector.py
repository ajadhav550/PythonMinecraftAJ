from mcpi.minecraft import Minecraft
mc=Minecraft.create()
pos=mc.player.getTilePos()
x,y,z=pos.x,pos.y,pos.z
for num in range(50):
    block=mc.getBlock(x,y-num,z)
    if block==56:
        mc.postToChat("The ore is {} below you".format(num))