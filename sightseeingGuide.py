from mcpi.minecraft import Minecraft
mc=Minecraft.create()

places={'Living room':(76,1,-61),'Bedroom':(61,9,-61)}

choice=""
while choice!="exit":
    choice=input("Enter a location('exit'to close):")
    if choice in places:
        location=places[choice]
        x,y,z=location[0],location[1],location[2]
        mc.player.setTilePos(x,y,z)