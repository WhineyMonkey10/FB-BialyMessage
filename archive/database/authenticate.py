from firebase_admin import firestore, credentials
import firebase_admin



def auth(projectid):
    cred = credentials.ApplicationDefault()
    firebase_admin.initialize_app(cred, {
    'projectId': projectid
    })