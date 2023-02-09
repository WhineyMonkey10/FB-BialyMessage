# Imports

import firebase_admin
from firebase_admin import firestore, credentials
from google.cloud import storage
import datetime
import colorama
from encrypt import encrypt

# Authenticate with ADC

def auth(projectid):
    cred = credentials.ApplicationDefault()
    firebase_admin.initialize_app(cred, {
    'projectId': projectid
    })
readMessages = []
auth("bialymessage")

db = firestore.client()



class Auth:
    def __init__(self) -> None:
        pass
    
    def createUser(username, password):
        
        if username == "":
            print("Username cannot be empty")
            return False
        
        if password == "":
            print("Password cannot be empty")
            return False
        
        if db.collection(u'users').document(username).get().exists:
            print("User already exists")
            return False
        
        elif db.collection(u'users').document(username).get().exists == False:
            
            user = {
                u'username': u"{}".format(username),
                u'password': u"{}".format(encrypt(password)),
            }
    
        db.collection(u'users').document(username).set(user)
        return True
        
    def getUser(id):
        doc = db.collection(u'users').document(id).get()
        
        username = doc.to_dict()['username']
        password = doc.to_dict()['password']
        return username, password

        
    def getUserbyUsername(username):
        doc = db.collection(u'users').document(username).get()
        username = doc.to_dict()['username']
        password = doc.to_dict()['password']
    
        return username, password
    
    def deleteUser(id):
        db.collection(u'users').document(id).delete()
        return True
        
    def deleteUserbyUsername(username):
        db.collection(u'users').document(username).delete()
        return True
    
    def checkUser(username, password):
        doc = db.collection(u'users').document(username).get()
        
        if doc.to_dict()['username'] == username:
            
            if doc.to_dict()['password'] == encrypt(password):
                return True
            else:
                return False
        else:
            return False
        
    