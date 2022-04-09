import sys
import pyrebase
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from LoginPage import Login_Page
from SignupPage import Signup_Page
from MainPage import Main_Page

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

# data={'username': '', 'pin': '', 'notification': True, 'e-wallet': 0, 'cars':'', 'cards':'', 'history':''}
# db.child('users').child("HaMQwP6aXESz3aHhnbH3TQAvflI3").set(data)

# temp = db.child("users").child("HaMQwP6aXESz3aHhnbH3TQAvflI3").get()
# print(temp.val()['notification'])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QStackedWidget()

    # login_page = Login_Page(auth, widget)
    # signup_page = Signup_Page(auth, widget)
    main_page = Main_Page(auth, widget)

    # widget.addWidget(login_page)
    # widget.addWidget(signup_page)
    widget.addWidget(main_page)

    widget.setFixedHeight(640)
    widget.setFixedWidth(360)
    widget.show()

    sys.exit(app.exec())