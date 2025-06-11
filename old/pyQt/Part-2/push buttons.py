from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QMenu
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys

class windows(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(100, 100, 400, 500)
        self.setWindowTitle("Q_push button")
        self.setWindowIcon(QIcon("icon.png"))

        self.create_button()
    def create_button(self):
        btn = QPushButton("choose fighter",self)
        btn.setGeometry(100,100,250,100)
        btn.setFont(QFont("times", 14, QFont.Weight.Bold))
        
        #also you can use Qicon in place of Qfont
        btn.setIcon(QIcon('icon.png'))
        #to set size of icon
        btn.setIconSize(QSize(36,36))

        menu = QMenu()
        menu.setStyleSheet("background-color:#F2B4C6")
        menu.addAction("longus dongus")
        menu.addAction("niggamus maximus")
        menu.addAction("badana fighter")
        btn.setMenu(menu)

app = QApplication(sys.argv)
window = windows()
window.show()
sys.exit(app.exec())