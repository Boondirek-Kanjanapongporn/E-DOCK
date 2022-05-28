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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFormLayout, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QRadioButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QTextEdit, QVBoxLayout, QWidget)

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
        self.stackedWidget.setStyleSheet(u"")
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
        self.homeScrollArea.setStyleSheet(u"")
        self.homeScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.homeScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -112, 342, 691))
        self.formLayout = QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setContentsMargins(20, 20, 20, 20)
        self.searchLineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.searchLineEdit.setObjectName(u"searchLineEdit")
        self.searchLineEdit.setMinimumSize(QSize(0, 35))
        self.searchLineEdit.setStyleSheet(u"QLineEdit\n"
"{\n"
"	border: 2px solid #71cd00;\n"
"	border-radius: 10px;\n"
"}\n"
"QLineEdit:focus\n"
"{\n"
"	border: 2px solid #2871cc;\n"
"}")

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.searchLineEdit)

        self.stationScrollArea = QScrollArea(self.scrollAreaWidgetContents)
        self.stationScrollArea.setObjectName(u"stationScrollArea")
        self.stationScrollArea.setMinimumSize(QSize(0, 192))
        self.stationScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.stationScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.stationScrollArea.setWidgetResizable(True)
        self.stationAreaWidgetContents = QWidget()
        self.stationAreaWidgetContents.setObjectName(u"stationAreaWidgetContents")
        self.stationAreaWidgetContents.setGeometry(QRect(0, 0, 400, 175))
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
        font.setPointSize(10)
        self.promotionPushButton6_3.setFont(font)
        self.promotionPushButton6_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.promotionPushButton6_3.setStyleSheet(u"QPushButton{\n"
"	color: #fafafa;\n"
"	border-radius: 20px;\n"
"	background-color: #28a428;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color:#228c22;\n"
"}")
        self.promotionPushButton6_3.setIconSize(QSize(20, 20))

        self.stationVerticalLayout.addWidget(self.promotionPushButton6_3)

        self.promotionPushButton6_4 = QPushButton(self.stationAreaWidgetContents)
        self.promotionPushButton6_4.setObjectName(u"promotionPushButton6_4")
        self.promotionPushButton6_4.setMinimumSize(QSize(83, 80))
        self.promotionPushButton6_4.setMaximumSize(QSize(80, 80))
        self.promotionPushButton6_4.setFont(font)
        self.promotionPushButton6_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.promotionPushButton6_4.setStyleSheet(u"QPushButton{\n"
"	color: #fafafa;\n"
"	border-radius: 20px;\n"
"	background-color: #28a428;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color:#228c22;\n"
"}")
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
        self.promotionPushButton6_5.setStyleSheet(u"QPushButton{\n"
"	color: #fafafa;\n"
"	border-radius: 20px;\n"
"	background-color: #28a428;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color:#228c22;\n"
"}")
        self.promotionPushButton6_5.setIconSize(QSize(20, 20))

        self.stationVerticalLayout_2.addWidget(self.promotionPushButton6_5)

        self.promotionPushButton6_6 = QPushButton(self.stationAreaWidgetContents)
        self.promotionPushButton6_6.setObjectName(u"promotionPushButton6_6")
        self.promotionPushButton6_6.setMinimumSize(QSize(83, 80))
        self.promotionPushButton6_6.setMaximumSize(QSize(80, 80))
        self.promotionPushButton6_6.setFont(font)
        self.promotionPushButton6_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.promotionPushButton6_6.setStyleSheet(u"QPushButton{\n"
"	color: #fafafa;\n"
"	border-radius: 20px;\n"
"	background-color: #28a428;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color:#228c22;\n"
"}")
        self.promotionPushButton6_6.setIconSize(QSize(20, 20))

        self.stationVerticalLayout_2.addWidget(self.promotionPushButton6_6)


        self.stationHorizontalLayout.addLayout(self.stationVerticalLayout_2)

        self.stationVerticalLayout_4 = QVBoxLayout()
        self.stationVerticalLayout_4.setObjectName(u"stationVerticalLayout_4")
        self.stationVerticalLayout_4.setContentsMargins(6, 6, 6, 0)
        self.promotionPushButton6_7 = QPushButton(self.stationAreaWidgetContents)
        self.promotionPushButton6_7.setObjectName(u"promotionPushButton6_7")
        self.promotionPushButton6_7.setMinimumSize(QSize(83, 80))
        self.promotionPushButton6_7.setMaximumSize(QSize(80, 80))
        self.promotionPushButton6_7.setFont(font)
        self.promotionPushButton6_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.promotionPushButton6_7.setStyleSheet(u"QPushButton{\n"
"	color: #fafafa;\n"
"	border-radius: 20px;\n"
"	background-color: #28a428;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color:#228c22;\n"
"}")
        self.promotionPushButton6_7.setIconSize(QSize(20, 20))

        self.stationVerticalLayout_4.addWidget(self.promotionPushButton6_7)

        self.promotionPushButton6_8 = QPushButton(self.stationAreaWidgetContents)
        self.promotionPushButton6_8.setObjectName(u"promotionPushButton6_8")
        self.promotionPushButton6_8.setMinimumSize(QSize(83, 80))
        self.promotionPushButton6_8.setMaximumSize(QSize(80, 80))
        self.promotionPushButton6_8.setFont(font)
        self.promotionPushButton6_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.promotionPushButton6_8.setStyleSheet(u"QPushButton{\n"
"	color: #fafafa;\n"
"	border-radius: 20px;\n"
"	background-color: #28a428;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color:#228c22;\n"
"}")
        self.promotionPushButton6_8.setIconSize(QSize(20, 20))

        self.stationVerticalLayout_4.addWidget(self.promotionPushButton6_8)


        self.stationHorizontalLayout.addLayout(self.stationVerticalLayout_4)

        self.stationVerticalLayout_5 = QVBoxLayout()
        self.stationVerticalLayout_5.setObjectName(u"stationVerticalLayout_5")
        self.stationVerticalLayout_5.setContentsMargins(6, 6, 6, 0)
        self.promotionPushButton6_9 = QPushButton(self.stationAreaWidgetContents)
        self.promotionPushButton6_9.setObjectName(u"promotionPushButton6_9")
        self.promotionPushButton6_9.setMinimumSize(QSize(83, 80))
        self.promotionPushButton6_9.setMaximumSize(QSize(80, 80))
        self.promotionPushButton6_9.setFont(font)
        self.promotionPushButton6_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.promotionPushButton6_9.setStyleSheet(u"QPushButton{\n"
"	color: #fafafa;\n"
"	border-radius: 20px;\n"
"	background-color: #28a428;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color:#228c22;\n"
"}")
        self.promotionPushButton6_9.setIconSize(QSize(20, 20))

        self.stationVerticalLayout_5.addWidget(self.promotionPushButton6_9)

        self.promotionPushButton6_10 = QPushButton(self.stationAreaWidgetContents)
        self.promotionPushButton6_10.setObjectName(u"promotionPushButton6_10")
        self.promotionPushButton6_10.setMinimumSize(QSize(83, 80))
        self.promotionPushButton6_10.setMaximumSize(QSize(80, 80))
        self.promotionPushButton6_10.setFont(font)
        self.promotionPushButton6_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.promotionPushButton6_10.setStyleSheet(u"QPushButton{\n"
"	color: #fafafa;\n"
"	border-radius: 20px;\n"
"	background-color: #28a428;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color:#228c22;\n"
"}")
        self.promotionPushButton6_10.setIconSize(QSize(20, 20))

        self.stationVerticalLayout_5.addWidget(self.promotionPushButton6_10)


        self.stationHorizontalLayout.addLayout(self.stationVerticalLayout_5)


        self.formLayout_6.setLayout(0, QFormLayout.FieldRole, self.stationHorizontalLayout)

        self.stationScrollArea.setWidget(self.stationAreaWidgetContents)

        self.formLayout.setWidget(4, QFormLayout.SpanningRole, self.stationScrollArea)

        self.otherservicesLayout = QHBoxLayout()
        self.otherservicesLayout.setSpacing(12)
        self.otherservicesLayout.setObjectName(u"otherservicesLayout")
        self.chargeVerticalLayout = QVBoxLayout()
        self.chargeVerticalLayout.setSpacing(0)
        self.chargeVerticalLayout.setObjectName(u"chargeVerticalLayout")
        self.chargePushButton = QPushButton(self.scrollAreaWidgetContents)
        self.chargePushButton.setObjectName(u"chargePushButton")
        self.chargePushButton.setMinimumSize(QSize(0, 31))
        self.chargePushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.chargePushButton.setStyleSheet(u"QPushButton{\n"
"	color: #fafafa;\n"
"	background-color: #fafafa;\n"
"	border: 2px solid #444444;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color:#f2f2f2;\n"
"}")
        icon = QIcon()
        icon.addFile(u"images/charge.png", QSize(), QIcon.Normal, QIcon.Off)
        self.chargePushButton.setIcon(icon)
        self.chargePushButton.setIconSize(QSize(20, 20))

        self.chargeVerticalLayout.addWidget(self.chargePushButton)

        self.chargeLabel = QLabel(self.scrollAreaWidgetContents)
        self.chargeLabel.setObjectName(u"chargeLabel")
        self.chargeLabel.setStyleSheet(u"")
        self.chargeLabel.setAlignment(Qt.AlignCenter)

        self.chargeVerticalLayout.addWidget(self.chargeLabel)


        self.otherservicesLayout.addLayout(self.chargeVerticalLayout)

        self.topupVerticalLayout = QVBoxLayout()
        self.topupVerticalLayout.setSpacing(0)
        self.topupVerticalLayout.setObjectName(u"topupVerticalLayout")
        self.topupPushButton = QPushButton(self.scrollAreaWidgetContents)
        self.topupPushButton.setObjectName(u"topupPushButton")
        self.topupPushButton.setMinimumSize(QSize(0, 31))
        self.topupPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.topupPushButton.setStyleSheet(u"QPushButton{\n"
"	color: #fafafa;\n"
"	background-color: #fafafa;\n"
"	border: 2px solid #444444;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color:#f2f2f2;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"images/topup.png", QSize(), QIcon.Normal, QIcon.Off)
        self.topupPushButton.setIcon(icon1)
        self.topupPushButton.setIconSize(QSize(18, 18))

        self.topupVerticalLayout.addWidget(self.topupPushButton)

        self.topupLabel = QLabel(self.scrollAreaWidgetContents)
        self.topupLabel.setObjectName(u"topupLabel")
        self.topupLabel.setStyleSheet(u"")
        self.topupLabel.setAlignment(Qt.AlignCenter)

        self.topupVerticalLayout.addWidget(self.topupLabel)


        self.otherservicesLayout.addLayout(self.topupVerticalLayout)

        self.carsVerticalLayout = QVBoxLayout()
        self.carsVerticalLayout.setSpacing(0)
        self.carsVerticalLayout.setObjectName(u"carsVerticalLayout")
        self.carsPushButton = QPushButton(self.scrollAreaWidgetContents)
        self.carsPushButton.setObjectName(u"carsPushButton")
        self.carsPushButton.setMinimumSize(QSize(0, 31))
        self.carsPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.carsPushButton.setStyleSheet(u"QPushButton{\n"
"	color: #fafafa;\n"
"	background-color: #fafafa;\n"
"	border: 2px solid #444444;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color:#f2f2f2;\n"
"}")
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
        self.cardsPushButton.setStyleSheet(u"QPushButton{\n"
"	color: #fafafa;\n"
"	background-color: #fafafa;\n"
"	border: 2px solid #444444;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color:#f2f2f2;\n"
"}")
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
        font1 = QFont()
        font1.setPointSize(11)
        self.promotionPushButton6.setFont(font1)
        self.promotionPushButton6.setCursor(QCursor(Qt.PointingHandCursor))
        self.promotionPushButton6.setStyleSheet(u"QPushButton{\n"
"	color: #fafafa;\n"
"	background-color: #ff751a;\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color:#ff6600;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"images/promotion_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.promotionPushButton6.setIcon(icon4)
        self.promotionPushButton6.setIconSize(QSize(20, 20))

        self.promotionHorizontalLayout.addWidget(self.promotionPushButton6)

        self.promotionPushButton5 = QPushButton(self.scrollAreaWidgetContents_2)
        self.promotionPushButton5.setObjectName(u"promotionPushButton5")
        self.promotionPushButton5.setMinimumSize(QSize(0, 65))
        self.promotionPushButton5.setFont(font1)
        self.promotionPushButton5.setCursor(QCursor(Qt.PointingHandCursor))
        self.promotionPushButton5.setStyleSheet(u"QPushButton{\n"
"	color: #fafafa;\n"
"	background-color: #ff751a;\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color:#ff6600;\n"
"}")
        self.promotionPushButton5.setIcon(icon4)
        self.promotionPushButton5.setIconSize(QSize(20, 20))

        self.promotionHorizontalLayout.addWidget(self.promotionPushButton5)

        self.promotionPushButton4 = QPushButton(self.scrollAreaWidgetContents_2)
        self.promotionPushButton4.setObjectName(u"promotionPushButton4")
        self.promotionPushButton4.setMinimumSize(QSize(0, 65))
        self.promotionPushButton4.setFont(font1)
        self.promotionPushButton4.setCursor(QCursor(Qt.PointingHandCursor))
        self.promotionPushButton4.setStyleSheet(u"QPushButton{\n"
"	color: #fafafa;\n"
"	background-color: #ff751a;\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color:#ff6600;\n"
"}")
        self.promotionPushButton4.setIcon(icon4)
        self.promotionPushButton4.setIconSize(QSize(20, 20))

        self.promotionHorizontalLayout.addWidget(self.promotionPushButton4)

        self.promotionPushButton3 = QPushButton(self.scrollAreaWidgetContents_2)
        self.promotionPushButton3.setObjectName(u"promotionPushButton3")
        self.promotionPushButton3.setMinimumSize(QSize(0, 65))
        self.promotionPushButton3.setFont(font1)
        self.promotionPushButton3.setCursor(QCursor(Qt.PointingHandCursor))
        self.promotionPushButton3.setStyleSheet(u"QPushButton{\n"
"	color: #fafafa;\n"
"	background-color: #ff751a;\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color:#ff6600;\n"
"}")
        self.promotionPushButton3.setIcon(icon4)
        self.promotionPushButton3.setIconSize(QSize(20, 20))

        self.promotionHorizontalLayout.addWidget(self.promotionPushButton3)

        self.promotionPushButton2 = QPushButton(self.scrollAreaWidgetContents_2)
        self.promotionPushButton2.setObjectName(u"promotionPushButton2")
        self.promotionPushButton2.setMinimumSize(QSize(0, 65))
        self.promotionPushButton2.setFont(font1)
        self.promotionPushButton2.setCursor(QCursor(Qt.PointingHandCursor))
        self.promotionPushButton2.setStyleSheet(u"QPushButton{\n"
"	color: #fafafa;\n"
"	background-color: #ff751a;\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color:#ff6600;\n"
"}")
        self.promotionPushButton2.setIcon(icon4)
        self.promotionPushButton2.setIconSize(QSize(20, 20))

        self.promotionHorizontalLayout.addWidget(self.promotionPushButton2)

        self.promotionPushButton1 = QPushButton(self.scrollAreaWidgetContents_2)
        self.promotionPushButton1.setObjectName(u"promotionPushButton1")
        self.promotionPushButton1.setMinimumSize(QSize(0, 65))
        self.promotionPushButton1.setFont(font1)
        self.promotionPushButton1.setCursor(QCursor(Qt.PointingHandCursor))
        self.promotionPushButton1.setStyleSheet(u"QPushButton{\n"
"	color: #fafafa;\n"
"	background-color: #ff751a;\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color:#ff6600;\n"
"}")
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
        self.exclusivedealsPushButton6.setFont(font1)
        self.exclusivedealsPushButton6.setCursor(QCursor(Qt.PointingHandCursor))
        self.exclusivedealsPushButton6.setStyleSheet(u"QPushButton{\n"
"	color: #fafafa;\n"
"	background-color: #da2c43;\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color:#c32238;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"images/exclusivedeals_white.png", QSize(), QIcon.Normal, QIcon.Off)
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
        self.exclusivedealsPushButton5.setFont(font1)
        self.exclusivedealsPushButton5.setCursor(QCursor(Qt.PointingHandCursor))
        self.exclusivedealsPushButton5.setStyleSheet(u"QPushButton{\n"
"	color: #fafafa;\n"
"	background-color: #da2c43;\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color:#c32238;\n"
"}")
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
        self.exclusivedealsPushButton4.setFont(font1)
        self.exclusivedealsPushButton4.setCursor(QCursor(Qt.PointingHandCursor))
        self.exclusivedealsPushButton4.setStyleSheet(u"QPushButton{\n"
"	color: #fafafa;\n"
"	background-color: #da2c43;\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color:#c32238;\n"
"}")
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
        self.exclusivedealsPushButton3.setFont(font1)
        self.exclusivedealsPushButton3.setCursor(QCursor(Qt.PointingHandCursor))
        self.exclusivedealsPushButton3.setStyleSheet(u"QPushButton{\n"
"	color: #fafafa;\n"
"	background-color: #da2c43;\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color:#c32238;\n"
"}")
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
        self.exclusivedealsPushButton2.setFont(font1)
        self.exclusivedealsPushButton2.setCursor(QCursor(Qt.PointingHandCursor))
        self.exclusivedealsPushButton2.setStyleSheet(u"QPushButton{\n"
"	color: #fafafa;\n"
"	background-color: #da2c43;\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color:#c32238;\n"
"}")
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
        self.exclusivedealsPushButton1.setFont(font1)
        self.exclusivedealsPushButton1.setCursor(QCursor(Qt.PointingHandCursor))
        self.exclusivedealsPushButton1.setStyleSheet(u"QPushButton{\n"
"	color: #fafafa;\n"
"	background-color: #da2c43;\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color:#c32238;\n"
"}")
        self.exclusivedealsPushButton1.setIcon(icon5)
        self.exclusivedealsPushButton1.setIconSize(QSize(20, 20))

        self.verticalLayout1.addWidget(self.exclusivedealsPushButton1)


        self.exclusivedealsHorizontalLayout.addLayout(self.verticalLayout1)


        self.formLayout_3.setLayout(0, QFormLayout.FieldRole, self.exclusivedealsHorizontalLayout)

        self.exclusivedealsScrollArea.setWidget(self.scrollAreaWidgetContents_3)

        self.formLayout.setWidget(10, QFormLayout.SpanningRole, self.exclusivedealsScrollArea)

        self.hiLabel = QLabel(self.scrollAreaWidgetContents)
        self.hiLabel.setObjectName(u"hiLabel")
        self.hiLabel.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.hiLabel)

        self.welcomeLabel = QLabel(self.scrollAreaWidgetContents)
        self.welcomeLabel.setObjectName(u"welcomeLabel")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.welcomeLabel.setFont(font2)
        self.welcomeLabel.setStyleSheet(u"QLabel{\n"
"	color: #71cd00;\n"
"}")

        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.welcomeLabel)

        self.otherservicesLabel = QLabel(self.scrollAreaWidgetContents)
        self.otherservicesLabel.setObjectName(u"otherservicesLabel")
        self.otherservicesLabel.setFont(font)

        self.formLayout.setWidget(5, QFormLayout.SpanningRole, self.otherservicesLabel)

        self.promotionLabel = QLabel(self.scrollAreaWidgetContents)
        self.promotionLabel.setObjectName(u"promotionLabel")
        self.promotionLabel.setFont(font)

        self.formLayout.setWidget(7, QFormLayout.SpanningRole, self.promotionLabel)

        self.exclusivedealsLabel = QLabel(self.scrollAreaWidgetContents)
        self.exclusivedealsLabel.setObjectName(u"exclusivedealsLabel")
        self.exclusivedealsLabel.setFont(font)

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
        self.historyVerticalLayout.setContentsMargins(0, 0, 0, -1)

        self.formLayout_4.setLayout(0, QFormLayout.FieldRole, self.historyVerticalLayout)

        self.historyScrollArea.setWidget(self.scrollAreaWidgetContents_4)
        self.historyLabel = QLabel(self.historyPage)
        self.historyLabel.setObjectName(u"historyLabel")
        self.historyLabel.setGeometry(QRect(20, 10, 121, 21))
        self.historyLabel.setFont(font1)
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
        self.accountLabel.setFont(font1)
        self.accountScrollArea = QScrollArea(self.accountPage)
        self.accountScrollArea.setObjectName(u"accountScrollArea")
        self.accountScrollArea.setGeometry(QRect(0, 40, 361, 541))
        sizePolicy.setHeightForWidth(self.accountScrollArea.sizePolicy().hasHeightForWidth())
        self.accountScrollArea.setSizePolicy(sizePolicy)
        self.accountScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.accountScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, -597, 342, 1136))
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
        self.ewalletLabel.setFont(font)
        self.ewalletLabel.setAlignment(Qt.AlignCenter)

        self.accountVerticalLayout.addWidget(self.ewalletLabel)

        self.moneyLabel = QLabel(self.scrollAreaWidgetContents_5)
        self.moneyLabel.setObjectName(u"moneyLabel")
        self.moneyLabel.setMinimumSize(QSize(0, 65))
        font4 = QFont()
        font4.setPointSize(24)
        self.moneyLabel.setFont(font4)
        self.moneyLabel.setAlignment(Qt.AlignCenter)

        self.accountVerticalLayout.addWidget(self.moneyLabel)

        self.notificationPushButton = QPushButton(self.scrollAreaWidgetContents_5)
        self.notificationPushButton.setObjectName(u"notificationPushButton")
        self.notificationPushButton.setMinimumSize(QSize(0, 35))
        self.notificationPushButton.setFont(font)
        self.notificationPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.notificationPushButton.setTabletTracking(False)
        self.notificationPushButton.setLayoutDirection(Qt.RightToLeft)
        self.notificationPushButton.setStyleSheet(u"QPushButton{\n"
"	color: #FFFFFF;\n"
"	background-color:#71cd00;\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: #468000;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"images/right-arrow_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.notificationPushButton.setIcon(icon6)
        self.notificationPushButton.setIconSize(QSize(15, 15))
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
        self.addcarPushButton.setFont(font)
        self.addcarPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.addcarPushButton.setTabletTracking(False)
        self.addcarPushButton.setLayoutDirection(Qt.RightToLeft)
        self.addcarPushButton.setStyleSheet(u"QPushButton{\n"
"	color: #FFFFFF;\n"
"	background-color:#71cd00;\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: #468000;\n"
"}")
        self.addcarPushButton.setIcon(icon6)
        self.addcarPushButton.setIconSize(QSize(21, 15))
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
        self.companyLineEdit.setStyleSheet(u"QLineEdit\n"
"{\n"
"	border: 2px solid #71cd00;\n"
"	border-radius: 10px;\n"
"}\n"
"QLineEdit:focus\n"
"{\n"
"	border: 2px solid #71cd00;\n"
"}")

        self.addcarVerticalLayout.addWidget(self.companyLineEdit)

        self.modelLabel = QLabel(self.layoutWidget1)
        self.modelLabel.setObjectName(u"modelLabel")

        self.addcarVerticalLayout.addWidget(self.modelLabel)

        self.modelLineEdit = QLineEdit(self.layoutWidget1)
        self.modelLineEdit.setObjectName(u"modelLineEdit")
        self.modelLineEdit.setMinimumSize(QSize(0, 30))
        self.modelLineEdit.setStyleSheet(u"QLineEdit\n"
"{\n"
"	border: 2px solid #71cd00;\n"
"	border-radius: 10px;\n"
"}\n"
"QLineEdit:focus\n"
"{\n"
"	border: 2px solid #71cd00;\n"
"}")

        self.addcarVerticalLayout.addWidget(self.modelLineEdit)

        self.batterycapacityLabel = QLabel(self.layoutWidget1)
        self.batterycapacityLabel.setObjectName(u"batterycapacityLabel")

        self.addcarVerticalLayout.addWidget(self.batterycapacityLabel)

        self.batterycapacityLineEdit = QLineEdit(self.layoutWidget1)
        self.batterycapacityLineEdit.setObjectName(u"batterycapacityLineEdit")
        self.batterycapacityLineEdit.setMinimumSize(QSize(0, 30))
        self.batterycapacityLineEdit.setStyleSheet(u"QLineEdit\n"
"{\n"
"	border: 2px solid #71cd00;\n"
"	border-radius: 10px;\n"
"}\n"
"QLineEdit:focus\n"
"{\n"
"	border: 2px solid #71cd00;\n"
"}")

        self.addcarVerticalLayout.addWidget(self.batterycapacityLineEdit)

        self.chargingcapacityLabel = QLabel(self.layoutWidget1)
        self.chargingcapacityLabel.setObjectName(u"chargingcapacityLabel")

        self.addcarVerticalLayout.addWidget(self.chargingcapacityLabel)

        self.chargingcapacityLineEdit = QLineEdit(self.layoutWidget1)
        self.chargingcapacityLineEdit.setObjectName(u"chargingcapacityLineEdit")
        self.chargingcapacityLineEdit.setMinimumSize(QSize(0, 30))
        self.chargingcapacityLineEdit.setStyleSheet(u"QLineEdit\n"
"{\n"
"	border: 2px solid #71cd00;\n"
"	border-radius: 10px;\n"
"}\n"
"QLineEdit:focus\n"
"{\n"
"	border: 2px solid #71cd00;\n"
"}")

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
        self.addcarPushButton_2.setStyleSheet(u"QPushButton{\n"
"	background-color:#71cd00;\n"
"	border-radius: 10px;\n"
"	color: #FFFFFF;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color:#468000;\n"
"}\n"
"	")
        icon7 = QIcon()
        icon7.addFile(u"images/add_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addcarPushButton_2.setIcon(icon7)
        self.addcarPushButton_2.setIconSize(QSize(20, 16))

        self.addcarHorizontalLayout.addWidget(self.addcarPushButton_2)


        self.addcarVerticalLayout.addLayout(self.addcarHorizontalLayout)


        self.accountVerticalLayout.addWidget(self.addcarWidget)

        self.addcardPushButton = QPushButton(self.scrollAreaWidgetContents_5)
        self.addcardPushButton.setObjectName(u"addcardPushButton")
        self.addcardPushButton.setMinimumSize(QSize(0, 35))
        self.addcardPushButton.setFont(font)
        self.addcardPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.addcardPushButton.setTabletTracking(False)
        self.addcardPushButton.setLayoutDirection(Qt.RightToLeft)
        self.addcardPushButton.setStyleSheet(u"QPushButton{\n"
"	color: #FFFFFF;\n"
"	background-color:#71cd00;\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: #468000;\n"
"}")
        self.addcardPushButton.setIcon(icon6)
        self.addcardPushButton.setIconSize(QSize(21, 15))
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
        self.cardnumberLineEdit.setStyleSheet(u"QLineEdit\n"
"{\n"
"	border: 2px solid #71cd00;\n"
"	border-radius: 10px;\n"
"}\n"
"QLineEdit:focus\n"
"{\n"
"	border: 2px solid #71cd00;\n"
"}")

        self.addcardVerticalLayout.addWidget(self.cardnumberLineEdit)

        self.cardholdernameLabel = QLabel(self.layoutWidget2)
        self.cardholdernameLabel.setObjectName(u"cardholdernameLabel")

        self.addcardVerticalLayout.addWidget(self.cardholdernameLabel)

        self.cardholdernameLineEdit = QLineEdit(self.layoutWidget2)
        self.cardholdernameLineEdit.setObjectName(u"cardholdernameLineEdit")
        self.cardholdernameLineEdit.setMinimumSize(QSize(0, 30))
        self.cardholdernameLineEdit.setStyleSheet(u"QLineEdit\n"
"{\n"
"	border: 2px solid #71cd00;\n"
"	border-radius: 10px;\n"
"}\n"
"QLineEdit:focus\n"
"{\n"
"	border: 2px solid #71cd00;\n"
"}")

        self.addcardVerticalLayout.addWidget(self.cardholdernameLineEdit)

        self.expiryLabel = QLabel(self.layoutWidget2)
        self.expiryLabel.setObjectName(u"expiryLabel")

        self.addcardVerticalLayout.addWidget(self.expiryLabel)

        self.expiryLineEdit = QLineEdit(self.layoutWidget2)
        self.expiryLineEdit.setObjectName(u"expiryLineEdit")
        self.expiryLineEdit.setMinimumSize(QSize(0, 30))
        self.expiryLineEdit.setStyleSheet(u"QLineEdit\n"
"{\n"
"	border: 2px solid #71cd00;\n"
"	border-radius: 10px;\n"
"}\n"
"QLineEdit:focus\n"
"{\n"
"	border: 2px solid #71cd00;\n"
"}")

        self.addcardVerticalLayout.addWidget(self.expiryLineEdit)

        self.cvvLabel = QLabel(self.layoutWidget2)
        self.cvvLabel.setObjectName(u"cvvLabel")

        self.addcardVerticalLayout.addWidget(self.cvvLabel)

        self.cvvLineEdit = QLineEdit(self.layoutWidget2)
        self.cvvLineEdit.setObjectName(u"cvvLineEdit")
        self.cvvLineEdit.setMinimumSize(QSize(0, 30))
        self.cvvLineEdit.setStyleSheet(u"QLineEdit\n"
"{\n"
"	border: 2px solid #71cd00;\n"
"	border-radius: 10px;\n"
"}\n"
"QLineEdit:focus\n"
"{\n"
"	border: 2px solid #71cd00;\n"
"}")

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
        self.addcardPushButton_2.setStyleSheet(u"QPushButton{\n"
"	background-color:#71cd00;\n"
"	border-radius: 10px;\n"
"	color: #FFFFFF;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color:#468000;\n"
"}\n"
"	")
        self.addcardPushButton_2.setIcon(icon7)
        self.addcardPushButton_2.setIconSize(QSize(20, 16))

        self.addcardHorizontalLayout.addWidget(self.addcardPushButton_2)


        self.addcardVerticalLayout.addLayout(self.addcardHorizontalLayout)


        self.accountVerticalLayout.addWidget(self.addcardWidget)

        self.changeusernamePushButton = QPushButton(self.scrollAreaWidgetContents_5)
        self.changeusernamePushButton.setObjectName(u"changeusernamePushButton")
        self.changeusernamePushButton.setMinimumSize(QSize(0, 35))
        self.changeusernamePushButton.setFont(font)
        self.changeusernamePushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.changeusernamePushButton.setLayoutDirection(Qt.RightToLeft)
        self.changeusernamePushButton.setStyleSheet(u"QPushButton{\n"
"	color: #FFFFFF;\n"
"	background-color:#71cd00;\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: #468000;\n"
"}")
        self.changeusernamePushButton.setIcon(icon6)
        self.changeusernamePushButton.setIconSize(QSize(21, 15))

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
        self.newusernameLineEdit.setStyleSheet(u"QLineEdit\n"
"{\n"
"	border: 2px solid #71cd00;\n"
"	border-radius: 10px;\n"
"}\n"
"QLineEdit:focus\n"
"{\n"
"	border: 2px solid #71cd00;\n"
"}")

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
        self.changeusernamePushButton_2.setStyleSheet(u"QPushButton{\n"
"	background-color:#71cd00;\n"
"	border-radius: 10px;\n"
"	color: #FFFFFF;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color:#468000;\n"
"}\n"
"	")
        icon8 = QIcon()
        icon8.addFile(u"images/change_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.changeusernamePushButton_2.setIcon(icon8)
        self.changeusernamePushButton_2.setIconSize(QSize(16, 15))

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
        self.changepinPushButton.setFont(font1)
        self.changepinPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.changepinPushButton.setStyleSheet(u"QPushButton{\n"
"	color: #fafafa;\n"
"	border-radius: 10px;\n"
"	background-color: #28a428;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color:#228c22;\n"
"}")
        self.changepinPushButton.setIcon(icon8)
        self.changepinPushButton.setIconSize(QSize(16, 15))

        self.verticalLayout_3.addWidget(self.changepinPushButton)

        self.changepasswordPushButton = QPushButton(self.scrollAreaWidgetContents_5)
        self.changepasswordPushButton.setObjectName(u"changepasswordPushButton")
        self.changepasswordPushButton.setMinimumSize(QSize(0, 35))
        self.changepasswordPushButton.setFont(font1)
        self.changepasswordPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.changepasswordPushButton.setStyleSheet(u"QPushButton{\n"
"	color: #fafafa;\n"
"	border-radius: 10px;\n"
"	background-color: #2871cc;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #225faa;\n"
"}")

        self.verticalLayout_3.addWidget(self.changepasswordPushButton)

        self.logoutPushButton = QPushButton(self.scrollAreaWidgetContents_5)
        self.logoutPushButton.setObjectName(u"logoutPushButton")
        self.logoutPushButton.setMinimumSize(QSize(0, 35))
        self.logoutPushButton.setFont(font1)
        self.logoutPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.logoutPushButton.setStyleSheet(u"QPushButton{\n"
"	color: #fafafa;\n"
"	border-radius: 10px;\n"
"	background-color: #aa1111;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color: #8b0e0e;\n"
"}")

        self.verticalLayout_3.addWidget(self.logoutPushButton)


        self.accountVerticalLayout.addLayout(self.verticalLayout_3)

        self.accountVerticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.accountVerticalLayout.addItem(self.accountVerticalSpacer)


        self.formLayout_5.setLayout(0, QFormLayout.FieldRole, self.accountVerticalLayout)

        self.accountScrollArea.setWidget(self.scrollAreaWidgetContents_5)
        self.stackedWidget.addWidget(self.accountPage)
        self.topupPage = QWidget()
        self.topupPage.setObjectName(u"topupPage")
        self.topupScrollArea_2 = QScrollArea(self.topupPage)
        self.topupScrollArea_2.setObjectName(u"topupScrollArea_2")
        self.topupScrollArea_2.setGeometry(QRect(0, 40, 361, 541))
        sizePolicy.setHeightForWidth(self.topupScrollArea_2.sizePolicy().hasHeightForWidth())
        self.topupScrollArea_2.setSizePolicy(sizePolicy)
        self.topupScrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.topupScrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 342, 540))
        sizePolicy1.setHeightForWidth(self.scrollAreaWidgetContents_6.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_6.setSizePolicy(sizePolicy1)
        self.scrollAreaWidgetContents_6.setMinimumSize(QSize(0, 0))
        self.formLayout_7 = QFormLayout(self.scrollAreaWidgetContents_6)
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.formLayout_7.setHorizontalSpacing(0)
        self.formLayout_7.setVerticalSpacing(0)
        self.formLayout_7.setContentsMargins(0, 0, 0, 0)
        self.topupVerticalLayout_2 = QVBoxLayout()
        self.topupVerticalLayout_2.setSpacing(0)
        self.topupVerticalLayout_2.setObjectName(u"topupVerticalLayout_2")
        self.topupVerticalLayout_2.setContentsMargins(0, 10, 0, 0)
        self.ewalletLabel_2 = QLabel(self.scrollAreaWidgetContents_6)
        self.ewalletLabel_2.setObjectName(u"ewalletLabel_2")
        self.ewalletLabel_2.setFont(font)
        self.ewalletLabel_2.setAlignment(Qt.AlignCenter)

        self.topupVerticalLayout_2.addWidget(self.ewalletLabel_2)

        self.moneyLabel_2 = QLabel(self.scrollAreaWidgetContents_6)
        self.moneyLabel_2.setObjectName(u"moneyLabel_2")
        self.moneyLabel_2.setMinimumSize(QSize(0, 65))
        self.moneyLabel_2.setFont(font4)
        self.moneyLabel_2.setAlignment(Qt.AlignCenter)

        self.topupVerticalLayout_2.addWidget(self.moneyLabel_2)

        self.topupvalueVerticalLayout = QVBoxLayout()
        self.topupvalueVerticalLayout.setSpacing(3)
        self.topupvalueVerticalLayout.setObjectName(u"topupvalueVerticalLayout")
        self.topupvalueVerticalLayout.setContentsMargins(20, 10, 20, 0)
        self.topupvalueLabel = QLabel(self.scrollAreaWidgetContents_6)
        self.topupvalueLabel.setObjectName(u"topupvalueLabel")
        self.topupvalueLabel.setFont(font1)
        self.topupvalueLabel.setAlignment(Qt.AlignCenter)

        self.topupvalueVerticalLayout.addWidget(self.topupvalueLabel)

        self.verticalSpacer_12 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.topupvalueVerticalLayout.addItem(self.verticalSpacer_12)

        self.topupvalueLineEdit = QLineEdit(self.scrollAreaWidgetContents_6)
        self.topupvalueLineEdit.setObjectName(u"topupvalueLineEdit")
        self.topupvalueLineEdit.setMinimumSize(QSize(0, 35))
        font5 = QFont()
        font5.setPointSize(15)
        self.topupvalueLineEdit.setFont(font5)
        self.topupvalueLineEdit.setStyleSheet(u"QLineEdit\n"
"{\n"
"	border: 2px solid #71cd00;\n"
"	border-radius: 10px;\n"
"}\n"
"QLineEdit:focus\n"
"{\n"
"	border: 2px solid #71cd00;\n"
"}")
        self.topupvalueLineEdit.setAlignment(Qt.AlignCenter)

        self.topupvalueVerticalLayout.addWidget(self.topupvalueLineEdit)

        self.verticalSpacer_11 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.topupvalueVerticalLayout.addItem(self.verticalSpacer_11)

        self.keyboardGridLayout = QGridLayout()
        self.keyboardGridLayout.setObjectName(u"keyboardGridLayout")
        self.keyboardGridLayout.setHorizontalSpacing(0)
        self.keyboardGridLayout.setVerticalSpacing(5)
        self.keyboardGridLayout.setContentsMargins(-1, 5, -1, 5)
        self.pushButton_delete = QPushButton(self.scrollAreaWidgetContents_6)
        self.pushButton_delete.setObjectName(u"pushButton_delete")
        self.pushButton_delete.setMinimumSize(QSize(65, 65))
        self.pushButton_delete.setMaximumSize(QSize(65, 65))
        self.pushButton_delete.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_delete.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #cecece;\n"
"	border-radius: 32px;\n"
"	font: 22px Arial;\n"
"	\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background: #bbbbbf;\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u"images/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_delete.setIcon(icon9)
        self.pushButton_delete.setIconSize(QSize(25, 25))

        self.keyboardGridLayout.addWidget(self.pushButton_delete, 4, 2, 1, 1)

        self.pushButton_9 = QPushButton(self.scrollAreaWidgetContents_6)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(65, 65))
        self.pushButton_9.setMaximumSize(QSize(65, 65))
        self.pushButton_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #cecece;\n"
"	border-radius: 32px;\n"
"	font: 22px Arial;\n"
"	\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background: #bbbbbf;\n"
"}")

        self.keyboardGridLayout.addWidget(self.pushButton_9, 3, 2, 1, 1)

        self.pushButton_3 = QPushButton(self.scrollAreaWidgetContents_6)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(65, 65))
        self.pushButton_3.setMaximumSize(QSize(65, 65))
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #cecece;\n"
"	border-radius: 32px;\n"
"	font: 22px Arial;\n"
"	\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background: #bbbbbf;\n"
"}")

        self.keyboardGridLayout.addWidget(self.pushButton_3, 1, 2, 1, 1)

        self.pushButton_7 = QPushButton(self.scrollAreaWidgetContents_6)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(65, 65))
        self.pushButton_7.setMaximumSize(QSize(65, 65))
        self.pushButton_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #cecece;\n"
"	border-radius: 32px;\n"
"	font: 22px Arial;\n"
"	\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background: #bbbbbf;\n"
"}")

        self.keyboardGridLayout.addWidget(self.pushButton_7, 3, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.scrollAreaWidgetContents_6)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy2)
        self.pushButton_2.setMinimumSize(QSize(65, 65))
        self.pushButton_2.setMaximumSize(QSize(65, 65))
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #cecece;\n"
"	border-radius: 32px;\n"
"	font: 22px Arial;\n"
"	\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background: #bbbbbf;\n"
"}")
        self.pushButton_2.setIconSize(QSize(16, 16))
        self.pushButton_2.setFlat(False)

        self.keyboardGridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)

        self.pushButton_0 = QPushButton(self.scrollAreaWidgetContents_6)
        self.pushButton_0.setObjectName(u"pushButton_0")
        self.pushButton_0.setMinimumSize(QSize(65, 65))
        self.pushButton_0.setMaximumSize(QSize(65, 65))
        self.pushButton_0.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_0.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #cecece;\n"
"	border-radius: 32px;\n"
"	font: 22px Arial;\n"
"	\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background: #bbbbbf;\n"
"}")

        self.keyboardGridLayout.addWidget(self.pushButton_0, 4, 1, 1, 1)

        self.pushButton_1 = QPushButton(self.scrollAreaWidgetContents_6)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setMinimumSize(QSize(65, 65))
        self.pushButton_1.setMaximumSize(QSize(65, 65))
        self.pushButton_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_1.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #cecece;\n"
"	font: 22px Arial;\n"
"	border-radius: 32px;\n"
"	\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background: #bbbbbf;\n"
"}")

        self.keyboardGridLayout.addWidget(self.pushButton_1, 1, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.scrollAreaWidgetContents_6)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(65, 65))
        self.pushButton_5.setMaximumSize(QSize(65, 65))
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #cecece;\n"
"	border-radius: 32px;\n"
"	font: 22px Arial;\n"
"	\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background: #bbbbbf;\n"
"}")

        self.keyboardGridLayout.addWidget(self.pushButton_5, 2, 1, 1, 1)

        self.pushButton_4 = QPushButton(self.scrollAreaWidgetContents_6)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(65, 65))
        self.pushButton_4.setMaximumSize(QSize(65, 65))
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #cecece;\n"
"	border-radius: 32px;\n"
"	font: 22px Arial;\n"
"	\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background: #bbbbbf;\n"
"}")

        self.keyboardGridLayout.addWidget(self.pushButton_4, 2, 0, 1, 1)

        self.pushButton_8 = QPushButton(self.scrollAreaWidgetContents_6)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(65, 65))
        self.pushButton_8.setMaximumSize(QSize(65, 65))
        self.pushButton_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_8.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #cecece;\n"
"	border-radius: 32px;\n"
"	font: 22px Arial;\n"
"	\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background: #bbbbbf;\n"
"}")

        self.keyboardGridLayout.addWidget(self.pushButton_8, 3, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.scrollAreaWidgetContents_6)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(65, 65))
        self.pushButton_6.setMaximumSize(QSize(65, 65))
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #cecece;\n"
"	border-radius: 32px;\n"
"	font: 22px Arial;\n"
"	\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background: #bbbbbf;\n"
"}")

        self.keyboardGridLayout.addWidget(self.pushButton_6, 2, 2, 1, 1)

        self.pushButton_dot = QPushButton(self.scrollAreaWidgetContents_6)
        self.pushButton_dot.setObjectName(u"pushButton_dot")
        self.pushButton_dot.setMinimumSize(QSize(65, 65))
        self.pushButton_dot.setMaximumSize(QSize(65, 65))
        self.pushButton_dot.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_dot.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #cecece;\n"
"	border-radius: 32px;\n"
"	font: 22px Arial;\n"
"	\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background: #bbbbbf;\n"
"}")

        self.keyboardGridLayout.addWidget(self.pushButton_dot, 4, 0, 1, 1)


        self.topupvalueVerticalLayout.addLayout(self.keyboardGridLayout)

        self.verticalSpacer_10 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.topupvalueVerticalLayout.addItem(self.verticalSpacer_10)

        self.topupvalueHorizontalLayout = QHBoxLayout()
        self.topupvalueHorizontalLayout.setSpacing(0)
        self.topupvalueHorizontalLayout.setObjectName(u"topupvalueHorizontalLayout")
        self.topupvaluePushButton = QPushButton(self.scrollAreaWidgetContents_6)
        self.topupvaluePushButton.setObjectName(u"topupvaluePushButton")
        self.topupvaluePushButton.setMinimumSize(QSize(0, 35))
        self.topupvaluePushButton.setMaximumSize(QSize(100, 16777215))
        font6 = QFont()
        font6.setPointSize(13)
        self.topupvaluePushButton.setFont(font6)
        self.topupvaluePushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.topupvaluePushButton.setStyleSheet(u"QPushButton{\n"
"	background-color: #71cd00;\n"
"	border-radius: 10px;\n"
"	color: #ffffff;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #468000;\n"
"}")
        self.topupvaluePushButton.setIconSize(QSize(20, 20))

        self.topupvalueHorizontalLayout.addWidget(self.topupvaluePushButton)


        self.topupvalueVerticalLayout.addLayout(self.topupvalueHorizontalLayout)


        self.topupVerticalLayout_2.addLayout(self.topupvalueVerticalLayout)


        self.formLayout_7.setLayout(0, QFormLayout.FieldRole, self.topupVerticalLayout_2)

        self.topupScrollArea_2.setWidget(self.scrollAreaWidgetContents_6)
        self.topupLabel_2 = QLabel(self.topupPage)
        self.topupLabel_2.setObjectName(u"topupLabel_2")
        self.topupLabel_2.setGeometry(QRect(20, 10, 111, 21))
        self.topupLabel_2.setFont(font1)
        self.stackedWidget.addWidget(self.topupPage)
        self.selectstationPage = QWidget()
        self.selectstationPage.setObjectName(u"selectstationPage")
        self.stationLabel = QLabel(self.selectstationPage)
        self.stationLabel.setObjectName(u"stationLabel")
        self.stationLabel.setGeometry(QRect(20, 10, 111, 21))
        self.stationLabel.setFont(font1)
        self.selectstationScrollArea = QScrollArea(self.selectstationPage)
        self.selectstationScrollArea.setObjectName(u"selectstationScrollArea")
        self.selectstationScrollArea.setGeometry(QRect(0, 40, 361, 541))
        sizePolicy.setHeightForWidth(self.selectstationScrollArea.sizePolicy().hasHeightForWidth())
        self.selectstationScrollArea.setSizePolicy(sizePolicy)
        self.selectstationScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.selectstationScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 359, 539))
        sizePolicy1.setHeightForWidth(self.scrollAreaWidgetContents_7.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_7.setSizePolicy(sizePolicy1)
        self.scrollAreaWidgetContents_7.setMinimumSize(QSize(0, 0))
        self.formLayout_8 = QFormLayout(self.scrollAreaWidgetContents_7)
        self.formLayout_8.setObjectName(u"formLayout_8")
        self.formLayout_8.setHorizontalSpacing(0)
        self.formLayout_8.setVerticalSpacing(0)
        self.formLayout_8.setContentsMargins(0, 0, 0, 0)
        self.selectstationVerticalLayout = QVBoxLayout()
        self.selectstationVerticalLayout.setSpacing(0)
        self.selectstationVerticalLayout.setObjectName(u"selectstationVerticalLayout")
        self.selectstationVerticalLayout.setContentsMargins(0, 10, 0, 0)
        self.verticalSpacer_16 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.selectstationVerticalLayout.addItem(self.verticalSpacer_16)

        self.enterstationidLabel = QLabel(self.scrollAreaWidgetContents_7)
        self.enterstationidLabel.setObjectName(u"enterstationidLabel")
        font7 = QFont()
        font7.setPointSize(12)
        self.enterstationidLabel.setFont(font7)
        self.enterstationidLabel.setAlignment(Qt.AlignCenter)

        self.selectstationVerticalLayout.addWidget(self.enterstationidLabel)

        self.enterstationidVerticalLayout = QVBoxLayout()
        self.enterstationidVerticalLayout.setSpacing(3)
        self.enterstationidVerticalLayout.setObjectName(u"enterstationidVerticalLayout")
        self.enterstationidVerticalLayout.setContentsMargins(10, 10, 10, 0)
        self.verticalSpacer_13 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.enterstationidVerticalLayout.addItem(self.verticalSpacer_13)

        self.enterstationidHorizontalLayout = QHBoxLayout()
        self.enterstationidHorizontalLayout.setSpacing(5)
        self.enterstationidHorizontalLayout.setObjectName(u"enterstationidHorizontalLayout")
        self.enterstationidHorizontalLayout.setContentsMargins(15, -1, 15, -1)
        self.stationid1 = QLineEdit(self.scrollAreaWidgetContents_7)
        self.stationid1.setObjectName(u"stationid1")
        self.stationid1.setMinimumSize(QSize(0, 35))
        self.stationid1.setMaximumSize(QSize(16777215, 16777215))
        self.stationid1.setFont(font5)
        self.stationid1.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	border: 2px solid #71cd00;\n"
"	border-top: none;\n"
"	border-right: none;\n"
"	border-left: none;\n"
"}\n"
"QLineEdit:focus\n"
"{\n"
"	border: 2px solid #71cd00;\n"
"}")
        self.stationid1.setAlignment(Qt.AlignCenter)

        self.enterstationidHorizontalLayout.addWidget(self.stationid1)

        self.stationid2 = QLineEdit(self.scrollAreaWidgetContents_7)
        self.stationid2.setObjectName(u"stationid2")
        self.stationid2.setMinimumSize(QSize(0, 35))
        self.stationid2.setMaximumSize(QSize(16777215, 16777215))
        self.stationid2.setFont(font5)
        self.stationid2.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	border: 2px solid #71cd00;\n"
"	border-top: none;\n"
"	border-right: none;\n"
"	border-left: none;\n"
"}\n"
"QLineEdit:focus\n"
"{\n"
"	border: 2px solid #71cd00;\n"
"}")
        self.stationid2.setAlignment(Qt.AlignCenter)

        self.enterstationidHorizontalLayout.addWidget(self.stationid2)

        self.stationid3 = QLineEdit(self.scrollAreaWidgetContents_7)
        self.stationid3.setObjectName(u"stationid3")
        self.stationid3.setMinimumSize(QSize(0, 35))
        self.stationid3.setMaximumSize(QSize(16777215, 16777215))
        self.stationid3.setFont(font5)
        self.stationid3.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	border: 2px solid #71cd00;\n"
"	border-top: none;\n"
"	border-right: none;\n"
"	border-left: none;\n"
"}\n"
"QLineEdit:focus\n"
"{\n"
"	border: 2px solid #71cd00;\n"
"}")
        self.stationid3.setAlignment(Qt.AlignCenter)

        self.enterstationidHorizontalLayout.addWidget(self.stationid3)

        self.stationid4 = QLineEdit(self.scrollAreaWidgetContents_7)
        self.stationid4.setObjectName(u"stationid4")
        self.stationid4.setMinimumSize(QSize(0, 35))
        self.stationid4.setMaximumSize(QSize(16777215, 16777215))
        self.stationid4.setFont(font5)
        self.stationid4.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	border: 2px solid #71cd00;\n"
"	border-top: none;\n"
"	border-right: none;\n"
"	border-left: none;\n"
"}\n"
"QLineEdit:focus\n"
"{\n"
"	border: 2px solid #71cd00;\n"
"}")
        self.stationid4.setAlignment(Qt.AlignCenter)

        self.enterstationidHorizontalLayout.addWidget(self.stationid4)

        self.stationid5 = QLineEdit(self.scrollAreaWidgetContents_7)
        self.stationid5.setObjectName(u"stationid5")
        self.stationid5.setMinimumSize(QSize(0, 35))
        self.stationid5.setMaximumSize(QSize(16777215, 16777215))
        self.stationid5.setFont(font5)
        self.stationid5.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	border: 2px solid #71cd00;\n"
"	border-top: none;\n"
"	border-right: none;\n"
"	border-left: none;\n"
"}\n"
"QLineEdit:focus\n"
"{\n"
"	border: 2px solid #71cd00;\n"
"}")
        self.stationid5.setAlignment(Qt.AlignCenter)

        self.enterstationidHorizontalLayout.addWidget(self.stationid5)

        self.stationid6 = QLineEdit(self.scrollAreaWidgetContents_7)
        self.stationid6.setObjectName(u"stationid6")
        self.stationid6.setMinimumSize(QSize(0, 35))
        self.stationid6.setMaximumSize(QSize(16777215, 16777215))
        self.stationid6.setFont(font5)
        self.stationid6.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	border: 2px solid #71cd00;\n"
"	border-top: none;\n"
"	border-right: none;\n"
"	border-left: none;\n"
"}\n"
"QLineEdit:focus\n"
"{\n"
"	border: 2px solid #71cd00;\n"
"}")
        self.stationid6.setAlignment(Qt.AlignCenter)

        self.enterstationidHorizontalLayout.addWidget(self.stationid6)


        self.enterstationidVerticalLayout.addLayout(self.enterstationidHorizontalLayout)

        self.verticalSpacer_14 = QSpacerItem(20, 35, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.enterstationidVerticalLayout.addItem(self.verticalSpacer_14)

        self.keyboardGridLayout_2 = QGridLayout()
        self.keyboardGridLayout_2.setObjectName(u"keyboardGridLayout_2")
        self.keyboardGridLayout_2.setHorizontalSpacing(0)
        self.keyboardGridLayout_2.setVerticalSpacing(5)
        self.keyboardGridLayout_2.setContentsMargins(-1, 5, -1, 5)
        self.pushButton_delete_2 = QPushButton(self.scrollAreaWidgetContents_7)
        self.pushButton_delete_2.setObjectName(u"pushButton_delete_2")
        self.pushButton_delete_2.setMinimumSize(QSize(65, 65))
        self.pushButton_delete_2.setMaximumSize(QSize(65, 65))
        self.pushButton_delete_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_delete_2.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #cecece;\n"
"	border-radius: 32px;\n"
"	font: 22px Arial;\n"
"	\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background: #bbbbbf;\n"
"}")
        self.pushButton_delete_2.setIcon(icon9)
        self.pushButton_delete_2.setIconSize(QSize(25, 25))

        self.keyboardGridLayout_2.addWidget(self.pushButton_delete_2, 4, 2, 1, 1)

        self.pushButton_9_2 = QPushButton(self.scrollAreaWidgetContents_7)
        self.pushButton_9_2.setObjectName(u"pushButton_9_2")
        self.pushButton_9_2.setMinimumSize(QSize(65, 65))
        self.pushButton_9_2.setMaximumSize(QSize(65, 65))
        self.pushButton_9_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_9_2.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #cecece;\n"
"	border-radius: 32px;\n"
"	font: 22px Arial;\n"
"	\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background: #bbbbbf;\n"
"}")

        self.keyboardGridLayout_2.addWidget(self.pushButton_9_2, 3, 2, 1, 1)

        self.pushButton_3_2 = QPushButton(self.scrollAreaWidgetContents_7)
        self.pushButton_3_2.setObjectName(u"pushButton_3_2")
        self.pushButton_3_2.setMinimumSize(QSize(65, 65))
        self.pushButton_3_2.setMaximumSize(QSize(65, 65))
        self.pushButton_3_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3_2.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #cecece;\n"
"	border-radius: 32px;\n"
"	font: 22px Arial;\n"
"	\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background: #bbbbbf;\n"
"}")

        self.keyboardGridLayout_2.addWidget(self.pushButton_3_2, 1, 2, 1, 1)

        self.pushButton_7_2 = QPushButton(self.scrollAreaWidgetContents_7)
        self.pushButton_7_2.setObjectName(u"pushButton_7_2")
        self.pushButton_7_2.setMinimumSize(QSize(65, 65))
        self.pushButton_7_2.setMaximumSize(QSize(65, 65))
        self.pushButton_7_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_7_2.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #cecece;\n"
"	border-radius: 32px;\n"
"	font: 22px Arial;\n"
"	\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background: #bbbbbf;\n"
"}")

        self.keyboardGridLayout_2.addWidget(self.pushButton_7_2, 3, 0, 1, 1)

        self.pushButton_2_2 = QPushButton(self.scrollAreaWidgetContents_7)
        self.pushButton_2_2.setObjectName(u"pushButton_2_2")
        sizePolicy2.setHeightForWidth(self.pushButton_2_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2_2.setSizePolicy(sizePolicy2)
        self.pushButton_2_2.setMinimumSize(QSize(65, 65))
        self.pushButton_2_2.setMaximumSize(QSize(65, 65))
        self.pushButton_2_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2_2.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #cecece;\n"
"	border-radius: 32px;\n"
"	font: 22px Arial;\n"
"	\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background: #bbbbbf;\n"
"}")
        self.pushButton_2_2.setIconSize(QSize(16, 16))
        self.pushButton_2_2.setFlat(False)

        self.keyboardGridLayout_2.addWidget(self.pushButton_2_2, 1, 1, 1, 1)

        self.pushButton_0_2 = QPushButton(self.scrollAreaWidgetContents_7)
        self.pushButton_0_2.setObjectName(u"pushButton_0_2")
        self.pushButton_0_2.setMinimumSize(QSize(65, 65))
        self.pushButton_0_2.setMaximumSize(QSize(65, 65))
        self.pushButton_0_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_0_2.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #cecece;\n"
"	border-radius: 32px;\n"
"	font: 22px Arial;\n"
"	\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background: #bbbbbf;\n"
"}")

        self.keyboardGridLayout_2.addWidget(self.pushButton_0_2, 4, 1, 1, 1)

        self.pushButton_1_2 = QPushButton(self.scrollAreaWidgetContents_7)
        self.pushButton_1_2.setObjectName(u"pushButton_1_2")
        self.pushButton_1_2.setMinimumSize(QSize(65, 65))
        self.pushButton_1_2.setMaximumSize(QSize(65, 65))
        self.pushButton_1_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_1_2.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #cecece;\n"
"	font: 22px Arial;\n"
"	border-radius: 32px;\n"
"	\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background: #bbbbbf;\n"
"}")

        self.keyboardGridLayout_2.addWidget(self.pushButton_1_2, 1, 0, 1, 1)

        self.pushButton_5_2 = QPushButton(self.scrollAreaWidgetContents_7)
        self.pushButton_5_2.setObjectName(u"pushButton_5_2")
        self.pushButton_5_2.setMinimumSize(QSize(65, 65))
        self.pushButton_5_2.setMaximumSize(QSize(65, 65))
        self.pushButton_5_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_5_2.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #cecece;\n"
"	border-radius: 32px;\n"
"	font: 22px Arial;\n"
"	\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background: #bbbbbf;\n"
"}")

        self.keyboardGridLayout_2.addWidget(self.pushButton_5_2, 2, 1, 1, 1)

        self.pushButton_4_2 = QPushButton(self.scrollAreaWidgetContents_7)
        self.pushButton_4_2.setObjectName(u"pushButton_4_2")
        self.pushButton_4_2.setMinimumSize(QSize(65, 65))
        self.pushButton_4_2.setMaximumSize(QSize(65, 65))
        self.pushButton_4_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_4_2.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #cecece;\n"
"	border-radius: 32px;\n"
"	font: 22px Arial;\n"
"	\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background: #bbbbbf;\n"
"}")

        self.keyboardGridLayout_2.addWidget(self.pushButton_4_2, 2, 0, 1, 1)

        self.pushButton_8_2 = QPushButton(self.scrollAreaWidgetContents_7)
        self.pushButton_8_2.setObjectName(u"pushButton_8_2")
        self.pushButton_8_2.setMinimumSize(QSize(65, 65))
        self.pushButton_8_2.setMaximumSize(QSize(65, 65))
        self.pushButton_8_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_8_2.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #cecece;\n"
"	border-radius: 32px;\n"
"	font: 22px Arial;\n"
"	\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background: #bbbbbf;\n"
"}")

        self.keyboardGridLayout_2.addWidget(self.pushButton_8_2, 3, 1, 1, 1)

        self.pushButton_6_2 = QPushButton(self.scrollAreaWidgetContents_7)
        self.pushButton_6_2.setObjectName(u"pushButton_6_2")
        self.pushButton_6_2.setMinimumSize(QSize(65, 65))
        self.pushButton_6_2.setMaximumSize(QSize(65, 65))
        self.pushButton_6_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_6_2.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #cecece;\n"
"	border-radius: 32px;\n"
"	font: 22px Arial;\n"
"	\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background: #bbbbbf;\n"
"}")

        self.keyboardGridLayout_2.addWidget(self.pushButton_6_2, 2, 2, 1, 1)

        self.pushButton_scan = QPushButton(self.scrollAreaWidgetContents_7)
        self.pushButton_scan.setObjectName(u"pushButton_scan")
        self.pushButton_scan.setMinimumSize(QSize(65, 65))
        self.pushButton_scan.setMaximumSize(QSize(65, 65))
        self.pushButton_scan.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_scan.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #cecece;\n"
"	border-radius: 32px;\n"
"	font: 22px Arial;\n"
"	\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background: #bbbbbf;\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u"images/scan.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_scan.setIcon(icon10)
        self.pushButton_scan.setIconSize(QSize(25, 25))

        self.keyboardGridLayout_2.addWidget(self.pushButton_scan, 4, 0, 1, 1)


        self.enterstationidVerticalLayout.addLayout(self.keyboardGridLayout_2)

        self.verticalSpacer_15 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.enterstationidVerticalLayout.addItem(self.verticalSpacer_15)

        self.searchvalueHorizontalLayout = QHBoxLayout()
        self.searchvalueHorizontalLayout.setSpacing(0)
        self.searchvalueHorizontalLayout.setObjectName(u"searchvalueHorizontalLayout")
        self.searchPushButton = QPushButton(self.scrollAreaWidgetContents_7)
        self.searchPushButton.setObjectName(u"searchPushButton")
        self.searchPushButton.setMinimumSize(QSize(0, 35))
        self.searchPushButton.setMaximumSize(QSize(100, 16777215))
        self.searchPushButton.setFont(font6)
        self.searchPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.searchPushButton.setStyleSheet(u"QPushButton{\n"
"	background-color: #71cd00;\n"
"	border-radius: 10px;\n"
"	color: #ffffff;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #468000;\n"
"}")
        self.searchPushButton.setIconSize(QSize(20, 20))

        self.searchvalueHorizontalLayout.addWidget(self.searchPushButton)


        self.enterstationidVerticalLayout.addLayout(self.searchvalueHorizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.enterstationidVerticalLayout.addItem(self.verticalSpacer)


        self.selectstationVerticalLayout.addLayout(self.enterstationidVerticalLayout)


        self.formLayout_8.setLayout(0, QFormLayout.FieldRole, self.selectstationVerticalLayout)

        self.selectstationScrollArea.setWidget(self.scrollAreaWidgetContents_7)
        self.stackedWidget.addWidget(self.selectstationPage)
        self.chargingstationPage = QWidget()
        self.chargingstationPage.setObjectName(u"chargingstationPage")
        self.chargingstationLabel = QLabel(self.chargingstationPage)
        self.chargingstationLabel.setObjectName(u"chargingstationLabel")
        self.chargingstationLabel.setGeometry(QRect(20, 10, 121, 21))
        self.chargingstationLabel.setFont(font1)
        self.chargingstationScrollArea = QScrollArea(self.chargingstationPage)
        self.chargingstationScrollArea.setObjectName(u"chargingstationScrollArea")
        self.chargingstationScrollArea.setGeometry(QRect(0, 40, 361, 541))
        sizePolicy.setHeightForWidth(self.chargingstationScrollArea.sizePolicy().hasHeightForWidth())
        self.chargingstationScrollArea.setSizePolicy(sizePolicy)
        self.chargingstationScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.chargingstationScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_8 = QWidget()
        self.scrollAreaWidgetContents_8.setObjectName(u"scrollAreaWidgetContents_8")
        self.scrollAreaWidgetContents_8.setGeometry(QRect(0, 0, 359, 539))
        sizePolicy1.setHeightForWidth(self.scrollAreaWidgetContents_8.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_8.setSizePolicy(sizePolicy1)
        self.scrollAreaWidgetContents_8.setMinimumSize(QSize(0, 0))
        self.formLayout_9 = QFormLayout(self.scrollAreaWidgetContents_8)
        self.formLayout_9.setObjectName(u"formLayout_9")
        self.formLayout_9.setHorizontalSpacing(0)
        self.formLayout_9.setVerticalSpacing(0)
        self.formLayout_9.setContentsMargins(0, 0, 0, 0)
        self.stationVerticalLayout_3 = QVBoxLayout()
        self.stationVerticalLayout_3.setSpacing(0)
        self.stationVerticalLayout_3.setObjectName(u"stationVerticalLayout_3")
        self.stationVerticalLayout_3.setContentsMargins(0, 10, 0, 0)
        self.verticalSpacer_17 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.stationVerticalLayout_3.addItem(self.verticalSpacer_17)

        self.stationidLabel_2 = QLabel(self.scrollAreaWidgetContents_8)
        self.stationidLabel_2.setObjectName(u"stationidLabel_2")
        self.stationidLabel_2.setMinimumSize(QSize(357, 0))
        self.stationidLabel_2.setFont(font7)
        self.stationidLabel_2.setAlignment(Qt.AlignCenter)

        self.stationVerticalLayout_3.addWidget(self.stationidLabel_2)

        self.enterstationidVerticalLayout_2 = QVBoxLayout()
        self.enterstationidVerticalLayout_2.setSpacing(3)
        self.enterstationidVerticalLayout_2.setObjectName(u"enterstationidVerticalLayout_2")
        self.enterstationidVerticalLayout_2.setContentsMargins(10, 10, 10, 0)
        self.verticalSpacer_18 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.enterstationidVerticalLayout_2.addItem(self.verticalSpacer_18)

        self.stationidvalueLabel = QLabel(self.scrollAreaWidgetContents_8)
        self.stationidvalueLabel.setObjectName(u"stationidvalueLabel")
        font8 = QFont()
        font8.setPointSize(14)
        self.stationidvalueLabel.setFont(font8)
        self.stationidvalueLabel.setAlignment(Qt.AlignCenter)

        self.enterstationidVerticalLayout_2.addWidget(self.stationidvalueLabel)

        self.verticalSpacer_19 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.enterstationidVerticalLayout_2.addItem(self.verticalSpacer_19)

        self.chargingstationiconPushButton = QPushButton(self.scrollAreaWidgetContents_8)
        self.chargingstationiconPushButton.setObjectName(u"chargingstationiconPushButton")
        self.chargingstationiconPushButton.setStyleSheet(u"QPushButton{\n"
"	border: None;\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u"images/charging-station.png", QSize(), QIcon.Normal, QIcon.Off)
        self.chargingstationiconPushButton.setIcon(icon11)
        self.chargingstationiconPushButton.setIconSize(QSize(150, 150))

        self.enterstationidVerticalLayout_2.addWidget(self.chargingstationiconPushButton)

        self.verticalSpacer_22 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.enterstationidVerticalLayout_2.addItem(self.verticalSpacer_22)

        self.companyHorizontalLayout = QHBoxLayout()
        self.companyHorizontalLayout.setSpacing(0)
        self.companyHorizontalLayout.setObjectName(u"companyHorizontalLayout")
        self.companyHorizontalLayout.setContentsMargins(40, -1, 0, -1)
        self.companyLabel_2 = QLabel(self.scrollAreaWidgetContents_8)
        self.companyLabel_2.setObjectName(u"companyLabel_2")
        self.companyLabel_2.setMaximumSize(QSize(100, 16777215))
        self.companyLabel_2.setFont(font1)

        self.companyHorizontalLayout.addWidget(self.companyLabel_2)

        self.companyvalueLabel_2 = QLabel(self.scrollAreaWidgetContents_8)
        self.companyvalueLabel_2.setObjectName(u"companyvalueLabel_2")
        self.companyvalueLabel_2.setMaximumSize(QSize(196, 16777215))
        self.companyvalueLabel_2.setFont(font1)

        self.companyHorizontalLayout.addWidget(self.companyvalueLabel_2)


        self.enterstationidVerticalLayout_2.addLayout(self.companyHorizontalLayout)

        self.verticalSpacer_23 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.enterstationidVerticalLayout_2.addItem(self.verticalSpacer_23)

        self.typeHorizontalLayout = QHBoxLayout()
        self.typeHorizontalLayout.setSpacing(0)
        self.typeHorizontalLayout.setObjectName(u"typeHorizontalLayout")
        self.typeHorizontalLayout.setContentsMargins(40, -1, 0, -1)
        self.typeLabel = QLabel(self.scrollAreaWidgetContents_8)
        self.typeLabel.setObjectName(u"typeLabel")
        self.typeLabel.setMaximumSize(QSize(100, 16777215))
        self.typeLabel.setFont(font1)

        self.typeHorizontalLayout.addWidget(self.typeLabel)

        self.typevalueLabel = QLabel(self.scrollAreaWidgetContents_8)
        self.typevalueLabel.setObjectName(u"typevalueLabel")
        self.typevalueLabel.setMaximumSize(QSize(196, 16777215))
        self.typevalueLabel.setFont(font1)

        self.typeHorizontalLayout.addWidget(self.typevalueLabel)


        self.enterstationidVerticalLayout_2.addLayout(self.typeHorizontalLayout)

        self.verticalSpacer_21 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.enterstationidVerticalLayout_2.addItem(self.verticalSpacer_21)

        self.locationHorizontalLayout = QHBoxLayout()
        self.locationHorizontalLayout.setSpacing(0)
        self.locationHorizontalLayout.setObjectName(u"locationHorizontalLayout")
        self.locationHorizontalLayout.setContentsMargins(40, -1, -1, -1)
        self.locationLabel_2 = QLabel(self.scrollAreaWidgetContents_8)
        self.locationLabel_2.setObjectName(u"locationLabel_2")
        self.locationLabel_2.setMinimumSize(QSize(100, 0))
        self.locationLabel_2.setMaximumSize(QSize(100, 16777215))
        self.locationLabel_2.setFont(font1)
        self.locationLabel_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.locationHorizontalLayout.addWidget(self.locationLabel_2)

        self.locationvalueTextEdit = QTextEdit(self.scrollAreaWidgetContents_8)
        self.locationvalueTextEdit.setObjectName(u"locationvalueTextEdit")
        self.locationvalueTextEdit.setMinimumSize(QSize(0, 0))
        self.locationvalueTextEdit.setMaximumSize(QSize(16777215, 90))
        self.locationvalueTextEdit.setBaseSize(QSize(0, 0))
        self.locationvalueTextEdit.setFont(font1)
        self.locationvalueTextEdit.setStyleSheet(u"QTextEdit{\n"
"	background-color: rgba( 0, 0, 0, 0 );\n"
"	border: none;\n"
"}")
        self.locationvalueTextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.locationvalueTextEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.locationvalueTextEdit.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)

        self.locationHorizontalLayout.addWidget(self.locationvalueTextEdit)


        self.enterstationidVerticalLayout_2.addLayout(self.locationHorizontalLayout)

        self.verticalSpacer_20 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.enterstationidVerticalLayout_2.addItem(self.verticalSpacer_20)

        self.confirmHorizontalLayout = QHBoxLayout()
        self.confirmHorizontalLayout.setSpacing(0)
        self.confirmHorizontalLayout.setObjectName(u"confirmHorizontalLayout")
        self.cancelPushButton = QPushButton(self.scrollAreaWidgetContents_8)
        self.cancelPushButton.setObjectName(u"cancelPushButton")
        self.cancelPushButton.setMinimumSize(QSize(0, 35))
        self.cancelPushButton.setMaximumSize(QSize(100, 16777215))
        self.cancelPushButton.setFont(font6)
        self.cancelPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancelPushButton.setStyleSheet(u"QPushButton{\n"
"	background-color: #aa1111;\n"
"	border-radius: 10px;\n"
"	color: #ffffff;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #a21010;\n"
"}")
        self.cancelPushButton.setIconSize(QSize(20, 20))

        self.confirmHorizontalLayout.addWidget(self.cancelPushButton)

        self.confirmPushButton = QPushButton(self.scrollAreaWidgetContents_8)
        self.confirmPushButton.setObjectName(u"confirmPushButton")
        self.confirmPushButton.setMinimumSize(QSize(0, 35))
        self.confirmPushButton.setMaximumSize(QSize(100, 16777215))
        self.confirmPushButton.setFont(font6)
        self.confirmPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.confirmPushButton.setStyleSheet(u"QPushButton{\n"
"	background-color: #71cd00;\n"
"	border-radius: 10px;\n"
"	color: #ffffff;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #468000;\n"
"}")
        self.confirmPushButton.setIconSize(QSize(20, 20))

        self.confirmHorizontalLayout.addWidget(self.confirmPushButton)


        self.enterstationidVerticalLayout_2.addLayout(self.confirmHorizontalLayout)

        self.verticalSpacer_4 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.enterstationidVerticalLayout_2.addItem(self.verticalSpacer_4)


        self.stationVerticalLayout_3.addLayout(self.enterstationidVerticalLayout_2)


        self.formLayout_9.setLayout(0, QFormLayout.FieldRole, self.stationVerticalLayout_3)

        self.chargingstationScrollArea.setWidget(self.scrollAreaWidgetContents_8)
        self.stackedWidget.addWidget(self.chargingstationPage)
        self.carsPage = QWidget()
        self.carsPage.setObjectName(u"carsPage")
        self.carsLabel_2 = QLabel(self.carsPage)
        self.carsLabel_2.setObjectName(u"carsLabel_2")
        self.carsLabel_2.setGeometry(QRect(10, 10, 121, 21))
        self.carsLabel_2.setFont(font1)
        self.carsScrollArea = QScrollArea(self.carsPage)
        self.carsScrollArea.setObjectName(u"carsScrollArea")
        self.carsScrollArea.setGeometry(QRect(0, 40, 361, 541))
        sizePolicy.setHeightForWidth(self.carsScrollArea.sizePolicy().hasHeightForWidth())
        self.carsScrollArea.setSizePolicy(sizePolicy)
        self.carsScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.carsScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_9 = QWidget()
        self.scrollAreaWidgetContents_9.setObjectName(u"scrollAreaWidgetContents_9")
        self.scrollAreaWidgetContents_9.setGeometry(QRect(0, 0, 359, 539))
        self.scrollAreaWidgetContents_9.setMinimumSize(QSize(0, 0))
        self.formLayout_10 = QFormLayout(self.scrollAreaWidgetContents_9)
        self.formLayout_10.setObjectName(u"formLayout_10")
        self.formLayout_10.setHorizontalSpacing(0)
        self.formLayout_10.setVerticalSpacing(0)
        self.formLayout_10.setContentsMargins(0, 0, 0, 0)
        self.carsVerticalLayout_2 = QVBoxLayout()
        self.carsVerticalLayout_2.setSpacing(6)
        self.carsVerticalLayout_2.setObjectName(u"carsVerticalLayout_2")
        self.carsVerticalLayout_2.setContentsMargins(0, 0, 0, -1)

        self.formLayout_10.setLayout(0, QFormLayout.FieldRole, self.carsVerticalLayout_2)

        self.carsScrollArea.setWidget(self.scrollAreaWidgetContents_9)
        self.stackedWidget.addWidget(self.carsPage)
        self.cardsPage = QWidget()
        self.cardsPage.setObjectName(u"cardsPage")
        self.cardsLabel_2 = QLabel(self.cardsPage)
        self.cardsLabel_2.setObjectName(u"cardsLabel_2")
        self.cardsLabel_2.setGeometry(QRect(10, 10, 121, 21))
        self.cardsLabel_2.setFont(font1)
        self.cardsScrollArea = QScrollArea(self.cardsPage)
        self.cardsScrollArea.setObjectName(u"cardsScrollArea")
        self.cardsScrollArea.setGeometry(QRect(0, 40, 361, 541))
        sizePolicy.setHeightForWidth(self.cardsScrollArea.sizePolicy().hasHeightForWidth())
        self.cardsScrollArea.setSizePolicy(sizePolicy)
        self.cardsScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.cardsScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_10 = QWidget()
        self.scrollAreaWidgetContents_10.setObjectName(u"scrollAreaWidgetContents_10")
        self.scrollAreaWidgetContents_10.setGeometry(QRect(0, 0, 359, 539))
        self.scrollAreaWidgetContents_10.setMinimumSize(QSize(0, 0))
        self.formLayout_11 = QFormLayout(self.scrollAreaWidgetContents_10)
        self.formLayout_11.setObjectName(u"formLayout_11")
        self.formLayout_11.setHorizontalSpacing(0)
        self.formLayout_11.setVerticalSpacing(0)
        self.formLayout_11.setContentsMargins(0, 0, 0, 0)
        self.cardsVerticalLayout_2 = QVBoxLayout()
        self.cardsVerticalLayout_2.setSpacing(6)
        self.cardsVerticalLayout_2.setObjectName(u"cardsVerticalLayout_2")
        self.cardsVerticalLayout_2.setContentsMargins(0, 0, 0, -1)

        self.formLayout_11.setLayout(0, QFormLayout.FieldRole, self.cardsVerticalLayout_2)

        self.cardsScrollArea.setWidget(self.scrollAreaWidgetContents_10)
        self.stackedWidget.addWidget(self.cardsPage)

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
"}\n"
"QPushButton:hover{\n"
"	color: #71cd00;\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u"images/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.homePushButton.setIcon(icon12)

        self.horizontalLayout.addWidget(self.homePushButton)

        self.historyPushButton = QPushButton(self.horizontalLayoutWidget)
        self.historyPushButton.setObjectName(u"historyPushButton")
        self.historyPushButton.setMinimumSize(QSize(90, 51))
        self.historyPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.historyPushButton.setStyleSheet(u"QPushButton{\n"
"	border: None;\n"
"}\n"
"QPushButton:hover{\n"
"	color: #71cd00;\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u"images/history.png", QSize(), QIcon.Normal, QIcon.Off)
        self.historyPushButton.setIcon(icon13)

        self.horizontalLayout.addWidget(self.historyPushButton)

        self.locationPushButton = QPushButton(self.horizontalLayoutWidget)
        self.locationPushButton.setObjectName(u"locationPushButton")
        self.locationPushButton.setMinimumSize(QSize(90, 51))
        self.locationPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.locationPushButton.setStyleSheet(u"QPushButton{\n"
"	border: None;\n"
"}\n"
"QPushButton:hover{\n"
"	color: #71cd00;\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u"images/location.png", QSize(), QIcon.Normal, QIcon.Off)
        self.locationPushButton.setIcon(icon14)
        self.locationPushButton.setIconSize(QSize(18, 18))

        self.horizontalLayout.addWidget(self.locationPushButton)

        self.accountPushButton = QPushButton(self.horizontalLayoutWidget)
        self.accountPushButton.setObjectName(u"accountPushButton")
        self.accountPushButton.setMinimumSize(QSize(90, 51))
        self.accountPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.accountPushButton.setStyleSheet(u"QPushButton{\n"
"	border: None;\n"
"}\n"
"QPushButton:hover{\n"
"	color: #71cd00;\n"
"}")
        icon15 = QIcon()
        icon15.addFile(u"images/account.png", QSize(), QIcon.Normal, QIcon.Off)
        self.accountPushButton.setIcon(icon15)
        self.accountPushButton.setIconSize(QSize(17, 17))

        self.horizontalLayout.addWidget(self.accountPushButton)


        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(0)
        self.notificationPushButton.setDefault(False)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.promotionPushButton6_3.setText(QCoreApplication.translate("Form", u"BANGCHAK", None))
        self.promotionPushButton6_4.setText(QCoreApplication.translate("Form", u"CALTEX", None))
        self.promotionPushButton6_5.setText(QCoreApplication.translate("Form", u"MG", None))
        self.promotionPushButton6_6.setText(QCoreApplication.translate("Form", u"PEA", None))
        self.promotionPushButton6_7.setText(QCoreApplication.translate("Form", u"PT", None))
        self.promotionPushButton6_8.setText(QCoreApplication.translate("Form", u"PTT", None))
        self.promotionPushButton6_9.setText(QCoreApplication.translate("Form", u"SHELL", None))
        self.promotionPushButton6_10.setText(QCoreApplication.translate("Form", u"SUSCO", None))
        self.chargePushButton.setText("")
#if QT_CONFIG(tooltip)
        self.chargeLabel.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.chargeLabel.setWhatsThis(QCoreApplication.translate("Form", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.chargeLabel.setText(QCoreApplication.translate("Form", u"Charge", None))
        self.topupPushButton.setText("")
#if QT_CONFIG(tooltip)
        self.topupLabel.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.topupLabel.setWhatsThis(QCoreApplication.translate("Form", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.topupLabel.setText(QCoreApplication.translate("Form", u"Top-Up", None))
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
        self.ewalletLabel_2.setText(QCoreApplication.translate("Form", u"E-Wallet:", None))
        self.moneyLabel_2.setText(QCoreApplication.translate("Form", u"0", None))
        self.topupvalueLabel.setText(QCoreApplication.translate("Form", u"Top-Up Value:", None))
        self.topupvalueLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Value <= 200,000", None))
        self.pushButton_delete.setText("")
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"9", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"3", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"7", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"2", None))
        self.pushButton_0.setText(QCoreApplication.translate("Form", u"0", None))
        self.pushButton_1.setText(QCoreApplication.translate("Form", u"1", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"5", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"4", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"8", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"6", None))
        self.pushButton_dot.setText(QCoreApplication.translate("Form", u".", None))
        self.topupvaluePushButton.setText(QCoreApplication.translate("Form", u"Top-Up", None))
        self.topupLabel_2.setText(QCoreApplication.translate("Form", u"Top-Up", None))
        self.stationLabel.setText(QCoreApplication.translate("Form", u"Station", None))
        self.enterstationidLabel.setText(QCoreApplication.translate("Form", u"Enter Station ID:", None))
        self.stationid1.setPlaceholderText("")
        self.stationid2.setPlaceholderText("")
        self.stationid3.setPlaceholderText("")
        self.stationid4.setPlaceholderText("")
        self.stationid5.setPlaceholderText("")
        self.stationid6.setPlaceholderText("")
        self.pushButton_delete_2.setText("")
        self.pushButton_9_2.setText(QCoreApplication.translate("Form", u"9", None))
        self.pushButton_3_2.setText(QCoreApplication.translate("Form", u"3", None))
        self.pushButton_7_2.setText(QCoreApplication.translate("Form", u"7", None))
        self.pushButton_2_2.setText(QCoreApplication.translate("Form", u"2", None))
        self.pushButton_0_2.setText(QCoreApplication.translate("Form", u"0", None))
        self.pushButton_1_2.setText(QCoreApplication.translate("Form", u"1", None))
        self.pushButton_5_2.setText(QCoreApplication.translate("Form", u"5", None))
        self.pushButton_4_2.setText(QCoreApplication.translate("Form", u"4", None))
        self.pushButton_8_2.setText(QCoreApplication.translate("Form", u"8", None))
        self.pushButton_6_2.setText(QCoreApplication.translate("Form", u"6", None))
        self.pushButton_scan.setText("")
        self.searchPushButton.setText(QCoreApplication.translate("Form", u"Search", None))
        self.chargingstationLabel.setText(QCoreApplication.translate("Form", u"Charging Station", None))
        self.stationidLabel_2.setText(QCoreApplication.translate("Form", u"Station ID:", None))
        self.stationidvalueLabel.setText("")
        self.chargingstationiconPushButton.setText("")
        self.companyLabel_2.setText(QCoreApplication.translate("Form", u"Company:", None))
        self.companyvalueLabel_2.setText("")
        self.typeLabel.setText(QCoreApplication.translate("Form", u"Type:", None))
        self.typevalueLabel.setText("")
        self.locationLabel_2.setText(QCoreApplication.translate("Form", u"Location:", None))
        self.cancelPushButton.setText(QCoreApplication.translate("Form", u"Cancel", None))
        self.confirmPushButton.setText(QCoreApplication.translate("Form", u"Confirm", None))
        self.carsLabel_2.setText(QCoreApplication.translate("Form", u"Cars List", None))
        self.cardsLabel_2.setText(QCoreApplication.translate("Form", u"Cards List", None))
#if QT_CONFIG(whatsthis)
        self.homePushButton.setWhatsThis(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.homePushButton.setText(QCoreApplication.translate("Form", u" Home", None))
        self.historyPushButton.setText(QCoreApplication.translate("Form", u" History", None))
        self.locationPushButton.setText(QCoreApplication.translate("Form", u" Location", None))
        self.accountPushButton.setText(QCoreApplication.translate("Form", u" Account", None))
    # retranslateUi

