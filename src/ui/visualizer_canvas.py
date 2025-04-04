from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtCore import Qt

class VisualizerCanvas(QWidget):
    def __init__(self):
        super().__init__()
        self.array = []

    def update_data(self, array):
        self.array = array
        self.repaint()

    def paintEvent(self, event):
        if not self.array:
            return

        painter = QPainter(self)
        bar_width = self.width() // len(self.array)
        for i, value in enumerate(self.array):
            height = value * 10
            x = i * bar_width
            y = self.height() - height
            painter.setBrush(QBrush(QColor(100, 200, 255)))
            painter.drawRect(x, y, bar_width - 2, height)
