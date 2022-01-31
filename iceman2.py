import mcpi.minecraft as minecraft
import mcpi.block as block
mc=minecraft.Minecraft.create()
while True:
    for hit in mc.events.pollBlockHits():
        mc.setBlock(hit.pos.x, hit.pos.y, hit.pos.z, block.GLASS)
mc.postToChat("Hey")