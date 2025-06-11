from PyQt6.QtWidgets import QApplication, QDialog
import sys

app = QApplication(sys.argv)
#Qdialog does not show option of maximize and minimize option and only show closed option (although you can change size of window)
window = QDialog()
window.show()
'''
here too both will not be executed
window.statusBar().showMessage("lol")
window.menuBar().addMenu("File")
'''
sys.exit(app.exec())