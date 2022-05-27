class User:
    def __init__(self, db, UID, email):
        self.db = db
        self.UID = UID
        self.email = email
    
    # def createUserInfo(self):
    #     if self.getUserInfo() is None:
    #         data={'username': '', 'pin': '', 'notification': True, 'e-wallet': 0, 'cars':'', 'cards':'', 'history':''}
    #         self.db.child('users').child(self.UID).set(data)
    #         return True
    #     else:
    #         return False
    def getUID(self):
        return self.UID

    def getEmail(self):
        return self.email

    def getUserInfo(self):
        try:
            userInfo = self.db.child('users').child(self.UID).get().val()
            return userInfo
        except:
            raise SystemError("UserInfo does not exists")

    def setUsername(self, username):
        try:
            self.db.child('users').child(self.UID).update({'username': username})
            return True
        except:
            raise SystemError("Can't set username")
    
    def setPin(self, pin):
        try:
            self.db.child('users').child(self.UID).update({'pin': pin})
            return True
        except:
            raise SystemError("Can't set pin")
    
    def setNotification(self, bool):
        try:
            self.db.child('users').child(self.UID).update({'notification': bool})
            return True
        except:
            raise SystemError("Can't set notification")
    
    def setMoney(self, money):
        try:
            self.db.child('users').child(self.UID).update({'money': money})
            return True
        except:
            raise SystemError("Can't set money")

    def addCar(self, car):
        try:
            self.db.child('users').child(self.UID).child('cars').push(car)
            return True
        except:
            raise SystemError("Can't add car")

    def addCard(self, card):
        try:
            self.db.child('users').child(self.UID).child('cards').push(card)
            return True
        except:
            raise SystemError("Can't add card")
    
    def addHistory(self, history):
        try:
            self.db.child('users').child(self.UID).child('histories').push(history)
            return True
        except:
            raise SystemError("Can't add history")

    # def setHistory(self, history):
    #     try:
    #         self.db.child('users').child(self.UID).update({'history': history})
    #         return True
    #     except:
    #         raise SystemError("Can't set history")
    
    def getUsername(self):
        try:
            userInfo = self.getUserInfo()
            return userInfo['username']
        except:
            raise SystemError("Can't get username")
    
    def getPin(self):
        try:
            userInfo = self.getUserInfo()
            return userInfo['pin']
        except:
            raise SystemError("Can't get pin")
    
    def getNotification(self):
        try:
            userInfo = self.getUserInfo()
            return userInfo['notification']
        except:
            raise SystemError("Can't get notification")
    
    def getMoney(self):
        try:
            userInfo = self.getUserInfo()
            return userInfo['money']
        except:
            raise SystemError("Can't get money")
    
    def getCars(self):
        try:
            userInfo = self.getUserInfo()
            return userInfo['cars']
        except:
            raise SystemError("Can't get cars")
    
    def getCards(self):
        try:
            userInfo = self.getUserInfo()
            return userInfo['cards']
        except:
            raise SystemError("Can't get cards")
    
    def getHistory(self):
        try:
            userInfo = self.getUserInfo()
            return userInfo['histories']
        except:
            raise SystemError("Can't get histories")
    
    def deleteAttribute(self, attribute):
        self.db.child('users').child(self.UID).child(attribute).remove()
    
    def topUptoE_Wallet(self, amount):
        currentMoney = self.getMoney()
        currentMoney += amount
        self.setMoney(currentMoney)
