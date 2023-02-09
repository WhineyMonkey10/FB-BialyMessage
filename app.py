import customtkinter as ctk
from authentication.customAuth.firebaseCustom.database import *
from authentication.customAuth.firebaseCustom.encrypt import *

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("600x400")


def chatGUI():

    def chat(message):
        print(message)

    def addMessageToFrame(message):
        # Add a label to the scrollable frame with the message
        ctk.CTkLabel(master=scrollable_frame, text=message).pack()

    frame = ctk.CTkFrame(master=root)
    frame.pack(fill="both", expand=True)


    # Make an input field for the user to type in, and a button to send the message by calling the chat function
    input_field = ctk.CTkEntry(master=frame)
    input_field.pack(padx=30, pady=5)

    send_button = ctk.CTkButton(master=frame, text="Send", command=lambda: addMessageToFrame(input_field.get()))
    send_button.pack(pady=0, padx=250, anchor="w")

    # Make a scrollable frame to display the messages, and a scrollbar to scroll through the messages
    scrollable_frame = ctk.CTkScrollableFrame(master=root)
    scrollable_frame.pack(fill="both", expand=True)
    
def loginGUI():
    
    def login(username, password):
        if Auth.checkUser(username, username):
            frame.destroy()
            chatGUI()
        elif Auth.checkUser(username, username) == False:
            pass
        
    
    
    

    frame = ctk.CTkFrame(master=root)
    frame.pack(fill="both", expand=True)
    
    username = ctk.CTkEntry(master=frame, placeholder_text="Username")
    password = ctk.CTkEntry(master=frame, placeholder_text="Password")
    
    username.pack(padx=30, pady=5)
    password.pack(padx=30, pady=5)
    
    loginButton = ctk.CTkButton(master=frame, text="Login", command=lambda: login(username.get(), password.get()))
    
    loginButton.pack(padx=30, pady=5)


loginGUI()


root.mainloop()