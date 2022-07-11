
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import Qt
import sys
from PyQt5 import QtWidgets, uic  
from PyQt5 import QtCore



class MainWindow(QMainWindow):
    def __init__(self):
    
        super(MainWindow, self).__init__()

        self.setWindowIcon(QtGui.QIcon('icon/app-icon.svg'))
        
        self.setWindowTitle("UPDATE : Rage Weather App")

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        for child in self.findChildren(QWidget):
            shadow = QGraphicsDropShadowEffect(blurRadius=5, xOffset=3, yOffset=3)
            child.setGraphicsEffect(shadow)


        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())



        uic.loadUi('update.ui', self)
        self.show()



        self.button = self.findChild(QtWidgets.QPushButton, 'close')
        self.button.clicked.connect(self.exit) 
        
  


    def exit(self):
        print('ok')
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

