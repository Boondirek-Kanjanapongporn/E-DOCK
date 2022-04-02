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
        self.signupLabel.setGeometry(QRect(160, 100, 51, 16))
        self.needanaccountLabel = QLabel(Form)
        self.needanaccountLabel.setObjectName(u"needanaccountLabel")
        self.needanaccountLabel.setGeometry(QRect(120, 500, 101, 16))
        self.emailLineEdit = QLineEdit(Form)
        self.emailLineEdit.setObjectName(u"emailLineEdit")
        self.emailLineEdit.setGeometry(QRect(40, 170, 281, 31))
        self.passwordLineEdit = QLineEdit(Form)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setGeometry(QRect(40, 250, 281, 31))
        self.emailLabel = QLabel(Form)
        self.emailLabel.setObjectName(u"emailLabel")
        self.emailLabel.setGeometry(QRect(40, 150, 61, 16))
        self.orLabel = QLabel(Form)
        self.orLabel.setObjectName(u"orLabel")
        self.orLabel.setGeometry(QRect(0, 450, 361, 20))
        self.orLabel.setAlignment(Qt.AlignCenter)
        self.passwordLabel = QLabel(Form)
        self.passwordLabel.setObjectName(u"passwordLabel")
        self.passwordLabel.setGeometry(QRect(40, 230, 51, 16))
        self.singupPushButton = QPushButton(Form)
        self.singupPushButton.setObjectName(u"singupPushButton")
        self.singupPushButton.setGeometry(QRect(40, 390, 281, 31))
        self.singupPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.loginPushButton = QPushButton(Form)
        self.loginPushButton.setObjectName(u"loginPushButton")
        self.loginPushButton.setGeometry(QRect(200, 500, 51, 16))
        self.loginPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.loginPushButton.setStyleSheet(u"QPushButton {\n"
"	border: None;\n"
"	text-decoration: underline;\n"
"}")
        self.confirmpasswordLabel = QLabel(Form)
        self.confirmpasswordLabel.setObjectName(u"confirmpasswordLabel")
        self.confirmpasswordLabel.setGeometry(QRect(40, 310, 101, 16))
        self.confirmpasswordLineEdit = QLineEdit(Form)
        self.confirmpasswordLineEdit.setObjectName(u"confirmpasswordLineEdit")
        self.confirmpasswordLineEdit.setGeometry(QRect(40, 330, 281, 31))
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
        self.passwordsdonotmatchLabel = QLabel(Form)
        self.passwordsdonotmatchLabel.setObjectName(u"passwordsdonotmatchLabel")
        self.passwordsdonotmatchLabel.setGeometry(QRect(190, 360, 141, 16))
        self.passwordsdonotmatchLabel.setStyleSheet(u"QLabel{\n"
"	color: #FF0000;\n"
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
        self.invalidpasswordLabel.setText(QCoreApplication.translate("Form", u"*Invalid Password", None))
        self.passwordsdonotmatchLabel.setText(QCoreApplication.translate("Form", u"*Passwords do not match", None))
    # retranslateUi

