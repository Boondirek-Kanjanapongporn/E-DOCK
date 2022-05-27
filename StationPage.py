from tkinter import Widget
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from ChargeStation import ChargeStation
from station import Ui_Form as Ui_Station
import datetime
import threading

class Station_Page(QWidget):
    def __init__(self, db, auth, widget, isAutoLogin, parentObject, user, stationID):
        QWidget.__init__(self, None)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.db = db
        self.auth = auth
        self.widget = widget
        self.isAutoLogin = isAutoLogin
        self.parentObject = parentObject
        self.user = user
        self.stationID = stationID
        self.timer = []
        self.stopTime = 0
        self.isfinishCharging = False

        self.chargestation = ChargeStation(self.db, self.stationID, self, self.user)

        self.ui = Ui_Station()
        self.ui.setupUi(self)

        # Set Timer Page ----------------------------------------------------------------------------------------------------
        self.ui.pushButton_0.clicked.connect(lambda: self.addNumbertoTimer(0))
        self.ui.pushButton_1.clicked.connect(lambda: self.addNumbertoTimer(1))
        self.ui.pushButton_2.clicked.connect(lambda: self.addNumbertoTimer(2))
        self.ui.pushButton_3.clicked.connect(lambda: self.addNumbertoTimer(3))
        self.ui.pushButton_4.clicked.connect(lambda: self.addNumbertoTimer(4))
        self.ui.pushButton_5.clicked.connect(lambda: self.addNumbertoTimer(5))
        self.ui.pushButton_6.clicked.connect(lambda: self.addNumbertoTimer(6))
        self.ui.pushButton_7.clicked.connect(lambda: self.addNumbertoTimer(7))
        self.ui.pushButton_8.clicked.connect(lambda: self.addNumbertoTimer(8))
        self.ui.pushButton_9.clicked.connect(lambda: self.addNumbertoTimer(9))
        self.ui.pushButton_delete.clicked.connect(lambda: self.deleteNumberfromTimer())
        self.ui.startPushButton.clicked.connect(self.checkTimerCondition)
        self.ui.closePushButton.clicked.connect(self.closeStationPage)

        # Charging Page -----------------------------------------------------------------------------------------------------
        self.ui.stopPushButton.clicked.connect(lambda: self.stopTimer(False))
        # Success Page ------------------------------------------------------------------------------------------------------
        self.ui.donePushButton.clicked.connect(lambda: self.closeStationPage(True))

    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    def showAlert(self, text):
        messageBox = QMessageBox(self)
        messageBox.setText(text)
        messageBox.exec()
    
    def showConfirmation(self, title, totalSeconds):
        hours = totalSeconds/3600
        avgWattage = 80
        chargeCost = (avgWattage * hours)/1000 * self.chargestation.stationRate
        
        time = self.secondstoTime(totalSeconds)
        messageBox = QMessageBox()
        messageBox.setWindowTitle(title)
        messageBox.setText(f"Time: \t\t{time} min\nEstimate Price: \t{chargeCost:.2f}\tTHB")
        messageBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        reply = messageBox.exec_()
        if reply == 16384:
            return True
        else:
            return False
    
    def secondstoTime(self, totalSeconds):
        time = str(datetime.timedelta(seconds=totalSeconds))
        if len(time) < 8:
            time = "0" + time
        return time

    # Set Timer Page functions ----------------------------------------------------------------------------------------------
    def addNumbertoTimer(self, val):
        if len(self.timer) < 6:
            self.timer.append(val)
            self.updateTimerLineEdit(len(self.timer))
    
    def deleteNumberfromTimer(self):
        if self.timer:
            self.timer.pop()
            self.updateTimerLineEdit(len(self.timer))
    
    def updateTimerLineEdit(self, timerLength):
        timerReversed = self.timer[::-1]

        if timerLength >= 1:
            self.ui.timer1.setText(str(timerReversed[0]))
            if timerLength >= 2:
                self.ui.timer2.setText(str(timerReversed[1]))
                if timerLength >= 3:
                    self.ui.timer3.setText(str(timerReversed[2]))
                    if timerLength >= 4:
                        self.ui.timer4.setText(str(timerReversed[3]))
                        if timerLength >= 5:
                            self.ui.timer5.setText(str(timerReversed[4]))
                            if timerLength >= 6:
                                self.ui.timer6.setText(str(timerReversed[5]))
                            else:
                                self.ui.timer6.setText("")
                        else:
                            self.ui.timer5.setText("")
                    else:
                        self.ui.timer4.setText("")
                else:
                    self.ui.timer3.setText("")
            else:
                self.ui.timer2.setText("")
        else:
            self.ui.timer1.setText("")
    
    def timetoSeconds(self):
        pass
    
    def checkTimerCondition(self):
        secondsList = [1, 10, 60, 600, 3600, 36000]
        timerReversed = self.timer[::-1]
        totalSeconds = 0
        for i in range(0, len(timerReversed)):
            totalSeconds += timerReversed[i] * secondsList[i]
        if totalSeconds >= 60:
            boolean = self.showConfirmation("Confirm Charging Details?", totalSeconds)
            if boolean:
                self.chargestation.setTotalSeconds(totalSeconds)
                self.gotoChargingPage()
        else:
            self.showAlert("Charge Time Must Be More than 1 Minute")
    
    def closeStationPage(self, boolean=False):
        if self.isAutoLogin:
            self.widget.removeWidget(self.widget.currentWidget())
            self.widget.setCurrentIndex(0)
        else:
            self.widget.removeWidget(self.widget.currentWidget())
        
        self.parentObject.setPinResult(boolean)
        self.close()
        return boolean
    
    # Charging Page functions -------------------------------------------------------------------------------------------
    def gotoChargingPage(self):
        self.refreshChargingPage()
        self.ui.stackedWidget.setCurrentWidget(self.ui.chargingPage)

        countdownThread = threading.Thread(target=self.chargestation.startCharging, args=(), kwargs={})
        countdownThread.start()
    
    def stopTimer(self, isTimerComplete=True):
        if not self.isfinishCharging:
            print("Timer Stop")
            self.chargestation.SmartPlug.turn_off()
            self.stopTime = self.ui.timercountdownLabel.text()
            self.gotoSuccessPage(isTimerComplete)
            self.isfinishCharging = True
    
    def refreshChargingPage(self):
        totalSeconds = self.chargestation.getTotalSeconds()
        time = self.secondstoTime(totalSeconds)
        self.ui.timercountdownLabel.setText(time)
    
    def setTimer(self, time):
        self.ui.timercountdownLabel.setText(time)

    # Success Page functions --------------------------------------------------------------------------------------------
    def gotoSuccessPage(self, isTimerComplete):
        self.refreshSuccessPage(isTimerComplete)
        self.ui.stackedWidget.setCurrentWidget(self.ui.successPage)
    
    def refreshSuccessPage(self, isTimerComplete):
        totalChargeTime = self.chargestation.getTotalSeconds()
        chargeCost = 0

        self.ui.stationidvalueLabel.setText(self.chargestation.getStationID())
        self.ui.companyvalueLabel.setText(self.chargestation.getStationCompany())
        self.ui.typevalueLabel.setText(self.chargestation.getStationType())
        # Check if the charging process stops before the timer ends
        if isTimerComplete:
            chargeCost = self.chargestation.calculatePrice(totalChargeTime)
            self.ui.moneyvalueLabel.setText(f"{chargeCost} THB")
            self.ui.timevalueLabel_2.setText(self.secondstoTime(totalChargeTime))
        else:
            secondsList = [1, 10, 60, 600, 3600, 36000]
            time = self.stopTime.replace(":","")
            timerReversed = time[::-1]
            totalSeconds = 0
            for i in range(0, len(timerReversed)):
                totalSeconds += int(timerReversed[i]) * secondsList[i]
            
            chargetime = totalChargeTime - totalSeconds
            chargeCost = self.chargestation.calculatePrice(chargetime)
            self.ui.moneyvalueLabel.setText(f"{chargeCost} THB")
            self.ui.timevalueLabel_2.setText(self.secondstoTime(chargetime))

        self.ui.ratevalueLabel.setText(str(self.chargestation.getStationRate()) + " THB/kwH")
        self.ui.timestampvalueLabel.setText(str(self.chargestation.getTimeStamp()))

        # Add Charge Details to History
        self.addtoHistory(chargeCost)
    
    def addtoHistory(self, chargeCost):
        userinfo = self.db.child('users').child(self.user.getUID()).get()

        if userinfo.val() is not None:
            cost = chargeCost
            stationid = self.ui.stationidvalueLabel.text()
            company = self.ui.companyvalueLabel.text()
            type = self.ui.typevalueLabel.text()
            time = self.ui.timevalueLabel_2.text()
            rate = self.ui.ratevalueLabel.text()
            timestamp = self.ui.timestampvalueLabel.text()

            newHistory = {'price': cost, 'stationid': stationid, 'company': company, 'type': type, 'duration': time, 'rate': rate, 'timestamp':timestamp}
            try:
                self.user.addHistory(newHistory)
            except:
                raise SystemError("Fail to add history")

