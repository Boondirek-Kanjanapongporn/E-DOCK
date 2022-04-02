from tkinter import Widget
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from login import Ui_Form as Ui_Login
from MainPage import Main_Page

class Login_Page(QWidget):
    def __init__(self, auth, widget):
        QWidget.__init__(self, None)
        self.auth = auth
        self.widget = widget

        self.ui = Ui_Login()
        self.ui.setupUi(self)
    
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
                    self.auth.sign_in_with_email_and_password(email, password)
                    print(f"Login account with email: {email} and password: {password} {checkbox}")

                    main_page = Main_Page(self.auth, self.widget)
                    self.widget.addWidget(main_page)
                    self.widget.setCurrentIndex(self.widget.currentIndex() + 2)
                except:
                    self.showAlert("Incorrect Email or Password")
            else:
                self.ui.invalidpasswordLabel.setVisible(True)
        else:
            self.ui.invalidemailLabel.setVisible(True)
    
    def gotoSignup_Page(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def showAlert(self, text):
        dialog = QDialog(self)
        layout = QVBoxLayout()
        label = QLabel(self)
        label.setText(text)
        layout.addWidget(label)
        dialog.setLayout(layout)
        dialog.show()