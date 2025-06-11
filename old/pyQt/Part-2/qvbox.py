from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout
from PyQt6.QtGui import QIcon
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle("Qvbox")
        self.setWindowIcon(QIcon("icon.png"))

        vbox = QVBoxLayout()

        btn1 = QPushButton("1")
        btn2 = QPushButton("2")
        btn3 = QPushButton("3")
        btn4 = QPushButton("4")

        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addWidget(btn4)
        self.setLayout(vbox)

        vbox.addSpacing(10)
        vbox.addStretch(100)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())