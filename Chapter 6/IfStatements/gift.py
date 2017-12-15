from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = 10
y = 11
z = 12

gift = mc.getBlock(x, y, z)
if gift == int(57):
    mc.postToChat('Thanks for the diamond')
elif gift == int(6):
    mc.postToChat('Thanks for the sapling')
else:
    mc.postToChat('Bring a gift to ' + str(x) + ", " + str(y) + ", " + str(z) + ".")
    
