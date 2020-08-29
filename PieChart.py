# This Python file uses the following encoding: utf-8
from PySide2.QtQuick import QQuickPaintedItem
from PySide2.QtGui import QColor, QPen, QPainter
from PySide2.QtCore import Signal, Property


class PieChart(QQuickPaintedItem):
    def __init__(self, parent=None):
        QQuickPaintedItem.__init__(self, parent)
        self._color = QColor()

    def paint(self, painter):
        pen = QPen(self._color, 2)
        painter.setPen(pen)
        painter.setRenderHints(QPainter.Antialiasing, True)
        painter.drawPie(self.boundingRect().adjusted(1, 1, -1, -1),
                        90 * 16, 290 * 16)

    def getColor(self):
        return self.color

    def setColor(self, value):
        if value != self._color:
            self._color = value
            self.update()
            self.colorChanged.emit()

    colorChanged = Signal()
    color = Property(QColor, getColor, setColor, notify=colorChanged)
