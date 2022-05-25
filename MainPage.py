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
        
        # Home Page -------------------------------------------------------------------------------------------------------
        self.ui.topupPushButton.clicked.connect(self.gotoTopupPage)

        # History Page ----------------------------------------------------------------------------------------------------
        historyTest = [{'company':'PTT', 'price':1000, 'duration':30, 'timestamp':'000:000'},
                        {'company':'PTT', 'price':1000, 'duration':30, 'timestamp':'000:000'},
                        {'company':'PTT', 'price':1000, 'duration':30, 'timestamp':'000:000'},
                        {'company':'PTT', 'price':1000, 'duration':30, 'timestamp':'000:000'},
                        {'company':'PTT', 'price':1000, 'duration':30, 'timestamp':'000:000'},
                        {'company':'PTT', 'price':1000, 'duration':30, 'timestamp':'000:000'},
                        {'company':'PTT', 'price':1000, 'duration':30, 'timestamp':'000:000'},
                        {'company':'PTT', 'price':1000, 'duration':30, 'timestamp':'000:000'},
                        {'company':'PTT', 'price':1000, 'duration':30, 'timestamp':'000:000'},
                        {'company':'PTT', 'price':1000, 'duration':30, 'timestamp':'000:000'},
                        {'company':'PTT', 'price':1000, 'duration':30, 'timestamp':'000:000'},
                        {'company':'PTT', 'price':1000, 'duration':30, 'timestamp':'000:000'},
                        {'company':'PTT', 'price':1000, 'duration':30, 'timestamp':'000:000'},
                        {'company':'PTT', 'price':1000, 'duration':30, 'timestamp':'000:000'},
                        {'company':'PTT', 'price':1000, 'duration':30, 'timestamp':'000:000'}]
        self.addHistoryList(historyTest)

        # Location Page -------------------------------------------------------------------------------------------------
        # Open EV station locations
        self.openStationLocations()

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

        # Handle Change Pin Settings
        self.ui.changepinPushButton.clicked.connect(self.handleChangePin)

        # Handle Change Password Settings
        self.ui.changepasswordPushButton.clicked.connect(self.handleChangePassword)

        # Handle Logout
        self.ui.logoutPushButton.clicked.connect(self.handleLogout)

        # Top-Up Page -----------------------------------------------------------------------------------------------
        self.ui.pushButton_0.clicked.connect(lambda: self.addNumbertoTopUp("0"))
        self.ui.pushButton_1.clicked.connect(lambda: self.addNumbertoTopUp("1"))
        self.ui.pushButton_2.clicked.connect(lambda: self.addNumbertoTopUp("2"))
        self.ui.pushButton_3.clicked.connect(lambda: self.addNumbertoTopUp("3"))
        self.ui.pushButton_4.clicked.connect(lambda: self.addNumbertoTopUp("4"))
        self.ui.pushButton_5.clicked.connect(lambda: self.addNumbertoTopUp("5"))
        self.ui.pushButton_6.clicked.connect(lambda: self.addNumbertoTopUp("6"))
        self.ui.pushButton_7.clicked.connect(lambda: self.addNumbertoTopUp("7"))
        self.ui.pushButton_8.clicked.connect(lambda: self.addNumbertoTopUp("8"))
        self.ui.pushButton_9.clicked.connect(lambda: self.addNumbertoTopUp("9"))
        self.ui.pushButton_delete.clicked.connect(lambda: self.deleteNumberfromTopUp())
        self.ui.pushButton_dot.clicked.connect(lambda: self.addNumbertoTopUp("."))
    
    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////
    def getPinResult(self):
        return self.pinResult
    
    def setPinResult(self, boolean):
        self.pinResult = boolean

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
        pin_page = Pin_Page(self.auth, self.widget, self.user, index, self.isAutoLogin, self)
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
        if self.getPinResult():
            self.setPinResult(False)
            return True
        return False
        
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
    
    def showAlert(self, text):
        dialog = QDialog(self)
        layout = QVBoxLayout()
        label = QLabel(self)
        label.setText(text)
        layout.addWidget(label)
        dialog.setLayout(layout)
        dialog.show()
    
    # Home Page functions -----------------------------------------------------------------------------------------------
    def hiUserLabel(self):
        username = User.getUsername
        if username:
            return username
        else:
            return self.auth.current_user['email']
    
    def gotoTopupPage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.topupPage)
        self.refreshTopupPage()
    
    def refreshTopupPage(self):
        self.ui.topupvalueLineEdit.setText("")
    
    # History Page functions ---------------------------------------------------------------------------------------------
    def addHistoryList(self, historyList):
        for history in historyList:
            self.ui.historyVerticalLayout.addWidget(self.createHistoryPushButton(history))
        self.ui.historyVerticalLayout.addStretch(1)
    
    def createHistoryPushButton(self, history):
        historyPushButton = QPushButton()
        historyPushButton.setText(f"{history.get('company')}\nPrice: {history.get('price')}\nDuration: {history.get('duration')}\nTimestamp: {history.get('timestamp')}")
        return historyPushButton
    
    # Location Page functions ------------------------------------------------------------------------------------------------
    def openStationLocations(self):
        layout = QVBoxLayout()
        web = QWebEngineView()
        web.load(QUrl("https://www.plugshare.com/"))
        layout.addWidget(web)
        self.ui.locationWidget.setLayout(layout)
    
    # Account Page functions --------------------------------------------------------------------------------------------------
    def toggleNotificationWidget(self):
        if self.ui.notificationWidget.isVisible():
            self.ui.notificationWidget.setVisible(False)
            self.ui.notificationPushButton.setIcon(QIcon("images\\right-arrow.png"))
        else:
            self.ui.notificationWidget.setVisible(True)
            self.ui.notificationPushButton.setIcon(QIcon("images\\down-arrow.png"))
            if self.user.getNotification:
                self.ui.opennotificationRadioButton.setChecked(True)
            else:
                self.ui.closenotificationRadioButton.setChecked(True)
    
    def toggleAddCarWidget(self):
        if self.ui.addcarWidget.isVisible():
            self.ui.addcarWidget.setVisible(False)
            self.ui.addcarPushButton.setIcon(QIcon("images\\right-arrow.png"))
        else:
            self.ui.addcarWidget.setVisible(True)
            self.ui.addcarPushButton.setIcon(QIcon("images\\down-arrow.png"))
    
    def toggleAddCardWidget(self):
        if self.ui.addcardWidget.isVisible():
            self.ui.addcardWidget.setVisible(False)
            self.ui.addcardPushButton.setIcon(QIcon("images\\right-arrow.png"))
        else:
            self.ui.addcardWidget.setVisible(True)
            self.ui.addcardPushButton.setIcon(QIcon("images\\down-arrow.png"))
    
    def toggleChangeUsernameWidget(self):
        if self.ui.changeusernameWidget.isVisible():
            self.ui.changeusernameWidget.setVisible(False)
            self.ui.changeusernamePushButton.setIcon(QIcon("images\\right-arrow.png"))
        else:
            self.ui.changeusernameWidget.setVisible(True)
            self.ui.changeusernamePushButton.setIcon(QIcon("images\\down-arrow.png"))
    
    def wait_object_destruction(self, my_object):
        loop = QEventLoop()
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
    
    def handleChangePin(self):
        if self.gotoPinPage(4):
            if self.gotoPinPage(1):
                self.showAlert("Pin has been changed")
            else:
                self.showAlert("Invalid Pin input")
    
    def handleChangePassword(self):
        if self.gotoPinPage(3):
            self.auth.send_password_reset_email(self.email)
            self.showAlert("Reset password has been sent to email")
    
    def handleLogout(self):
        if self.gotoPinPage(3):
            self.widget.removeWidget(self.widget.currentWidget())
            # self.widget.setCurrentIndex(2)
            print("logged out")
    
    # TopUp Page functions ----------------------------------------------------------------------------------------------
    def addNumbertoTopUp(self, str):
        topupStr = self.ui.topupvalueLineEdit.text()

        if "." in topupStr and str == ".":
            print("Can't add 2 dots")
        else:
            topupStr += str
            if float(topupStr) <= 200000:
                self.ui.topupvalueLineEdit.setText(topupStr)
            else:
                print("Value can't be over 200000")
        return
    
    def deleteNumberfromTopUp(self):
        topupStr = self.ui.topupvalueLineEdit.text()
        if topupStr is not empty:
            self.ui.topupvalueLineEdit.setText(topupStr[:-1])
        




        