from tkinter import Widget
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from login import Ui_Form as Ui_Login
from MainPage import Main_Page
import pickle

class Login_Page(QWidget):
    def __init__(self, db, auth, widget):
        QWidget.__init__(self, None)
        self.db = db
        self.auth = auth
        self.widget = widget

        self.ui = Ui_Login()
        self.ui.setupUi(self)

        # Try autoLogin
        self.autoLogin()
    
        self.ui.loginPushButton.clicked.connect(self.Login)

        self.ui.signupPushButton.clicked.connect(self.gotoSignup_Page)

        self.ui.forgotpasswordPushButton.clicked.connect(self.gotoSignup_Page)

        self.ui.invalidemailLabel.setVisible(False)
        self.ui.invalidpasswordLabel.setVisible(False)
    
    def Login(self):
        email = self.ui.emailLineEdit.text()
        password = self.ui.passwordLineEdit.text()
        checkbox = self.ui.remembermeCheckBox.isChecked()

        if email != "" and not email.isspace() and "@" in email:
            self.ui.invalidemailLabel.setVisible(False)

            if password != "" and not password.isspace():
                self.ui.invalidpasswordLabel.setVisible(False)

                try:
                    checkAuth = self.auth.sign_in_with_email_and_password(email, password)
                    print("Login to account")
                    # print(f"Login account with email: {email} and password: {password} {checkbox}")
                except:
                    self.showAlert("Incorrect Email or Password")

                if checkAuth:
                    if checkbox:
                        self.saveRememberMe(email, password)
                    self.gotoMain_Page()
            else:
                self.ui.invalidpasswordLabel.setVisible(True)
        else:
            self.ui.invalidemailLabel.setVisible(True)
    
    def gotoSignup_Page(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
    
    def gotoMain_Page(self, isAutoLogin=False):
        main_page = Main_Page(self.db, self.auth, self.widget, isAutoLogin)
        self.widget.addWidget(main_page)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 2)
    
    def saveRememberMe(self, email, password):
        userData = {"email": email, "password": password}
        with open('rememberUser.pkl','wb') as rememberUser:
            pickle.dump(userData, rememberUser)
    
    def autoLogin(self):
        try:
            with open('rememberUser.pkl', 'rb') as rememberUser:
                    userData = pickle.load(rememberUser)
                    self.auth.sign_in_with_email_and_password(userData['email'], userData['password'])
                    print("Login to account")
                    # print(f"Login account with email: {userData['email']} and password: {userData['password']}")
                    
                    self.gotoMain_Page(True)
        except:
            print('No rememberUser file found')

    def showAlert(self, text):
        dialog = QDialog(self)
        layout = QVBoxLayout()
        label = QLabel(self)
        label.setText(text)
        layout.addWidget(label)
        dialog.setLayout(layout)
        dialog.show()