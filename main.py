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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(362, 640)
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 342, 687))
        self.formLayout = QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setContentsMargins(20, 20, 20, 20)
        self.searchLineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.searchLineEdit.setObjectName(u"searchLineEdit")
        self.searchLineEdit.setMinimumSize(QSize(0, 35))

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.searchLineEdit)

        self.stationScrollArea = QScrollArea(self.scrollAreaWidgetContents)
        self.stationScrollArea.setObjectName(u"stationScrollArea")
        self.stationScrollArea.setMinimumSize(QSize(0, 192))
        self.stationScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.stationScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.stationScrollArea.setWidgetResizable(True)
        self.stationAreaWidgetContents = QWidget()
        self.stationAreaWidgetContents.setObjectName(u"stationAreaWidgetContents")
        self.stationAreaWidgetContents.setGeometry(QRect(0, 0, 300, 175))
        self.stationAreaWidgetContents.setMinimumSize(QSize(0, 0))
        self.formLayout_6 = QFormLayout(self.stationAreaWidgetContents)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.formLayout_6.setHorizontalSpacing(0)
        self.formLayout_6.setVerticalSpacing(0)
        self.formLayout_6.setContentsMargins(0, 0, 0, 0)
        self.stationHorizontalLayout = QHBoxLayout()
        self.stationHorizontalLayout.setSpacing(6)
        self.stationHorizontalLayout.setObjectName(u"stationHorizontalLayout")
        self.stationHorizontalLayout.setContentsMargins(0, 0, -1, -1)
        self.stationVerticalLayout = QVBoxLayout()
        self.stationVerticalLayout.setObjectName(u"stationVerticalLayout")
        self.stationVerticalLayout.setContentsMargins(6, 6, 6, 0)
        self.promotionPushButton6_3 = QPushButton(self.stationAreaWidgetContents)
        self.promotionPushButton6_3.setObjectName(u"promotionPushButton6_3")
        self.promotionPushButton6_3.setMinimumSize(QSize(83, 80))
        self.promotionPushButton6_3.setMaximumSize(QSize(85, 80))
        font = QFont()
        font.setPointSize(11)
        self.promotionPushButton6_3.setFont(font)
        self.promotionPushButton6_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.promotionPushButton6_3.setIconSize(QSize(20, 20))

        self.stationVerticalLayout.addWidget(self.promotionPushButton6_3)

        self.promotionPushButton6_4 = QPushButton(self.stationAreaWidgetContents)
        self.promotionPushButton6_4.setObjectName(u"promotionPushButton6_4")
        self.promotionPushButton6_4.setMinimumSize(QSize(83, 80))
        self.promotionPushButton6_4.setMaximumSize(QSize(80, 80))
        self.promotionPushButton6_4.setFont(font)
        self.promotionPushButton6_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.promotionPushButton6_4.setIconSize(QSize(20, 20))

        self.stationVerticalLayout.addWidget(self.promotionPushButton6_4)


        self.stationHorizontalLayout.addLayout(self.stationVerticalLayout)

        self.stationVerticalLayout_2 = QVBoxLayout()
        self.stationVerticalLayout_2.setObjectName(u"stationVerticalLayout_2")
        self.stationVerticalLayout_2.setContentsMargins(6, 6, 6, 0)
        self.promotionPushButton6_5 = QPushButton(self.stationAreaWidgetContents)
        self.promotionPushButton6_5.setObjectName(u"promotionPushButton6_5")
        self.promotionPushButton6_5.setMinimumSize(QSize(83, 80))
        self.promotionPushButton6_5.setMaximumSize(QSize(80, 80))
        self.promotionPushButton6_5.setFont(font)
        self.promotionPushButton6_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.promotionPushButton6_5.setIconSize(QSize(20, 20))

        self.stationVerticalLayout_2.addWidget(self.promotionPushButton6_5)

        self.promotionPushButton6_6 = QPushButton(self.stationAreaWidgetContents)
        self.promotionPushButton6_6.setObjectName(u"promotionPushButton6_6")
        self.promotionPushButton6_6.setMinimumSize(QSize(83, 80))
        self.promotionPushButton6_6.setMaximumSize(QSize(80, 80))
        self.promotionPushButton6_6.setFont(font)
        self.promotionPushButton6_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.promotionPushButton6_6.setIconSize(QSize(20, 20))

        self.stationVerticalLayout_2.addWidget(self.promotionPushButton6_6)


        self.stationHorizontalLayout.addLayout(self.stationVerticalLayout_2)


        self.formLayout_6.setLayout(0, QFormLayout.FieldRole, self.stationHorizontalLayout)

        self.stationScrollArea.setWidget(self.stationAreaWidgetContents)

        self.formLayout.setWidget(4, QFormLayout.SpanningRole, self.stationScrollArea)

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

        self.promotionScrollArea = QScrollArea(self.scrollAreaWidgetContents)
        self.promotionScrollArea.setObjectName(u"promotionScrollArea")
        self.promotionScrollArea.setMinimumSize(QSize(0, 85))
        self.promotionScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.promotionScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 500, 67))
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
        self.promotionPushButton6.setFont(font)
        self.promotionPushButton6.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u"images/promotion.png", QSize(), QIcon.Normal, QIcon.Off)
        self.promotionPushButton6.setIcon(icon4)
        self.promotionPushButton6.setIconSize(QSize(20, 20))

        self.promotionHorizontalLayout.addWidget(self.promotionPushButton6)

        self.promotionPushButton5 = QPushButton(self.scrollAreaWidgetContents_2)
        self.promotionPushButton5.setObjectName(u"promotionPushButton5")
        self.promotionPushButton5.setMinimumSize(QSize(0, 65))
        self.promotionPushButton5.setFont(font)
        self.promotionPushButton5.setCursor(QCursor(Qt.PointingHandCursor))
        self.promotionPushButton5.setIcon(icon4)
        self.promotionPushButton5.setIconSize(QSize(20, 20))

        self.promotionHorizontalLayout.addWidget(self.promotionPushButton5)

        self.promotionPushButton4 = QPushButton(self.scrollAreaWidgetContents_2)
        self.promotionPushButton4.setObjectName(u"promotionPushButton4")
        self.promotionPushButton4.setMinimumSize(QSize(0, 65))
        self.promotionPushButton4.setFont(font)
        self.promotionPushButton4.setCursor(QCursor(Qt.PointingHandCursor))
        self.promotionPushButton4.setIcon(icon4)
        self.promotionPushButton4.setIconSize(QSize(20, 20))

        self.promotionHorizontalLayout.addWidget(self.promotionPushButton4)

        self.promotionPushButton3 = QPushButton(self.scrollAreaWidgetContents_2)
        self.promotionPushButton3.setObjectName(u"promotionPushButton3")
        self.promotionPushButton3.setMinimumSize(QSize(0, 65))
        self.promotionPushButton3.setFont(font)
        self.promotionPushButton3.setCursor(QCursor(Qt.PointingHandCursor))
        self.promotionPushButton3.setIcon(icon4)
        self.promotionPushButton3.setIconSize(QSize(20, 20))

        self.promotionHorizontalLayout.addWidget(self.promotionPushButton3)

        self.promotionPushButton2 = QPushButton(self.scrollAreaWidgetContents_2)
        self.promotionPushButton2.setObjectName(u"promotionPushButton2")
        self.promotionPushButton2.setMinimumSize(QSize(0, 65))
        self.promotionPushButton2.setFont(font)
        self.promotionPushButton2.setCursor(QCursor(Qt.PointingHandCursor))
        self.promotionPushButton2.setIcon(icon4)
        self.promotionPushButton2.setIconSize(QSize(20, 20))

        self.promotionHorizontalLayout.addWidget(self.promotionPushButton2)

        self.promotionPushButton1 = QPushButton(self.scrollAreaWidgetContents_2)
        self.promotionPushButton1.setObjectName(u"promotionPushButton1")
        self.promotionPushButton1.setMinimumSize(QSize(0, 65))
        self.promotionPushButton1.setFont(font)
        self.promotionPushButton1.setCursor(QCursor(Qt.PointingHandCursor))
        self.promotionPushButton1.setIcon(icon4)
        self.promotionPushButton1.setIconSize(QSize(20, 20))

        self.promotionHorizontalLayout.addWidget(self.promotionPushButton1)


        self.formLayout_2.setLayout(0, QFormLayout.FieldRole, self.promotionHorizontalLayout)

        self.promotionScrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.formLayout.setWidget(8, QFormLayout.SpanningRole, self.promotionScrollArea)

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
        self.exclusivedealsPushButton6.setFont(font)
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
        self.exclusivedealsPushButton5.setFont(font)
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
        self.exclusivedealsPushButton4.setFont(font)
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
        self.exclusivedealsPushButton3.setFont(font)
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
        self.exclusivedealsPushButton2.setFont(font)
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
        self.exclusivedealsPushButton1.setFont(font)
        self.exclusivedealsPushButton1.setCursor(QCursor(Qt.PointingHandCursor))
        self.exclusivedealsPushButton1.setIcon(icon5)
        self.exclusivedealsPushButton1.setIconSize(QSize(20, 20))

        self.verticalLayout1.addWidget(self.exclusivedealsPushButton1)


        self.exclusivedealsHorizontalLayout.addLayout(self.verticalLayout1)


        self.formLayout_3.setLayout(0, QFormLayout.FieldRole, self.exclusivedealsHorizontalLayout)

        self.exclusivedealsScrollArea.setWidget(self.scrollAreaWidgetContents_3)

        self.formLayout.setWidget(10, QFormLayout.SpanningRole, self.exclusivedealsScrollArea)

        self.hiLabel = QLabel(self.scrollAreaWidgetContents)
        self.hiLabel.setObjectName(u"hiLabel")
        font1 = QFont()
        font1.setPointSize(10)
        self.hiLabel.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.hiLabel)

        self.welcomeLabel = QLabel(self.scrollAreaWidgetContents)
        self.welcomeLabel.setObjectName(u"welcomeLabel")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.welcomeLabel.setFont(font2)

        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.welcomeLabel)

        self.otherservicesLabel = QLabel(self.scrollAreaWidgetContents)
        self.otherservicesLabel.setObjectName(u"otherservicesLabel")
        self.otherservicesLabel.setFont(font1)

        self.formLayout.setWidget(5, QFormLayout.SpanningRole, self.otherservicesLabel)

        self.promotionLabel = QLabel(self.scrollAreaWidgetContents)
        self.promotionLabel.setObjectName(u"promotionLabel")
        self.promotionLabel.setFont(font1)

        self.formLayout.setWidget(7, QFormLayout.SpanningRole, self.promotionLabel)

        self.exclusivedealsLabel = QLabel(self.scrollAreaWidgetContents)
        self.exclusivedealsLabel.setObjectName(u"exclusivedealsLabel")
        self.exclusivedealsLabel.setFont(font1)

        self.formLayout.setWidget(9, QFormLayout.SpanningRole, self.exclusivedealsLabel)

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
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 359, 539))
        self.scrollAreaWidgetContents_4.setMinimumSize(QSize(0, 0))
        self.formLayout_4 = QFormLayout(self.scrollAreaWidgetContents_4)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setHorizontalSpacing(0)
        self.formLayout_4.setVerticalSpacing(0)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.historyVerticalLayout = QVBoxLayout()
        self.historyVerticalLayout.setSpacing(6)
        self.historyVerticalLayout.setObjectName(u"historyVerticalLayout")
        self.historyVerticalLayout.setContentsMargins(0, 10, 0, -1)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.line = QFrame(self.scrollAreaWidgetContents_4)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.pushButton = QPushButton(self.scrollAreaWidgetContents_4)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 50))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"}")

        self.verticalLayout_2.addWidget(self.pushButton)

        self.line_2 = QFrame(self.scrollAreaWidgetContents_4)
        self.line_2.setObjectName(u"line_2")
        font3 = QFont()
        font3.setBold(False)
        self.line_2.setFont(font3)
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)


        self.historyVerticalLayout.addLayout(self.verticalLayout_2)

        self.historyVerticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.historyVerticalLayout.addItem(self.historyVerticalSpacer)


        self.formLayout_4.setLayout(0, QFormLayout.FieldRole, self.historyVerticalLayout)

        self.historyScrollArea.setWidget(self.scrollAreaWidgetContents_4)
        self.historyLabel = QLabel(self.historyPage)
        self.historyLabel.setObjectName(u"historyLabel")
        self.historyLabel.setGeometry(QRect(20, 10, 121, 21))
        self.historyLabel.setFont(font)
        self.stackedWidget.addWidget(self.historyPage)
        self.locationPage = QWidget()
        self.locationPage.setObjectName(u"locationPage")
        self.locationWidget = QWidget(self.locationPage)
        self.locationWidget.setObjectName(u"locationWidget")
        self.locationWidget.setGeometry(QRect(0, 40, 361, 541))
        self.locationLabel = QLabel(self.locationPage)
        self.locationLabel.setObjectName(u"locationLabel")
        self.locationLabel.setGeometry(QRect(20, 10, 71, 21))
        font4 = QFont()
        font4.setPointSize(11)
        font4.setBold(False)
        self.locationLabel.setFont(font4)
        self.stackedWidget.addWidget(self.locationPage)
        self.accountPage = QWidget()
        self.accountPage.setObjectName(u"accountPage")
        self.accountLabel = QLabel(self.accountPage)
        self.accountLabel.setObjectName(u"accountLabel")
        self.accountLabel.setGeometry(QRect(20, 10, 121, 21))
        self.accountLabel.setFont(font)
        self.accountScrollArea = QScrollArea(self.accountPage)
        self.accountScrollArea.setObjectName(u"accountScrollArea")
        self.accountScrollArea.setGeometry(QRect(0, 40, 361, 541))
        sizePolicy.setHeightForWidth(self.accountScrollArea.sizePolicy().hasHeightForWidth())
        self.accountScrollArea.setSizePolicy(sizePolicy)
        self.accountScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.accountScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 342, 1136))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollAreaWidgetContents_5.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_5.setSizePolicy(sizePolicy1)
        self.scrollAreaWidgetContents_5.setMinimumSize(QSize(0, 0))
        self.formLayout_5 = QFormLayout(self.scrollAreaWidgetContents_5)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.formLayout_5.setHorizontalSpacing(0)
        self.formLayout_5.setVerticalSpacing(0)
        self.formLayout_5.setContentsMargins(0, 0, 0, 0)
        self.accountVerticalLayout = QVBoxLayout()
        self.accountVerticalLayout.setSpacing(0)
        self.accountVerticalLayout.setObjectName(u"accountVerticalLayout")
        self.accountVerticalLayout.setContentsMargins(0, 10, 0, 10)
        self.ewalletLabel = QLabel(self.scrollAreaWidgetContents_5)
        self.ewalletLabel.setObjectName(u"ewalletLabel")
        self.ewalletLabel.setFont(font1)
        self.ewalletLabel.setAlignment(Qt.AlignCenter)

        self.accountVerticalLayout.addWidget(self.ewalletLabel)

        self.moneyLabel = QLabel(self.scrollAreaWidgetContents_5)
        self.moneyLabel.setObjectName(u"moneyLabel")
        self.moneyLabel.setMinimumSize(QSize(0, 65))
        font5 = QFont()
        font5.setPointSize(24)
        self.moneyLabel.setFont(font5)
        self.moneyLabel.setAlignment(Qt.AlignCenter)

        self.accountVerticalLayout.addWidget(self.moneyLabel)

        self.notificationPushButton = QPushButton(self.scrollAreaWidgetContents_5)
        self.notificationPushButton.setObjectName(u"notificationPushButton")
        self.notificationPushButton.setMinimumSize(QSize(0, 35))
        self.notificationPushButton.setFont(font1)
        self.notificationPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.notificationPushButton.setTabletTracking(False)
        self.notificationPushButton.setLayoutDirection(Qt.RightToLeft)
        icon6 = QIcon()
        icon6.addFile(u"images/right-arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.notificationPushButton.setIcon(icon6)
        self.notificationPushButton.setIconSize(QSize(21, 21))
        self.notificationPushButton.setAutoExclusive(False)
        self.notificationPushButton.setAutoDefault(False)
        self.notificationPushButton.setFlat(False)

        self.accountVerticalLayout.addWidget(self.notificationPushButton)

        self.notificationWidget = QWidget(self.scrollAreaWidgetContents_5)
        self.notificationWidget.setObjectName(u"notificationWidget")
        sizePolicy1.setHeightForWidth(self.notificationWidget.sizePolicy().hasHeightForWidth())
        self.notificationWidget.setSizePolicy(sizePolicy1)
        self.notificationWidget.setMinimumSize(QSize(0, 73))
        self.layoutWidget = QWidget(self.notificationWidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 340, 73))
        self.notificationVerticalLayout = QVBoxLayout(self.layoutWidget)
        self.notificationVerticalLayout.setObjectName(u"notificationVerticalLayout")
        self.notificationVerticalLayout.setContentsMargins(20, 10, 20, 0)
        self.opennotificationRadioButton = QRadioButton(self.layoutWidget)
        self.opennotificationRadioButton.setObjectName(u"opennotificationRadioButton")
        self.opennotificationRadioButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.notificationVerticalLayout.addWidget(self.opennotificationRadioButton)

        self.closenotificationRadioButton = QRadioButton(self.layoutWidget)
        self.closenotificationRadioButton.setObjectName(u"closenotificationRadioButton")
        self.closenotificationRadioButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.notificationVerticalLayout.addWidget(self.closenotificationRadioButton)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.notificationVerticalLayout.addItem(self.verticalSpacer_2)


        self.accountVerticalLayout.addWidget(self.notificationWidget)

        self.addcarPushButton = QPushButton(self.scrollAreaWidgetContents_5)
        self.addcarPushButton.setObjectName(u"addcarPushButton")
        self.addcarPushButton.setMinimumSize(QSize(0, 35))
        self.addcarPushButton.setFont(font1)
        self.addcarPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.addcarPushButton.setTabletTracking(False)
        self.addcarPushButton.setLayoutDirection(Qt.RightToLeft)
        self.addcarPushButton.setIcon(icon6)
        self.addcarPushButton.setIconSize(QSize(21, 21))
        self.addcarPushButton.setAutoExclusive(False)
        self.addcarPushButton.setAutoDefault(False)

        self.accountVerticalLayout.addWidget(self.addcarPushButton)

        self.addcarWidget = QWidget(self.scrollAreaWidgetContents_5)
        self.addcarWidget.setObjectName(u"addcarWidget")
        sizePolicy1.setHeightForWidth(self.addcarWidget.sizePolicy().hasHeightForWidth())
        self.addcarWidget.setSizePolicy(sizePolicy1)
        self.addcarWidget.setMinimumSize(QSize(0, 273))
        self.layoutWidget1 = QWidget(self.addcarWidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 0, 340, 273))
        self.addcarVerticalLayout = QVBoxLayout(self.layoutWidget1)
        self.addcarVerticalLayout.setSpacing(3)
        self.addcarVerticalLayout.setObjectName(u"addcarVerticalLayout")
        self.addcarVerticalLayout.setContentsMargins(20, 10, 20, 10)
        self.companyLabel = QLabel(self.layoutWidget1)
        self.companyLabel.setObjectName(u"companyLabel")

        self.addcarVerticalLayout.addWidget(self.companyLabel)

        self.companyLineEdit = QLineEdit(self.layoutWidget1)
        self.companyLineEdit.setObjectName(u"companyLineEdit")
        self.companyLineEdit.setMinimumSize(QSize(0, 30))

        self.addcarVerticalLayout.addWidget(self.companyLineEdit)

        self.modelLabel = QLabel(self.layoutWidget1)
        self.modelLabel.setObjectName(u"modelLabel")

        self.addcarVerticalLayout.addWidget(self.modelLabel)

        self.modelLineEdit = QLineEdit(self.layoutWidget1)
        self.modelLineEdit.setObjectName(u"modelLineEdit")
        self.modelLineEdit.setMinimumSize(QSize(0, 30))

        self.addcarVerticalLayout.addWidget(self.modelLineEdit)

        self.batterycapacityLabel = QLabel(self.layoutWidget1)
        self.batterycapacityLabel.setObjectName(u"batterycapacityLabel")

        self.addcarVerticalLayout.addWidget(self.batterycapacityLabel)

        self.batterycapacityLineEdit = QLineEdit(self.layoutWidget1)
        self.batterycapacityLineEdit.setObjectName(u"batterycapacityLineEdit")
        self.batterycapacityLineEdit.setMinimumSize(QSize(0, 30))

        self.addcarVerticalLayout.addWidget(self.batterycapacityLineEdit)

        self.chargingcapacityLabel = QLabel(self.layoutWidget1)
        self.chargingcapacityLabel.setObjectName(u"chargingcapacityLabel")

        self.addcarVerticalLayout.addWidget(self.chargingcapacityLabel)

        self.chargingcapacityLineEdit = QLineEdit(self.layoutWidget1)
        self.chargingcapacityLineEdit.setObjectName(u"chargingcapacityLineEdit")
        self.chargingcapacityLineEdit.setMinimumSize(QSize(0, 30))

        self.addcarVerticalLayout.addWidget(self.chargingcapacityLineEdit)

        self.verticalSpacer_6 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.addcarVerticalLayout.addItem(self.verticalSpacer_6)

        self.addcarHorizontalLayout = QHBoxLayout()
        self.addcarHorizontalLayout.setSpacing(0)
        self.addcarHorizontalLayout.setObjectName(u"addcarHorizontalLayout")
        self.addcarPushButton_2 = QPushButton(self.layoutWidget1)
        self.addcarPushButton_2.setObjectName(u"addcarPushButton_2")
        self.addcarPushButton_2.setMinimumSize(QSize(0, 30))
        self.addcarPushButton_2.setMaximumSize(QSize(100, 16777215))
        self.addcarPushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u"images/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addcarPushButton_2.setIcon(icon7)
        self.addcarPushButton_2.setIconSize(QSize(20, 20))

        self.addcarHorizontalLayout.addWidget(self.addcarPushButton_2)


        self.addcarVerticalLayout.addLayout(self.addcarHorizontalLayout)


        self.accountVerticalLayout.addWidget(self.addcarWidget)

        self.addcardPushButton = QPushButton(self.scrollAreaWidgetContents_5)
        self.addcardPushButton.setObjectName(u"addcardPushButton")
        self.addcardPushButton.setMinimumSize(QSize(0, 35))
        self.addcardPushButton.setFont(font1)
        self.addcardPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.addcardPushButton.setTabletTracking(False)
        self.addcardPushButton.setLayoutDirection(Qt.RightToLeft)
        self.addcardPushButton.setIcon(icon6)
        self.addcardPushButton.setIconSize(QSize(21, 21))
        self.addcardPushButton.setAutoExclusive(False)
        self.addcardPushButton.setAutoDefault(False)

        self.accountVerticalLayout.addWidget(self.addcardPushButton)

        self.addcardWidget = QWidget(self.scrollAreaWidgetContents_5)
        self.addcardWidget.setObjectName(u"addcardWidget")
        self.addcardWidget.setMinimumSize(QSize(0, 273))
        self.layoutWidget2 = QWidget(self.addcardWidget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(0, 0, 340, 273))
        self.addcardVerticalLayout = QVBoxLayout(self.layoutWidget2)
        self.addcardVerticalLayout.setSpacing(3)
        self.addcardVerticalLayout.setObjectName(u"addcardVerticalLayout")
        self.addcardVerticalLayout.setContentsMargins(20, 10, 20, 10)
        self.cardnumberLabel = QLabel(self.layoutWidget2)
        self.cardnumberLabel.setObjectName(u"cardnumberLabel")

        self.addcardVerticalLayout.addWidget(self.cardnumberLabel)

        self.cardnumberLineEdit = QLineEdit(self.layoutWidget2)
        self.cardnumberLineEdit.setObjectName(u"cardnumberLineEdit")
        self.cardnumberLineEdit.setMinimumSize(QSize(0, 30))

        self.addcardVerticalLayout.addWidget(self.cardnumberLineEdit)

        self.cardholdernameLabel = QLabel(self.layoutWidget2)
        self.cardholdernameLabel.setObjectName(u"cardholdernameLabel")

        self.addcardVerticalLayout.addWidget(self.cardholdernameLabel)

        self.cardholdernameLineEdit = QLineEdit(self.layoutWidget2)
        self.cardholdernameLineEdit.setObjectName(u"cardholdernameLineEdit")
        self.cardholdernameLineEdit.setMinimumSize(QSize(0, 30))

        self.addcardVerticalLayout.addWidget(self.cardholdernameLineEdit)

        self.expiryLabel = QLabel(self.layoutWidget2)
        self.expiryLabel.setObjectName(u"expiryLabel")

        self.addcardVerticalLayout.addWidget(self.expiryLabel)

        self.expiryLineEdit = QLineEdit(self.layoutWidget2)
        self.expiryLineEdit.setObjectName(u"expiryLineEdit")
        self.expiryLineEdit.setMinimumSize(QSize(0, 30))

        self.addcardVerticalLayout.addWidget(self.expiryLineEdit)

        self.cvvLabel = QLabel(self.layoutWidget2)
        self.cvvLabel.setObjectName(u"cvvLabel")

        self.addcardVerticalLayout.addWidget(self.cvvLabel)

        self.cvvLineEdit = QLineEdit(self.layoutWidget2)
        self.cvvLineEdit.setObjectName(u"cvvLineEdit")
        self.cvvLineEdit.setMinimumSize(QSize(0, 30))

        self.addcardVerticalLayout.addWidget(self.cvvLineEdit)

        self.verticalSpacer_7 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.addcardVerticalLayout.addItem(self.verticalSpacer_7)

        self.addcardHorizontalLayout = QHBoxLayout()
        self.addcardHorizontalLayout.setSpacing(0)
        self.addcardHorizontalLayout.setObjectName(u"addcardHorizontalLayout")
        self.addcardPushButton_2 = QPushButton(self.layoutWidget2)
        self.addcardPushButton_2.setObjectName(u"addcardPushButton_2")
        self.addcardPushButton_2.setMinimumSize(QSize(0, 30))
        self.addcardPushButton_2.setMaximumSize(QSize(100, 16777215))
        self.addcardPushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.addcardPushButton_2.setIcon(icon7)
        self.addcardPushButton_2.setIconSize(QSize(20, 20))

        self.addcardHorizontalLayout.addWidget(self.addcardPushButton_2)


        self.addcardVerticalLayout.addLayout(self.addcardHorizontalLayout)


        self.accountVerticalLayout.addWidget(self.addcardWidget)

        self.changeusernamePushButton = QPushButton(self.scrollAreaWidgetContents_5)
        self.changeusernamePushButton.setObjectName(u"changeusernamePushButton")
        self.changeusernamePushButton.setMinimumSize(QSize(0, 35))
        self.changeusernamePushButton.setFont(font1)
        self.changeusernamePushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.changeusernamePushButton.setLayoutDirection(Qt.RightToLeft)
        self.changeusernamePushButton.setIcon(icon6)
        self.changeusernamePushButton.setIconSize(QSize(21, 21))

        self.accountVerticalLayout.addWidget(self.changeusernamePushButton)

        self.changeusernameWidget = QWidget(self.scrollAreaWidgetContents_5)
        self.changeusernameWidget.setObjectName(u"changeusernameWidget")
        self.changeusernameWidget.setMinimumSize(QSize(0, 117))
        self.layoutWidget3 = QWidget(self.changeusernameWidget)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(0, 0, 340, 117))
        self.changeusernameVerticalLayout = QVBoxLayout(self.layoutWidget3)
        self.changeusernameVerticalLayout.setSpacing(3)
        self.changeusernameVerticalLayout.setObjectName(u"changeusernameVerticalLayout")
        self.changeusernameVerticalLayout.setContentsMargins(20, 10, 20, 10)
        self.newusernameLabel = QLabel(self.layoutWidget3)
        self.newusernameLabel.setObjectName(u"newusernameLabel")

        self.changeusernameVerticalLayout.addWidget(self.newusernameLabel)

        self.newusernameLineEdit = QLineEdit(self.layoutWidget3)
        self.newusernameLineEdit.setObjectName(u"newusernameLineEdit")
        self.newusernameLineEdit.setMinimumSize(QSize(0, 30))

        self.changeusernameVerticalLayout.addWidget(self.newusernameLineEdit)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.changeusernameVerticalLayout.addItem(self.verticalSpacer_3)

        self.changeusernameHorizontalLayout = QHBoxLayout()
        self.changeusernameHorizontalLayout.setSpacing(0)
        self.changeusernameHorizontalLayout.setObjectName(u"changeusernameHorizontalLayout")
        self.changeusernamePushButton_2 = QPushButton(self.layoutWidget3)
        self.changeusernamePushButton_2.setObjectName(u"changeusernamePushButton_2")
        self.changeusernamePushButton_2.setMinimumSize(QSize(0, 30))
        self.changeusernamePushButton_2.setMaximumSize(QSize(100, 16777215))
        self.changeusernamePushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u"images/change.png", QSize(), QIcon.Normal, QIcon.Off)
        self.changeusernamePushButton_2.setIcon(icon8)
        self.changeusernamePushButton_2.setIconSize(QSize(16, 16))

        self.changeusernameHorizontalLayout.addWidget(self.changeusernamePushButton_2)


        self.changeusernameVerticalLayout.addLayout(self.changeusernameHorizontalLayout)


        self.accountVerticalLayout.addWidget(self.changeusernameWidget)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(100, 20, 100, 20)
        self.changepinPushButton = QPushButton(self.scrollAreaWidgetContents_5)
        self.changepinPushButton.setObjectName(u"changepinPushButton")
        self.changepinPushButton.setMinimumSize(QSize(0, 35))
        self.changepinPushButton.setFont(font)
        self.changepinPushButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.changepinPushButton)

        self.changepasswordPushButton = QPushButton(self.scrollAreaWidgetContents_5)
        self.changepasswordPushButton.setObjectName(u"changepasswordPushButton")
        self.changepasswordPushButton.setMinimumSize(QSize(0, 35))
        self.changepasswordPushButton.setFont(font)
        self.changepasswordPushButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.changepasswordPushButton)

        self.logoutPushButton = QPushButton(self.scrollAreaWidgetContents_5)
        self.logoutPushButton.setObjectName(u"logoutPushButton")
        self.logoutPushButton.setMinimumSize(QSize(0, 35))
        self.logoutPushButton.setFont(font)
        self.logoutPushButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.logoutPushButton)


        self.accountVerticalLayout.addLayout(self.verticalLayout_3)

        self.accountVerticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.accountVerticalLayout.addItem(self.accountVerticalSpacer)


        self.formLayout_5.setLayout(0, QFormLayout.FieldRole, self.accountVerticalLayout)

        self.accountScrollArea.setWidget(self.scrollAreaWidgetContents_5)
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
        icon9 = QIcon()
        icon9.addFile(u"images/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.homePushButton.setIcon(icon9)

        self.horizontalLayout.addWidget(self.homePushButton)

        self.historyPushButton = QPushButton(self.horizontalLayoutWidget)
        self.historyPushButton.setObjectName(u"historyPushButton")
        self.historyPushButton.setMinimumSize(QSize(90, 51))
        self.historyPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.historyPushButton.setStyleSheet(u"QPushButton{\n"
"	border: None;\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u"images/history.png", QSize(), QIcon.Normal, QIcon.Off)
        self.historyPushButton.setIcon(icon10)

        self.horizontalLayout.addWidget(self.historyPushButton)

        self.locationPushButton = QPushButton(self.horizontalLayoutWidget)
        self.locationPushButton.setObjectName(u"locationPushButton")
        self.locationPushButton.setMinimumSize(QSize(90, 51))
        self.locationPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.locationPushButton.setStyleSheet(u"QPushButton{\n"
"	border: None;\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u"images/location.png", QSize(), QIcon.Normal, QIcon.Off)
        self.locationPushButton.setIcon(icon11)
        self.locationPushButton.setIconSize(QSize(18, 18))

        self.horizontalLayout.addWidget(self.locationPushButton)

        self.accountPushButton = QPushButton(self.horizontalLayoutWidget)
        self.accountPushButton.setObjectName(u"accountPushButton")
        self.accountPushButton.setMinimumSize(QSize(90, 51))
        self.accountPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.accountPushButton.setStyleSheet(u"QPushButton{\n"
"	border: None;\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u"images/account.png", QSize(), QIcon.Normal, QIcon.Off)
        self.accountPushButton.setIcon(icon12)
        self.accountPushButton.setIconSize(QSize(17, 17))

        self.horizontalLayout.addWidget(self.accountPushButton)


        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(0)
        self.notificationPushButton.setDefault(False)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.promotionPushButton6_3.setText(QCoreApplication.translate("Form", u"Elex", None))
        self.promotionPushButton6_4.setText(QCoreApplication.translate("Form", u"PPA", None))
        self.promotionPushButton6_5.setText(QCoreApplication.translate("Form", u"Elex", None))
        self.promotionPushButton6_6.setText(QCoreApplication.translate("Form", u"PPA", None))
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
        self.promotionPushButton6.setText(QCoreApplication.translate("Form", u" 55%", None))
        self.promotionPushButton5.setText(QCoreApplication.translate("Form", u" 50%", None))
        self.promotionPushButton4.setText(QCoreApplication.translate("Form", u" 45%", None))
        self.promotionPushButton3.setText(QCoreApplication.translate("Form", u" 40%", None))
        self.promotionPushButton2.setText(QCoreApplication.translate("Form", u" 35%", None))
        self.promotionPushButton1.setText(QCoreApplication.translate("Form", u" 30%", None))
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
        self.hiLabel.setText(QCoreApplication.translate("Form", u"Hi, ", None))
        self.welcomeLabel.setText(QCoreApplication.translate("Form", u"Welcome to E-DOCK!", None))
        self.otherservicesLabel.setText(QCoreApplication.translate("Form", u"Other Services", None))
        self.promotionLabel.setText(QCoreApplication.translate("Form", u"Promotions", None))
        self.exclusivedealsLabel.setText(QCoreApplication.translate("Form", u"Exclusive Deals for debit/credit card user", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Hello\n"
"Hi", None))
        self.historyLabel.setText(QCoreApplication.translate("Form", u"Charging History", None))
        self.locationLabel.setText(QCoreApplication.translate("Form", u"Location", None))
        self.accountLabel.setText(QCoreApplication.translate("Form", u"Account Settings", None))
        self.ewalletLabel.setText(QCoreApplication.translate("Form", u"E-Wallet:", None))
        self.moneyLabel.setText(QCoreApplication.translate("Form", u"0", None))
        self.notificationPushButton.setText(QCoreApplication.translate("Form", u"Notification                                                              ", None))
        self.opennotificationRadioButton.setText(QCoreApplication.translate("Form", u"Open Notification", None))
        self.closenotificationRadioButton.setText(QCoreApplication.translate("Form", u"Close Notification", None))
        self.addcarPushButton.setText(QCoreApplication.translate("Form", u"Add Car                                                                    ", None))
        self.companyLabel.setText(QCoreApplication.translate("Form", u"Company:", None))
        self.modelLabel.setText(QCoreApplication.translate("Form", u"Model:", None))
        self.batterycapacityLabel.setText(QCoreApplication.translate("Form", u"Battery Capacity:", None))
        self.chargingcapacityLabel.setText(QCoreApplication.translate("Form", u"Charging Capacity:", None))
        self.addcarPushButton_2.setText(QCoreApplication.translate("Form", u" Add Car", None))
        self.addcardPushButton.setText(QCoreApplication.translate("Form", u"Add Debit/Credit Card                                             ", None))
        self.cardnumberLabel.setText(QCoreApplication.translate("Form", u"Card Number:", None))
        self.cardholdernameLabel.setText(QCoreApplication.translate("Form", u"Cardholder Name:", None))
        self.expiryLabel.setText(QCoreApplication.translate("Form", u"Expiry (MM /YY):", None))
        self.cvvLabel.setText(QCoreApplication.translate("Form", u"CVV:", None))
        self.addcardPushButton_2.setText(QCoreApplication.translate("Form", u" Add Card", None))
        self.changeusernamePushButton.setText(QCoreApplication.translate("Form", u"Change Username                                                    ", None))
        self.newusernameLabel.setText(QCoreApplication.translate("Form", u"New Username:", None))
        self.changeusernamePushButton_2.setText(QCoreApplication.translate("Form", u" Change", None))
        self.changepinPushButton.setText(QCoreApplication.translate("Form", u"Change Pin", None))
        self.changepasswordPushButton.setText(QCoreApplication.translate("Form", u"Change Password", None))
        self.logoutPushButton.setText(QCoreApplication.translate("Form", u"Logout", None))
#if QT_CONFIG(whatsthis)
        self.homePushButton.setWhatsThis(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.homePushButton.setText(QCoreApplication.translate("Form", u" Home", None))
        self.historyPushButton.setText(QCoreApplication.translate("Form", u" History", None))
        self.locationPushButton.setText(QCoreApplication.translate("Form", u" Location", None))
        self.accountPushButton.setText(QCoreApplication.translate("Form", u" Account", None))
    # retranslateUi

