from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

app = QApplication(sys.argv)

window = QMainWindow()
window.show()
window.statusBar().showMessage("lol")
window.menuBar().addMenu("File")
sys.exit(app.exec())