# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableView,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(360, 640)
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 361, 581))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.verticalLayoutWidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.homeScrollArea = QScrollArea(self.homePage)
        self.homeScrollArea.setObjectName(u"homeScrollArea")
        self.homeScrollArea.setGeometry(QRect(0, 0, 361, 581))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.homeScrollArea.sizePolicy().hasHeightForWidth())
        self.homeScrollArea.setSizePolicy(sizePolicy)
        self.homeScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.homeScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 342, 690))
        self.formLayout = QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setContentsMargins(20, 20, 20, 20)
        self.hiLabel = QLabel(self.scrollAreaWidgetContents)
        self.hiLabel.setObjectName(u"hiLabel")
        font = QFont()
        font.setPointSize(10)
        self.hiLabel.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.hiLabel)

        self.welcomeLabel = QLabel(self.scrollAreaWidgetContents)
        self.welcomeLabel.setObjectName(u"welcomeLabel")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.welcomeLabel.setFont(font1)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.welcomeLabel)

        self.searchLineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.searchLineEdit.setObjectName(u"searchLineEdit")
        self.searchLineEdit.setMinimumSize(QSize(0, 40))

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.searchLineEdit)

        self.stationTableView = QTableView(self.scrollAreaWidgetContents)
        self.stationTableView.setObjectName(u"stationTableView")
        self.stationTableView.setMinimumSize(QSize(0, 190))

        self.formLayout.setWidget(4, QFormLayout.SpanningRole, self.stationTableView)

        self.otherservicesLabel = QLabel(self.scrollAreaWidgetContents)
        self.otherservicesLabel.setObjectName(u"otherservicesLabel")
        self.otherservicesLabel.setFont(font)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.otherservicesLabel)

        self.otherservicesLayout = QHBoxLayout()
        self.otherservicesLayout.setSpacing(12)
        self.otherservicesLayout.setObjectName(u"otherservicesLayout")
        self.topupVerticalLayout = QVBoxLayout()
        self.topupVerticalLayout.setSpacing(0)
        self.topupVerticalLayout.setObjectName(u"topupVerticalLayout")
        self.topupPushButton = QPushButton(self.scrollAreaWidgetContents)
        self.topupPushButton.setObjectName(u"topupPushButton")
        self.topupPushButton.setMinimumSize(QSize(0, 31))
        self.topupPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.topupPushButton.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u"images/topup.png", QSize(), QIcon.Normal, QIcon.Off)
        self.topupPushButton.setIcon(icon)
        self.topupPushButton.setIconSize(QSize(18, 18))

        self.topupVerticalLayout.addWidget(self.topupPushButton)

        self.topupLabel = QLabel(self.scrollAreaWidgetContents)
        self.topupLabel.setObjectName(u"topupLabel")
        self.topupLabel.setStyleSheet(u"")
        self.topupLabel.setAlignment(Qt.AlignCenter)

        self.topupVerticalLayout.addWidget(self.topupLabel)


        self.otherservicesLayout.addLayout(self.topupVerticalLayout)

        self.paymentVerticalLayout = QVBoxLayout()
        self.paymentVerticalLayout.setSpacing(0)
        self.paymentVerticalLayout.setObjectName(u"paymentVerticalLayout")
        self.paymentPushButton = QPushButton(self.scrollAreaWidgetContents)
        self.paymentPushButton.setObjectName(u"paymentPushButton")
        self.paymentPushButton.setMinimumSize(QSize(0, 31))
        self.paymentPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"images/scan.png", QSize(), QIcon.Normal, QIcon.Off)
        self.paymentPushButton.setIcon(icon1)
        self.paymentPushButton.setIconSize(QSize(18, 18))

        self.paymentVerticalLayout.addWidget(self.paymentPushButton)

        self.paymentLabel = QLabel(self.scrollAreaWidgetContents)
        self.paymentLabel.setObjectName(u"paymentLabel")
        self.paymentLabel.setStyleSheet(u"")
        self.paymentLabel.setAlignment(Qt.AlignCenter)

        self.paymentVerticalLayout.addWidget(self.paymentLabel)


        self.otherservicesLayout.addLayout(self.paymentVerticalLayout)

        self.carsVerticalLayout = QVBoxLayout()
        self.carsVerticalLayout.setSpacing(0)
        self.carsVerticalLayout.setObjectName(u"carsVerticalLayout")
        self.carsPushButton = QPushButton(self.scrollAreaWidgetContents)
        self.carsPushButton.setObjectName(u"carsPushButton")
        self.carsPushButton.setMinimumSize(QSize(0, 31))
        self.carsPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u"images/car.png", QSize(), QIcon.Normal, QIcon.Off)
        self.carsPushButton.setIcon(icon2)
        self.carsPushButton.setIconSize(QSize(24, 24))

        self.carsVerticalLayout.addWidget(self.carsPushButton)

        self.carsLabel = QLabel(self.scrollAreaWidgetContents)
        self.carsLabel.setObjectName(u"carsLabel")
        self.carsLabel.setStyleSheet(u"")
        self.carsLabel.setAlignment(Qt.AlignCenter)

        self.carsVerticalLayout.addWidget(self.carsLabel)


        self.otherservicesLayout.addLayout(self.carsVerticalLayout)

        self.cardsVerticalLayout = QVBoxLayout()
        self.cardsVerticalLayout.setSpacing(0)
        self.cardsVerticalLayout.setObjectName(u"cardsVerticalLayout")
        self.cardsPushButton = QPushButton(self.scrollAreaWidgetContents)
        self.cardsPushButton.setObjectName(u"cardsPushButton")
        self.cardsPushButton.setMinimumSize(QSize(0, 31))
        self.cardsPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u"images/card.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cardsPushButton.setIcon(icon3)
        self.cardsPushButton.setIconSize(QSize(19, 19))

        self.cardsVerticalLayout.addWidget(self.cardsPushButton)

        self.cardsLabel = QLabel(self.scrollAreaWidgetContents)
        self.cardsLabel.setObjectName(u"cardsLabel")
        self.cardsLabel.setStyleSheet(u"")
        self.cardsLabel.setAlignment(Qt.AlignCenter)

        self.cardsVerticalLayout.addWidget(self.cardsLabel)


        self.otherservicesLayout.addLayout(self.cardsVerticalLayout)


        self.formLayout.setLayout(6, QFormLayout.SpanningRole, self.otherservicesLayout)

        self.promotionLabel = QLabel(self.scrollAreaWidgetContents)
        self.promotionLabel.setObjectName(u"promotionLabel")
        self.promotionLabel.setFont(font)

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.promotionLabel)

        self.promotionScrollArea = QScrollArea(self.scrollAreaWidgetContents)
        self.promotionScrollArea.setObjectName(u"promotionScrollArea")
        self.promotionScrollArea.setMinimumSize(QSize(0, 85))
        self.promotionScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.promotionScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(-178, 0, 500, 67))
        self.scrollAreaWidgetContents_2.setMinimumSize(QSize(500, 0))
        self.formLayout_2 = QFormLayout(self.scrollAreaWidgetContents_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setHorizontalSpacing(0)
        self.formLayout_2.setVerticalSpacing(0)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.promotionHorizontalLayout = QHBoxLayout()
        self.promotionHorizontalLayout.setSpacing(8)
        self.promotionHorizontalLayout.setObjectName(u"promotionHorizontalLayout")
        self.promotionPushButton6 = QPushButton(self.scrollAreaWidgetContents_2)
        self.promotionPushButton6.setObjectName(u"promotionPushButton6")
        self.promotionPushButton6.setMinimumSize(QSize(0, 65))
        font2 = QFont()
        font2.setPointSize(11)
        self.promotionPushButton6.setFont(font2)
        self.promotionPushButton6.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u"images/promotion.png", QSize(), QIcon.Normal, QIcon.Off)
        self.promotionPushButton6.setIcon(icon4)
        self.promotionPushButton6.setIconSize(QSize(20, 20))

        self.promotionHorizontalLayout.addWidget(self.promotionPushButton6)

        self.promotionPushButton5 = QPushButton(self.scrollAreaWidgetContents_2)
        self.promotionPushButton5.setObjectName(u"promotionPushButton5")
        self.promotionPushButton5.setMinimumSize(QSize(0, 65))
        self.promotionPushButton5.setFont(font2)
        self.promotionPushButton5.setCursor(QCursor(Qt.PointingHandCursor))
        self.promotionPushButton5.setIcon(icon4)
        self.promotionPushButton5.setIconSize(QSize(20, 20))

        self.promotionHorizontalLayout.addWidget(self.promotionPushButton5)

        self.promotionPushButton4 = QPushButton(self.scrollAreaWidgetContents_2)
        self.promotionPushButton4.setObjectName(u"promotionPushButton4")
        self.promotionPushButton4.setMinimumSize(QSize(0, 65))
        self.promotionPushButton4.setFont(font2)
        self.promotionPushButton4.setCursor(QCursor(Qt.PointingHandCursor))
        self.promotionPushButton4.setIcon(icon4)
        self.promotionPushButton4.setIconSize(QSize(20, 20))

        self.promotionHorizontalLayout.addWidget(self.promotionPushButton4)

        self.promotionPushButton3 = QPushButton(self.scrollAreaWidgetContents_2)
        self.promotionPushButton3.setObjectName(u"promotionPushButton3")
        self.promotionPushButton3.setMinimumSize(QSize(0, 65))
        self.promotionPushButton3.setFont(font2)
        self.promotionPushButton3.setCursor(QCursor(Qt.PointingHandCursor))
        self.promotionPushButton3.setIcon(icon4)
        self.promotionPushButton3.setIconSize(QSize(20, 20))

        self.promotionHorizontalLayout.addWidget(self.promotionPushButton3)

        self.promotionPushButton2 = QPushButton(self.scrollAreaWidgetContents_2)
        self.promotionPushButton2.setObjectName(u"promotionPushButton2")
        self.promotionPushButton2.setMinimumSize(QSize(0, 65))
        self.promotionPushButton2.setFont(font2)
        self.promotionPushButton2.setCursor(QCursor(Qt.PointingHandCursor))
        self.promotionPushButton2.setIcon(icon4)
        self.promotionPushButton2.setIconSize(QSize(20, 20))

        self.promotionHorizontalLayout.addWidget(self.promotionPushButton2)

        self.promotionPushButton1 = QPushButton(self.scrollAreaWidgetContents_2)
        self.promotionPushButton1.setObjectName(u"promotionPushButton1")
        self.promotionPushButton1.setMinimumSize(QSize(0, 65))
        self.promotionPushButton1.setFont(font2)
        self.promotionPushButton1.setCursor(QCursor(Qt.PointingHandCursor))
        self.promotionPushButton1.setIcon(icon4)
        self.promotionPushButton1.setIconSize(QSize(20, 20))

        self.promotionHorizontalLayout.addWidget(self.promotionPushButton1)


        self.formLayout_2.setLayout(0, QFormLayout.FieldRole, self.promotionHorizontalLayout)

        self.promotionScrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.formLayout.setWidget(8, QFormLayout.SpanningRole, self.promotionScrollArea)

        self.exclusivedealsLabel = QLabel(self.scrollAreaWidgetContents)
        self.exclusivedealsLabel.setObjectName(u"exclusivedealsLabel")
        self.exclusivedealsLabel.setFont(font)

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.exclusivedealsLabel)

        self.exclusivedealsScrollArea = QScrollArea(self.scrollAreaWidgetContents)
        self.exclusivedealsScrollArea.setObjectName(u"exclusivedealsScrollArea")
        self.exclusivedealsScrollArea.setMinimumSize(QSize(0, 94))
        self.exclusivedealsScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.exclusivedealsScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 500, 75))
        self.scrollAreaWidgetContents_3.setMinimumSize(QSize(500, 0))
        self.formLayout_3 = QFormLayout(self.scrollAreaWidgetContents_3)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setHorizontalSpacing(0)
        self.formLayout_3.setVerticalSpacing(0)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.exclusivedealsHorizontalLayout = QHBoxLayout()
        self.exclusivedealsHorizontalLayout.setSpacing(8)
        self.exclusivedealsHorizontalLayout.setObjectName(u"exclusivedealsHorizontalLayout")
        self.verticalLayout6 = QVBoxLayout()
        self.verticalLayout6.setSpacing(0)
        self.verticalLayout6.setObjectName(u"verticalLayout6")
        self.exclusivedealsLabel6 = QLabel(self.scrollAreaWidgetContents_3)
        self.exclusivedealsLabel6.setObjectName(u"exclusivedealsLabel6")
        self.exclusivedealsLabel6.setAlignment(Qt.AlignCenter)

        self.verticalLayout6.addWidget(self.exclusivedealsLabel6)

        self.exclusivedealsPushButton6 = QPushButton(self.scrollAreaWidgetContents_3)
        self.exclusivedealsPushButton6.setObjectName(u"exclusivedealsPushButton6")
        self.exclusivedealsPushButton6.setMinimumSize(QSize(0, 55))
        self.exclusivedealsPushButton6.setFont(font2)
        self.exclusivedealsPushButton6.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u"images/exlusivedeals.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exclusivedealsPushButton6.setIcon(icon5)
        self.exclusivedealsPushButton6.setIconSize(QSize(20, 20))

        self.verticalLayout6.addWidget(self.exclusivedealsPushButton6)


        self.exclusivedealsHorizontalLayout.addLayout(self.verticalLayout6)

        self.verticalLayout5 = QVBoxLayout()
        self.verticalLayout5.setSpacing(0)
        self.verticalLayout5.setObjectName(u"verticalLayout5")
        self.exclusivedealsLabel5 = QLabel(self.scrollAreaWidgetContents_3)
        self.exclusivedealsLabel5.setObjectName(u"exclusivedealsLabel5")
        self.exclusivedealsLabel5.setAlignment(Qt.AlignCenter)

        self.verticalLayout5.addWidget(self.exclusivedealsLabel5)

        self.exclusivedealsPushButton5 = QPushButton(self.scrollAreaWidgetContents_3)
        self.exclusivedealsPushButton5.setObjectName(u"exclusivedealsPushButton5")
        self.exclusivedealsPushButton5.setMinimumSize(QSize(0, 55))
        self.exclusivedealsPushButton5.setFont(font2)
        self.exclusivedealsPushButton5.setCursor(QCursor(Qt.PointingHandCursor))
        self.exclusivedealsPushButton5.setIcon(icon5)
        self.exclusivedealsPushButton5.setIconSize(QSize(20, 20))

        self.verticalLayout5.addWidget(self.exclusivedealsPushButton5)


        self.exclusivedealsHorizontalLayout.addLayout(self.verticalLayout5)

        self.verticalLayout4 = QVBoxLayout()
        self.verticalLayout4.setSpacing(0)
        self.verticalLayout4.setObjectName(u"verticalLayout4")
        self.exclusivedealsLabel4 = QLabel(self.scrollAreaWidgetContents_3)
        self.exclusivedealsLabel4.setObjectName(u"exclusivedealsLabel4")
        self.exclusivedealsLabel4.setAlignment(Qt.AlignCenter)

        self.verticalLayout4.addWidget(self.exclusivedealsLabel4)

        self.exclusivedealsPushButton4 = QPushButton(self.scrollAreaWidgetContents_3)
        self.exclusivedealsPushButton4.setObjectName(u"exclusivedealsPushButton4")
        self.exclusivedealsPushButton4.setMinimumSize(QSize(0, 55))
        self.exclusivedealsPushButton4.setFont(font2)
        self.exclusivedealsPushButton4.setCursor(QCursor(Qt.PointingHandCursor))
        self.exclusivedealsPushButton4.setIcon(icon5)
        self.exclusivedealsPushButton4.setIconSize(QSize(20, 20))

        self.verticalLayout4.addWidget(self.exclusivedealsPushButton4)


        self.exclusivedealsHorizontalLayout.addLayout(self.verticalLayout4)

        self.verticalLayout3 = QVBoxLayout()
        self.verticalLayout3.setSpacing(0)
        self.verticalLayout3.setObjectName(u"verticalLayout3")
        self.exclusivedealsLabel3 = QLabel(self.scrollAreaWidgetContents_3)
        self.exclusivedealsLabel3.setObjectName(u"exclusivedealsLabel3")
        self.exclusivedealsLabel3.setAlignment(Qt.AlignCenter)

        self.verticalLayout3.addWidget(self.exclusivedealsLabel3)

        self.exclusivedealsPushButton3 = QPushButton(self.scrollAreaWidgetContents_3)
        self.exclusivedealsPushButton3.setObjectName(u"exclusivedealsPushButton3")
        self.exclusivedealsPushButton3.setMinimumSize(QSize(0, 55))
        self.exclusivedealsPushButton3.setFont(font2)
        self.exclusivedealsPushButton3.setCursor(QCursor(Qt.PointingHandCursor))
        self.exclusivedealsPushButton3.setIcon(icon5)
        self.exclusivedealsPushButton3.setIconSize(QSize(20, 20))

        self.verticalLayout3.addWidget(self.exclusivedealsPushButton3)


        self.exclusivedealsHorizontalLayout.addLayout(self.verticalLayout3)

        self.verticalLayout2 = QVBoxLayout()
        self.verticalLayout2.setSpacing(0)
        self.verticalLayout2.setObjectName(u"verticalLayout2")
        self.exclusivedealsLabel2 = QLabel(self.scrollAreaWidgetContents_3)
        self.exclusivedealsLabel2.setObjectName(u"exclusivedealsLabel2")
        self.exclusivedealsLabel2.setAlignment(Qt.AlignCenter)

        self.verticalLayout2.addWidget(self.exclusivedealsLabel2)

        self.exclusivedealsPushButton2 = QPushButton(self.scrollAreaWidgetContents_3)
        self.exclusivedealsPushButton2.setObjectName(u"exclusivedealsPushButton2")
        self.exclusivedealsPushButton2.setMinimumSize(QSize(0, 55))
        self.exclusivedealsPushButton2.setFont(font2)
        self.exclusivedealsPushButton2.setCursor(QCursor(Qt.PointingHandCursor))
        self.exclusivedealsPushButton2.setIcon(icon5)
        self.exclusivedealsPushButton2.setIconSize(QSize(20, 20))

        self.verticalLayout2.addWidget(self.exclusivedealsPushButton2)


        self.exclusivedealsHorizontalLayout.addLayout(self.verticalLayout2)

        self.verticalLayout1 = QVBoxLayout()
        self.verticalLayout1.setSpacing(0)
        self.verticalLayout1.setObjectName(u"verticalLayout1")
        self.exclusivedealsLabel1 = QLabel(self.scrollAreaWidgetContents_3)
        self.exclusivedealsLabel1.setObjectName(u"exclusivedealsLabel1")
        self.exclusivedealsLabel1.setAlignment(Qt.AlignCenter)

        self.verticalLayout1.addWidget(self.exclusivedealsLabel1)

        self.exclusivedealsPushButton1 = QPushButton(self.scrollAreaWidgetContents_3)
        self.exclusivedealsPushButton1.setObjectName(u"exclusivedealsPushButton1")
        self.exclusivedealsPushButton1.setMinimumSize(QSize(0, 55))
        self.exclusivedealsPushButton1.setFont(font2)
        self.exclusivedealsPushButton1.setCursor(QCursor(Qt.PointingHandCursor))
        self.exclusivedealsPushButton1.setIcon(icon5)
        self.exclusivedealsPushButton1.setIconSize(QSize(20, 20))

        self.verticalLayout1.addWidget(self.exclusivedealsPushButton1)


        self.exclusivedealsHorizontalLayout.addLayout(self.verticalLayout1)


        self.formLayout_3.setLayout(0, QFormLayout.FieldRole, self.exclusivedealsHorizontalLayout)

        self.exclusivedealsScrollArea.setWidget(self.scrollAreaWidgetContents_3)

        self.formLayout.setWidget(10, QFormLayout.SpanningRole, self.exclusivedealsScrollArea)

        self.homeScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.stackedWidget.addWidget(self.homePage)
        self.historyPage = QWidget()
        self.historyPage.setObjectName(u"historyPage")
        self.historyScrollArea = QScrollArea(self.historyPage)
        self.historyScrollArea.setObjectName(u"historyScrollArea")
        self.historyScrollArea.setGeometry(QRect(0, 40, 361, 541))
        sizePolicy.setHeightForWidth(self.historyScrollArea.sizePolicy().hasHeightForWidth())
        self.historyScrollArea.setSizePolicy(sizePolicy)
        self.historyScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.historyScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 342, 550))
        self.scrollAreaWidgetContents_4.setMinimumSize(QSize(0, 550))
        self.formLayout_4 = QFormLayout(self.scrollAreaWidgetContents_4)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setHorizontalSpacing(0)
        self.formLayout_4.setVerticalSpacing(0)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.historyVerticalLayout = QVBoxLayout()
        self.historyVerticalLayout.setSpacing(0)
        self.historyVerticalLayout.setObjectName(u"historyVerticalLayout")
        self.historyVerticalLayout.setContentsMargins(20, -1, 20, -1)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.historyVerticalLayout.addItem(self.verticalSpacer)


        self.formLayout_4.setLayout(0, QFormLayout.FieldRole, self.historyVerticalLayout)

        self.historyScrollArea.setWidget(self.scrollAreaWidgetContents_4)
        self.historyLabel = QLabel(self.historyPage)
        self.historyLabel.setObjectName(u"historyLabel")
        self.historyLabel.setGeometry(QRect(20, 10, 121, 21))
        self.historyLabel.setFont(font2)
        self.stackedWidget.addWidget(self.historyPage)
        self.locationPage = QWidget()
        self.locationPage.setObjectName(u"locationPage")
        self.locationWidget = QWidget(self.locationPage)
        self.locationWidget.setObjectName(u"locationWidget")
        self.locationWidget.setGeometry(QRect(0, 40, 361, 541))
        self.locationLabel = QLabel(self.locationPage)
        self.locationLabel.setObjectName(u"locationLabel")
        self.locationLabel.setGeometry(QRect(20, 10, 71, 21))
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(False)
        self.locationLabel.setFont(font3)
        self.stackedWidget.addWidget(self.locationPage)
        self.accountPage = QWidget()
        self.accountPage.setObjectName(u"accountPage")
        self.accountLabel = QLabel(self.accountPage)
        self.accountLabel.setObjectName(u"accountLabel")
        self.accountLabel.setGeometry(QRect(20, 10, 121, 21))
        self.accountLabel.setFont(font2)
        self.stackedWidget.addWidget(self.accountPage)

        self.verticalLayout.addWidget(self.stackedWidget)

        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 580, 362, 61))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.homePushButton = QPushButton(self.horizontalLayoutWidget)
        self.homePushButton.setObjectName(u"homePushButton")
        self.homePushButton.setMinimumSize(QSize(90, 51))
        self.homePushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.homePushButton.setLayoutDirection(Qt.LeftToRight)
        self.homePushButton.setStyleSheet(u"QPushButton{\n"
"	border: None;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"images/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.homePushButton.setIcon(icon6)

        self.horizontalLayout.addWidget(self.homePushButton)

        self.historyPushButton = QPushButton(self.horizontalLayoutWidget)
        self.historyPushButton.setObjectName(u"historyPushButton")
        self.historyPushButton.setMinimumSize(QSize(90, 51))
        self.historyPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.historyPushButton.setStyleSheet(u"QPushButton{\n"
"	border: None;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"images/history.png", QSize(), QIcon.Normal, QIcon.Off)
        self.historyPushButton.setIcon(icon7)

        self.horizontalLayout.addWidget(self.historyPushButton)

        self.locationPushButton = QPushButton(self.horizontalLayoutWidget)
        self.locationPushButton.setObjectName(u"locationPushButton")
        self.locationPushButton.setMinimumSize(QSize(90, 51))
        self.locationPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.locationPushButton.setStyleSheet(u"QPushButton{\n"
"	border: None;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"images/location.png", QSize(), QIcon.Normal, QIcon.Off)
        self.locationPushButton.setIcon(icon8)
        self.locationPushButton.setIconSize(QSize(18, 18))

        self.horizontalLayout.addWidget(self.locationPushButton)

        self.accountPushButton = QPushButton(self.horizontalLayoutWidget)
        self.accountPushButton.setObjectName(u"accountPushButton")
        self.accountPushButton.setMinimumSize(QSize(90, 51))
        self.accountPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.accountPushButton.setStyleSheet(u"QPushButton{\n"
"	border: None;\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u"images/account.png", QSize(), QIcon.Normal, QIcon.Off)
        self.accountPushButton.setIcon(icon9)
        self.accountPushButton.setIconSize(QSize(17, 17))

        self.horizontalLayout.addWidget(self.accountPushButton)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.hiLabel.setText(QCoreApplication.translate("Form", u"Hi, ", None))
        self.welcomeLabel.setText(QCoreApplication.translate("Form", u"Welcome to E-DOCK!", None))
        self.otherservicesLabel.setText(QCoreApplication.translate("Form", u"Other Services", None))
        self.topupPushButton.setText("")
#if QT_CONFIG(tooltip)
        self.topupLabel.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.topupLabel.setWhatsThis(QCoreApplication.translate("Form", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.topupLabel.setText(QCoreApplication.translate("Form", u"Top-Up", None))
        self.paymentPushButton.setText("")
#if QT_CONFIG(tooltip)
        self.paymentLabel.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.paymentLabel.setWhatsThis(QCoreApplication.translate("Form", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.paymentLabel.setText(QCoreApplication.translate("Form", u"Payment", None))
        self.carsPushButton.setText("")
#if QT_CONFIG(tooltip)
        self.carsLabel.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.carsLabel.setWhatsThis(QCoreApplication.translate("Form", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.carsLabel.setText(QCoreApplication.translate("Form", u"Cars", None))
        self.cardsPushButton.setText("")
#if QT_CONFIG(tooltip)
        self.cardsLabel.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.cardsLabel.setWhatsThis(QCoreApplication.translate("Form", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.cardsLabel.setText(QCoreApplication.translate("Form", u"Cards", None))
        self.promotionLabel.setText(QCoreApplication.translate("Form", u"Promotions", None))
        self.promotionPushButton6.setText(QCoreApplication.translate("Form", u" 55%", None))
        self.promotionPushButton5.setText(QCoreApplication.translate("Form", u" 50%", None))
        self.promotionPushButton4.setText(QCoreApplication.translate("Form", u" 45%", None))
        self.promotionPushButton3.setText(QCoreApplication.translate("Form", u" 40%", None))
        self.promotionPushButton2.setText(QCoreApplication.translate("Form", u" 35%", None))
        self.promotionPushButton1.setText(QCoreApplication.translate("Form", u" 30%", None))
        self.exclusivedealsLabel.setText(QCoreApplication.translate("Form", u"Exclusive Deals for debit/credit card user", None))
        self.exclusivedealsLabel6.setText(QCoreApplication.translate("Form", u"CITI", None))
        self.exclusivedealsPushButton6.setText(QCoreApplication.translate("Form", u" 150.-", None))
        self.exclusivedealsLabel5.setText(QCoreApplication.translate("Form", u"CENTRAL", None))
        self.exclusivedealsPushButton5.setText(QCoreApplication.translate("Form", u" 100.-", None))
        self.exclusivedealsLabel4.setText(QCoreApplication.translate("Form", u"CIMB THAI", None))
        self.exclusivedealsPushButton4.setText(QCoreApplication.translate("Form", u" 80.-", None))
        self.exclusivedealsLabel3.setText(QCoreApplication.translate("Form", u"Krungsri", None))
        self.exclusivedealsPushButton3.setText(QCoreApplication.translate("Form", u" 80.-", None))
        self.exclusivedealsLabel2.setText(QCoreApplication.translate("Form", u"TTB", None))
        self.exclusivedealsPushButton2.setText(QCoreApplication.translate("Form", u" 60.-", None))
        self.exclusivedealsLabel1.setText(QCoreApplication.translate("Form", u"VISA", None))
        self.exclusivedealsPushButton1.setText(QCoreApplication.translate("Form", u" 50.-", None))
        self.historyLabel.setText(QCoreApplication.translate("Form", u"Charging History", None))
        self.locationLabel.setText(QCoreApplication.translate("Form", u"Location", None))
        self.accountLabel.setText(QCoreApplication.translate("Form", u"Account Settings", None))
#if QT_CONFIG(whatsthis)
        self.homePushButton.setWhatsThis(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.homePushButton.setText(QCoreApplication.translate("Form", u" Home", None))
        self.historyPushButton.setText(QCoreApplication.translate("Form", u" History", None))
        self.locationPushButton.setText(QCoreApplication.translate("Form", u" Location", None))
        self.accountPushButton.setText(QCoreApplication.translate("Form", u" Account", None))
    # retranslateUi

