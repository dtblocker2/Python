from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QHBoxLayout
from PyQt6.QtGui import QIcon, QFont
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle("Qevent Handling")
        self.setWindowIcon(QIcon("icon.png"))

        self.create_widget()

    def create_widget(self):
        hbox = QHBoxLayout()
        self.label = QLabel("LOL:")
        btn = QPushButton("change text style")

        hbox.addWidget(self.label)
        hbox.addWidget(btn)

        self.setLayout(hbox)
        btn.clicked.connect(self.when_clicked)
    
    def when_clicked(self):
        self.label.setText("LoL_2: ")
        self.label.setFont(QFont("times",15,13))
        self.label.setStyleSheet("color:red")
        

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())