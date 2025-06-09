from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtCore import Qt
import pygame
import sys

class TimedMessageApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Каникулы (Holidays)")
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon("Каникулы (Holidays).jpg"))
        pygame.mixer.init()
        pygame.mixer.music.load("Каникулы .mp3")
        pygame.mixer.music.play(loops=-1)


        self.label = QLabel("", self)
        self.label.setStyleSheet("font-size: 30px;"
                                 "font-family:Ariel;")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setScaledContents(True)
        QTimer.singleShot(000, lambda: self.label.setText("Каникулы:"))
        QTimer.singleShot(2020, lambda: self.label.setText("Завтра"))
        QTimer.singleShot(2400, lambda: self.label.setText("Завтра я на"))
        QTimer.singleShot(2600, lambda: self.label.setText("Завтра я на всё"))
        QTimer.singleShot(2800, lambda: self.label.setText("Завтра я на всё забью"))
        QTimer.singleShot(3700, lambda: self.label.setText("На"))
        QTimer.singleShot(4000, lambda: self.label.setText("На учёбу"))
        QTimer.singleShot(4200, lambda: self.label.setText("На учёбу не пойду"))
        QTimer.singleShot(5200, lambda: self.label.setText("How "))
        QTimer.singleShot(5600, lambda: self.label.setText("How do you"))
        QTimer.singleShot(5900, lambda: self.label.setText("How do you, do you"))
        QTimer.singleShot(6500, lambda: self.label.setText("How do you, do you do?"))
        QTimer.singleShot(7000, lambda: self.label.setText("Каникулы:"))
        QTimer.singleShot(8500, lambda: self.label.setText("Завтра я на"))
        QTimer.singleShot(9000, lambda: self.label.setText("Завтра я на всё"))
        QTimer.singleShot(9400, lambda: self.label.setText("Завтра я на всё забью"))
        QTimer.singleShot(10500, lambda: self.label.setText("На"))
        QTimer.singleShot(10900, lambda: self.label.setText("На учёбу"))
        QTimer.singleShot(11100, lambda: self.label.setText("На учёбу не пойду"))
        QTimer.singleShot(12100, lambda: self.label.setText("How"))
        QTimer.singleShot(12500, lambda: self.label.setText("How do you"))
        QTimer.singleShot(12800, lambda: self.label.setText("How do you, do you"))
        QTimer.singleShot(13400, lambda: self.label.setText("How do you, do you do?"))
        QTimer.singleShot(14100, lambda: self.label.setText("Каникулы"))
        QTimer.singleShot(16000, lambda: self.label.setText("────୨ৎ────"))


        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TimedMessageApp()
    window.show()
    sys.exit(app.exec_())