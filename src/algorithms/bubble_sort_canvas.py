import random
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QTimer


class BubbleSortCanvas(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumHeight(250)
        self.array = []
        self.current = 0
        self.sorted = False
        self.timer = QTimer()
        self.timer.timeout.connect(self.sort_step)

    def reset(self):
        if not self.array:
            self.array = [random.randint(10, 300) for _ in range(50)]
        self.current = 0
        self.sorted = False
        self.update()

    def start(self):
        self.timer.start(30)

    def sort_step(self):
        if self.current >= len(self.array) - 1:
            self.current = 0
            self.sorted = all(self.array[i] <= self.array[i + 1] for i in range(len(self.array) - 1))
            if self.sorted:
                self.timer.stop()
                return

        if self.array[self.current] > self.array[self.current + 1]:
            self.array[self.current], self.array[self.current + 1] = self.array[self.current + 1], self.array[self.current]
        self.current += 1
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        if not self.array:
            return
        bar_width = self.width() / len(self.array)
        for i, val in enumerate(self.array):
            color = QColor(100, 200, 255) if i != self.current and i != self.current + 1 else QColor(255, 100, 100)
            painter.setBrush(color)
            painter.drawRect(int(i * bar_width), self.height() - val, int(bar_width - 2), val)

    def set_speed(self, ms):
        self.timer.setInterval(ms)