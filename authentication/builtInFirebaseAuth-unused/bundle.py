from createAcc import *
from deleteAcc import *
from listAll import *
from updateAcc import *

class Authentication:
    def __init__(self):
        pass

    def createAcc(self, email, password, display_name):
        try:
            createAcc(email, password, display_name)
            return True
        except Exception as e:
            print(e)
            return False
    def deleteAcc(self, uid):
        try:
            deleteAcc(uid)
            return True
        except Exception as e:
            print(e)
            return False
    def listAll(self):
        try:
            listAll()
            return True
        except Exception as e:
            print(e)
            return False

    def updateAcc(self, uid, display_name):
        try:
            updateDisplayName(uid, display_name)
            return True
        except Exception as e:
            print(e)
            return False