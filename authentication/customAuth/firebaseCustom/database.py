# Imports

import firebase_admin
from firebase_admin import firestore, credentials
from google.cloud import storage
import datetime
import colorama
import base64

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
    
    def encrypt(string):
        encryptBytes = string.encode("ascii")
        encryptString = base64.b64encode(encryptBytes)
        encryptString = encryptString.decode("ascii")
        return encryptString
    
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
                u'password': u"{}".format(Auth.encrypt(password)),
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
        if db.collection(u'users').document(username).get().exists:
            if Auth.getUserbyUsername(username)[1] == Auth.encrypt(password):
                if username == "admin":
                    return "admin"
                else:
                    return True
            else:
                return False
        else:
            return False