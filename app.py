import customtkinter as ctk
from authentication.customAuth.firebaseCustom.database import *
from src.messaging.firebase.noinit import *
import time

# Session data
Gusername = []

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("600x400")

def chatGUI():

    def addMessageToFrame(message):
        # Add a label to the scrollable frame with the message
        ctk.CTkLabel(master=scrollable_frame, text=message).pack()
    
    def chat(message):
        input_field.option_clear()
        Message.sendMessage(message, username)

    frame = ctk.CTkFrame(master=root)
    frame.pack(fill="both", expand=True)
    
    username = " ".join(Gusername) 
    username = username.replace("[", "")
    username = username.replace("]", "")
    username = username.replace("'", "")
    
    usernameLabel = ctk.CTkLabel(master=frame, text="Username: {}".format(username))
    usernameLabel.pack(pady=5, padx=5, anchor="w")
    
    input_field = ctk.CTkEntry(master=frame)
    input_field.pack(padx=30, pady=5)

    send_button = ctk.CTkButton(master=frame, text="Send", command=lambda: chat(input_field.get()))
    send_button.pack(pady=0, padx=250, anchor="w")

    scrollable_frame = ctk.CTkScrollableFrame(master=root)
    scrollable_frame.pack(fill="both", expand=True)
    
    # Repeat this every 0.1 seconds, using the root.after method
    def repeat():
        root.after(200, repeat)
        messageContent = Message.UnreadablereadMessages()
        user = "user"
        message = "message"
        
        if messageContent != None:
            addMessageToFrame(f"{messageContent[user]} : {messageContent[message]}")
        elif messageContent == None:
            pass
        
    repeat()
        
def loginGUI():
    
    def login(username, password):
        error.configure(text="")
        if Auth.checkUser(username, password):
            Gusername.append(username)
            frame.destroy()
            chatGUI()
            

        elif Auth.checkUser(username, username) == False:
            error.configure(text="Incorrect username or password")
    
    

    frame = ctk.CTkFrame(master=root)
    frame.pack(fill="both", expand=True)
    
    username = ctk.CTkEntry(master=frame, placeholder_text="Username")
    password = ctk.CTkEntry(master=frame, placeholder_text="Password")
    error = ctk.CTkLabel(master=frame, text="")
    
    
    
    error.pack(padx=30, pady=6)
    username.pack(padx=30, pady=5)
    password.pack(padx=30, pady=5)
    
    loginButton = ctk.CTkButton(master=frame, text="Login", command=lambda: login(username.get(), password.get()))
    
    loginButton.pack(padx=30, pady=5)


def adminGUI():
    frame = ctk.CTkFrame(master=root)
    frame.pack(fill="both", expand=True)
    
    def createAccount(username, password):
        Auth.createUser(username, password)
        confirmMessage.configure(text="Account created")
        
    def deleteAccount(username):
        Auth.deleteUser(username)
        confirmMessage.configure(text="Account deleted")
        
    username = ctk.CTkEntry(master=frame, placeholder_text="Username")
    password = ctk.CTkEntry(master=frame, placeholder_text="Password")
    
    createAccountButton = ctk.CTkButton(master=frame, text="Create Account", command=lambda: createAccount(username.get(), password.get()))
    deleteAccountButton = ctk.CTkButton(master=frame, text="Delete Account", command=lambda: deleteAccount(username.get()))
    
    confirmMessage = ctk.CTkLabel(master=frame, text="")
    
    username.pack(padx=30, pady=5)
    password.pack(padx=30, pady=5)
    
    createAccountButton.pack(padx=30, pady=5)
    deleteAccountButton.pack(padx=30, pady=5)
    
    confirmMessage.pack(padx=30, pady=5)

loginGUI()


root.mainloop()