from mcpi.minecraft import Minecraft
mc = Minecraft.create()

air = 0
water = 9

while True:
    pos = mc.player.getTilePos()
    blockBelow = mc.getBlock(pos.x, pos.y - 1, pos.z)

    if blockBelow == 8 or blockBelow == 0:
        mc.setBlock(pos.x, pos.y - 1, pos.z , 41)
        
