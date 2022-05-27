# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'station.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(359, 640)
        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 361, 641))
        self.settimerPage = QWidget()
        self.settimerPage.setObjectName(u"settimerPage")
        self.settimerPage.setStyleSheet(u"")
        self.timerLabel = QLabel(self.settimerPage)
        self.timerLabel.setObjectName(u"timerLabel")
        self.timerLabel.setGeometry(QRect(20, 10, 121, 21))
        font = QFont()
        font.setPointSize(11)
        self.timerLabel.setFont(font)
        self.settimerScrollArea = QScrollArea(self.settimerPage)
        self.settimerScrollArea.setObjectName(u"settimerScrollArea")
        self.settimerScrollArea.setGeometry(QRect(0, 40, 361, 601))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settimerScrollArea.sizePolicy().hasHeightForWidth())
        self.settimerScrollArea.setSizePolicy(sizePolicy)
        self.settimerScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.settimerScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.settimerScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 361, 599))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollAreaWidgetContents_7.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_7.setSizePolicy(sizePolicy1)
        self.scrollAreaWidgetContents_7.setMinimumSize(QSize(0, 0))
        self.formLayout_8 = QFormLayout(self.scrollAreaWidgetContents_7)
        self.formLayout_8.setObjectName(u"formLayout_8")
        self.formLayout_8.setHorizontalSpacing(0)
        self.formLayout_8.setVerticalSpacing(0)
        self.formLayout_8.setContentsMargins(0, 0, 0, 0)
        self.settimerVerticalLayout = QVBoxLayout()
        self.settimerVerticalLayout.setSpacing(0)
        self.settimerVerticalLayout.setObjectName(u"settimerVerticalLayout")
        self.settimerVerticalLayout.setContentsMargins(0, 10, 0, 0)
        self.verticalSpacer_16 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.settimerVerticalLayout.addItem(self.verticalSpacer_16)

        self.settimerLabel = QLabel(self.scrollAreaWidgetContents_7)
        self.settimerLabel.setObjectName(u"settimerLabel")
        font1 = QFont()
        font1.setPointSize(13)
        self.settimerLabel.setFont(font1)
        self.settimerLabel.setAlignment(Qt.AlignCenter)

        self.settimerVerticalLayout.addWidget(self.settimerLabel)

        self.timerVerticalLayout_2 = QVBoxLayout()
        self.timerVerticalLayout_2.setSpacing(3)
        self.timerVerticalLayout_2.setObjectName(u"timerVerticalLayout_2")
        self.timerVerticalLayout_2.setContentsMargins(10, 10, 10, 0)
        self.verticalSpacer_13 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.timerVerticalLayout_2.addItem(self.verticalSpacer_13)

        self.enterstationidHorizontalLayout = QHBoxLayout()
        self.enterstationidHorizontalLayout.setSpacing(5)
        self.enterstationidHorizontalLayout.setObjectName(u"enterstationidHorizontalLayout")
        self.enterstationidHorizontalLayout.setContentsMargins(15, -1, 15, -1)
        self.timer6 = QLineEdit(self.scrollAreaWidgetContents_7)
        self.timer6.setObjectName(u"timer6")
        self.timer6.setMinimumSize(QSize(0, 35))
        self.timer6.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setPointSize(15)
        self.timer6.setFont(font2)
        self.timer6.setStyleSheet(u"QLineEdit\n"
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
        self.timer6.setAlignment(Qt.AlignCenter)

        self.enterstationidHorizontalLayout.addWidget(self.timer6)

        self.timer5 = QLineEdit(self.scrollAreaWidgetContents_7)
        self.timer5.setObjectName(u"timer5")
        self.timer5.setMinimumSize(QSize(0, 35))
        self.timer5.setMaximumSize(QSize(16777215, 16777215))
        self.timer5.setFont(font2)
        self.timer5.setStyleSheet(u"QLineEdit\n"
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
        self.timer5.setAlignment(Qt.AlignCenter)

        self.enterstationidHorizontalLayout.addWidget(self.timer5)

        self.colonLabel1 = QLabel(self.scrollAreaWidgetContents_7)
        self.colonLabel1.setObjectName(u"colonLabel1")
        self.colonLabel1.setFont(font2)

        self.enterstationidHorizontalLayout.addWidget(self.colonLabel1)

        self.timer4 = QLineEdit(self.scrollAreaWidgetContents_7)
        self.timer4.setObjectName(u"timer4")
        self.timer4.setMinimumSize(QSize(0, 35))
        self.timer4.setMaximumSize(QSize(16777215, 16777215))
        self.timer4.setFont(font2)
        self.timer4.setStyleSheet(u"QLineEdit\n"
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
        self.timer4.setAlignment(Qt.AlignCenter)

        self.enterstationidHorizontalLayout.addWidget(self.timer4)

        self.timer3 = QLineEdit(self.scrollAreaWidgetContents_7)
        self.timer3.setObjectName(u"timer3")
        self.timer3.setMinimumSize(QSize(0, 35))
        self.timer3.setMaximumSize(QSize(16777215, 16777215))
        self.timer3.setFont(font2)
        self.timer3.setStyleSheet(u"QLineEdit\n"
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
        self.timer3.setAlignment(Qt.AlignCenter)

        self.enterstationidHorizontalLayout.addWidget(self.timer3)

        self.colonLabel2 = QLabel(self.scrollAreaWidgetContents_7)
        self.colonLabel2.setObjectName(u"colonLabel2")
        self.colonLabel2.setFont(font2)

        self.enterstationidHorizontalLayout.addWidget(self.colonLabel2)

        self.timer2 = QLineEdit(self.scrollAreaWidgetContents_7)
        self.timer2.setObjectName(u"timer2")
        self.timer2.setMinimumSize(QSize(0, 35))
        self.timer2.setMaximumSize(QSize(16777215, 16777215))
        self.timer2.setFont(font2)
        self.timer2.setStyleSheet(u"QLineEdit\n"
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
        self.timer2.setAlignment(Qt.AlignCenter)

        self.enterstationidHorizontalLayout.addWidget(self.timer2)

        self.timer1 = QLineEdit(self.scrollAreaWidgetContents_7)
        self.timer1.setObjectName(u"timer1")
        self.timer1.setMinimumSize(QSize(0, 35))
        self.timer1.setMaximumSize(QSize(16777215, 16777215))
        self.timer1.setFont(font2)
        self.timer1.setStyleSheet(u"QLineEdit\n"
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
        self.timer1.setAlignment(Qt.AlignCenter)

        self.enterstationidHorizontalLayout.addWidget(self.timer1)


        self.timerVerticalLayout_2.addLayout(self.enterstationidHorizontalLayout)

        self.verticalSpacer_14 = QSpacerItem(20, 35, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.timerVerticalLayout_2.addItem(self.verticalSpacer_14)

        self.keyboardGridLayout = QGridLayout()
        self.keyboardGridLayout.setObjectName(u"keyboardGridLayout")
        self.keyboardGridLayout.setHorizontalSpacing(0)
        self.keyboardGridLayout.setVerticalSpacing(5)
        self.keyboardGridLayout.setContentsMargins(-1, 5, -1, 5)
        self.pushButton_delete = QPushButton(self.scrollAreaWidgetContents_7)
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
        icon = QIcon()
        icon.addFile(u"images/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_delete.setIcon(icon)
        self.pushButton_delete.setIconSize(QSize(25, 25))

        self.keyboardGridLayout.addWidget(self.pushButton_delete, 4, 2, 1, 1)

        self.pushButton_9 = QPushButton(self.scrollAreaWidgetContents_7)
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

        self.pushButton_3 = QPushButton(self.scrollAreaWidgetContents_7)
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

        self.pushButton_7 = QPushButton(self.scrollAreaWidgetContents_7)
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

        self.pushButton_2 = QPushButton(self.scrollAreaWidgetContents_7)
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

        self.pushButton_0 = QPushButton(self.scrollAreaWidgetContents_7)
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

        self.pushButton_1 = QPushButton(self.scrollAreaWidgetContents_7)
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

        self.pushButton_5 = QPushButton(self.scrollAreaWidgetContents_7)
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

        self.pushButton_4 = QPushButton(self.scrollAreaWidgetContents_7)
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

        self.pushButton_8 = QPushButton(self.scrollAreaWidgetContents_7)
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

        self.pushButton_6 = QPushButton(self.scrollAreaWidgetContents_7)
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


        self.timerVerticalLayout_2.addLayout(self.keyboardGridLayout)

        self.verticalSpacer_15 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.timerVerticalLayout_2.addItem(self.verticalSpacer_15)

        self.startHorizontalLayout = QHBoxLayout()
        self.startHorizontalLayout.setSpacing(0)
        self.startHorizontalLayout.setObjectName(u"startHorizontalLayout")
        self.startPushButton = QPushButton(self.scrollAreaWidgetContents_7)
        self.startPushButton.setObjectName(u"startPushButton")
        self.startPushButton.setMinimumSize(QSize(0, 35))
        self.startPushButton.setMaximumSize(QSize(100, 16777215))
        self.startPushButton.setFont(font1)
        self.startPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.startPushButton.setStyleSheet(u"QPushButton{\n"
"	background-color: #71cd00;\n"
"	border-radius: 10px;\n"
"	color: #ffffff;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #468000;\n"
"}")
        self.startPushButton.setIconSize(QSize(20, 20))

        self.startHorizontalLayout.addWidget(self.startPushButton)


        self.timerVerticalLayout_2.addLayout(self.startHorizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.timerVerticalLayout_2.addItem(self.verticalSpacer)


        self.settimerVerticalLayout.addLayout(self.timerVerticalLayout_2)


        self.formLayout_8.setLayout(0, QFormLayout.FieldRole, self.settimerVerticalLayout)

        self.settimerScrollArea.setWidget(self.scrollAreaWidgetContents_7)
        self.closePushButton = QPushButton(self.settimerPage)
        self.closePushButton.setObjectName(u"closePushButton")
        self.closePushButton.setGeometry(QRect(320, 10, 31, 24))
        self.closePushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.closePushButton.setStyleSheet(u"QPushButton{\n"
"	border: None;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"images/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closePushButton.setIcon(icon1)
        self.closePushButton.setIconSize(QSize(20, 20))
        self.stackedWidget.addWidget(self.settimerPage)
        self.chargingPage = QWidget()
        self.chargingPage.setObjectName(u"chargingPage")
        self.chargingScrollArea = QScrollArea(self.chargingPage)
        self.chargingScrollArea.setObjectName(u"chargingScrollArea")
        self.chargingScrollArea.setGeometry(QRect(0, 40, 360, 601))
        sizePolicy.setHeightForWidth(self.chargingScrollArea.sizePolicy().hasHeightForWidth())
        self.chargingScrollArea.setSizePolicy(sizePolicy)
        self.chargingScrollArea.setMaximumSize(QSize(360, 16777215))
        self.chargingScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.chargingScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_8 = QWidget()
        self.scrollAreaWidgetContents_8.setObjectName(u"scrollAreaWidgetContents_8")
        self.scrollAreaWidgetContents_8.setGeometry(QRect(0, 0, 358, 599))
        sizePolicy1.setHeightForWidth(self.scrollAreaWidgetContents_8.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_8.setSizePolicy(sizePolicy1)
        self.scrollAreaWidgetContents_8.setMinimumSize(QSize(0, 0))
        self.scrollAreaWidgetContents_8.setMaximumSize(QSize(358, 16777215))
        self.formLayout_9 = QFormLayout(self.scrollAreaWidgetContents_8)
        self.formLayout_9.setObjectName(u"formLayout_9")
        self.formLayout_9.setHorizontalSpacing(0)
        self.formLayout_9.setVerticalSpacing(0)
        self.formLayout_9.setContentsMargins(0, 0, 0, 0)
        self.chargingVerticalLayout = QVBoxLayout()
        self.chargingVerticalLayout.setSpacing(0)
        self.chargingVerticalLayout.setObjectName(u"chargingVerticalLayout")
        self.chargingVerticalLayout.setContentsMargins(0, 10, 0, 0)
        self.countdownVerticalLayout_2 = QVBoxLayout()
        self.countdownVerticalLayout_2.setSpacing(3)
        self.countdownVerticalLayout_2.setObjectName(u"countdownVerticalLayout_2")
        self.countdownVerticalLayout_2.setContentsMargins(10, 10, 10, 0)
        self.verticalSpacer_19 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.countdownVerticalLayout_2.addItem(self.verticalSpacer_19)

        self.charginginprocessLabel = QLabel(self.scrollAreaWidgetContents_8)
        self.charginginprocessLabel.setObjectName(u"charginginprocessLabel")
        self.charginginprocessLabel.setMinimumSize(QSize(336, 0))
        self.charginginprocessLabel.setMaximumSize(QSize(336, 16777215))
        self.charginginprocessLabel.setFont(font1)
        self.charginginprocessLabel.setAlignment(Qt.AlignCenter)

        self.countdownVerticalLayout_2.addWidget(self.charginginprocessLabel)

        self.verticalSpacer_17 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.countdownVerticalLayout_2.addItem(self.verticalSpacer_17)

        self.chargingstationiconPushButton = QPushButton(self.scrollAreaWidgetContents_8)
        self.chargingstationiconPushButton.setObjectName(u"chargingstationiconPushButton")
        self.chargingstationiconPushButton.setStyleSheet(u"QPushButton{\n"
"	border: None;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"images/charging.png", QSize(), QIcon.Normal, QIcon.Off)
        self.chargingstationiconPushButton.setIcon(icon2)
        self.chargingstationiconPushButton.setIconSize(QSize(150, 150))

        self.countdownVerticalLayout_2.addWidget(self.chargingstationiconPushButton)

        self.timeLabel = QLabel(self.scrollAreaWidgetContents_8)
        self.timeLabel.setObjectName(u"timeLabel")
        self.timeLabel.setMinimumSize(QSize(336, 0))
        self.timeLabel.setMaximumSize(QSize(336, 16777215))
        font3 = QFont()
        font3.setPointSize(14)
        self.timeLabel.setFont(font3)
        self.timeLabel.setAlignment(Qt.AlignCenter)

        self.countdownVerticalLayout_2.addWidget(self.timeLabel)

        self.timercountdownLabel = QLabel(self.scrollAreaWidgetContents_8)
        self.timercountdownLabel.setObjectName(u"timercountdownLabel")
        self.timercountdownLabel.setMinimumSize(QSize(0, 80))
        font4 = QFont()
        font4.setPointSize(45)
        self.timercountdownLabel.setFont(font4)
        self.timercountdownLabel.setAlignment(Qt.AlignCenter)

        self.countdownVerticalLayout_2.addWidget(self.timercountdownLabel)

        self.verticalSpacer_20 = QSpacerItem(20, 80, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.countdownVerticalLayout_2.addItem(self.verticalSpacer_20)

        self.stopHorizontalLayout = QHBoxLayout()
        self.stopHorizontalLayout.setSpacing(0)
        self.stopHorizontalLayout.setObjectName(u"stopHorizontalLayout")
        self.stopPushButton = QPushButton(self.scrollAreaWidgetContents_8)
        self.stopPushButton.setObjectName(u"stopPushButton")
        self.stopPushButton.setMinimumSize(QSize(0, 35))
        self.stopPushButton.setMaximumSize(QSize(100, 16777215))
        self.stopPushButton.setFont(font1)
        self.stopPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.stopPushButton.setStyleSheet(u"QPushButton{\n"
"	background-color: #aa1111;\n"
"	border-radius: 10px;\n"
"	color: #ffffff;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #a21010;\n"
"}")
        self.stopPushButton.setIconSize(QSize(20, 20))

        self.stopHorizontalLayout.addWidget(self.stopPushButton)


        self.countdownVerticalLayout_2.addLayout(self.stopHorizontalLayout)

        self.verticalSpacer_4 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.countdownVerticalLayout_2.addItem(self.verticalSpacer_4)


        self.chargingVerticalLayout.addLayout(self.countdownVerticalLayout_2)


        self.formLayout_9.setLayout(0, QFormLayout.FieldRole, self.chargingVerticalLayout)

        self.chargingScrollArea.setWidget(self.scrollAreaWidgetContents_8)
        self.chargingLabel = QLabel(self.chargingPage)
        self.chargingLabel.setObjectName(u"chargingLabel")
        self.chargingLabel.setGeometry(QRect(20, 10, 121, 21))
        self.chargingLabel.setFont(font)
        self.stackedWidget.addWidget(self.chargingPage)
        self.successPage = QWidget()
        self.successPage.setObjectName(u"successPage")
        self.successScrollArea = QScrollArea(self.successPage)
        self.successScrollArea.setObjectName(u"successScrollArea")
        self.successScrollArea.setGeometry(QRect(0, 40, 361, 601))
        sizePolicy.setHeightForWidth(self.successScrollArea.sizePolicy().hasHeightForWidth())
        self.successScrollArea.setSizePolicy(sizePolicy)
        self.successScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.successScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_9 = QWidget()
        self.scrollAreaWidgetContents_9.setObjectName(u"scrollAreaWidgetContents_9")
        self.scrollAreaWidgetContents_9.setGeometry(QRect(0, 0, 359, 599))
        sizePolicy1.setHeightForWidth(self.scrollAreaWidgetContents_9.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_9.setSizePolicy(sizePolicy1)
        self.scrollAreaWidgetContents_9.setMinimumSize(QSize(0, 0))
        self.formLayout_10 = QFormLayout(self.scrollAreaWidgetContents_9)
        self.formLayout_10.setObjectName(u"formLayout_10")
        self.formLayout_10.setHorizontalSpacing(0)
        self.formLayout_10.setVerticalSpacing(0)
        self.formLayout_10.setContentsMargins(0, 0, 0, 0)
        self.successVerticalLayout = QVBoxLayout()
        self.successVerticalLayout.setSpacing(0)
        self.successVerticalLayout.setObjectName(u"successVerticalLayout")
        self.successVerticalLayout.setContentsMargins(0, 10, 0, 0)
        self.verticalSpacer_18 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.successVerticalLayout.addItem(self.verticalSpacer_18)

        self.chargesuccessfullyLabel = QLabel(self.scrollAreaWidgetContents_9)
        self.chargesuccessfullyLabel.setObjectName(u"chargesuccessfullyLabel")
        self.chargesuccessfullyLabel.setMinimumSize(QSize(357, 0))
        self.chargesuccessfullyLabel.setFont(font1)
        self.chargesuccessfullyLabel.setAlignment(Qt.AlignCenter)

        self.successVerticalLayout.addWidget(self.chargesuccessfullyLabel)

        self.chargesuccessfullyVerticalLayout = QVBoxLayout()
        self.chargesuccessfullyVerticalLayout.setSpacing(3)
        self.chargesuccessfullyVerticalLayout.setObjectName(u"chargesuccessfullyVerticalLayout")
        self.chargesuccessfullyVerticalLayout.setContentsMargins(10, 10, 10, 0)
        self.verticalSpacer_21 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.chargesuccessfullyVerticalLayout.addItem(self.verticalSpacer_21)

        self.successiconPushButton = QPushButton(self.scrollAreaWidgetContents_9)
        self.successiconPushButton.setObjectName(u"successiconPushButton")
        self.successiconPushButton.setStyleSheet(u"QPushButton{\n"
"	border: None;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"images/success.png", QSize(), QIcon.Normal, QIcon.Off)
        self.successiconPushButton.setIcon(icon3)
        self.successiconPushButton.setIconSize(QSize(120, 120))

        self.chargesuccessfullyVerticalLayout.addWidget(self.successiconPushButton)

        self.verticalSpacer_23 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.chargesuccessfullyVerticalLayout.addItem(self.verticalSpacer_23)

        self.moneyLabel = QLabel(self.scrollAreaWidgetContents_9)
        self.moneyLabel.setObjectName(u"moneyLabel")
        self.moneyLabel.setMinimumSize(QSize(0, 0))
        font5 = QFont()
        font5.setPointSize(20)
        self.moneyLabel.setFont(font5)
        self.moneyLabel.setAlignment(Qt.AlignCenter)

        self.chargesuccessfullyVerticalLayout.addWidget(self.moneyLabel)

        self.verticalSpacer_24 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.chargesuccessfullyVerticalLayout.addItem(self.verticalSpacer_24)

        self.moneyvalueLabel = QLabel(self.scrollAreaWidgetContents_9)
        self.moneyvalueLabel.setObjectName(u"moneyvalueLabel")
        self.moneyvalueLabel.setMinimumSize(QSize(0, 0))
        self.moneyvalueLabel.setFont(font5)
        self.moneyvalueLabel.setAlignment(Qt.AlignCenter)

        self.chargesuccessfullyVerticalLayout.addWidget(self.moneyvalueLabel)

        self.verticalSpacer_25 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.chargesuccessfullyVerticalLayout.addItem(self.verticalSpacer_25)

        self.detailsLabel = QLabel(self.scrollAreaWidgetContents_9)
        self.detailsLabel.setObjectName(u"detailsLabel")
        self.detailsLabel.setMinimumSize(QSize(0, 0))
        self.detailsLabel.setFont(font1)
        self.detailsLabel.setAlignment(Qt.AlignCenter)

        self.chargesuccessfullyVerticalLayout.addWidget(self.detailsLabel)

        self.stationidHorizontalLayout = QHBoxLayout()
        self.stationidHorizontalLayout.setSpacing(0)
        self.stationidHorizontalLayout.setObjectName(u"stationidHorizontalLayout")
        self.stationidHorizontalLayout.setContentsMargins(40, -1, 0, -1)
        self.stationidLabel = QLabel(self.scrollAreaWidgetContents_9)
        self.stationidLabel.setObjectName(u"stationidLabel")
        self.stationidLabel.setMaximumSize(QSize(100, 16777215))
        self.stationidLabel.setFont(font)

        self.stationidHorizontalLayout.addWidget(self.stationidLabel)

        self.stationidvalueLabel = QLabel(self.scrollAreaWidgetContents_9)
        self.stationidvalueLabel.setObjectName(u"stationidvalueLabel")
        self.stationidvalueLabel.setMaximumSize(QSize(196, 16777215))
        self.stationidvalueLabel.setFont(font)

        self.stationidHorizontalLayout.addWidget(self.stationidvalueLabel)


        self.chargesuccessfullyVerticalLayout.addLayout(self.stationidHorizontalLayout)

        self.companyHorizontalLayout = QHBoxLayout()
        self.companyHorizontalLayout.setSpacing(0)
        self.companyHorizontalLayout.setObjectName(u"companyHorizontalLayout")
        self.companyHorizontalLayout.setContentsMargins(40, -1, 0, -1)
        self.companyLabel = QLabel(self.scrollAreaWidgetContents_9)
        self.companyLabel.setObjectName(u"companyLabel")
        self.companyLabel.setMaximumSize(QSize(100, 16777215))
        self.companyLabel.setFont(font)

        self.companyHorizontalLayout.addWidget(self.companyLabel)

        self.companyvalueLabel = QLabel(self.scrollAreaWidgetContents_9)
        self.companyvalueLabel.setObjectName(u"companyvalueLabel")
        self.companyvalueLabel.setMaximumSize(QSize(196, 16777215))
        self.companyvalueLabel.setFont(font)

        self.companyHorizontalLayout.addWidget(self.companyvalueLabel)


        self.chargesuccessfullyVerticalLayout.addLayout(self.companyHorizontalLayout)

        self.typeHorizontalLayout = QHBoxLayout()
        self.typeHorizontalLayout.setSpacing(0)
        self.typeHorizontalLayout.setObjectName(u"typeHorizontalLayout")
        self.typeHorizontalLayout.setContentsMargins(40, -1, 0, -1)
        self.typeLabel = QLabel(self.scrollAreaWidgetContents_9)
        self.typeLabel.setObjectName(u"typeLabel")
        self.typeLabel.setMaximumSize(QSize(100, 16777215))
        self.typeLabel.setFont(font)

        self.typeHorizontalLayout.addWidget(self.typeLabel)

        self.typevalueLabel = QLabel(self.scrollAreaWidgetContents_9)
        self.typevalueLabel.setObjectName(u"typevalueLabel")
        self.typevalueLabel.setMaximumSize(QSize(196, 16777215))
        self.typevalueLabel.setFont(font)

        self.typeHorizontalLayout.addWidget(self.typevalueLabel)


        self.chargesuccessfullyVerticalLayout.addLayout(self.typeHorizontalLayout)

        self.timeHorizontalLayout = QHBoxLayout()
        self.timeHorizontalLayout.setSpacing(0)
        self.timeHorizontalLayout.setObjectName(u"timeHorizontalLayout")
        self.timeHorizontalLayout.setContentsMargins(40, -1, 0, -1)
        self.timeLabel_2 = QLabel(self.scrollAreaWidgetContents_9)
        self.timeLabel_2.setObjectName(u"timeLabel_2")
        self.timeLabel_2.setMaximumSize(QSize(100, 16777215))
        self.timeLabel_2.setFont(font)

        self.timeHorizontalLayout.addWidget(self.timeLabel_2)

        self.timevalueLabel_2 = QLabel(self.scrollAreaWidgetContents_9)
        self.timevalueLabel_2.setObjectName(u"timevalueLabel_2")
        self.timevalueLabel_2.setMaximumSize(QSize(196, 16777215))
        self.timevalueLabel_2.setFont(font)

        self.timeHorizontalLayout.addWidget(self.timevalueLabel_2)


        self.chargesuccessfullyVerticalLayout.addLayout(self.timeHorizontalLayout)

        self.rateHorizontalLayout = QHBoxLayout()
        self.rateHorizontalLayout.setSpacing(0)
        self.rateHorizontalLayout.setObjectName(u"rateHorizontalLayout")
        self.rateHorizontalLayout.setContentsMargins(40, -1, 0, -1)
        self.rateLabel = QLabel(self.scrollAreaWidgetContents_9)
        self.rateLabel.setObjectName(u"rateLabel")
        self.rateLabel.setMaximumSize(QSize(100, 16777215))
        self.rateLabel.setFont(font)

        self.rateHorizontalLayout.addWidget(self.rateLabel)

        self.ratevalueLabel = QLabel(self.scrollAreaWidgetContents_9)
        self.ratevalueLabel.setObjectName(u"ratevalueLabel")
        self.ratevalueLabel.setMaximumSize(QSize(196, 16777215))
        self.ratevalueLabel.setFont(font)

        self.rateHorizontalLayout.addWidget(self.ratevalueLabel)


        self.chargesuccessfullyVerticalLayout.addLayout(self.rateHorizontalLayout)

        self.timestampHorizontalLayout = QHBoxLayout()
        self.timestampHorizontalLayout.setSpacing(0)
        self.timestampHorizontalLayout.setObjectName(u"timestampHorizontalLayout")
        self.timestampHorizontalLayout.setContentsMargins(40, -1, 0, -1)
        self.timestampLabel = QLabel(self.scrollAreaWidgetContents_9)
        self.timestampLabel.setObjectName(u"timestampLabel")
        self.timestampLabel.setMaximumSize(QSize(100, 16777215))
        self.timestampLabel.setFont(font)

        self.timestampHorizontalLayout.addWidget(self.timestampLabel)

        self.timestampvalueLabel = QLabel(self.scrollAreaWidgetContents_9)
        self.timestampvalueLabel.setObjectName(u"timestampvalueLabel")
        self.timestampvalueLabel.setMaximumSize(QSize(196, 16777215))
        self.timestampvalueLabel.setFont(font)

        self.timestampHorizontalLayout.addWidget(self.timestampvalueLabel)


        self.chargesuccessfullyVerticalLayout.addLayout(self.timestampHorizontalLayout)

        self.verticalSpacer_22 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.chargesuccessfullyVerticalLayout.addItem(self.verticalSpacer_22)

        self.doneHorizontalLayout = QHBoxLayout()
        self.doneHorizontalLayout.setSpacing(0)
        self.doneHorizontalLayout.setObjectName(u"doneHorizontalLayout")
        self.donePushButton = QPushButton(self.scrollAreaWidgetContents_9)
        self.donePushButton.setObjectName(u"donePushButton")
        self.donePushButton.setMinimumSize(QSize(0, 35))
        self.donePushButton.setMaximumSize(QSize(100, 16777215))
        self.donePushButton.setFont(font1)
        self.donePushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.donePushButton.setStyleSheet(u"QPushButton{\n"
"	background-color: #f6da23;\n"
"	border-radius: 10px;\n"
"	color: #ffffff;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #f5d60a;\n"
"}")
        self.donePushButton.setIconSize(QSize(20, 20))

        self.doneHorizontalLayout.addWidget(self.donePushButton)


        self.chargesuccessfullyVerticalLayout.addLayout(self.doneHorizontalLayout)

        self.verticalSpacer_5 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.chargesuccessfullyVerticalLayout.addItem(self.verticalSpacer_5)


        self.successVerticalLayout.addLayout(self.chargesuccessfullyVerticalLayout)


        self.formLayout_10.setLayout(0, QFormLayout.FieldRole, self.successVerticalLayout)

        self.successScrollArea.setWidget(self.scrollAreaWidgetContents_9)
        self.successLabel = QLabel(self.successPage)
        self.successLabel.setObjectName(u"successLabel")
        self.successLabel.setGeometry(QRect(10, 10, 121, 21))
        self.successLabel.setFont(font)
        self.stackedWidget.addWidget(self.successPage)
        self.countdownLabel_3 = QLabel(Form)
        self.countdownLabel_3.setObjectName(u"countdownLabel_3")
        self.countdownLabel_3.setGeometry(QRect(280, 80, 357, 23))
        self.countdownLabel_3.setMinimumSize(QSize(357, 0))
        self.countdownLabel_3.setFont(font1)
        self.countdownLabel_3.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.timerLabel.setText(QCoreApplication.translate("Form", u"Timer", None))
        self.settimerLabel.setText(QCoreApplication.translate("Form", u"Set Timer:", None))
        self.timer6.setPlaceholderText("")
        self.timer5.setPlaceholderText("")
        self.colonLabel1.setText(QCoreApplication.translate("Form", u":", None))
        self.timer4.setPlaceholderText("")
        self.timer3.setPlaceholderText("")
        self.colonLabel2.setText(QCoreApplication.translate("Form", u":", None))
        self.timer2.setPlaceholderText("")
        self.timer1.setPlaceholderText("")
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
        self.startPushButton.setText(QCoreApplication.translate("Form", u"Start", None))
        self.closePushButton.setText("")
        self.charginginprocessLabel.setText(QCoreApplication.translate("Form", u"Charging In Process:", None))
        self.chargingstationiconPushButton.setText("")
        self.timeLabel.setText(QCoreApplication.translate("Form", u"Time:", None))
        self.timercountdownLabel.setText(QCoreApplication.translate("Form", u"00:00:00", None))
        self.stopPushButton.setText(QCoreApplication.translate("Form", u"STOP", None))
        self.chargingLabel.setText(QCoreApplication.translate("Form", u"Charging", None))
        self.chargesuccessfullyLabel.setText(QCoreApplication.translate("Form", u"Charge Successfully:", None))
        self.successiconPushButton.setText("")
        self.moneyLabel.setText(QCoreApplication.translate("Form", u"Money:", None))
        self.moneyvalueLabel.setText(QCoreApplication.translate("Form", u"0     THB", None))
        self.detailsLabel.setText(QCoreApplication.translate("Form", u"Details:", None))
        self.stationidLabel.setText(QCoreApplication.translate("Form", u"Station ID:", None))
        self.stationidvalueLabel.setText("")
        self.companyLabel.setText(QCoreApplication.translate("Form", u"Company:", None))
        self.companyvalueLabel.setText("")
        self.typeLabel.setText(QCoreApplication.translate("Form", u"Type:", None))
        self.typevalueLabel.setText("")
        self.timeLabel_2.setText(QCoreApplication.translate("Form", u"Time:", None))
        self.timevalueLabel_2.setText("")
        self.rateLabel.setText(QCoreApplication.translate("Form", u"Rate:", None))
        self.ratevalueLabel.setText("")
        self.timestampLabel.setText(QCoreApplication.translate("Form", u"TimeStamp:", None))
        self.timestampvalueLabel.setText("")
        self.donePushButton.setText(QCoreApplication.translate("Form", u"DONE", None))
        self.successLabel.setText(QCoreApplication.translate("Form", u"Success", None))
        self.countdownLabel_3.setText(QCoreApplication.translate("Form", u"Charge Successfully:", None))
    # retranslateUi

