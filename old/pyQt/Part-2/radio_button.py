from PyQt6.QtWidgets import QWidget, QApplication, QRadioButton, QHBoxLayout, QVBoxLayout, QLabel
from PyQt6.QtGui import QIcon
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle("Qradio Button")
        self.setWindowIcon(QIcon("icon.png"))

        self.create_radio()        

    def create_radio(self):
        self.text = QLabel(f"You have selected:",self)

        btn1 = QRadioButton("Red",self)
        btn2 = QRadioButton("Green",self)
        btn3 = QRadioButton("Blue",self)

        btn1.toggled.connect(self.checked_radio)
        btn2.toggled.connect(self.checked_radio)
        btn3.toggled.connect(self.checked_radio)

        hbox = QHBoxLayout()
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addWidget(btn3)

        vbox = QVBoxLayout()
        vbox.addWidget(self.text)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

    def checked_radio(self):
        radio_btn = self.sender()
        if radio_btn.isChecked():
            self.text.setText(f"You have selected: {radio_btn.text()}")
            self.text.setStyleSheet(f"color: {radio_btn.text()}")

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())