from PyQt5.QtWidgets import QWidget,QVBoxLayout, QPushButton, QLabel

class HomePage(QWidget):
    def __init__(self, switch_func):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("🏠 Chọn thuật toán để visualize:"))

        btn1 = QPushButton("📊 Bubble Sort")
        btn2 = QPushButton("⚡ Quick Sort")

        btn1.clicked.connect(lambda: switch_func("bubble"))
        btn2.clicked.connect(lambda: switch_func("quick"))

        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addStretch()
        self.setLayout(layout)