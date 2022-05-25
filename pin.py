# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pin.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QStackedWidget, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(361, 640)
        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 361, 641))
        self.createpinPage = QWidget()
        self.createpinPage.setObjectName(u"createpinPage")
        self.gridLayoutWidget = QWidget(self.createpinPage)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 250, 361, 391))
        self.keyboardGridLayout = QGridLayout(self.gridLayoutWidget)
        self.keyboardGridLayout.setSpacing(0)
        self.keyboardGridLayout.setObjectName(u"keyboardGridLayout")
        self.keyboardGridLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_7 = QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(75, 75))
        self.pushButton_7.setMaximumSize(QSize(75, 75))
        self.pushButton_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #cecece;\n"
"	border-radius: 37px;\n"
"	font: 22px Arial;\n"
"	\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background: #bbbbbf;\n"
"}")

        self.keyboardGridLayout.addWidget(self.pushButton_7, 2, 0, 1, 1)

        self.pushButton_1 = QPushButton(self.gridLayoutWidget)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setMinimumSize(QSize(75, 75))
        self.pushButton_1.setMaximumSize(QSize(75, 75))
        self.pushButton_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_1.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #cecece;\n"
"	border-radius: 37px;\n"
"	font: 22px Arial;\n"
"	\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background: #bbbbbf;\n"
"}")

        self.keyboardGridLayout.addWidget(self.pushButton_1, 0, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(75, 75))
        self.pushButton_5.setMaximumSize(QSize(75, 75))
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #cecece;\n"
"	border-radius: 37px;\n"
"	font: 22px Arial;\n"
"	\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background: #bbbbbf;\n"
"}")

        self.keyboardGridLayout.addWidget(self.pushButton_5, 1, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(75, 75))
        self.pushButton_3.setMaximumSize(QSize(75, 75))
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #cecece;\n"
"	border-radius: 37px;\n"
"	font: 22px Arial;\n"
"	\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background: #bbbbbf;\n"
"}")

        self.keyboardGridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)

        self.pushButton_4 = QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(75, 75))
        self.pushButton_4.setMaximumSize(QSize(75, 75))
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #cecece;\n"
"	border-radius: 37px;\n"
"	font: 22px Arial;\n"
"	\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background: #bbbbbf;\n"
"}")

        self.keyboardGridLayout.addWidget(self.pushButton_4, 1, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QSize(75, 75))
        self.pushButton_2.setMaximumSize(QSize(75, 75))
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #cecece;\n"
"	border-radius: 37px;\n"
"	font: 22px Arial;\n"
"	\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background: #bbbbbf;\n"
"}")
        self.pushButton_2.setIconSize(QSize(16, 16))
        self.pushButton_2.setFlat(False)

        self.keyboardGridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.pushButton_9 = QPushButton(self.gridLayoutWidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(75, 75))
        self.pushButton_9.setMaximumSize(QSize(75, 75))
        self.pushButton_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #cecece;\n"
"	border-radius: 37px;\n"
"	font: 22px Arial;\n"
"	\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background: #bbbbbf;\n"
"}")

        self.keyboardGridLayout.addWidget(self.pushButton_9, 2, 2, 1, 1)

        self.pushButton_0 = QPushButton(self.gridLayoutWidget)
        self.pushButton_0.setObjectName(u"pushButton_0")
        self.pushButton_0.setMinimumSize(QSize(75, 75))
        self.pushButton_0.setMaximumSize(QSize(75, 75))
        self.pushButton_0.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_0.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #cecece;\n"
"	border-radius: 37px;\n"
"	font: 22px Arial;\n"
"	\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background: #bbbbbf;\n"
"}")

        self.keyboardGridLayout.addWidget(self.pushButton_0, 3, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(75, 75))
        self.pushButton_6.setMaximumSize(QSize(75, 75))
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #cecece;\n"
"	border-radius: 37px;\n"
"	font: 22px Arial;\n"
"	\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background: #bbbbbf;\n"
"}")

        self.keyboardGridLayout.addWidget(self.pushButton_6, 1, 2, 1, 1)

        self.pushButton_8 = QPushButton(self.gridLayoutWidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(75, 75))
        self.pushButton_8.setMaximumSize(QSize(75, 75))
        self.pushButton_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_8.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #cecece;\n"
"	border-radius: 37px;\n"
"	font: 22px Arial;\n"
"	\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background: #bbbbbf;\n"
"}")

        self.keyboardGridLayout.addWidget(self.pushButton_8, 2, 1, 1, 1)

        self.pushButton_delete = QPushButton(self.gridLayoutWidget)
        self.pushButton_delete.setObjectName(u"pushButton_delete")
        self.pushButton_delete.setMinimumSize(QSize(75, 75))
        self.pushButton_delete.setMaximumSize(QSize(75, 75))
        self.pushButton_delete.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_delete.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #cecece;\n"
"	border-radius: 37px;\n"
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

        self.keyboardGridLayout.addWidget(self.pushButton_delete, 3, 2, 1, 1)

        self.createapincodeLabel = QLabel(self.createpinPage)
        self.createapincodeLabel.setObjectName(u"createapincodeLabel")
        self.createapincodeLabel.setGeometry(QRect(0, 70, 361, 31))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setBold(False)
        font.setItalic(False)
        self.createapincodeLabel.setFont(font)
        self.createapincodeLabel.setStyleSheet(u"font: 20px Arial;\n"
"color: black;")
        self.createapincodeLabel.setAlignment(Qt.AlignCenter)
        self.pin1 = QPushButton(self.createpinPage)
        self.pin1.setObjectName(u"pin1")
        self.pin1.setGeometry(QRect(90, 160, 20, 20))
        self.pin1.setMinimumSize(QSize(20, 20))
        self.pin1.setMaximumSize(QSize(20, 20))
        self.pin1.setStyleSheet(u"QPushButton\n"
"{\n"
"	border-radius: 10px;\n"
"	border: 3px solid #cecece;\n"
"}\n"
"")
        self.pin2 = QPushButton(self.createpinPage)
        self.pin2.setObjectName(u"pin2")
        self.pin2.setGeometry(QRect(120, 160, 20, 20))
        self.pin2.setMinimumSize(QSize(20, 20))
        self.pin2.setMaximumSize(QSize(20, 20))
        self.pin2.setStyleSheet(u"QPushButton\n"
"{\n"
"	border-radius: 10px;\n"
"	border: 3px solid #cecece;\n"
"}\n"
"")
        self.pin3 = QPushButton(self.createpinPage)
        self.pin3.setObjectName(u"pin3")
        self.pin3.setGeometry(QRect(150, 160, 20, 20))
        self.pin3.setMinimumSize(QSize(20, 20))
        self.pin3.setMaximumSize(QSize(20, 20))
        self.pin3.setStyleSheet(u"QPushButton\n"
"{\n"
"	border-radius: 10px;\n"
"	border: 3px solid #cecece;\n"
"}\n"
"")
        self.pin4 = QPushButton(self.createpinPage)
        self.pin4.setObjectName(u"pin4")
        self.pin4.setGeometry(QRect(180, 160, 20, 20))
        self.pin4.setMinimumSize(QSize(20, 20))
        self.pin4.setMaximumSize(QSize(20, 20))
        self.pin4.setStyleSheet(u"QPushButton\n"
"{\n"
"	border-radius: 10px;\n"
"	border: 3px solid #cecece;\n"
"}\n"
"")
        self.pin6 = QPushButton(self.createpinPage)
        self.pin6.setObjectName(u"pin6")
        self.pin6.setGeometry(QRect(240, 160, 20, 20))
        self.pin6.setMinimumSize(QSize(20, 20))
        self.pin6.setMaximumSize(QSize(20, 20))
        self.pin6.setStyleSheet(u"QPushButton\n"
"{\n"
"	border-radius: 10px;\n"
"	border: 3px solid #cecece;\n"
"}\n"
"")
        self.pin5 = QPushButton(self.createpinPage)
        self.pin5.setObjectName(u"pin5")
        self.pin5.setGeometry(QRect(210, 160, 20, 20))
        self.pin5.setMinimumSize(QSize(20, 20))
        self.pin5.setMaximumSize(QSize(20, 20))
        self.pin5.setStyleSheet(u"QPushButton\n"
"{\n"
"	border-radius: 10px;\n"
"	border: 3px solid #cecece;\n"
"}\n"
"")
        self.stackedWidget.addWidget(self.createpinPage)
        self.confirmpinPage = QWidget()
        self.confirmpinPage.setObjectName(u"confirmpinPage")
        self.gridLayoutWidget_2 = QWidget(self.confirmpinPage)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(0, 250, 361, 391))
        self.keyboardGridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.keyboardGridLayout_2.setSpacing(0)
        self.keyboardGridLayout_2.setObjectName(u"keyboardGridLayout_2")
        self.keyboardGridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_1_2 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_1_2.setObjectName(u"pushButton_1_2")
        self.pushButton_1_2.setMinimumSize(QSize(75, 75))
        self.pushButton_1_2.setMaximumSize(QSize(75, 75))
        self.pushButton_1_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_1_2.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #cecece;\n"
"	border-radius: 37px;\n"
"	font: 22px Arial;\n"
"	\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background: #bbbbbf;\n"
"}")

        self.keyboardGridLayout_2.addWidget(self.pushButton_1_2, 0, 0, 1, 1)

        self.pushButton_5_2 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_5_2.setObjectName(u"pushButton_5_2")
        self.pushButton_5_2.setMinimumSize(QSize(75, 75))
        self.pushButton_5_2.setMaximumSize(QSize(75, 75))
        self.pushButton_5_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_5_2.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #cecece;\n"
"	border-radius: 37px;\n"
"	font: 22px Arial;\n"
"	\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background: #bbbbbf;\n"
"}")

        self.keyboardGridLayout_2.addWidget(self.pushButton_5_2, 1, 1, 1, 1)

        self.pushButton_6_2 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_6_2.setObjectName(u"pushButton_6_2")
        self.pushButton_6_2.setMinimumSize(QSize(75, 75))
        self.pushButton_6_2.setMaximumSize(QSize(75, 75))
        self.pushButton_6_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_6_2.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #cecece;\n"
"	border-radius: 37px;\n"
"	font: 22px Arial;\n"
"	\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background: #bbbbbf;\n"
"}")

        self.keyboardGridLayout_2.addWidget(self.pushButton_6_2, 1, 2, 1, 1)

        self.pushButton_4_2 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_4_2.setObjectName(u"pushButton_4_2")
        self.pushButton_4_2.setMinimumSize(QSize(75, 75))
        self.pushButton_4_2.setMaximumSize(QSize(75, 75))
        self.pushButton_4_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_4_2.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #cecece;\n"
"	border-radius: 37px;\n"
"	font: 22px Arial;\n"
"	\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background: #bbbbbf;\n"
"}")

        self.keyboardGridLayout_2.addWidget(self.pushButton_4_2, 1, 0, 1, 1)

        self.pushButton_2_2 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_2_2.setObjectName(u"pushButton_2_2")
        self.pushButton_2_2.setMinimumSize(QSize(75, 75))
        self.pushButton_2_2.setMaximumSize(QSize(75, 75))
        self.pushButton_2_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2_2.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #cecece;\n"
"	border-radius: 37px;\n"
"	font: 22px Arial;\n"
"	\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background: #bbbbbf;\n"
"}")

        self.keyboardGridLayout_2.addWidget(self.pushButton_2_2, 0, 1, 1, 1)

        self.pushButton_7_2 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_7_2.setObjectName(u"pushButton_7_2")
        self.pushButton_7_2.setMinimumSize(QSize(75, 75))
        self.pushButton_7_2.setMaximumSize(QSize(75, 75))
        self.pushButton_7_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_7_2.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #cecece;\n"
"	border-radius: 37px;\n"
"	font: 22px Arial;\n"
"	\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background: #bbbbbf;\n"
"}")

        self.keyboardGridLayout_2.addWidget(self.pushButton_7_2, 2, 0, 1, 1)

        self.pushButton_8_2 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_8_2.setObjectName(u"pushButton_8_2")
        self.pushButton_8_2.setMinimumSize(QSize(75, 75))
        self.pushButton_8_2.setMaximumSize(QSize(75, 75))
        self.pushButton_8_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_8_2.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #cecece;\n"
"	border-radius: 37px;\n"
"	font: 22px Arial;\n"
"	\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background: #bbbbbf;\n"
"}")

        self.keyboardGridLayout_2.addWidget(self.pushButton_8_2, 2, 1, 1, 1)

        self.pushButton_9_2 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_9_2.setObjectName(u"pushButton_9_2")
        self.pushButton_9_2.setMinimumSize(QSize(75, 75))
        self.pushButton_9_2.setMaximumSize(QSize(75, 75))
        self.pushButton_9_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_9_2.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #cecece;\n"
"	border-radius: 37px;\n"
"	font: 22px Arial;\n"
"	\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background: #bbbbbf;\n"
"}")

        self.keyboardGridLayout_2.addWidget(self.pushButton_9_2, 2, 2, 1, 1)

        self.pushButton_0_2 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_0_2.setObjectName(u"pushButton_0_2")
        self.pushButton_0_2.setMinimumSize(QSize(75, 75))
        self.pushButton_0_2.setMaximumSize(QSize(75, 75))
        self.pushButton_0_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_0_2.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #cecece;\n"
"	border-radius: 37px;\n"
"	font: 22px Arial;\n"
"	\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background: #bbbbbf;\n"
"}")

        self.keyboardGridLayout_2.addWidget(self.pushButton_0_2, 3, 1, 1, 1)

        self.pushButton_delete_2 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_delete_2.setObjectName(u"pushButton_delete_2")
        self.pushButton_delete_2.setMinimumSize(QSize(75, 75))
        self.pushButton_delete_2.setMaximumSize(QSize(75, 75))
        self.pushButton_delete_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_delete_2.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #cecece;\n"
"	border-radius: 37px;\n"
"	font: 22px Arial;\n"
"	\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background: #bbbbbf;\n"
"}")
        self.pushButton_delete_2.setIcon(icon)
        self.pushButton_delete_2.setIconSize(QSize(25, 25))

        self.keyboardGridLayout_2.addWidget(self.pushButton_delete_2, 3, 2, 1, 1)

        self.pushButton_3_2 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_3_2.setObjectName(u"pushButton_3_2")
        self.pushButton_3_2.setMinimumSize(QSize(75, 75))
        self.pushButton_3_2.setMaximumSize(QSize(75, 75))
        self.pushButton_3_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3_2.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #cecece;\n"
"	border-radius: 37px;\n"
"	font: 22px Arial;\n"
"	\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background: #bbbbbf;\n"
"}")

        self.keyboardGridLayout_2.addWidget(self.pushButton_3_2, 0, 2, 1, 1)

        self.confirmpincodeLabel = QLabel(self.confirmpinPage)
        self.confirmpincodeLabel.setObjectName(u"confirmpincodeLabel")
        self.confirmpincodeLabel.setGeometry(QRect(0, 70, 361, 31))
        self.confirmpincodeLabel.setFont(font)
        self.confirmpincodeLabel.setStyleSheet(u"font: 20px Arial;\n"
"color: black;")
        self.confirmpincodeLabel.setAlignment(Qt.AlignCenter)
        self.pin1_2 = QPushButton(self.confirmpinPage)
        self.pin1_2.setObjectName(u"pin1_2")
        self.pin1_2.setGeometry(QRect(90, 160, 20, 20))
        self.pin1_2.setMinimumSize(QSize(20, 20))
        self.pin1_2.setMaximumSize(QSize(20, 20))
        self.pin1_2.setStyleSheet(u"QPushButton\n"
"{\n"
"	border-radius: 10px;\n"
"	border: 3px solid #cecece;\n"
"}\n"
"")
        self.pin2_2 = QPushButton(self.confirmpinPage)
        self.pin2_2.setObjectName(u"pin2_2")
        self.pin2_2.setGeometry(QRect(120, 160, 20, 20))
        self.pin2_2.setMinimumSize(QSize(20, 20))
        self.pin2_2.setMaximumSize(QSize(20, 20))
        self.pin2_2.setStyleSheet(u"QPushButton\n"
"{\n"
"	border-radius: 10px;\n"
"	border: 3px solid #cecece;\n"
"}\n"
"")
        self.pin3_2 = QPushButton(self.confirmpinPage)
        self.pin3_2.setObjectName(u"pin3_2")
        self.pin3_2.setGeometry(QRect(150, 160, 20, 20))
        self.pin3_2.setMinimumSize(QSize(20, 20))
        self.pin3_2.setMaximumSize(QSize(20, 20))
        self.pin3_2.setStyleSheet(u"QPushButton\n"
"{\n"
"	border-radius: 10px;\n"
"	border: 3px solid #cecece;\n"
"}\n"
"")
        self.pin4_2 = QPushButton(self.confirmpinPage)
        self.pin4_2.setObjectName(u"pin4_2")
        self.pin4_2.setGeometry(QRect(180, 160, 20, 20))
        self.pin4_2.setMinimumSize(QSize(20, 20))
        self.pin4_2.setMaximumSize(QSize(20, 20))
        self.pin4_2.setStyleSheet(u"QPushButton\n"
"{\n"
"	border-radius: 10px;\n"
"	border: 3px solid #cecece;\n"
"}\n"
"")
        self.pin5_2 = QPushButton(self.confirmpinPage)
        self.pin5_2.setObjectName(u"pin5_2")
        self.pin5_2.setGeometry(QRect(210, 160, 20, 20))
        self.pin5_2.setMinimumSize(QSize(20, 20))
        self.pin5_2.setMaximumSize(QSize(20, 20))
        self.pin5_2.setStyleSheet(u"QPushButton\n"
"{\n"
"	border-radius: 10px;\n"
"	border: 3px solid #cecece;\n"
"}\n"
"")
        self.pin6_2 = QPushButton(self.confirmpinPage)
        self.pin6_2.setObjectName(u"pin6_2")
        self.pin6_2.setGeometry(QRect(240, 160, 20, 20))
        self.pin6_2.setMinimumSize(QSize(20, 20))
        self.pin6_2.setMaximumSize(QSize(20, 20))
        self.pin6_2.setStyleSheet(u"QPushButton\n"
"{\n"
"	border-radius: 10px;\n"
"	border: 3px solid #cecece;\n"
"}\n"
"")
        self.stackedWidget.addWidget(self.confirmpinPage)
        self.enterpinPage = QWidget()
        self.enterpinPage.setObjectName(u"enterpinPage")
        self.pin1_3 = QPushButton(self.enterpinPage)
        self.pin1_3.setObjectName(u"pin1_3")
        self.pin1_3.setGeometry(QRect(90, 160, 20, 20))
        self.pin1_3.setMinimumSize(QSize(20, 20))
        self.pin1_3.setMaximumSize(QSize(20, 20))
        self.pin1_3.setStyleSheet(u"QPushButton\n"
"{\n"
"	border-radius: 10px;\n"
"	border: 3px solid #cecece;\n"
"}\n"
"")
        self.pin2_3 = QPushButton(self.enterpinPage)
        self.pin2_3.setObjectName(u"pin2_3")
        self.pin2_3.setGeometry(QRect(120, 160, 20, 20))
        self.pin2_3.setMinimumSize(QSize(20, 20))
        self.pin2_3.setMaximumSize(QSize(20, 20))
        self.pin2_3.setStyleSheet(u"QPushButton\n"
"{\n"
"	border-radius: 10px;\n"
"	border: 3px solid #cecece;\n"
"}\n"
"")
        self.gridLayoutWidget_3 = QWidget(self.enterpinPage)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(0, 250, 361, 391))
        self.keyboardGridLayout3 = QGridLayout(self.gridLayoutWidget_3)
        self.keyboardGridLayout3.setSpacing(0)
        self.keyboardGridLayout3.setObjectName(u"keyboardGridLayout3")
        self.keyboardGridLayout3.setContentsMargins(0, 0, 0, 0)
        self.pushButton_7_3 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_7_3.setObjectName(u"pushButton_7_3")
        self.pushButton_7_3.setMinimumSize(QSize(75, 75))
        self.pushButton_7_3.setMaximumSize(QSize(75, 75))
        self.pushButton_7_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_7_3.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #cecece;\n"
"	border-radius: 37px;\n"
"	font: 22px Arial;\n"
"	\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background: #bbbbbf;\n"
"}")

        self.keyboardGridLayout3.addWidget(self.pushButton_7_3, 2, 0, 1, 1)

        self.pushButton_1_3 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_1_3.setObjectName(u"pushButton_1_3")
        self.pushButton_1_3.setMinimumSize(QSize(75, 75))
        self.pushButton_1_3.setMaximumSize(QSize(75, 75))
        self.pushButton_1_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_1_3.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #cecece;\n"
"	border-radius: 37px;\n"
"	font: 22px Arial;\n"
"	\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background: #bbbbbf;\n"
"}")

        self.keyboardGridLayout3.addWidget(self.pushButton_1_3, 0, 0, 1, 1)

        self.pushButton_5_3 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_5_3.setObjectName(u"pushButton_5_3")
        self.pushButton_5_3.setMinimumSize(QSize(75, 75))
        self.pushButton_5_3.setMaximumSize(QSize(75, 75))
        self.pushButton_5_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_5_3.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #cecece;\n"
"	border-radius: 37px;\n"
"	font: 22px Arial;\n"
"	\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background: #bbbbbf;\n"
"}")

        self.keyboardGridLayout3.addWidget(self.pushButton_5_3, 1, 1, 1, 1)

        self.pushButton_3_3 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_3_3.setObjectName(u"pushButton_3_3")
        self.pushButton_3_3.setMinimumSize(QSize(75, 75))
        self.pushButton_3_3.setMaximumSize(QSize(75, 75))
        self.pushButton_3_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3_3.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #cecece;\n"
"	border-radius: 37px;\n"
"	font: 22px Arial;\n"
"	\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background: #bbbbbf;\n"
"}")

        self.keyboardGridLayout3.addWidget(self.pushButton_3_3, 0, 2, 1, 1)

        self.pushButton_4_3 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_4_3.setObjectName(u"pushButton_4_3")
        self.pushButton_4_3.setMinimumSize(QSize(75, 75))
        self.pushButton_4_3.setMaximumSize(QSize(75, 75))
        self.pushButton_4_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_4_3.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #cecece;\n"
"	border-radius: 37px;\n"
"	font: 22px Arial;\n"
"	\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background: #bbbbbf;\n"
"}")

        self.keyboardGridLayout3.addWidget(self.pushButton_4_3, 1, 0, 1, 1)

        self.pushButton_2_3 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_2_3.setObjectName(u"pushButton_2_3")
        sizePolicy.setHeightForWidth(self.pushButton_2_3.sizePolicy().hasHeightForWidth())
        self.pushButton_2_3.setSizePolicy(sizePolicy)
        self.pushButton_2_3.setMinimumSize(QSize(75, 75))
        self.pushButton_2_3.setMaximumSize(QSize(75, 75))
        self.pushButton_2_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2_3.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #cecece;\n"
"	border-radius: 37px;\n"
"	font: 22px Arial;\n"
"	\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background: #bbbbbf;\n"
"}")
        self.pushButton_2_3.setIconSize(QSize(16, 16))
        self.pushButton_2_3.setFlat(False)

        self.keyboardGridLayout3.addWidget(self.pushButton_2_3, 0, 1, 1, 1)

        self.pushButton_9_3 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_9_3.setObjectName(u"pushButton_9_3")
        self.pushButton_9_3.setMinimumSize(QSize(75, 75))
        self.pushButton_9_3.setMaximumSize(QSize(75, 75))
        self.pushButton_9_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_9_3.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #cecece;\n"
"	border-radius: 37px;\n"
"	font: 22px Arial;\n"
"	\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background: #bbbbbf;\n"
"}")

        self.keyboardGridLayout3.addWidget(self.pushButton_9_3, 2, 2, 1, 1)

        self.pushButton_0_3 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_0_3.setObjectName(u"pushButton_0_3")
        self.pushButton_0_3.setMinimumSize(QSize(75, 75))
        self.pushButton_0_3.setMaximumSize(QSize(75, 75))
        self.pushButton_0_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_0_3.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #cecece;\n"
"	border-radius: 37px;\n"
"	font: 22px Arial;\n"
"	\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background: #bbbbbf;\n"
"}")

        self.keyboardGridLayout3.addWidget(self.pushButton_0_3, 3, 1, 1, 1)

        self.pushButton_6_3 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_6_3.setObjectName(u"pushButton_6_3")
        self.pushButton_6_3.setMinimumSize(QSize(75, 75))
        self.pushButton_6_3.setMaximumSize(QSize(75, 75))
        self.pushButton_6_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_6_3.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #cecece;\n"
"	border-radius: 37px;\n"
"	font: 22px Arial;\n"
"	\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background: #bbbbbf;\n"
"}")

        self.keyboardGridLayout3.addWidget(self.pushButton_6_3, 1, 2, 1, 1)

        self.pushButton_8_3 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_8_3.setObjectName(u"pushButton_8_3")
        self.pushButton_8_3.setMinimumSize(QSize(75, 75))
        self.pushButton_8_3.setMaximumSize(QSize(75, 75))
        self.pushButton_8_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_8_3.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #cecece;\n"
"	border-radius: 37px;\n"
"	font: 22px Arial;\n"
"	\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background: #bbbbbf;\n"
"}")

        self.keyboardGridLayout3.addWidget(self.pushButton_8_3, 2, 1, 1, 1)

        self.pushButton_delete_3 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_delete_3.setObjectName(u"pushButton_delete_3")
        self.pushButton_delete_3.setMinimumSize(QSize(75, 75))
        self.pushButton_delete_3.setMaximumSize(QSize(75, 75))
        self.pushButton_delete_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_delete_3.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #cecece;\n"
"	border-radius: 37px;\n"
"	font: 22px Arial;\n"
"	\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background: #bbbbbf;\n"
"}")
        self.pushButton_delete_3.setIcon(icon)
        self.pushButton_delete_3.setIconSize(QSize(25, 25))

        self.keyboardGridLayout3.addWidget(self.pushButton_delete_3, 3, 2, 1, 1)

        self.pin4_3 = QPushButton(self.enterpinPage)
        self.pin4_3.setObjectName(u"pin4_3")
        self.pin4_3.setGeometry(QRect(180, 160, 20, 20))
        self.pin4_3.setMinimumSize(QSize(20, 20))
        self.pin4_3.setMaximumSize(QSize(20, 20))
        self.pin4_3.setStyleSheet(u"QPushButton\n"
"{\n"
"	border-radius: 10px;\n"
"	border: 3px solid #cecece;\n"
"}\n"
"")
        self.pin6_3 = QPushButton(self.enterpinPage)
        self.pin6_3.setObjectName(u"pin6_3")
        self.pin6_3.setGeometry(QRect(240, 160, 20, 20))
        self.pin6_3.setMinimumSize(QSize(20, 20))
        self.pin6_3.setMaximumSize(QSize(20, 20))
        self.pin6_3.setStyleSheet(u"QPushButton\n"
"{\n"
"	border-radius: 10px;\n"
"	border: 3px solid #cecece;\n"
"}\n"
"")
        self.pin3_3 = QPushButton(self.enterpinPage)
        self.pin3_3.setObjectName(u"pin3_3")
        self.pin3_3.setGeometry(QRect(150, 160, 20, 20))
        self.pin3_3.setMinimumSize(QSize(20, 20))
        self.pin3_3.setMaximumSize(QSize(20, 20))
        self.pin3_3.setStyleSheet(u"QPushButton\n"
"{\n"
"	border-radius: 10px;\n"
"	border: 3px solid #cecece;\n"
"}\n"
"")
        self.entepincodeLabel = QLabel(self.enterpinPage)
        self.entepincodeLabel.setObjectName(u"entepincodeLabel")
        self.entepincodeLabel.setGeometry(QRect(0, 70, 361, 31))
        self.entepincodeLabel.setFont(font)
        self.entepincodeLabel.setStyleSheet(u"font: 20px Arial;\n"
"color: black;")
        self.entepincodeLabel.setAlignment(Qt.AlignCenter)
        self.pin5_3 = QPushButton(self.enterpinPage)
        self.pin5_3.setObjectName(u"pin5_3")
        self.pin5_3.setGeometry(QRect(210, 160, 20, 20))
        self.pin5_3.setMinimumSize(QSize(20, 20))
        self.pin5_3.setMaximumSize(QSize(20, 20))
        self.pin5_3.setStyleSheet(u"QPushButton\n"
"{\n"
"	border-radius: 10px;\n"
"	border: 3px solid #cecece;\n"
"}\n"
"")
        self.closePushButton = QPushButton(self.enterpinPage)
        self.closePushButton.setObjectName(u"closePushButton")
        self.closePushButton.setGeometry(QRect(320, 20, 31, 24))
        self.closePushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.closePushButton.setStyleSheet(u"QPushButton{\n"
"	border: None;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"images/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closePushButton.setIcon(icon1)
        self.closePushButton.setIconSize(QSize(20, 20))
        self.stackedWidget.addWidget(self.enterpinPage)
        self.enterpasswordPage = QWidget()
        self.enterpasswordPage.setObjectName(u"enterpasswordPage")
        self.enterpasswordLabel = QLabel(self.enterpasswordPage)
        self.enterpasswordLabel.setObjectName(u"enterpasswordLabel")
        self.enterpasswordLabel.setGeometry(QRect(0, 130, 361, 31))
        self.enterpasswordLabel.setFont(font)
        self.enterpasswordLabel.setStyleSheet(u"font: 20px Arial;\n"
"color: black;")
        self.enterpasswordLabel.setAlignment(Qt.AlignCenter)
        self.enterpasswordLineEdit = QLineEdit(self.enterpasswordPage)
        self.enterpasswordLineEdit.setObjectName(u"enterpasswordLineEdit")
        self.enterpasswordLineEdit.setGeometry(QRect(20, 190, 321, 51))
        self.enterpasswordLineEdit.setStyleSheet(u"QLineEdit\n"
"{\n"
"	border: 2px solid #71cd00;\n"
"	border-radius: 10px;\n"
"font: 18pt Arial;\n"
"}\n"
"QLineEdit:focus\n"
"{\n"
"	border: 2px solid #71cd00;\n"
"}")
        self.okPushButton = QPushButton(self.enterpasswordPage)
        self.okPushButton.setObjectName(u"okPushButton")
        self.okPushButton.setGeometry(QRect(140, 290, 75, 51))
        self.okPushButton.setFont(font)
        self.okPushButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: #71cd00;\n"
"	border-radius: 10px;\n"
"	font: 20px Arial;\n"
"	color: #ffffff;\n"
"	\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background: #468000;;\n"
"}")
        self.closePushButton_2 = QPushButton(self.enterpasswordPage)
        self.closePushButton_2.setObjectName(u"closePushButton_2")
        self.closePushButton_2.setGeometry(QRect(320, 20, 31, 24))
        self.closePushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.closePushButton_2.setStyleSheet(u"QPushButton{\n"
"	border: None;\n"
"}")
        self.closePushButton_2.setIcon(icon1)
        self.closePushButton_2.setIconSize(QSize(20, 20))
        self.stackedWidget.addWidget(self.enterpasswordPage)

        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"7", None))
        self.pushButton_1.setText(QCoreApplication.translate("Form", u"1", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"5", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"3", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"4", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"2", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"9", None))
        self.pushButton_0.setText(QCoreApplication.translate("Form", u"0", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"6", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"8", None))
        self.pushButton_delete.setText("")
        self.createapincodeLabel.setText(QCoreApplication.translate("Form", u"Create a PIN Code", None))
        self.pin1.setText("")
        self.pin2.setText("")
        self.pin3.setText("")
        self.pin4.setText("")
        self.pin6.setText("")
        self.pin5.setText("")
        self.pushButton_1_2.setText(QCoreApplication.translate("Form", u"1", None))
        self.pushButton_5_2.setText(QCoreApplication.translate("Form", u"5", None))
        self.pushButton_6_2.setText(QCoreApplication.translate("Form", u"6", None))
        self.pushButton_4_2.setText(QCoreApplication.translate("Form", u"4", None))
        self.pushButton_2_2.setText(QCoreApplication.translate("Form", u"2", None))
        self.pushButton_7_2.setText(QCoreApplication.translate("Form", u"7", None))
        self.pushButton_8_2.setText(QCoreApplication.translate("Form", u"8", None))
        self.pushButton_9_2.setText(QCoreApplication.translate("Form", u"9", None))
        self.pushButton_0_2.setText(QCoreApplication.translate("Form", u"0", None))
        self.pushButton_delete_2.setText("")
        self.pushButton_3_2.setText(QCoreApplication.translate("Form", u"3", None))
        self.confirmpincodeLabel.setText(QCoreApplication.translate("Form", u"Confirm PIN Code", None))
        self.pin1_2.setText("")
        self.pin2_2.setText("")
        self.pin3_2.setText("")
        self.pin4_2.setText("")
        self.pin5_2.setText("")
        self.pin6_2.setText("")
        self.pin1_3.setText("")
        self.pin2_3.setText("")
        self.pushButton_7_3.setText(QCoreApplication.translate("Form", u"7", None))
        self.pushButton_1_3.setText(QCoreApplication.translate("Form", u"1", None))
        self.pushButton_5_3.setText(QCoreApplication.translate("Form", u"5", None))
        self.pushButton_3_3.setText(QCoreApplication.translate("Form", u"3", None))
        self.pushButton_4_3.setText(QCoreApplication.translate("Form", u"4", None))
        self.pushButton_2_3.setText(QCoreApplication.translate("Form", u"2", None))
        self.pushButton_9_3.setText(QCoreApplication.translate("Form", u"9", None))
        self.pushButton_0_3.setText(QCoreApplication.translate("Form", u"0", None))
        self.pushButton_6_3.setText(QCoreApplication.translate("Form", u"6", None))
        self.pushButton_8_3.setText(QCoreApplication.translate("Form", u"8", None))
        self.pushButton_delete_3.setText("")
        self.pin4_3.setText("")
        self.pin6_3.setText("")
        self.pin3_3.setText("")
        self.entepincodeLabel.setText(QCoreApplication.translate("Form", u"Enter a PIN Code", None))
        self.pin5_3.setText("")
        self.closePushButton.setText("")
        self.enterpasswordLabel.setText(QCoreApplication.translate("Form", u"Enter Password", None))
        self.okPushButton.setText(QCoreApplication.translate("Form", u"OK", None))
        self.closePushButton_2.setText("")
    # retranslateUi

