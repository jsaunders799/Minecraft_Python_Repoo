from mcpi.minecraft import Minecraft
mc = Minecraft.create()

username = input("Please enter username: ")

while True:
    message = input("enter your message: ")
    mc.postToChat(username + " : " + message)

    if message == "exit":
        break

    
