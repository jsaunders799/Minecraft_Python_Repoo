from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
highestBlockY = mc.getHeight(x, z)
if pos.y > highestBlockY:
    mc.postToChat('The player is above ground: True')

else:
    mc.postToChat('The Player is above ground: False')
