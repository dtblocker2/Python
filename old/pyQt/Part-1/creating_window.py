from PyQt6.QtWidgets import QApplication, QWidget
import sys

app = QApplication(sys.argv)

window = QWidget()
window.show()
'''below wont be applicable for q widget but is applicable for Qwindow'''
#window.statusBar().showMessage("lol")
#window.menuBar().addMenu("File")
sys.exit(app.exec())