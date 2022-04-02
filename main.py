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
    QSizePolicy, QStackedWidget, QTableView, QVBoxLayout,
    QWidget)

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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 342, 653))
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
        self.welcomeLabel.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.welcomeLabel)

        self.searchLineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.searchLineEdit.setObjectName(u"searchLineEdit")
        self.searchLineEdit.setMinimumSize(QSize(0, 40))

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.searchLineEdit)

        self.otherservicesLabel = QLabel(self.scrollAreaWidgetContents)
        self.otherservicesLabel.setObjectName(u"otherservicesLabel")
        self.otherservicesLabel.setFont(font)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.otherservicesLabel)

        self.otherservicesLayout = QHBoxLayout()
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

        self.promotionTableView = QTableView(self.scrollAreaWidgetContents)
        self.promotionTableView.setObjectName(u"promotionTableView")

        self.formLayout.setWidget(8, QFormLayout.SpanningRole, self.promotionTableView)

        self.exclusivedealsLabel = QLabel(self.scrollAreaWidgetContents)
        self.exclusivedealsLabel.setObjectName(u"exclusivedealsLabel")
        self.exclusivedealsLabel.setFont(font)

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.exclusivedealsLabel)

        self.exclusivedealsTableView = QTableView(self.scrollAreaWidgetContents)
        self.exclusivedealsTableView.setObjectName(u"exclusivedealsTableView")

        self.formLayout.setWidget(10, QFormLayout.SpanningRole, self.exclusivedealsTableView)

        self.stationTableView = QTableView(self.scrollAreaWidgetContents)
        self.stationTableView.setObjectName(u"stationTableView")
        self.stationTableView.setMinimumSize(QSize(0, 190))

        self.formLayout.setWidget(4, QFormLayout.SpanningRole, self.stationTableView)

        self.homeScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.stackedWidget.addWidget(self.homePage)
        self.historyPage = QWidget()
        self.historyPage.setObjectName(u"historyPage")
        self.stackedWidget.addWidget(self.historyPage)
        self.locationPage = QWidget()
        self.locationPage.setObjectName(u"locationPage")
        self.stackedWidget.addWidget(self.locationPage)
        self.accountPage = QWidget()
        self.accountPage.setObjectName(u"accountPage")
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
        icon4 = QIcon()
        icon4.addFile(u"images/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.homePushButton.setIcon(icon4)

        self.horizontalLayout.addWidget(self.homePushButton)

        self.historyPushButton = QPushButton(self.horizontalLayoutWidget)
        self.historyPushButton.setObjectName(u"historyPushButton")
        self.historyPushButton.setMinimumSize(QSize(90, 51))
        self.historyPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.historyPushButton.setStyleSheet(u"QPushButton{\n"
"	border: None;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"images/history.png", QSize(), QIcon.Normal, QIcon.Off)
        self.historyPushButton.setIcon(icon5)

        self.horizontalLayout.addWidget(self.historyPushButton)

        self.locationPushButton = QPushButton(self.horizontalLayoutWidget)
        self.locationPushButton.setObjectName(u"locationPushButton")
        self.locationPushButton.setMinimumSize(QSize(90, 51))
        self.locationPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.locationPushButton.setStyleSheet(u"QPushButton{\n"
"	border: None;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"images/location.png", QSize(), QIcon.Normal, QIcon.Off)
        self.locationPushButton.setIcon(icon6)
        self.locationPushButton.setIconSize(QSize(18, 18))

        self.horizontalLayout.addWidget(self.locationPushButton)

        self.accountPushButton = QPushButton(self.horizontalLayoutWidget)
        self.accountPushButton.setObjectName(u"accountPushButton")
        self.accountPushButton.setMinimumSize(QSize(90, 51))
        self.accountPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.accountPushButton.setStyleSheet(u"QPushButton{\n"
"	border: None;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"images/account.png", QSize(), QIcon.Normal, QIcon.Off)
        self.accountPushButton.setIcon(icon7)
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
        self.exclusivedealsLabel.setText(QCoreApplication.translate("Form", u"Exclusive Deals for debit/credit card user", None))
#if QT_CONFIG(whatsthis)
        self.homePushButton.setWhatsThis(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.homePushButton.setText(QCoreApplication.translate("Form", u" Home", None))
        self.historyPushButton.setText(QCoreApplication.translate("Form", u" History", None))
        self.locationPushButton.setText(QCoreApplication.translate("Form", u" Location", None))
        self.accountPushButton.setText(QCoreApplication.translate("Form", u" Account", None))
    # retranslateUi

