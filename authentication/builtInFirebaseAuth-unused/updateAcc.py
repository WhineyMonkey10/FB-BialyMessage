import firebase_admin
from firebase_admin import credentials, firestore, auth

cred = credentials.ApplicationDefault()

default_app = firebase_admin.initialize_app(cred)

def updateDisplayName(display_name, uid):
    user = auth.update_user(
        uid,
        display_name=display_name
    )
    