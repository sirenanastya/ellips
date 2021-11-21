import sys
from random import randint
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import uic  # Импортируем uic


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('u1.ui', self)  # Загружаем дизайн
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        qp.setBrush(QColor(255, 204, 0))
        r = randint(20, 150)
        qp.drawEllipse(150,90, r, r)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())