from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget, QVBoxLayout, QLabel, QPushButton
import sys

class Page1(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("This is Page 1"))
        self.setLayout(layout)

class Page2(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("This is Page 2"))
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QStackedWidget Example")

        # Create a QStackedWidget
        self.stacked_widget = QStackedWidget()

        # Add pages
        self.page1 = Page1()
        self.page2 = Page2()
        self.stacked_widget.addWidget(self.page1)
        self.stacked_widget.addWidget(self.page2)

        # Add navigation buttons
        self.page1.layout().addWidget(QPushButton("Go to Page 2", clicked=lambda: self.stacked_widget.setCurrentWidget(self.page2)))
        self.page2.layout().addWidget(QPushButton("Go to Page 1", clicked=lambda: self.stacked_widget.setCurrentWidget(self.page1)))

        # Set the stacked widget as the central widget
        self.setCentralWidget(self.stacked_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())