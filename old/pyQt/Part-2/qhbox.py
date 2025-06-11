from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QHBoxLayout
from PyQt6.QtGui import QIcon
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle("Qhbox")
        self.setWindowIcon(QIcon("icon.png"))

        hbox = QHBoxLayout()

        btn1 = QPushButton("1")
        btn2 = QPushButton("2")
        btn3 = QPushButton("3")
        btn4 = QPushButton("4")

        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addWidget(btn3)
        hbox.addWidget(btn4)
        self.setLayout(hbox)

        hbox.addSpacing(10)
        hbox.addStretch(100)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())