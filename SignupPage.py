from PySide6.QtWidgets import *
from PySide6.QtCore import *
from signup import Ui_Form as Ui_Signup

class Signup_Page(QWidget):
    def __init__(self, auth, widget):
        QWidget.__init__(self, None)
        self.auth = auth
        self.widget = widget

        self.ui = Ui_Signup()
        self.ui.setupUi(self)

        self.ui.singupPushButton.clicked.connect(self.Signup)

        self.ui.loginPushButton.clicked.connect(self.gotoLogin_Page)

        self.ui.invalidemailLabel.setVisible(False)
        self.ui.invalidpasswordLabel.setVisible(False)
        self.ui.passwordsdonotmatchLabel.setVisible(False)
    
    def Signup(self):
        email = self.ui.emailLineEdit.text()
        password = self.ui.passwordLineEdit.text()
        confirmpassword = self.ui.confirmpasswordLineEdit.text()

        if email != "" and not email.isspace() and "@" in email:
            self.ui.invalidemailLabel.setVisible(False)

            if password != "" and not password.isspace():
                self.ui.invalidpasswordLabel.setVisible(False)

                if password == confirmpassword:
                    self.ui.passwordsdonotmatchLabel.setVisible(False)

                    try:
                        self.auth.create_user_with_email_and_password(email, password)
                        print(f"Successfully created account with email: {email} and password: {password}")
                    except:
                        self.showAlert("Email is already taken")
                else:
                    self.ui.passwordsdonotmatchLabel.setVisible(True)
            else:
                self.ui.invalidpasswordLabel.setVisible(True)
        else:
            self.ui.invalidemailLabel.setVisible(True)
    
    def gotoLogin_Page(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
    
    def showAlert(self, text):
        dialog = QDialog(self)
        layout = QVBoxLayout()
        label = QLabel(self)
        label.setText(text)
        layout.addWidget(label)
        dialog.setLayout(layout)
        dialog.show()