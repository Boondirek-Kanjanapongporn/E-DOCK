from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWebEngineWidgets import *
from main import Ui_Form as Ui_Main

class Main_Page(QWidget):
    def __init__(self, auth, widget):
        QWidget.__init__(self, None)
        self.auth = auth
        self.widget = widget

        self.ui = Ui_Main()
        self.ui.setupUi(self)

        # Pages from stackedWidget
        self.ui.homePushButton.clicked.connect(self.gotoHomePage)
        self.ui.historyPushButton.clicked.connect(self.gotoHistoryPage)
        self.ui.locationPushButton.clicked.connect(self.gotoLocationPage)
        self.ui.accountPushButton.clicked.connect(self.gotoAccountPage)

        self.openStationLocations()

        # Home Page
        if (self.ui.stackedWidget.currentWidget() == self.ui.homePage):
            self.ui.stackedWidget.currentWidget()

            # Setting up stations for testing
            stations=('Elex','Why','How','What','When','Aow','Im')
            stationModel = QStandardItemModel(len(stations), 1)
            stationModel.setHorizontalHeaderLabels(['Stations'])

            for row, station in enumerate(stations):
                item = QStandardItem(station)
                stationModel.setItem(row, 0, item)
            
            filter_proxy_model = QSortFilterProxyModel()
            filter_proxy_model.setSourceModel(stationModel)
            filter_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
            filter_proxy_model.setFilterKeyColumn(0)

            self.ui.searchLineEdit.textChanged.connect(filter_proxy_model.setFilterRegularExpression)

            self.ui.stationTableView.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.ui.stationTableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.ui.stationTableView.setModel(filter_proxy_model)
        
        elif (self.ui.stackedWidget.currentWidget() == self.ui.locationPage):
            pass
    
    def gotoHomePage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.homePage)
    
    def gotoHistoryPage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.historyPage)

    def gotoLocationPage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.locationPage)

    def gotoAccountPage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.accountPage)

    def openStationLocations(self):
        layout = QVBoxLayout()
        web = QWebEngineView()
        web.load(QUrl("https://www.plugshare.com/"))
        layout.addWidget(web)
        self.ui.locationWidget.setLayout(layout)
        




        