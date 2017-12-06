from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = 10
y = 11
z = 12
melon = 103
block = mc.getBlock(x, y, z)

nonMelon = melon != block

mc.postToChat('You need ot get some food : ' + str(nonMelon))
