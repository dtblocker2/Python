from PyQt6.QtWidgets import QWidget, QApplication, QLineEdit
from PyQt6.QtGui import QIcon, QFont
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle("Qline")
        self.setWindowIcon(QIcon("icon.png"))

        qline = QLineEdit(self)
        qline.setPlaceholderText("lol type password here")
        #qline.setEnabled(False)---> to block user from typing
        qline.setEchoMode(QLineEdit.EchoMode.Password)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())