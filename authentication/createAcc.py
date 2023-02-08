import firebase_admin
from firebase_admin import credentials, firestore, auth

cred = credentials.ApplicationDefault()

default_app = firebase_admin.initialize_app(cred)

def createAcc(email, password, display_name):
    user = auth.create_user(
        email=email,
        email_verified=False,
        password=password,
        display_name=display_name,
        disabled=False
    )
