from mcpi.minecraft import Minecraft
mc =  Minecraft.create()

position = mc.player.getTilePos()
x = position.x
y = position.y
z = position.z

y = y + 256
mc.player.setTilePos(x, y, z, )
