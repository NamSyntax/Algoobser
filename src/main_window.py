from PyQt5.QtWidgets import QMainWindow, QStackedWidget

from .home_page import HomePage
from .visualizer_page import VisualizerPage
from .algorithms.bubble_sort_canvas import BubbleSortCanvas
from .algorithms.quick_sort_canvas import QuickSortCanvas

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Visualizer App")
        self.setGeometry(100, 100, 1600, 900)

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        self.home_page = HomePage(self.show_visualizer_with_algo)
        self.visualizer_page = VisualizerPage(self.show_home)

        self.stack.addWidget(self.home_page)         # index 0
        self.stack.addWidget(self.visualizer_page)   # index 1

    def show_visualizer_with_algo(self, algo_name):
        if algo_name == "bubble":
            self.visualizer_page.set_visualizer(BubbleSortCanvas())
        elif algo_name == "quick":
            self.visualizer_page.set_visualizer(QuickSortCanvas())
        self.stack.setCurrentIndex(1)

    def show_home(self):
        # Khi quay lại, reset lại mọi thứ đang chạy
        if self.visualizer_page.canvas:
            self.visualizer_page.canvas.timer.stop()
            self.visualizer_page.start_btn.setEnabled(True)  # Enable nút Start khi quay lại
            self.visualizer_page.reset_btn.setEnabled(False)  # Disable nút Reset khi quay lại
        self.stack.setCurrentIndex(0)
