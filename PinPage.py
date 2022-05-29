from PySide6.QtWidgets import *
from PySide6.QtCore import *
from pin import Ui_Form as Ui_Pin

class Pin_Page(QWidget):
    def __init__(self, auth, widget, user, index, isAutoLogin, parentObject):
        QWidget.__init__(self, None)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.auth = auth
        self.widget = widget
        self.user = user
        self.index = index
        self.isAutoLogin = isAutoLogin
        self.parentObject = parentObject
        self.pincode = []
        self.confirmpincode = []

        self.ui = Ui_Pin()
        self.ui.setupUi(self)

        self.refreshPinPassword()

        # Open the selected pin page by index
        if index == 1:
            self.ui.stackedWidget.setCurrentWidget(self.ui.createpinPage)
        elif index == 2:
            self.ui.stackedWidget.setCurrentWidget(self.ui.confirmpinPage)
        elif index == 3:
            self.ui.stackedWidget.setCurrentWidget(self.ui.enterpinPage)
        elif index == 4:
            self.ui.stackedWidget.setCurrentWidget(self.ui.enterpasswordPage)
        
        # Create Pin Page -------------------------------------------------------------------------
        self.ui.pushButton_0.clicked.connect(lambda: self.addNumbertoPin(0,1))
        self.ui.pushButton_1.clicked.connect(lambda: self.addNumbertoPin(1,1))
        self.ui.pushButton_2.clicked.connect(lambda: self.addNumbertoPin(2,1))
        self.ui.pushButton_3.clicked.connect(lambda: self.addNumbertoPin(3,1))
        self.ui.pushButton_4.clicked.connect(lambda: self.addNumbertoPin(4,1))
        self.ui.pushButton_5.clicked.connect(lambda: self.addNumbertoPin(5,1))
        self.ui.pushButton_6.clicked.connect(lambda: self.addNumbertoPin(6,1))
        self.ui.pushButton_7.clicked.connect(lambda: self.addNumbertoPin(7,1))
        self.ui.pushButton_8.clicked.connect(lambda: self.addNumbertoPin(8,1))
        self.ui.pushButton_9.clicked.connect(lambda: self.addNumbertoPin(9,1))
        self.ui.pushButton_delete.clicked.connect(lambda: self.deleteNumberfromPin(1))

        # Confirm Pin Page ------------------------------------------------------------------------
        self.ui.pushButton_0_2.clicked.connect(lambda: self.addNumbertoPin(0,2))
        self.ui.pushButton_1_2.clicked.connect(lambda: self.addNumbertoPin(1,2))
        self.ui.pushButton_2_2.clicked.connect(lambda: self.addNumbertoPin(2,2))
        self.ui.pushButton_3_2.clicked.connect(lambda: self.addNumbertoPin(3,2))
        self.ui.pushButton_4_2.clicked.connect(lambda: self.addNumbertoPin(4,2))
        self.ui.pushButton_5_2.clicked.connect(lambda: self.addNumbertoPin(5,2))
        self.ui.pushButton_6_2.clicked.connect(lambda: self.addNumbertoPin(6,2))
        self.ui.pushButton_7_2.clicked.connect(lambda: self.addNumbertoPin(7,2))
        self.ui.pushButton_8_2.clicked.connect(lambda: self.addNumbertoPin(8,2))
        self.ui.pushButton_9_2.clicked.connect(lambda: self.addNumbertoPin(9,2))
        self.ui.pushButton_delete_2.clicked.connect(lambda: self.deleteNumberfromPin(2))

        # Enter Pin Page ------------------------------------------------------------------------
        self.ui.pushButton_0_3.clicked.connect(lambda: self.addNumbertoPin(0,3))
        self.ui.pushButton_1_3.clicked.connect(lambda: self.addNumbertoPin(1,3))
        self.ui.pushButton_2_3.clicked.connect(lambda: self.addNumbertoPin(2,3))
        self.ui.pushButton_3_3.clicked.connect(lambda: self.addNumbertoPin(3,3))
        self.ui.pushButton_4_3.clicked.connect(lambda: self.addNumbertoPin(4,3))
        self.ui.pushButton_5_3.clicked.connect(lambda: self.addNumbertoPin(5,3))
        self.ui.pushButton_6_3.clicked.connect(lambda: self.addNumbertoPin(6,3))
        self.ui.pushButton_7_3.clicked.connect(lambda: self.addNumbertoPin(7,3))
        self.ui.pushButton_8_3.clicked.connect(lambda: self.addNumbertoPin(8,3))
        self.ui.pushButton_9_3.clicked.connect(lambda: self.addNumbertoPin(9,3))
        self.ui.pushButton_delete_3.clicked.connect(lambda: self.deleteNumberfromPin(3))
        self.ui.closePushButton.clicked.connect(self.closePinPage)

        # Enter Password Page
        self.ui.okPushButton.clicked.connect(self.authPassword)
        self.ui.closePushButton_2.clicked.connect(self.closePinPage)
    
    def refreshPinPassword(self):
        self.pincode = []
        self.confirmpincode = []

        self.ui.pin1.setStyleSheet("QPushButton { border-radius: 10px; border: 3px solid #cecece; } ")
        self.ui.pin2.setStyleSheet("QPushButton { border-radius: 10px; border: 3px solid #cecece; } ")
        self.ui.pin3.setStyleSheet("QPushButton { border-radius: 10px; border: 3px solid #cecece; } ")
        self.ui.pin4.setStyleSheet("QPushButton { border-radius: 10px; border: 3px solid #cecece; } ")
        self.ui.pin5.setStyleSheet("QPushButton { border-radius: 10px; border: 3px solid #cecece; } ")
        self.ui.pin6.setStyleSheet("QPushButton { border-radius: 10px; border: 3px solid #cecece; } ")

        self.ui.pin1_2.setStyleSheet("QPushButton { border-radius: 10px; border: 3px solid #cecece; } ")
        self.ui.pin2_2.setStyleSheet("QPushButton { border-radius: 10px; border: 3px solid #cecece; } ")
        self.ui.pin3_2.setStyleSheet("QPushButton { border-radius: 10px; border: 3px solid #cecece; } ")
        self.ui.pin4_2.setStyleSheet("QPushButton { border-radius: 10px; border: 3px solid #cecece; } ")
        self.ui.pin5_2.setStyleSheet("QPushButton { border-radius: 10px; border: 3px solid #cecece; } ")
        self.ui.pin6_2.setStyleSheet("QPushButton { border-radius: 10px; border: 3px solid #cecece; } ")

        self.ui.pin1_3.setStyleSheet("QPushButton { border-radius: 10px; border: 3px solid #cecece; } ")
        self.ui.pin2_3.setStyleSheet("QPushButton { border-radius: 10px; border: 3px solid #cecece; } ")
        self.ui.pin3_3.setStyleSheet("QPushButton { border-radius: 10px; border: 3px solid #cecece; } ")
        self.ui.pin4_3.setStyleSheet("QPushButton { border-radius: 10px; border: 3px solid #cecece; } ")
        self.ui.pin5_3.setStyleSheet("QPushButton { border-radius: 10px; border: 3px solid #cecece; } ")
        self.ui.pin6_3.setStyleSheet("QPushButton { border-radius: 10px; border: 3px solid #cecece; } ")
    
    def updatePinColor(self, val, index):
        if index == 1:
            if val >= 1:
                self.ui.pin1.setStyleSheet("QPushButton { border-radius: 10px; border: 3px solid #cecece; background-color: #71cd00; } ")
                if val >= 2:
                    self.ui.pin2.setStyleSheet("QPushButton { border-radius: 10px; border: 3px solid #cecece; background-color: #71cd00; } ")
                    if val >= 3:
                        self.ui.pin3.setStyleSheet("QPushButton { border-radius: 10px; border: 3px solid #cecece; background-color: #71cd00; } ")
                        if val >= 4:
                            self.ui.pin4.setStyleSheet("QPushButton { border-radius: 10px; border: 3px solid #cecece; background-color: #71cd00; } ")
                            if val >= 5:
                                self.ui.pin5.setStyleSheet("QPushButton { border-radius: 10px; border: 3px solid #cecece; background-color: #71cd00; } ")
                                if val >= 6:
                                    self.ui.pin6.setStyleSheet("QPushButton { border-radius: 10px; border: 3px solid #cecece; background-color: #71cd00; } ")
                                else:
                                    self.ui.pin6.setStyleSheet("QPushButton { border-radius: 10px; border: 3px solid #cecece; } ")
                            else:
                                self.ui.pin5.setStyleSheet("QPushButton { border-radius: 10px; border: 3px solid #cecece; } ")
                        else:
                            self.ui.pin4.setStyleSheet("QPushButton { border-radius: 10px; border: 3px solid #cecece; } ")
                    else:
                        self.ui.pin3.setStyleSheet("QPushButton { border-radius: 10px; border: 3px solid #cecece; } ")
                else:
                    self.ui.pin2.setStyleSheet("QPushButton { border-radius: 10px; border: 3px solid #cecece; } ")
            else:
                self.ui.pin1.setStyleSheet("QPushButton { border-radius: 10px; border: 3px solid #cecece; } ")
        elif index == 2:
            if val >= 1:
                self.ui.pin1_2.setStyleSheet("QPushButton { border-radius: 10px; border: 3px solid #cecece; background-color: #71cd00; } ")
                if val >= 2:
                    self.ui.pin2_2.setStyleSheet("QPushButton { border-radius: 10px; border: 3px solid #cecece; background-color: #71cd00; } ")
                    if val >= 3:
                        self.ui.pin3_2.setStyleSheet("QPushButton { border-radius: 10px; border: 3px solid #cecece; background-color: #71cd00; } ")
                        if val >= 4:
                            self.ui.pin4_2.setStyleSheet("QPushButton { border-radius: 10px; border: 3px solid #cecece; background-color: #71cd00; } ")
                            if val >= 5:
                                self.ui.pin5_2.setStyleSheet("QPushButton { border-radius: 10px; border: 3px solid #cecece; background-color: #71cd00; } ")
                                if val >= 6:
                                    self.ui.pin6_2.setStyleSheet("QPushButton { border-radius: 10px; border: 3px solid #cecece; background-color: #71cd00; } ")
                                else:
                                    self.ui.pin6_2.setStyleSheet("QPushButton { border-radius: 10px; border: 3px solid #cecece; } ")
                            else:
                                self.ui.pin5_2.setStyleSheet("QPushButton { border-radius: 10px; border: 3px solid #cecece; } ")
                        else:
                            self.ui.pin4_2.setStyleSheet("QPushButton { border-radius: 10px; border: 3px solid #cecece; } ")
                    else:
                        self.ui.pin3_2.setStyleSheet("QPushButton { border-radius: 10px; border: 3px solid #cecece; } ")
                else:
                    self.ui.pin2_2.setStyleSheet("QPushButton { border-radius: 10px; border: 3px solid #cecece; } ")
            else:
                self.ui.pin1_2.setStyleSheet("QPushButton { border-radius: 10px; border: 3px solid #cecece; } ")
        elif index == 3:
            if val >= 1:
                self.ui.pin1_3.setStyleSheet("QPushButton { border-radius: 10px; border: 3px solid #cecece; background-color: #71cd00; } ")
                if val >= 2:
                    self.ui.pin2_3.setStyleSheet("QPushButton { border-radius: 10px; border: 3px solid #cecece; background-color: #71cd00; } ")
                    if val >= 3:
                        self.ui.pin3_3.setStyleSheet("QPushButton { border-radius: 10px; border: 3px solid #cecece; background-color: #71cd00; } ")
                        if val >= 4:
                            self.ui.pin4_3.setStyleSheet("QPushButton { border-radius: 10px; border: 3px solid #cecece; background-color: #71cd00; } ")
                            if val >= 5:
                                self.ui.pin5_3.setStyleSheet("QPushButton { border-radius: 10px; border: 3px solid #cecece; background-color: #71cd00; } ")
                                if val >= 6:
                                    self.ui.pin6_3.setStyleSheet("QPushButton { border-radius: 10px; border: 3px solid #cecece; background-color: #71cd00; } ")
                                else:
                                    self.ui.pin6_3.setStyleSheet("QPushButton { border-radius: 10px; border: 3px solid #cecece; } ")
                            else:
                                self.ui.pin5_3.setStyleSheet("QPushButton { border-radius: 10px; border: 3px solid #cecece; } ")
                        else:
                            self.ui.pin4_3.setStyleSheet("QPushButton { border-radius: 10px; border: 3px solid #cecece; } ")
                    else:
                        self.ui.pin3_3.setStyleSheet("QPushButton { border-radius: 10px; border: 3px solid #cecece; } ")
                else:
                    self.ui.pin2_3.setStyleSheet("QPushButton { border-radius: 10px; border: 3px solid #cecece; } ")
            else:
                self.ui.pin1_3.setStyleSheet("QPushButton { border-radius: 10px; border: 3px solid #cecece; } ")
    
    def addNumbertoPin(self, val, index):
        if index == 1:
            self.pincode.append(val)
            self.updatePinColor(len(self.pincode), index)
            if len(self.pincode) == 6:
                self.ui.stackedWidget.setCurrentWidget(self.ui.confirmpinPage)
        elif index == 2:
            self.confirmpincode.append(val)
            self.updatePinColor(len(self.confirmpincode), index)
            if len(self.confirmpincode) == 6:
                pincodeStr = ''.join(str(e) for e in self.pincode)
                confirmpincodeStr = ''.join(str(e) for e in self.confirmpincode)
                if pincodeStr == confirmpincodeStr:
                    self.user.setPin(pincodeStr)
                    print("Pin initialized successfully")
                    self.closePinPage(True)
                else:
                    self.showAlert("Pins are not the same")
                    self.refreshPinPassword()
                    self.ui.stackedWidget.setCurrentWidget(self.ui.createpinPage)
        elif index == 3:
            self.pincode.append(val)
            self.updatePinColor(len(self.pincode), index)
            if len(self.pincode) == 6:
                pincodeStr = ''.join(str(e) for e in self.pincode)
                if pincodeStr == self.user.getPin():
                    self.closePinPage(True)
                else:
                    self.closePinPage()
    
    def deleteNumberfromPin(self, index):
        if index == 1 or index == 3:
            if self.pincode:
                self.pincode.pop()
                self.updatePinColor(len(self.pincode), index)
        elif index == 2:
            if self.confirmpincode:
                self.confirmpincode.pop()
                self.updatePinColor(len(self.confirmpincode), index)
    
    def closePinPage(self, boolean=False):
        if self.isAutoLogin:
            self.widget.removeWidget(self.widget.currentWidget())
            self.widget.setCurrentIndex(0)
        else:
            self.widget.removeWidget(self.widget.currentWidget())
        
        self.parentObject.setPinResult(boolean)
        self.close()
        return boolean
    
    def authPassword(self):
        password = self.ui.enterpasswordLineEdit.text()
        try:
            self.auth.sign_in_with_email_and_password(self.user.getEmail(), password)
            self.closePinPage(True)
        except:
            print("Incorrect Password")
            self.closePinPage()

    def showAlert(self, text):
        messageBox = QMessageBox(self)
        messageBox.setText(text)
        messageBox.exec()