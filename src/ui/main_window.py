from PyQt5.QtWidgets import QWidget, QVBoxLayout
from src.ui.visualizer_canvas import VisualizerCanvas
from src.ui.controls import ControlPanel
from src.algorithms.bubble_sort import BubbleSort

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bubble Sort Visualizer")
        self.setGeometry(100, 100, 1600, 800)

        self.data = [5, 1, 4, 2, 3]
        self.algorithm = BubbleSort(self.data)
        self.current_step = 0

        self.canvas = VisualizerCanvas()
        self.controls = ControlPanel()

        self.controls.next_btn.clicked.connect(self.next_step)

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        layout.addWidget(self.controls)
        self.setLayout(layout)

        self.canvas.update_data(self.data)

    def next_step(self):
        self.current_step += 1
        new_data = self.algorithm.get_step(self.current_step)
        self.canvas.update_data(new_data)
