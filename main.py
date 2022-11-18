import sys
from random import randint
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.flag = False
        self.pushButton.clicked.connect(self.drawf)

    def drawf(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.r = randint(10, 100)
            self.x = randint(100, 370)
            self.y = randint(100, 260)
            c1, c2, c3 = randint(0, 255), randint(0, 255), randint(0, 255)
            self.qp.setPen(QColor(c1, c2, c3))
            self.qp.drawEllipse(self.x, self.y, self.r, self.r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())