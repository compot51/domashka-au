import sys, time
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class StopWatchWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Stopwatch")
        self.setGeometry(100, 100, 300, 200)

        self.counter = 0
        self.second_counter = 0
        self.minute_counter = 0
        
        self.count = '00'
        self.second = '00'
        self.minute = '00'

        self.startWatch = False

        self.label = QLabel(self)
        self.label.setGeometry(100, 40, 150, 70)

        self.start = QPushButton("Start", self)
        self.start.setGeometry(50, 120, 100, 40)
        self.start.pressed.connect(self.Start)

        resetWatch = QPushButton("Reset", self)
        resetWatch.setGeometry(160, 120, 100, 40)
        resetWatch.pressed.connect(self.Reset)

        timer = QTimer(self)
        timer.timeout.connect(self.showCounter)
        timer.start(10)

        self.move(900, 400)
        self.show()

    def showCounter(self):
        if self.startWatch:
            self.counter += 1
            if self.counter < 10:
                self.count = '0' + str(self.counter)
            elif self.counter < 100:
                self.count = str(self.counter)
            else:
                self.counter = 0
                self.count = '00'
                self.second_counter += 1
                if self.second_counter < 10:
                    self.second = '0' + str(self.second_counter)
                elif self.second_counter < 60:
                    self.second = str(self.second_counter)
                else:
                    self.second_counter = 0
                    self.second = '00'
                    self.minute_counter += 1
                    if self.minute_counter < 10:
                        self.minute = '0' + str(self.minute_counter)
                    else:
                        self.minute = str(self.minute_counter)

        text = self.minute + ':' + self.second + ':' + self.count
        self.label.setText('<h1>' + text + '</h1>')

    def Start(self):
        if self.start.text() == 'Stop':
            self.start.setText('Resume')
            self.startWatch = False
        else:
            self.startWatch = True
            self.start.setText('Stop')

    def Reset(self):
        self.startWatch = False
        self.counter = 0
        self.minute = '00'
        self.second = '00'
        self.count = '00'
        self.label.setText(str(self.counter))

app = QApplication(sys.argv)
stopWt = StopWatchWindow()
app.exec()
