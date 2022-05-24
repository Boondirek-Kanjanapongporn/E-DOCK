from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWebEngineWidgets import *
import time
from main import Ui_Form as Ui_Main
from User import User
from PinPage import Pin_Page

class Main_Page(QWidget):
    def __init__(self, db, auth, widget, isAutoLogin):
        QWidget.__init__(self, None)
        self.db = db
        self.auth = auth
        self.widget = widget
        self.isAutoLogin = isAutoLogin
        self.pinResult = False

        self.UID = self.auth.current_user['localId']
        self.email = self.auth.current_user['email']
        
        self.user = User(self.db, self.UID, self.email)

        self.ui = Ui_Main()
        self.ui.setupUi(self)

        # create Pin on first account creation
        self.createPin()

        # goto Pages in Navbar
        self.ui.homePushButton.clicked.connect(self.gotoHomePage)
        self.ui.historyPushButton.clicked.connect(self.gotoHistoryPage)
        self.ui.locationPushButton.clicked.connect(self.gotoLocationPage)
        self.ui.accountPushButton.clicked.connect(self.gotoAccountPage)

        # Set default
        self.refreshHomePage()
        self.refreshHistoryPage()
        self.refreshLocationPage()
        self.refreshAccountPage()

        # Open EV station locations
        self.openStationLocations()
        
        # Home Page
        # History Page
        #Location Page

        # Account Page -----------------------------------------------------------------------------------------
        # Toggle Open/Close Settings
        self.ui.notificationPushButton.clicked.connect(self.toggleNotificationWidget)
        self.ui.addcarPushButton.clicked.connect(self.toggleAddCarWidget)
        self.ui.addcardPushButton.clicked.connect(self.toggleAddCardWidget)
        self.ui.changeusernamePushButton.clicked.connect(self.toggleChangeUsernameWidget)

        # Handle Notification Settings
        self.ui.opennotificationRadioButton.clicked.connect(lambda: self.user.setNotification(True))
        self.ui.closenotificationRadioButton.clicked.connect(lambda: self.user.setNotification(False))

        # Handle Add Car Settings
        self.ui.addcarPushButton_2.clicked.connect(self.handleAddCar)

        # Handle Add Card Settings
        self.ui.addcardPushButton_2.clicked.connect(self.handleAddCard)

        # Handle Change Username Settings
        self.ui.changeusernamePushButton_2.clicked.connect(self.handleChangeUsername)

        # Handle Change Password Settings
        self.ui.changepasswordPushButton.clicked.connect(self.handleChangePassword)

        # Handle Logout
        self.ui.logoutPushButton.clicked.connect(self.handleLogout)
    
        # ------------------------------------------------------------------------------------------------------
    def createPin(self):
        userinfo = self.db.child('users').child(self.UID).get()
        if userinfo.val() is not None:
            if self.user.getPin() == '':
                self.gotoPinPage(1, True)
            else:
                return True
        else:
            raise SystemError('User Database does not Exist')

    def gotoPinPage(self, index, isCreatePin=False):
        pin_page = Pin_Page(self.widget, self.user, index, self.isAutoLogin, self)
        self.widget.addWidget(pin_page)
        if isCreatePin:
            if self.isAutoLogin:
                self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
            else:
                self.widget.setCurrentIndex(self.widget.currentIndex() + 2)
        else:
            if self.isAutoLogin:
                self.widget.setCurrentIndex(self.widget.currentIndex() + 3)
            else:
                self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
            # Wait for Pin Page to close
            self.wait_object_destruction(pin_page)
            if self.getPinResult() == True:
                self.setPinResult(False)
                return True
            return False
    
    def getPinResult(self):
        return self.pinResult
    
    def setPinResult(self, boolean):
        self.pinResult = boolean
        
    def gotoHomePage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.homePage)
        self.refreshHomePage()
    
    def gotoHistoryPage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.historyPage)
        self.refreshHistoryPage()

    def gotoLocationPage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.locationPage)
        self.refreshLocationPage()

    def gotoAccountPage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.accountPage)
        self.refreshAccountPage()
    
    def refreshHomePage(self):
        username = self.user.getUsername()

        if username:
            self.ui.hiLabel.setText(f"Hi, {username}")
        else:
            self.ui.hiLabel.setText(f"Hi, {self.email}")

    def refreshHistoryPage(self):
        pass

    def refreshLocationPage(self):
        pass

    def refreshAccountPage(self):
        self.ui.notificationWidget.setVisible(False)
        self.ui.addcarWidget.setVisible(False)
        self.ui.addcardWidget.setVisible(False)
        self.ui.changeusernameWidget.setVisible(False)
    
    def toggleNotificationWidget(self):
        if self.ui.notificationWidget.isVisible():
            self.ui.notificationWidget.setVisible(False)
        else:
            self.ui.notificationWidget.setVisible(True)
            if self.user.getNotification:
                self.ui.opennotificationRadioButton.setChecked(True)
            else:
                self.ui.closenotificationRadioButton.setChecked(True)
    
    def toggleAddCarWidget(self):
        if self.ui.addcarWidget.isVisible():
            self.ui.addcarWidget.setVisible(False)
        else:
            self.ui.addcarWidget.setVisible(True)
    
    def toggleAddCardWidget(self):
        if self.ui.addcardWidget.isVisible():
            self.ui.addcardWidget.setVisible(False)
        else:
            self.ui.addcardWidget.setVisible(True)
    
    def toggleChangeUsernameWidget(self):
        if self.ui.changeusernameWidget.isVisible():
            self.ui.changeusernameWidget.setVisible(False)
        else:
            self.ui.changeusernameWidget.setVisible(True)
    
    def wait_object_destruction(self, my_object):
        loop = QEventLoop()
        name = my_object.objectName()
        my_object.destroyed.connect(loop.quit)
        loop.exec_()
        return None
    
    def handleAddCar(self):
        if self.gotoPinPage(3):
            userinfo = self.db.child('users').child(self.UID).get()
            if userinfo.val() is not None:
                company = self.ui.companyLineEdit.text()
                model = self.ui.modelLineEdit.text()
                batteryCapacity = self.ui.batterycapacityLineEdit.text()
                chargingCapacity = self.ui.chargingcapacityLineEdit.text()
                timestamp = time.time()

                if company != "" and model != "" and batteryCapacity != "" and chargingCapacity != "" and not company.isspace() and not model.isspace() and not batteryCapacity.isspace() and not chargingCapacity.isspace():
                    newCar = {'company': company, 'model': model, 'batterCapacity': batteryCapacity, 'chargingCapacity': chargingCapacity, 'timestamp': timestamp}
                    try:
                        self.user.addCar(newCar)
                        self.showAlert("New car added")
                    except:
                        self.showAlert("Can't add car")
                else:
                    self.showAlert("Invalid car input")
            else:
                raise SystemError('User Database does not Exist')
    
    def handleAddCard(self):
        if self.gotoPinPage(3):
            userinfo = self.db.child('users').child(self.UID).get()

            if userinfo.val() is not None:
                cardNumber = self.ui.cardnumberLineEdit.text()
                cardHolderName = self.ui.cardholdernameLineEdit.text()
                expiry = self.ui.expiryLineEdit.text()
                cvv = self.ui.cvvLineEdit.text()
                timestamp = time.time()

                if cardNumber != "" and cardHolderName != "" and expiry != "" and cvv != "" and not cardNumber.isspace() and not cardHolderName.isspace() and not expiry.isspace() and not cvv.isspace():
                    newCard = {'cardNumber': cardNumber, 'cardHolderName': cardHolderName, 'expiry': expiry, 'cvv': cvv, 'timestamp': timestamp}
                    try:
                        self.user.addCard(newCard)
                        self.showAlert("New card added")
                    except:
                        self.showAlert("Can't add card")
                else:
                    self.showAlert("Invalid card input")
            else:
                raise SystemError('User Database does not Exist')

    def handleChangeUsername(self):
        if self.gotoPinPage(3):
            userinfo = self.db.child('users').child(self.UID).get()

            if userinfo.val() is not None:
                newUsername = self.ui.newusernameLineEdit.text()

                if newUsername != "" and not newUsername.isspace():
                    try:
                        self.user.setUsername(newUsername)
                        self.showAlert("Username has been changed")
                    except:
                        self.showAlert("Can't change username")
                else:
                    self.showAlert("Invalid username input")
            else:
                raise SystemError('User Database does not Exist')
    
    def handleChangePassword(self):
        if self.gotoPinPage(3):
            self.auth.send_password_reset_email(self.email)
            self.showAlert("Reset password has been sent to email")
    
    def handleLogout(self):
        if self.gotoPinPage(3):
            self.widget.removeWidget(self.widget.currentWidget())
            # self.widget.setCurrentIndex(2)
            print("logged out")

    def openStationLocations(self):
        layout = QVBoxLayout()
        web = QWebEngineView()
        web.load(QUrl("https://www.plugshare.com/"))
        layout.addWidget(web)
        self.ui.locationWidget.setLayout(layout)
    
    def hiUserLabel(self):
        username = User.getUsername
        if username:
            return username
        else:
            return self.auth.current_user['email']
    
    def showAlert(self, text):
        dialog = QDialog(self)
        layout = QVBoxLayout()
        label = QLabel(self)
        label.setText(text)
        layout.addWidget(label)
        dialog.setLayout(layout)
        dialog.show()
        




        