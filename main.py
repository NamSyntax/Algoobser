import sys
from PyQt5.QtWidgets import QApplication
from src.main_window import MainWindow

def run_app():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run_app()