from tkinter import messagebox
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWebEngineWidgets import *
from scb_payment import QRCodePayment
import qrcode
import datetime
from StationPage import Station_Page

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
        self.stationid = []

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
        self.ui.chargePushButton.clicked.connect(self.gotoSelectStationPage)
        self.ui.topupPushButton.clicked.connect(self.gotoTopupPage)

        # History Page ----------------------------------------------------------------------------------------------------
        
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
        self.ui.topupvaluePushButton.clicked.connect(lambda: self.generateQRCode())

        # Select Station Page ----------------------------------------------------------------------------------------
        self.ui.pushButton_0_2.clicked.connect(lambda: self.addNumbertoStationID(0))
        self.ui.pushButton_1_2.clicked.connect(lambda: self.addNumbertoStationID(1))
        self.ui.pushButton_2_2.clicked.connect(lambda: self.addNumbertoStationID(2))
        self.ui.pushButton_3_2.clicked.connect(lambda: self.addNumbertoStationID(3))
        self.ui.pushButton_4_2.clicked.connect(lambda: self.addNumbertoStationID(4))
        self.ui.pushButton_5_2.clicked.connect(lambda: self.addNumbertoStationID(5))
        self.ui.pushButton_6_2.clicked.connect(lambda: self.addNumbertoStationID(6))
        self.ui.pushButton_7_2.clicked.connect(lambda: self.addNumbertoStationID(7))
        self.ui.pushButton_8_2.clicked.connect(lambda: self.addNumbertoStationID(8))
        self.ui.pushButton_9_2.clicked.connect(lambda: self.addNumbertoStationID(9))
        self.ui.pushButton_delete_2.clicked.connect(lambda: self.deleteNumberfromStationID())
        self.ui.searchPushButton.clicked.connect(lambda: self.searchStationID())

        # Charging Station Page --------------------------------------------------------------------------------------
        self.ui.cancelPushButton.clicked.connect(self.gotoSelectStationPage)
        self.ui.confirmPushButton.clicked.connect(self.gotoStationPage)
    
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
        self.clearLayout(self.ui.historyVerticalLayout)
        try:
            historyNodes = self.user.getHistory()
            historyList = []
            for value in historyNodes.values():
                historyList.append(value)
            self.addHistoryList(historyList[::-1])
        except:
            print("No histories")
    
    def clearLayout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def refreshLocationPage(self):
        pass

    def refreshAccountPage(self):
        self.ui.moneyLabel.setText(f"{self.user.getMoney():.5f}")
        self.ui.notificationWidget.setVisible(False)
        self.ui.addcarWidget.setVisible(False)
        self.ui.addcardWidget.setVisible(False)
        self.ui.changeusernameWidget.setVisible(False)
    
    def showAlert(self, text):
        messageBox = QMessageBox(self)
        messageBox.setText(text)
        messageBox.exec()
    
    # Home Page functions -----------------------------------------------------------------------------------------------
    def hiUserLabel(self):
        username = User.getUsername
        if username:
            return username
        else:
            return self.auth.current_user['email']
    
    def gotoSelectStationPage(self):
        self.refreshSelectStationPage()
        self.ui.stackedWidget.setCurrentWidget(self.ui.selectstationPage)

    def gotoTopupPage(self):
        self.refreshTopupPage()
        self.ui.stackedWidget.setCurrentWidget(self.ui.topupPage)
    
    def refreshTopupPage(self):
        self.ui.topupvalueLineEdit.setText("")
        self.ui.moneyLabel_2.setText(f"{self.user.getMoney():.5f}")
    
    def refreshSelectStationPage(self):
        self.stationid = []
        self.ui.stationid1.setText("")
        self.ui.stationid2.setText("")
        self.ui.stationid3.setText("")
        self.ui.stationid4.setText("")
        self.ui.stationid5.setText("")
        self.ui.stationid6.setText("")

    
    # History Page functions ---------------------------------------------------------------------------------------------
    def addHistoryList(self, historyList):
        for history in historyList:
            self.ui.historyVerticalLayout.addWidget(self.createHistoryPushButton(history))
        self.ui.historyVerticalLayout.addStretch(1)
    
    def createHistoryPushButton(self, history):
        historyPushButton = QPushButton()
        historyPushButton.setText(f"{history.get('company')}\nStation ID: {history.get('stationid')}\nPrice: {history.get('price')} THB\nDuration: {history.get('duration')}\nTimestamp: {history.get('timestamp')}")
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
                timestamp = datetime.datetime.now()

                if company != "" and model != "" and batteryCapacity != "" and chargingCapacity != "" and not company.isspace() and not model.isspace() and not batteryCapacity.isspace() and not chargingCapacity.isspace():
                    newCar = {'company': company, 'model': model, 'batterCapacity': batteryCapacity, 'chargingCapacity': chargingCapacity, 'timestamp': str(timestamp)}
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
                timestamp = datetime.datetime.now()

                if cardNumber != "" and cardHolderName != "" and expiry != "" and cvv != "" and not cardNumber.isspace() and not cardHolderName.isspace() and not expiry.isspace() and not cvv.isspace():
                    newCard = {'cardNumber': cardNumber, 'cardHolderName': cardHolderName, 'expiry': expiry, 'cvv': cvv, 'timestamp': str(timestamp)}
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
    
    # Top-Up Page functions ----------------------------------------------------------------------------------------------
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
        if topupStr:
            self.ui.topupvalueLineEdit.setText(topupStr[:-1])
    
    def generateQRCode(self):
        topupValue = float(self.ui.topupvalueLineEdit.text())
    
        API_KEY = 'l707545b5ae3244b1b8482de4db7dc9b9e'
        API_SECRET = '87d9ea4c8b7640369348bd347d3e741c'
        MERCHANT = '272263407857060'
        TERMINAL = '946017491380534'
        BILLER = '987134826044678'

        # initial object
        qr_payment = QRCodePayment(API_KEY, API_SECRET, MERCHANT, TERMINAL, BILLER)

        qrData = qr_payment.gererate_qr_30(amount = topupValue, ref1="TH1234", ref2="THG456", ref3="SCB0987")
        data = qrData.get('data').get('qrRawData')

        img = qrcode.make(data)
        imgload = open('images//QR-Code.png','wb') #สร้างไฟล์ไบต์ใหม่ขึ้นมา กำหนดสิทธิ์เขียนไฟล์ได้
        img.save(imgload, 'PNG') #บันทึกค่า QR Code เข้าไปยังไฟล์
        imgload.close() #ปิดไฟล์

        self.displayQR(topupValue)
        self.user.topUptoE_Wallet(topupValue)
        self.ui.moneyLabel.setText(f"{self.user.getMoney():.5f}")
        self.ui.moneyLabel_2.setText(f"{self.user.getMoney():.5f}")
    
    def displayQR(self, val):
        dialog = QDialog(self)
        layout = QVBoxLayout()
        qrCode = QPushButton()
        # Create top up label
        topupLabel = QLabel()
        topupLabel.setText("Top-Up: {0:.2f} THB".format(val))
        # Create QrCode image
        qrCode.setIcon(QIcon("images/QR-Code.png"))
        qrCode.setStyleSheet("QPushButton { border: none; background-color: rgba(0,0,0,0) } ")
        qrCode.setIconSize(QSize(200, 200))
        # Add elements to layout
        layout.addWidget(topupLabel)
        layout.addWidget(qrCode)
        dialog.setLayout(layout)
        dialog.exec_()
        return True
    
    # Select Station functions -------------------------------------------------------------------------------------------
    def addNumbertoStationID(self, val):
        if len(self.stationid) < 6:
            self.stationid.append(val)
            self.updateStationIDLineEdit(len(self.stationid))
    
    def deleteNumberfromStationID(self):
        if self.stationid:
            self.stationid.pop()
            self.updateStationIDLineEdit(len(self.stationid))
    
    def searchStationID(self):
        stations = self.db.child('stations').get().val()
        stationidStr = ''.join(str(e) for e in self.stationid)
        if stationidStr in stations.keys():
            self.gotoChargingStationPage(stationidStr, stations.get(stationidStr))
        else:
            self.showAlert("StationID not found!!!")
    
    def updateStationIDLineEdit(self, idLength):
        if idLength >= 1:
            self.ui.stationid1.setText(str(self.stationid[0]))
            if idLength >= 2:
                self.ui.stationid2.setText(str(self.stationid[1]))
                if idLength >= 3:
                    self.ui.stationid3.setText(str(self.stationid[2]))
                    if idLength >= 4:
                        self.ui.stationid4.setText(str(self.stationid[3]))
                        if idLength >= 5:
                            self.ui.stationid5.setText(str(self.stationid[4]))
                            if idLength >= 6:
                                self.ui.stationid6.setText(str(self.stationid[5]))
                            else:
                                self.ui.stationid6.setText("")
                        else:
                            self.ui.stationid5.setText("")
                    else:
                        self.ui.stationid4.setText("")
                else:
                    self.ui.stationid3.setText("")
            else:
                self.ui.stationid2.setText("")
        else:
            self.ui.stationid1.setText("")

    def gotoChargingStationPage(self, stationidStr, stationInfo):
        self.refreshChargingStationPage(stationidStr, stationInfo)
        self.ui.stackedWidget.setCurrentWidget(self.ui.chargingstationPage)
    
    # Charging Station functions ------------------------------------------------------------------------------------------
    def refreshChargingStationPage(self, stationidStr, stationInfo):
        self.ui.stationidvalueLabel.setText(stationidStr)
        self.ui.companyvalueLabel_2.setText(stationInfo.get('company'))
        self.ui.typevalueLabel.setText(stationInfo.get('type'))
        self.ui.locationvalueTextEdit.setText(stationInfo.get('location'))
    
    def gotoStationPage(self):
        if self.gotoPinPage(3):
            stationidStr = ''.join(str(e) for e in self.stationid)
            station_page = Station_Page(self.db, self.auth, self.widget, self.isAutoLogin, self, self.user, stationidStr)
            self.widget.addWidget(station_page)

            if self.isAutoLogin:
                self.widget.setCurrentIndex(self.widget.currentIndex() + 3)
            else:
                self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
            
            # Wait for Station Page to close
            self.wait_object_destruction(station_page)
            print("Station Page Destructed")
            if self.getPinResult():
                self.setPinResult(False)
                self.gotoHomePage()
                return True
            return False
        else:
            self.showAlert("Invalid Pin Input")
        




        