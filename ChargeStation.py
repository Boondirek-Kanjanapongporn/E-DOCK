import datetime
import time
from pyHS100 import SmartPlug as TPLinkSP

class ChargeStation:
    def __init__(self, db, stationID, parentObject, user):
        self.db = db
        self.parentObject = parentObject
        self.user = user
        self.stations = self.db.child('stations').get().val()
        self.stationID = stationID
        self.stationInfo = self.stations.get(stationID)

        # Station details
        self.stationCompany = self.stationInfo.get('company')
        self.stationType = self.stationInfo.get('type')
        self.stationLocation = self.stationInfo.get('location')
        self.stationRate = self.findChargingRate()

        # Charging details
        self.totalSeconds = 0
        self.timeStamp = 0
        self.wattageList = []
        self.SmartPlug = TPLinkSP("192.168.137.54")
        self.SmartPlug.turn_off()
    
    def getStationID(self):
        return self.stationID
    
    def getStationInfo(self):
        return self.stationInfo
    
    def getStationCompany(self):
        return self.stationCompany
    
    def getStationType(self):
        return self.stationType
    
    def getStationLocation(self):
        return self.stationLocation
    
    def getStationRate(self):
        return self.stationRate
    
    def getTotalSeconds(self):
        return self.totalSeconds
    
    def getTimeStamp(self):
        return self.timeStamp
    
    def setStationID(self, stationID):
        self.stationID = stationID
        self.stationInfo = self.stations.get(stationID)
        self.stationCompany = self.stationInfo.get('company')
        self.stationType = self.stationInfo.get('type')
        self.stationLocation = self.stationInfo.get('location')
        self.stationRate = 0
        self.totalSeconds = 0
    
    def setStationInfo(self, stationInfo):
        self.stationInfo = stationInfo
    
    def setStationCompany(self, stationCompany):
        self.stationCompany = stationCompany
    
    def setStationType(self, stationType):
        self.stationType = stationType
    
    def setStationLocation(self, stationLocation):
        self.stationLocation = stationLocation
    
    def setStationRate(self, stationRate):
        self.stationRate = stationRate
    
    def setTotalSeconds(self, totalSeconds):
        self.totalSeconds = totalSeconds
    
    def setTimeStamp(self, timeStamp):
        self.timeStamp = timeStamp
    
    def startCharging(self):
        self.timeStamp = datetime.datetime.now()
        self.SmartPlug.turn_on()
        secondsTemp = self.totalSeconds
        while secondsTemp:
            secondsTemp -= 1
            self.parentObject.setTimer(self.secondstoTime(secondsTemp))
            # Check condition if battery full before the timer ends
            wattageTemp = self.SmartPlug.current_consumption()
            self.wattageList.append(wattageTemp)
            time.sleep(1)
        self.parentObject.stopTimer(True)
        return True
    
    def findChargingRate(self):
        weekday = datetime.datetime.today().weekday()
        if weekday == 0:
            return self.db.child('companies').child(self.stationCompany).child('monday').get().val()
        elif weekday == 1:
            return self.db.child('companies').child(self.stationCompany).child('tuesday').get().val()
        elif weekday == 2:
            return self.db.child('companies').child(self.stationCompany).child('wednesday').get().val()
        elif weekday == 3:
            return self.db.child('companies').child(self.stationCompany).child('thursday').get().val()
        elif weekday == 4:
            return self.db.child('companies').child(self.stationCompany).child('friday').get().val()
        elif weekday == 5:
            return self.db.child('companies').child(self.stationCompany).child('saturday').get().val()
        elif weekday == 6:
            return self.db.child('companies').child(self.stationCompany).child('sunday').get().val()
    
    def calculatePrice(self, seconds):
        hours = seconds/3600
        avgWattage = sum(self.wattageList)/len(self.wattageList)
        chargeCost = round((avgWattage * hours)/1000 * self.stationRate, 5)
        self.payChargeFee(chargeCost)
        return chargeCost
    
    def payChargeFee(self, fee):
        currentMoney = self.user.getMoney() - fee
        self.user.setMoney(currentMoney)
    
    def secondstoTime(self, totalSeconds):
        time = str(datetime.timedelta(seconds=totalSeconds))
        if len(time) < 8:
            time = "0" + time
        return time
    