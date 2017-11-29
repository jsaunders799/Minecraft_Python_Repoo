from mcpi.minecraft import Minecraft
mc = Minecraft.create()
message = input ("enter your message: ")
mc.postToChat(message)
