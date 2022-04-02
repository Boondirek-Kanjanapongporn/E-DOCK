from PySide6.QtWidgets import *
from PySide6.QtCore import *
from main import Ui_Form as Ui_Main

class Main_Page(QWidget):
    def __init__(self, auth, widget):
        QWidget.__init__(self, None)
        self.auth = auth
        self.widget = widget

        self.ui = Ui_Main()
        self.ui.setupUi(self)

        # self.ui.homeScrollArea.setWidget(self.ui.homePage)

        # Pages
        self.ui.homePushButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.homePage))
        self.ui.historyPushButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.historyPage))
        self.ui.locationPushButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.locationPage))
        self.ui.accountPushButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.accountPage))


        