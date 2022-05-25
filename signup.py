# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signup.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(360, 640)
        self.signupLabel = QLabel(Form)
        self.signupLabel.setObjectName(u"signupLabel")
        self.signupLabel.setGeometry(QRect(40, 70, 91, 21))
        self.signupLabel.setStyleSheet(u"font: 20pt, Arial;\n"
"color: #444444;")
        self.needanaccountLabel = QLabel(Form)
        self.needanaccountLabel.setObjectName(u"needanaccountLabel")
        self.needanaccountLabel.setGeometry(QRect(110, 520, 101, 16))
        self.emailLineEdit = QLineEdit(Form)
        self.emailLineEdit.setObjectName(u"emailLineEdit")
        self.emailLineEdit.setGeometry(QRect(40, 140, 281, 35))
        self.emailLineEdit.setMinimumSize(QSize(0, 35))
        font = QFont()
        font.setPointSize(9)
        self.emailLineEdit.setFont(font)
        self.emailLineEdit.setStyleSheet(u"QLineEdit\n"
"{\n"
"	border: 2px solid #71cd00;\n"
"	border-radius: 10px;\n"
"}\n"
"QLineEdit:focus\n"
"{\n"
"	border: 2px solid #71cd00;\n"
"}")
        self.passwordLineEdit = QLineEdit(Form)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setGeometry(QRect(40, 230, 281, 35))
        self.passwordLineEdit.setMinimumSize(QSize(0, 35))
        self.passwordLineEdit.setStyleSheet(u"QLineEdit\n"
"{\n"
"	border: 2px solid #71cd00;\n"
"	border-radius: 10px;\n"
"}\n"
"QLineEdit:focus\n"
"{\n"
"	border: 2px solid #71cd00;\n"
"}")
        self.emailLabel = QLabel(Form)
        self.emailLabel.setObjectName(u"emailLabel")
        self.emailLabel.setGeometry(QRect(40, 120, 271, 16))
        self.emailLabel.setStyleSheet(u"font: 16pt, Arial;\n"
"color: #444444;")
        self.orLabel = QLabel(Form)
        self.orLabel.setObjectName(u"orLabel")
        self.orLabel.setGeometry(QRect(0, 470, 361, 20))
        self.orLabel.setAlignment(Qt.AlignCenter)
        self.passwordLabel = QLabel(Form)
        self.passwordLabel.setObjectName(u"passwordLabel")
        self.passwordLabel.setGeometry(QRect(40, 210, 271, 16))
        self.passwordLabel.setStyleSheet(u"font: 16pt, Arial;\n"
"color: #444444;")
        self.singupPushButton = QPushButton(Form)
        self.singupPushButton.setObjectName(u"singupPushButton")
        self.singupPushButton.setGeometry(QRect(40, 410, 281, 41))
        self.singupPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.singupPushButton.setStyleSheet(u"QPushButton{\n"
"	background-color:#71cd00;\n"
"	border-radius: 10px;\n"
"	color: #FFFFFF;\n"
"	font: 16px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color:#468000;\n"
"}\n"
"	")
        self.loginPushButton = QPushButton(Form)
        self.loginPushButton.setObjectName(u"loginPushButton")
        self.loginPushButton.setGeometry(QRect(200, 520, 51, 16))
        self.loginPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.loginPushButton.setStyleSheet(u"QPushButton {\n"
"	border: None;\n"
"	text-decoration: underline;\n"
"	color: #1c33de;\n"
"}")
        self.confirmpasswordLabel = QLabel(Form)
        self.confirmpasswordLabel.setObjectName(u"confirmpasswordLabel")
        self.confirmpasswordLabel.setGeometry(QRect(40, 310, 271, 16))
        self.confirmpasswordLabel.setStyleSheet(u"font: 16pt, Arial;\n"
"color: #444444;")
        self.confirmpasswordLineEdit = QLineEdit(Form)
        self.confirmpasswordLineEdit.setObjectName(u"confirmpasswordLineEdit")
        self.confirmpasswordLineEdit.setGeometry(QRect(40, 330, 281, 35))
        self.confirmpasswordLineEdit.setMinimumSize(QSize(0, 35))
        self.confirmpasswordLineEdit.setStyleSheet(u"QLineEdit\n"
"{\n"
"	border: 2px solid #71cd00;\n"
"	border-radius: 10px;\n"
"}\n"
"QLineEdit:focus\n"
"{\n"
"	border: 2px solid #71cd00;\n"
"}")
        self.invalidemailLabel = QLabel(Form)
        self.invalidemailLabel.setObjectName(u"invalidemailLabel")
        self.invalidemailLabel.setGeometry(QRect(250, 180, 81, 16))
        self.invalidemailLabel.setStyleSheet(u"QLabel{\n"
"	color: #AA1111;\n"
"}")
        self.invalidpasswordLabel = QLabel(Form)
        self.invalidpasswordLabel.setObjectName(u"invalidpasswordLabel")
        self.invalidpasswordLabel.setGeometry(QRect(160, 270, 161, 31))
        self.invalidpasswordLabel.setStyleSheet(u"QLabel{\n"
"	color: #aa1111;\n"
"}")
        self.invalidpasswordLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.passwordsdonotmatchLabel = QLabel(Form)
        self.passwordsdonotmatchLabel.setObjectName(u"passwordsdonotmatchLabel")
        self.passwordsdonotmatchLabel.setGeometry(QRect(170, 370, 161, 20))
        self.passwordsdonotmatchLabel.setStyleSheet(u"QLabel{\n"
"	color: #aa1111;\n"
"}")
        self.passwordsdonotmatchLabel.raise_()
        self.invalidpasswordLabel.raise_()
        self.invalidemailLabel.raise_()
        self.signupLabel.raise_()
        self.needanaccountLabel.raise_()
        self.emailLabel.raise_()
        self.orLabel.raise_()
        self.passwordLabel.raise_()
        self.singupPushButton.raise_()
        self.loginPushButton.raise_()
        self.confirmpasswordLabel.raise_()
        self.emailLineEdit.raise_()
        self.passwordLineEdit.raise_()
        self.confirmpasswordLineEdit.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.signupLabel.setText(QCoreApplication.translate("Form", u"SIGN UP", None))
        self.needanaccountLabel.setText(QCoreApplication.translate("Form", u"Already a user?", None))
        self.emailLabel.setText(QCoreApplication.translate("Form", u"Email", None))
        self.orLabel.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>--------------------------- OR ---------------------------</p></body></html>", None))
        self.passwordLabel.setText(QCoreApplication.translate("Form", u"Password", None))
        self.singupPushButton.setText(QCoreApplication.translate("Form", u"Sign up", None))
        self.loginPushButton.setText(QCoreApplication.translate("Form", u"LOGIN", None))
        self.confirmpasswordLabel.setText(QCoreApplication.translate("Form", u"Confirm Password", None))
        self.invalidemailLabel.setText(QCoreApplication.translate("Form", u"*Invalid Email", None))
        self.invalidpasswordLabel.setText(QCoreApplication.translate("Form", u"*Invalid Password\n"
"*Must be more than 8 digits", None))
        self.passwordsdonotmatchLabel.setText(QCoreApplication.translate("Form", u"*Passwords do not match", None))
    # retranslateUi

