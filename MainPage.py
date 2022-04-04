from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from main import Ui_Form as Ui_Main

class Main_Page(QWidget):
    def __init__(self, auth, widget):
        QWidget.__init__(self, None)
        self.auth = auth
        self.widget = widget

        self.ui = Ui_Main()
        self.ui.setupUi(self)

        # Pages from stackedWidget
        self.ui.homePushButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.homePage))
        self.ui.historyPushButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.historyPage))
        self.ui.locationPushButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.locationPage))
        self.ui.accountPushButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.accountPage))

        # Home Page
        if (self.ui.stackedWidget.currentWidget() == self.ui.homePage):
            self.ui.stackedWidget.currentWidget()

            # Setting up stations for testing
            self.stations=('Elex','Why','How','What','When','Aow','Im')
            self.stationModel = QStandardItemModel(len(self.stations), 1)
            self.stationModel.setHorizontalHeaderLabels(['Stations'])

            for row, station in enumerate(self.stations):
                item = QStandardItem(station)
                self.stationModel.setItem(row, 0, item)
            
            self.filter_proxy_model = QSortFilterProxyModel()
            self.filter_proxy_model.setSourceModel(self.stationModel)
            self.filter_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
            self.filter_proxy_model.setFilterKeyColumn(0)

            self.ui.searchLineEdit.textChanged.connect(self.filter_proxy_model.setFilterRegularExpression)

            self.ui.stationTableView.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.ui.stationTableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.ui.stationTableView.setModel(self.filter_proxy_model)


        