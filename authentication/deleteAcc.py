import firebase_admin
from firebase_admin import credentials, firestore, auth

cred = credentials.ApplicationDefault()

default_app = firebase_admin.initialize_app(cred)

def deleteAcc(uid):
    auth.delete_user(uid)
