from PyQt6.QtWidgets import QApplication, QMainWindow, QRadioButton, QVBoxLayout, QGroupBox, QWidget
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Radio Button Groups")

        # Create a main layout
        main_layout = QVBoxLayout()

        # Group 1
        group1_box = QGroupBox()
        group1_box.setStyleSheet('border:None')
        group1_layout = QVBoxLayout()
        radio1_1 = QRadioButton("Option 1.1")
        radio1_2 = QRadioButton("Option 1.2")
        radio1_3 = QRadioButton("Option 1.3")
        group1_layout.addWidget(radio1_1)
        group1_layout.addWidget(radio1_2)
        group1_layout.addWidget(radio1_3)
        group1_box.setLayout(group1_layout)

        # Group 2
        group2_box = QGroupBox()
        group2_box.setStyleSheet('border:None')
        group2_layout = QVBoxLayout()
        radio2_1 = QRadioButton("Option 2.1")
        radio2_2 = QRadioButton("Option 2.2")
        radio2_3 = QRadioButton("Option 2.3")
        group2_layout.addWidget(radio2_1)
        group2_layout.addWidget(radio2_2)
        group2_layout.addWidget(radio2_3)
        group2_box.setLayout(group2_layout)

        # Add groups to the main layout
        main_layout.addWidget(group1_box)
        main_layout.addWidget(group2_box)

        # Set the central widget
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
