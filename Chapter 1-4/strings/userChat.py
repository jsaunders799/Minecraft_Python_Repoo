from mcpi.minecraft import Minecraft
mc = Minecraft.create()
username = input ("Please enter username: ")
message = input ("enter your message: ")
mc.postToChat(username+" : "+message)

