import sys
import time
import pyrebase
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from LoginPage import Login_Page
from SignupPage import Signup_Page
from SplashPage import Splash_Page

firebaseConfig={
    'apiKey': "AIzaSyBNtpVvn25ATKbJ0lg0ZdV-rhjJ1vkd5dA",
    'authDomain': "e-dock-9930a.firebaseapp.com",
    'projectId': "e-dock-9930a",
    'storageBucket': "e-dock-9930a.appspot.com",
    'messagingSenderId': "626659128643",
    'appId': "1:626659128643:web:bc6bd4770e9d25992b6bf6",
    'measurementId': "G-S6J5Y76HND",
    "databaseURL": "https://e-dock-9930a-default-rtdb.firebaseio.com/",
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()
storage = firebase.storage()

def wait_object_destruction(my_object):
        loop = QEventLoop()
        my_object.destroyed.connect(loop.quit)
        loop.exec_()
        return None

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QStackedWidget()

    login_page = Login_Page(db, auth, widget)
    signup_page = Signup_Page(db, auth, widget)

    widget.addWidget(login_page)
    widget.addWidget(signup_page)

    widget.setFixedHeight(640)
    widget.setFixedWidth(360)
    widget.show()

    sys.exit(app.exec())

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     widget = QStackedWidget()

#     # Create Splash Screen
#     splash_page = Splash_Page()
#     widget.addWidget(splash_page)

#     widget.setFixedHeight(640)
#     widget.setFixedWidth(360)
#     widget.show()

#     splash_page.startSplash()
#     time.sleep(1)
#     login_page = Login_Page(db, auth, widget)
#     wait_object_destruction(splash_page)
    
#     signup_page = Signup_Page(db, auth, widget)

#     widget.addWidget(login_page)
#     widget.addWidget(signup_page)

#     sys.exit(app.exec())
