# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(360, 640)
        self.emailLabel = QLabel(Form)
        self.emailLabel.setObjectName(u"emailLabel")
        self.emailLabel.setGeometry(QRect(40, 145, 281, 21))
        self.emailLabel.setStyleSheet(u"font: 16pt;\n"
"color: #444444;")
        self.passwordLabel = QLabel(Form)
        self.passwordLabel.setObjectName(u"passwordLabel")
        self.passwordLabel.setGeometry(QRect(40, 235, 281, 21))
        self.passwordLabel.setStyleSheet(u"font: 16pt;\n"
"color: #444444")
        self.loginPushButton = QPushButton(Form)
        self.loginPushButton.setObjectName(u"loginPushButton")
        self.loginPushButton.setGeometry(QRect(40, 350, 281, 41))
        self.loginPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.loginPushButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: #71cd00;\n"
"	border-radius: 10px;\n"
"	font: 16pt, arial;\n"
"	color: #ffffff;\n"
"}\n"
"QPushButton-Hover:\n"
"{\n"
"	background-color: #549900;\n"
"}\n"
"")
        self.emailLineEdit = QLineEdit(Form)
        self.emailLineEdit.setObjectName(u"emailLineEdit")
        self.emailLineEdit.setGeometry(QRect(40, 170, 281, 35))
        self.emailLineEdit.setMinimumSize(QSize(0, 35))
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
        self.passwordLineEdit.setGeometry(QRect(40, 260, 281, 35))
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
        self.remembermeCheckBox = QCheckBox(Form)
        self.remembermeCheckBox.setObjectName(u"remembermeCheckBox")
        self.remembermeCheckBox.setGeometry(QRect(40, 300, 121, 20))
        self.remembermeCheckBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.orLabel = QLabel(Form)
        self.orLabel.setObjectName(u"orLabel")
        self.orLabel.setGeometry(QRect(20, 430, 321, 20))
        self.orLabel.setAlignment(Qt.AlignCenter)
        self.needanaccountLabel = QLabel(Form)
        self.needanaccountLabel.setObjectName(u"needanaccountLabel")
        self.needanaccountLabel.setGeometry(QRect(100, 480, 121, 16))
        self.needanaccountLabel.setStyleSheet(u"")
        self.needanaccountLabel.setAlignment(Qt.AlignCenter)
        self.signupPushButton = QPushButton(Form)
        self.signupPushButton.setObjectName(u"signupPushButton")
        self.signupPushButton.setGeometry(QRect(210, 480, 71, 16))
        self.signupPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.signupPushButton.setStyleSheet(u"QPushButton {\n"
"	border: None;\n"
"	text-decoration: underline;\n"
"	color: #1c33de;\n"
"	\n"
"}")
        self.forgotpasswordPushButton = QPushButton(Form)
        self.forgotpasswordPushButton.setObjectName(u"forgotpasswordPushButton")
        self.forgotpasswordPushButton.setGeometry(QRect(220, 400, 111, 16))
        self.forgotpasswordPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.forgotpasswordPushButton.setStyleSheet(u"QPushButton{\n"
"	border: None\n"
"}")
        self.invalidemailLabel = QLabel(Form)
        self.invalidemailLabel.setObjectName(u"invalidemailLabel")
        self.invalidemailLabel.setGeometry(QRect(250, 210, 81, 16))
        self.invalidemailLabel.setStyleSheet(u"QLabel{\n"
"	color: #aa1111;\n"
"}")
        self.invalidpasswordLabel = QLabel(Form)
        self.invalidpasswordLabel.setObjectName(u"invalidpasswordLabel")
        self.invalidpasswordLabel.setGeometry(QRect(220, 300, 101, 21))
        self.invalidpasswordLabel.setStyleSheet(u"QLabel{\n"
"	color: #aa1111;\n"
"}")
        self.invalidpasswordLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.loginLabel = QLabel(Form)
        self.loginLabel.setObjectName(u"loginLabel")
        self.loginLabel.setGeometry(QRect(40, 100, 91, 21))
        self.loginLabel.setStyleSheet(u"font: 20pt, Arial;\n"
"color: #444444;")
        self.invalidemailLabel.raise_()
        self.invalidpasswordLabel.raise_()
        self.emailLabel.raise_()
        self.passwordLabel.raise_()
        self.loginPushButton.raise_()
        self.remembermeCheckBox.raise_()
        self.orLabel.raise_()
        self.needanaccountLabel.raise_()
        self.signupPushButton.raise_()
        self.forgotpasswordPushButton.raise_()
        self.emailLineEdit.raise_()
        self.passwordLineEdit.raise_()
        self.loginLabel.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.emailLabel.setText(QCoreApplication.translate("Form", u"Email", None))
        self.passwordLabel.setText(QCoreApplication.translate("Form", u"Password", None))
        self.loginPushButton.setText(QCoreApplication.translate("Form", u"Login", None))
        self.remembermeCheckBox.setText(QCoreApplication.translate("Form", u"Remember me?", None))
        self.orLabel.setText(QCoreApplication.translate("Form", u"--------------------------- OR ---------------------------", None))
        self.needanaccountLabel.setText(QCoreApplication.translate("Form", u"Need an account?", None))
        self.signupPushButton.setText(QCoreApplication.translate("Form", u"SIGN UP", None))
        self.forgotpasswordPushButton.setText(QCoreApplication.translate("Form", u"Forgot Password?", None))
        self.invalidemailLabel.setText(QCoreApplication.translate("Form", u"*Invalid Email", None))
        self.invalidpasswordLabel.setText(QCoreApplication.translate("Form", u"*Invalid Password", None))
        self.loginLabel.setText(QCoreApplication.translate("Form", u"LOGIN", None))
    # retranslateUi

