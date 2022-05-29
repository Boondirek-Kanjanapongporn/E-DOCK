from PySide6.QtWidgets import *
from PySide6.QtCore import *
from splash import Ui_Form as Ui_Splash
import time

class Splash_Page(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.ui = Ui_Splash()
        self.ui.setupUi(self)
    
    def startSplash(self):
        time.sleep(2)
        self.close()