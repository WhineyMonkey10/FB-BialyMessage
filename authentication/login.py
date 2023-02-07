import firebase_admin
from firebase_admin import credentials, firestore, auth

cred = credentials.RefreshToken('./authentication/config/bialymessage-firebase-adminsdk-uega3-f367c4e9d4.json')
default_app = firebase_admin.initialize_app(cred)

user = auth.get_user('wNY9OWgyeTc0QcBelkojNOatxMZ2')
print('Successfully fetched user data: {0}'.format(user.uid))