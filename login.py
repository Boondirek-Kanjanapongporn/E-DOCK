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
        self.loginLabel = QLabel(Form)
        self.loginLabel.setObjectName(u"loginLabel")
        self.loginLabel.setGeometry(QRect(160, 100, 41, 16))
        self.emailLabel = QLabel(Form)
        self.emailLabel.setObjectName(u"emailLabel")
        self.emailLabel.setGeometry(QRect(40, 150, 61, 16))
        self.passwordLabel = QLabel(Form)
        self.passwordLabel.setObjectName(u"passwordLabel")
        self.passwordLabel.setGeometry(QRect(40, 230, 51, 16))
        self.loginPushButton = QPushButton(Form)
        self.loginPushButton.setObjectName(u"loginPushButton")
        self.loginPushButton.setGeometry(QRect(40, 330, 281, 31))
        self.loginPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.emailLineEdit = QLineEdit(Form)
        self.emailLineEdit.setObjectName(u"emailLineEdit")
        self.emailLineEdit.setGeometry(QRect(40, 170, 281, 31))
        self.passwordLineEdit = QLineEdit(Form)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setGeometry(QRect(40, 250, 281, 31))
        self.remembermeCheckBox = QCheckBox(Form)
        self.remembermeCheckBox.setObjectName(u"remembermeCheckBox")
        self.remembermeCheckBox.setGeometry(QRect(40, 290, 111, 20))
        self.remembermeCheckBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.orLabel = QLabel(Form)
        self.orLabel.setObjectName(u"orLabel")
        self.orLabel.setGeometry(QRect(0, 410, 361, 20))
        self.orLabel.setAlignment(Qt.AlignCenter)
        self.needanaccountLabel = QLabel(Form)
        self.needanaccountLabel.setObjectName(u"needanaccountLabel")
        self.needanaccountLabel.setGeometry(QRect(110, 460, 101, 16))
        self.signupPushButton = QPushButton(Form)
        self.signupPushButton.setObjectName(u"signupPushButton")
        self.signupPushButton.setGeometry(QRect(210, 460, 51, 16))
        self.signupPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.signupPushButton.setStyleSheet(u"QPushButton {\n"
"	border: None;\n"
"	text-decoration: underline;\n"
"}")
        self.forgotpasswordPushButton = QPushButton(Form)
        self.forgotpasswordPushButton.setObjectName(u"forgotpasswordPushButton")
        self.forgotpasswordPushButton.setGeometry(QRect(220, 370, 111, 16))
        self.forgotpasswordPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.forgotpasswordPushButton.setStyleSheet(u"QPushButton{\n"
"	border: None\n"
"}")
        self.invalidemailLabel = QLabel(Form)
        self.invalidemailLabel.setObjectName(u"invalidemailLabel")
        self.invalidemailLabel.setGeometry(QRect(250, 200, 81, 16))
        self.invalidemailLabel.setStyleSheet(u"QLabel{\n"
"	color: #FF0000;\n"
"}")
        self.invalidpasswordLabel = QLabel(Form)
        self.invalidpasswordLabel.setObjectName(u"invalidpasswordLabel")
        self.invalidpasswordLabel.setGeometry(QRect(230, 280, 101, 16))
        self.invalidpasswordLabel.setStyleSheet(u"QLabel{\n"
"	color: #FF0000;\n"
"}")
        self.invalidemailLabel.raise_()
        self.invalidpasswordLabel.raise_()
        self.loginLabel.raise_()
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

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.loginLabel.setText(QCoreApplication.translate("Form", u"LOGIN", None))
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
    # retranslateUi

