from PySide6.QtWidgets import *
from PySide6.QtCore import *
from signup import Ui_Form as Ui_Signup
from MainPage import Main_Page

class Signup_Page(QWidget):
    def __init__(self, db, auth, widget):
        QWidget.__init__(self, None)
        self.db = db
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

            if password != "" and not password.isspace() and len(password) >= 8:
                self.ui.invalidpasswordLabel.setVisible(False)

                if password == confirmpassword:
                    self.ui.passwordsdonotmatchLabel.setVisible(False)

                    try:
                        checkAuth = self.auth.create_user_with_email_and_password(email, password)
                        print("Sign up successfully")
                        # print(f"Successfully created account with email: {email} and password: {password}")
                    except:
                        self.showAlert("Email is already exists")

                    if checkAuth:
                        self.autoLogin(email, password)
                else:
                    self.ui.passwordsdonotmatchLabel.setVisible(True)
            else:
                self.ui.invalidpasswordLabel.setVisible(True)
        else:
            self.ui.invalidemailLabel.setVisible(True)
    
    def gotoLogin_Page(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
    
    def gotoMain_page(self):
        main_page = Main_Page(self.db, self.auth, self.widget)
        self.widget.addWidget(main_page)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
    
    def autoLogin(self, email, password):
        self.auth.sign_in_with_email_and_password(email, password)
        self.createDatabaseUser()
        self.gotoMain_page()
    
    def createDatabaseUser(self):
        uid = self.auth.current_user['localId']
        userinfo = self.db.child('users').child(uid).get()

        if userinfo.val() is None:
            data={'username': '', 'pin': '', 'notification': True, 'money': 0, 'cars':'', 'cards':'', 'history':''}
            self.db.child('users').child(uid).set(data)
        else:
            raise SystemError('User Database is already Exists')

    def showAlert(self, text):
        dialog = QDialog(self)
        layout = QVBoxLayout()
        label = QLabel(self)
        label.setText(text)
        layout.addWidget(label)
        dialog.setLayout(layout)
        dialog.show()