from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QGridLayout
from PyQt6.QtGui import QIcon
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle("Qgrid")
        self.setWindowIcon(QIcon("icon.png"))

        grid = QGridLayout()

        btn1 = QPushButton("1")
        btn2 = QPushButton("2")
        btn3 = QPushButton("3")
        btn4 = QPushButton("4")

        grid.addWidget(btn1, 1, 1)
        grid.addWidget(btn2,2,2)
        grid.addWidget(btn3,3,4)
        grid.addWidget(btn4,5,2)
        self.setLayout(grid)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())