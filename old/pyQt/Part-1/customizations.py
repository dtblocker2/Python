from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtGui import QIcon
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 250, 700, 500)
        self.setWindowTitle("First App")
        self.setWindowIcon(QIcon('icon.png'))
        #self.setFixedSize(500,500)
        self.setStyleSheet('background-color:blue')
        self.setWindowOpacity(0.5)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())