from PyQt6.QtWidgets import QWidget, QApplication, QLabel
from PyQt6.QtGui import QIcon, QPixmap, QMovie
import sys

class windows(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 400, 500)
        self.setWindowTitle("add image")
        self.setWindowIcon(QIcon("icon.png"))

        '''
        image = QLabel(self)
        image_src = QPixmap('icon.png')
        image.setPixmap(image_src)'''
        #to show gif use(means no audio will be played)
        animation = QLabel(self)
        movie = QMovie('image.gif')
        animation.setMovie(movie)
        movie.setSpeed(350) # to set animation speed normal speed = 100
        movie.start()

#-------------------------------
lol = QApplication(sys.argv)
window = windows()
window.show()
sys.exit(lol.exec())