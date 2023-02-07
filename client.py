from bundle import Application

user = input("Username: ")

while True:
    message = input("Message: ")
    Application.sendMessage(message, user)
    Application.readMessages()
