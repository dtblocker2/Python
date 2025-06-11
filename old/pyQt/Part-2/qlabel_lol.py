from PyQt6.QtWidgets import QWidget, QApplication, QLabel
from PyQt6.QtGui import QIcon, QFont
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle("Q-label")
        self.setWindowIcon(QIcon("icon.png"))

        #print() statement analogous
        label = QLabel("This Text will be printed on screen",self)
        label.setText("this is second text and first text will be hidden")
        label_2 = QLabel("lol this is sencond sentence", self)
        label_2.move(0,100)
        label.setFont(QFont("sanserif",13))
        label.setStyleSheet('color:red')

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())