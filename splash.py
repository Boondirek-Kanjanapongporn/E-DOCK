# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(360, 640)
        Form.setStyleSheet(u"QWidget{\n"
"	background-color: #FAFAFA;\n"
"}")
        self.edockiconPushButton = QPushButton(Form)
        self.edockiconPushButton.setObjectName(u"edockiconPushButton")
        self.edockiconPushButton.setGeometry(QRect(10, 210, 341, 81))
        self.edockiconPushButton.setStyleSheet(u"QPushButton{\n"
"	background-color:rgba(0,0,0,0);\n"
"}")
        icon = QIcon()
        icon.addFile(u"images/edock.png", QSize(), QIcon.Normal, QIcon.Off)
        self.edockiconPushButton.setIcon(icon)
        self.edockiconPushButton.setIconSize(QSize(180, 180))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 570, 161, 71))
        self.label.setStyleSheet(u"background-color:none;")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 580, 91, 61))
        self.label_2.setStyleSheet(u"background-color:none;")
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(290, 570, 61, 71))
        self.label_3.setStyleSheet(u"background-color:none;")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.edockiconPushButton.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"Boondirek Kanjanapongporn\n"
"Navin Jongyin\n"
"Yanapat Emdee", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Created By:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"63011117 \n"
"630120\n"
"63011382", None))
    # retranslateUi

