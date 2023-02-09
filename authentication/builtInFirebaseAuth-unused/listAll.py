import firebase_admin
from firebase_admin import credentials, firestore, auth

cred = credentials.ApplicationDefault()

default_app = firebase_admin.initialize_app(cred)

def listAll():

    page = auth.list_users()
    while page:
        for user in page.users:
            print('User: ' + user.uid)
        # Get next batch of users.
        page = page.get_next_page()
    
    # Iterate through all users. This will still retrieve users in batches,
    # buffering no more than 1000 users in memory at a time.
    for user in auth.list_users().iterate_all():
        print('User: ' + user.uid)