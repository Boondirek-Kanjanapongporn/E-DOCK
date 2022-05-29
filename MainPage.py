from tkinter import messagebox
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWebEngineWidgets import *
from PySide6.QtCharts import *
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
        self.onHomePage()
        
        # Home Page -------------------------------------------------------------------------------------------------------
        self.ui.searchLineEdit.textChanged.connect(self.handleSearch)
        self.ui.chargePushButton.clicked.connect(self.gotoSelectStationPage)
        self.ui.topupPushButton.clicked.connect(self.gotoTopupPage)
        self.ui.carsPushButton.clicked.connect(self.gotoCarsPage)
        self.ui.cardsPushButton.clicked.connect(self.gotoCardsPage)

        self.ui.bangchakPushButton.clicked.connect(lambda: self.gotoCompanyPage("BANGCHAK"))
        self.ui.caltexPushButton.clicked.connect(lambda: self.gotoCompanyPage("CALTEX"))
        self.ui.mgPushButton.clicked.connect(lambda: self.gotoCompanyPage("MG"))
        self.ui.peaPushButton.clicked.connect(lambda: self.gotoCompanyPage("PEA"))
        self.ui.ptPushButton.clicked.connect(lambda: self.gotoCompanyPage("PT"))
        self.ui.pttPushButton.clicked.connect(lambda: self.gotoCompanyPage("PTT"))
        self.ui.shellPushButton.clicked.connect(lambda: self.gotoCompanyPage("SHELL"))
        self.ui.suscoPushButton.clicked.connect(lambda: self.gotoCompanyPage("SUSCO"))

        # History Page ----------------------------------------------------------------------------------------------------
        
        # Location Page -------------------------------------------------------------------------------------------------
        # Open EV station locations
        self.openStationLocations()

        # Account Page ---------------------------------------------------------------------------------------------------

        # Company Page ---------------------------------------------------------------------------------------------------
        self.ui.homePushButton_2.clicked.connect(self.gotoHomePage)

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

        # Cars Page --------------------------------------------------------------------------------------------------

        # Cards Page -------------------------------------------------------------------------------------------------
    
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
        self.refreshHomePage()
        self.refreshNavBar()
        self.onHomePage()
        self.ui.stackedWidget.setCurrentWidget(self.ui.homePage)
    
    def gotoHistoryPage(self):
        self.refreshHistoryPage()
        self.refreshNavBar()
        self.onHistoryPage()
        self.ui.stackedWidget.setCurrentWidget(self.ui.historyPage)

    def gotoLocationPage(self):
        self.refreshLocationPage()
        self.refreshNavBar()
        self.onLocationPage()
        self.ui.stackedWidget.setCurrentWidget(self.ui.locationPage)

    def gotoAccountPage(self):
        self.refreshAccountPage()
        self.refreshNavBar()
        self.onAccountPage()
        self.ui.stackedWidget.setCurrentWidget(self.ui.accountPage)
    
    def refreshHomePage(self):
        username = self.user.getUsername()
        if username:
            self.ui.hiLabel.setText(f"Hi, {username}")
        else:
            self.ui.hiLabel.setText(f"Hi, {self.email}")

    def refreshHistoryPage(self):
        self.addHistoryList()
    
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
    
    def refreshNavBar(self):
        self.ui.homePushButton.setIcon(QIcon("images\\home.png"))
        self.ui.historyPushButton.setIcon(QIcon("images\\history.png"))
        self.ui.locationPushButton.setIcon(QIcon("images\\location.png"))
        self.ui.accountPushButton.setIcon(QIcon("images\\account.png"))

        self.ui.homePushButton.setStyleSheet("QPushButton{border: None;} QPushButton:hover{background-color: #71cd00;color: #fafafa;}")
        self.ui.historyPushButton.setStyleSheet("QPushButton{border: None;} QPushButton:hover{background-color: #71cd00;color: #fafafa;}")
        self.ui.locationPushButton.setStyleSheet("QPushButton{border: None;} QPushButton:hover{background-color: #71cd00;color: #fafafa;}")
        self.ui.accountPushButton.setStyleSheet("QPushButton{border: None;} QPushButton:hover{background-color: #71cd00;color: #fafafa;}")
    
    def onHomePage(self):
        self.ui.homePushButton.setIcon(QIcon("images\\home_white.png"))
        self.ui.homePushButton.setStyleSheet("QPushButton{border:None; background-color: #71cd00; color: #fafafa;} QPushButton:hover{background-color: #468000;")

    def onHistoryPage(self):
        self.ui.historyPushButton.setIcon(QIcon("images\\history_white.png"))
        self.ui.historyPushButton.setStyleSheet("QPushButton{border:None; background-color: #71cd00; color: #fafafa;} QPushButton:hover{background-color: #468000;")

    def onLocationPage(self):
        self.ui.locationPushButton.setIcon(QIcon("images\\location_white.png"))
        self.ui.locationPushButton.setStyleSheet("QPushButton{border:None; background-color: #71cd00; color: #fafafa;} QPushButton:hover{background-color: #468000;")

    def onAccountPage(self):
        self.ui.accountPushButton.setIcon(QIcon("images\\account_white.png"))
        self.ui.accountPushButton.setStyleSheet("QPushButton{border:None; background-color: #71cd00; color: #fafafa;} QPushButton:hover{background-color: #468000;")

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
    
    def handleSearch(self):
        searchText = self.ui.searchLineEdit.text().upper()
        companies = self.db.child('companies').get().val()
        companies = list(companies.keys())
        if searchText != "" and not searchText.isspace():
            for i in range(self.ui.stationHorizontalLayout.count()):
                childLayout = self.ui.stationHorizontalLayout.itemAt(i)
                for j in range(childLayout.count()):
                    childButton = childLayout.itemAt(j)
                    if searchText in childButton.widget().text():
                        childButton.widget().setVisible(True)
                    else:
                        childButton.widget().setVisible(False)
        else:
            for i in range(self.ui.stationHorizontalLayout.count()):
                childLayout = self.ui.stationHorizontalLayout.itemAt(i)
                for j in range(childLayout.count()):
                    childButton = childLayout.itemAt(j)
                    childButton.widget().setVisible(True)
    
    def gotoSelectStationPage(self):
        self.refreshSelectStationPage()
        self.ui.stackedWidget.setCurrentWidget(self.ui.selectstationPage)

    def gotoTopupPage(self):
        self.refreshTopupPage()
        self.ui.stackedWidget.setCurrentWidget(self.ui.topupPage)
    
    def gotoCarsPage(self):
        self.refreshCarsPage()
        self.ui.stackedWidget.setCurrentWidget(self.ui.carsPage)

    def gotoCardsPage(self):
        self.refreshCardsPage()
        self.ui.stackedWidget.setCurrentWidget(self.ui.cardsPage)
    
    def gotoCompanyPage(self, company):
        self.refreshCompanyPage(company)
        self.ui.stackedWidget.setCurrentWidget(self.ui.companyPage)
    
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
    
    def refreshCarsPage(self):
        self.addCarsList()

    def refreshCardsPage(self):
        self.addCardsList()
    
    def refreshCompanyPage(self, company):
        weekRates = self.db.child('companies').child(company).get().val()
        mondayRate = weekRates.get('monday')
        tuesdayRate = weekRates.get('tuesday')
        wednesdayRate = weekRates.get('wednesday')
        thursdayRate = weekRates.get('thursday')
        fridayRate = weekRates.get('friday')
        saturdayRate = weekRates.get('saturday')
        sundayRate = weekRates.get('sunday')

        lineseries = QLineSeries()
        lineseries.append(0, mondayRate)
        lineseries.append(5, tuesdayRate)
        lineseries.append(10, wednesdayRate)
        lineseries.append(15, thursdayRate)
        lineseries.append(20, fridayRate)
        lineseries.append(25, saturdayRate)
        lineseries.append(30, sundayRate)

        chart = QChart()
        chart.legend().setVisible(False)
        chart.addSeries(lineseries)
        chart.createDefaultAxes()
        chart.setTitle("Weekly Charge Rates")

        self.ui.ratesGraphicsView.setChart(chart)
        self.ui.ratesGraphicsView.setRenderHint(QPainter.Antialiasing)


        self.ui.companyvalueLabel.setText(company)
        self.ui.mondayvalueLabel.setText(str(mondayRate))
        self.ui.tuesdayvalueLabel.setText(str(tuesdayRate))
        self.ui.wednesdayvalueLabel.setText(str(wednesdayRate))
        self.ui.thursdayvalueLabel.setText(str(thursdayRate))
        self.ui.fridayvalueLabel.setText(str(fridayRate))
        self.ui.saturdayvalueLabel.setText(str(saturdayRate))
        self.ui.sundayvalueLabel.setText(str(sundayRate))

    
    # History Page functions ---------------------------------------------------------------------------------------------
    def addHistoryList(self):
        self.clearLayout(self.ui.historyVerticalLayout)
        try:
            historyList = self.user.getHistory()
            for value in reversed(list(historyList.values())):
                self.ui.historyVerticalLayout.addWidget(self.createHistoryPushButton(value))
            self.ui.historyVerticalLayout.addStretch(1)
        except:
            print("No histories")
    
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
            self.ui.notificationPushButton.setIcon(QIcon("images\\right-arrow_white.png"))
        else:
            self.ui.notificationWidget.setVisible(True)
            self.ui.notificationPushButton.setIcon(QIcon("images\\down-arrow_white.png"))
            if self.user.getNotification:
                self.ui.opennotificationRadioButton.setChecked(True)
            else:
                self.ui.closenotificationRadioButton.setChecked(True)
    
    def toggleAddCarWidget(self):
        if self.ui.addcarWidget.isVisible():
            self.ui.addcarWidget.setVisible(False)
            self.ui.addcarPushButton.setIcon(QIcon("images\\right-arrow_white.png"))
        else:
            self.ui.addcarWidget.setVisible(True)
            self.ui.addcarPushButton.setIcon(QIcon("images\\down-arrow_white.png"))
    
    def toggleAddCardWidget(self):
        if self.ui.addcardWidget.isVisible():
            self.ui.addcardWidget.setVisible(False)
            self.ui.addcardPushButton.setIcon(QIcon("images\\right-arrow_white.png"))
        else:
            self.ui.addcardWidget.setVisible(True)
            self.ui.addcardPushButton.setIcon(QIcon("images\\down-arrow_white.png"))
    
    def toggleChangeUsernameWidget(self):
        if self.ui.changeusernameWidget.isVisible():
            self.ui.changeusernameWidget.setVisible(False)
            self.ui.changeusernamePushButton.setIcon(QIcon("images\\right-arrow_white.png"))
        else:
            self.ui.changeusernameWidget.setVisible(True)
            self.ui.changeusernamePushButton.setIcon(QIcon("images\\down-arrow_white.png"))
    
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
                    newCar = {'company': company, 'model': model, 'batteryCapacity': batteryCapacity, 'chargingCapacity': chargingCapacity, 'timestamp': str(timestamp)}
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
        company = stationInfo.get('company')
        stationRate = self.findChargingRate(company)
        self.ui.stationidvalueLabel.setText(stationidStr)
        self.ui.companyvalueLabel_2.setText(company)
        self.ui.typevalueLabel.setText(stationInfo.get('type'))
        self.ui.ratevalueLabel.setText(str(stationRate) + " THB/kwH")
        self.ui.locationvalueTextEdit.setText(stationInfo.get('location'))
    
    def findChargingRate(self, company):
        weekday = datetime.datetime.today().weekday()
        if weekday == 0:
            return self.db.child('companies').child(company).child('monday').get().val()
        elif weekday == 1:
            return self.db.child('companies').child(company).child('tuesday').get().val()
        elif weekday == 2:
            return self.db.child('companies').child(company).child('wednesday').get().val()
        elif weekday == 3:
            return self.db.child('companies').child(company).child('thursday').get().val()
        elif weekday == 4:
            return self.db.child('companies').child(company).child('friday').get().val()
        elif weekday == 5:
            return self.db.child('companies').child(company).child('saturday').get().val()
        elif weekday == 6:
            return self.db.child('companies').child(company).child('sunday').get().val()
    
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
    
    # Cars Page function ---------------------------------------------------------------------------------------------------
    def addCarsList(self):
        self.clearLayout(self.ui.carsVerticalLayout_2)
        try:
            carsList = self.user.getCars()
            for value in reversed(list(carsList.values())):
                self.ui.carsVerticalLayout_2.addWidget(self.createCarPushButton(value))
            self.ui.carsVerticalLayout_2.addStretch(1)
        except:
            print("No cars")
    
    def createCarPushButton(self, car):
        carPushButton = QPushButton()
        carPushButton.setText(f"{car.get('company')}\nModel: {car.get('model')}\nBattery-Capacity: {car.get('batteryCapacity')} mAh\nCharge-Capacity: {car.get('chargingCapacity')} kW\nTimestamp: {car.get('timestamp')}")
        return carPushButton
    
    # Cars Page function ---------------------------------------------------------------------------------------------------
    def addCardsList(self):
        self.clearLayout(self.ui.cardsVerticalLayout_2)
        try:
            cardsList = self.user.getCards()
            for value in reversed(list(cardsList.values())):
                self.ui.cardsVerticalLayout_2.addWidget(self.createCardPushButton(value))
            self.ui.cardsVerticalLayout_2.addStretch(1)
        except:
            print("No cards")
    
    def createCardPushButton(self, card):
        cardPushButton = QPushButton()
        cardPushButton.setText(f"Card Number:{card.get('cardNumber')}\nCardholder: {card.get('cardHolderName')}\nTimestamp: {card.get('timestamp')}")
        return cardPushButton
        




        