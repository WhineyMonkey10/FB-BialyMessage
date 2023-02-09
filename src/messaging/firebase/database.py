# Imports

import firebase_admin
from firebase_admin import firestore, credentials
from google.cloud import storage
import datetime
import colorama

# Authenticate with ADC

def auth(projectid):
    cred = credentials.ApplicationDefault()
    firebase_admin.initialize_app(cred, {
    'projectId': projectid
    })
readMessages = []
auth("bialymessage")

db = firestore.client()



class Message:
    def __init__(self) -> None:
        pass
    def sendMessage(message, user):
        messageContent = {
            u'message': u"{}".format(message),
            u'user': u"{}".format(user),
            u'date': u"{}".format(datetime.datetime.now().strftime("%Y-%m-%d")),
        }

        db.collection(u'messages').add(messageContent)
        
    def getMessages():
        docs = db.collection(u'messages').stream()
        for doc in docs:
            print(f'{doc.id} => {doc.to_dict()}')
            
    def getMessage(id):
        doc = db.collection(u'messages').document(id).get()
        print(f'{doc.id} => {doc.to_dict()}')
    
    def getMessagebyMessageValue(message):
        docs = db.collection(u'messages').where(u'message', u'==', message).stream()
        for doc in docs:
            print(f'{doc.id} => {doc.to_dict()}')
    
    def UnreadablereadMessages():
        docs = db.collection(u'messages').stream()
        for doc in docs:
            if doc.id not in readMessages:
                print(f'{doc.id} => {doc.to_dict()}')
                readMessages.append(doc.id)
                #db.collection(u'messages').document(doc.id).delete()
                
    def readMessages():
        docs = db.collection(u'messages').stream()
        for doc in docs:
            if doc.id not in readMessages:
                messageContent = doc.to_dict()
                
                message = messageContent['message']
                userSent = messageContent['user']
                
                date = messageContent['date']
                

                print(f'{colorama.Fore.GREEN}{date}{colorama.Fore.RESET} {colorama.Fore.BLUE}{userSent}{colorama.Fore.RESET}: {message}')
                readMessages.append(doc.id)
                #db.collection(u'messages').document(doc.id).delete()