


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import Qt
import sys
from PyQt5 import uic  
import signal
import os
import subprocess
import time

os.chdir('web')
subprocess.Popen(["flask","run"])
os.chdir('../')
time.sleep(1)
class MainWindow(QMainWindow):
    def __init__(self):
    
        super(MainWindow, self).__init__()

        self.setWindowIcon(QtGui.QIcon('icon/app-icon.png'))
        
        self.setWindowTitle("Rage Weather App")

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        for child in self.findChildren(QWidget):
            shadow = QGraphicsDropShadowEffect(blurRadius=5, xOffset=3, yOffset=3)
            child.setGraphicsEffect(shadow)

        uic.loadUi('main_error.ui', self)
        self.show()

       

        self.button = self.findChild(QtWidgets.QPushButton, 'close')
        self.button.clicked.connect(self.exit) 
        
        self.button1 = self.findChild(QtWidgets.QPushButton, 'mini')
        self.button1.clicked.connect(self.showMinimized)    


    def exit(self):
        try:
            for line in os.popen("ps ax | grep flask | grep -v grep"):
                fields = line.split()
                pid = fields[0]
                os.kill(int(pid), signal.SIGKILL)


            for line in os.popen("ps ax | grep http.server | grep -v grep"):
                fields = line.split()
                pid = fields[0]
                os.kill(int(pid), signal.SIGKILL)
            print("BYE !!")         
        except:
            print("Its's A BUG")

        sys.exit()



    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.offset = event.pos()
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.offset is not None and event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.pos() - self.offset)
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.offset = None
        super().mouseReleaseEvent(event)







if __name__ == "__main__":
    app =QApplication(sys.argv)
    window = MainWindow()
    app.exec_()

'''

from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import Qt
import sys
from PyQt5 import QtWidgets, uic  
from PyQt5 import QtCore
import time


class Ui(QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()


        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        for child in self.findChildren(QWidget):
            shadow = QGraphicsDropShadowEffect(blurRadius=5, xOffset=3, yOffset=3)
            child.setGraphicsEffect(shadow)

        uic.loadUi('main.ui', self)
        self.show()



        self.button = self.findChild(QtWidgets.QPushButton, 'close')
        self.button.clicked.connect(self.exit) 
        
        self.button1 = self.findChild(QtWidgets.QPushButton, 'mini')
        self.button1.clicked.connect(self.showMinimized)    


    def exit(self):
        sys.exit()



    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.offset = event.pos()
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.offset is not None and event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.pos() - self.offset)
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.offset = None
        super().mouseReleaseEvent(event)

if __name__ == '__main__':
    app =QApplication(sys.argv)
    window = Ui()
    
    app.exec_()

'''
