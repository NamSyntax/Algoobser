from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout

class ControlPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.next_btn = QPushButton("Next")
        layout = QHBoxLayout()
        layout.addWidget(self.next_btn)
        self.setLayout(layout)
