from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = -3.5
y = 1
z = 70.8

gift = mc.getBlock(x, y, z)
if gift != 0:
    if gift == 57:
        mc.setBlock(-4.6, 1, 69.7, 0)
        mc.setBlock(-4.6, 0, 69.7, 0)
    else:
        
        mc.setBlock(-2.6, -1, 69.7, 10)
    
else:
    mc.postToChat("Place an offering on the pedestal.")
    
