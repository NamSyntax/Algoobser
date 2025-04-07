import random
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QTimer

class QuickSortCanvas(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumHeight(250)
        self.array = []
        self.stack = []
        self.i = self.j = self.pivot = None
        self.step_mode = 'partition'
        self.timer = QTimer()
        self.timer.timeout.connect(self.sort_step)

    def reset(self):
        self.array = [random.randint(10, 300) for _ in range(50)]
        self.stack = [(0, len(self.array) - 1)]
        self.i = self.j = self.pivot = None
        self.step_mode = 'partition'
        self.update()

    def start(self):
        self.timer.start(50)

    def sort_step(self):
        if not self.stack:
            self.timer.stop()
            self.i = self.j = self.pivot = None
            return

        low, high = self.stack[-1]

        if low >= high:
            self.stack.pop()
            return

        if self.step_mode == 'partition':
            self.pivot = high
            self.i = low - 1
            self.j = low
            self.step_mode = 'partition_loop'

        elif self.step_mode == 'partition_loop':
            if self.j < self.pivot:
                if self.array[self.j] < self.array[self.pivot]:
                    self.i += 1
                    self.array[self.i], self.array[self.j] = self.array[self.j], self.array[self.i]
                self.j += 1
            else:
                self.i += 1
                self.array[self.i], self.array[self.pivot] = self.array[self.pivot], self.array[self.i]
                self.stack.pop()
                self.stack.append((low, self.i - 1))
                self.stack.append((self.i + 1, high))
                self.step_mode = 'partition'

        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        if not self.array:
            return
        bar_width = self.width() / len(self.array)
        for i, val in enumerate(self.array):
            if i == self.pivot:
                color = QColor(255, 100, 100)
            elif i == self.i or i == self.j:
                color = QColor(100, 255, 100)
            else:
                color = QColor(100, 200, 255)
            painter.setBrush(color)
            painter.drawRect(int(i * bar_width), self.height() - val, int(bar_width - 2), val)

    def set_speed(self, ms):
        self.timer.setInterval(ms)