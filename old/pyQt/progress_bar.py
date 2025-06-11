from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QProgressBar
)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QPainter, QColor, QBrush
import sys


class HeadedProgressBar(QProgressBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTextVisible(False)
        self.setMinimum(0)
        self.setMaximum(100)
        self.setValue(0)

    def paintEvent(self, event):
        super().paintEvent(event)

        painter = QPainter(self)
        rect = self.rect()

        # Calculate progress width
        progress = (self.value() - self.minimum()) / (self.maximum() - self.minimum())
        bar_width = int(progress * rect.width())

        # Draw red head circle
        radius = 8
        x = bar_width - radius
        y = rect.height() // 2 - radius

        if 0 < x < rect.width() - radius:
            painter.setRenderHint(QPainter.RenderHint.Antialiasing)
            painter.setBrush(QBrush(QColor("red")))
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawEllipse(x, y, radius * 2, radius * 2)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Progress Bar with Red Head")
        self.resize(400, 150)

        layout = QVBoxLayout()
        self.progress = HeadedProgressBar()
        layout.addWidget(self.progress)

        self.btn = QPushButton("Start Progress")
        self.btn.clicked.connect(self.start_progress)
        layout.addWidget(self.btn)

        self.setLayout(layout)

        self.timer = QTimer(self) #to update gui without making it uninteractable
        self.timer.timeout.connect(self.update_progress)
        self.progress_value = 0

    def start_progress(self):
        self.progress_value = 0
        self.progress.setValue(0)
        self.timer.start(100)  # Update every 100ms

    def update_progress(self):
        if self.progress_value <= 100:
            self.progress.setValue(self.progress_value)
            self.progress_value += 1
        else:
            self.timer.stop()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
