from src.messaging.firebase.database import *

class Application:
        def __init__(self) -> None:
                pass
            
        def readMessages():
                try:
                        Message.readMessages()
                        return True
        
                except Exception as e:
                        print(e)
                        print("Error reading message")
                        return False
                
        def sendMessage(message, user):
                try:   
                        Message.sendMessage(message, user)
                        return True
                except Exception as e:
                        print(e)
                        print("Error sending message")
                        return False
        