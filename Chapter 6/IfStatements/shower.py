from mcpi.minecraft import Minecraft
mc = Minecraft.create()

shwrX = 90
shwrY = 14
shwrZ = 82

width = 12
height = 12
length = 12

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

print ("program running")

if shwrX <= x < shwrX + width and shwrY <= y < shwrY + height and shwrZ <= z < shwrZ + length:

    mc.setBlocks(shwrX, shwrY + height, shwrZ, shwrX + width, shwrY + height, shwrZ + length, 8)
    print("raining")

else:
    mc.setBlocks(shwrX, shwrY + height, shwrZ, shwrX + width, shwrY + height, shwrZ + length, 0)
    print("not raining")

print("program ran already")
