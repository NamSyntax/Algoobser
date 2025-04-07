import random
from PyQt5.QtWidgets import QWidget, QLineEdit, QTextEdit, QVBoxLayout, QPushButton, QLabel, QSlider, QFormLayout
from PyQt5.QtCore import Qt

class VisualizerPage(QWidget):
    def __init__(self, back_func):
        super().__init__()
        self.layout = QVBoxLayout()
        self.label = QLabel("🔍 Visualization")
        self.canvas = None

        # Các nút và widget nhập liệu
        self.start_btn = QPushButton("▶ Bắt đầu")
        self.reset_btn = QPushButton("🔄 Reset")
        self.back_btn = QPushButton("🔙 Quay lại")
        
        self.num_elements_input = QLineEdit()
        self.num_elements_input.setPlaceholderText("Nhập số lượng phần tử (N) cho Random")
        
        self.manual_input = QTextEdit()
        self.manual_input.setPlaceholderText("Nhập mảng thủ công (các số cách nhau bằng dấu cách hoặc dấu phẩy)")
        
        self.generate_random_btn = QPushButton("Tạo Mảng Ngẫu Nhiên")
        self.generate_manual_btn = QPushButton("Nhập Mảng Thủ Công")

        # slider 4 mức (tốc độ visualize)
        self.speed_slider = QSlider(Qt.Horizontal)
        self.speed_slider.setRange(0, 4)  # Chỉ có 4 mốc: 0, 1, 2, 3
        self.speed_slider.setTickPosition(QSlider.TicksBelow)
        self.speed_slider.setTickInterval(1)  # Mỗi mốc cách nhau 1 giá trị
        self.speed_slider.setValue(2)  # mặc định nằm giữa
        self.speed_slider.setToolTip("Tốc độ chạy (ms)")
        
        # Cột chỉ
        self.speed_indicator = QLabel("500ms")  # Dùng label để chỉ tốc độ
        self.speed_indicator.setAlignment(Qt.AlignCenter)

        # Kết nối các sự kiện
        self.back_btn.clicked.connect(back_func)
        self.start_btn.clicked.connect(self.start_sort)
        self.reset_btn.clicked.connect(self.reset_sort)
        self.generate_random_btn.clicked.connect(self.generate_random_array)
        self.generate_manual_btn.clicked.connect(self.generate_manual_array)
        self.speed_slider.valueChanged.connect(self.update_speed)

        # Layout cho nhập liệu
        input_layout = QFormLayout()
        input_layout.addRow("Số lượng phần tử ngẫu nhiên:", self.num_elements_input)
        input_layout.addRow("Nhập mảng thủ công:", self.manual_input)
        
        # Thêm các widget vào layout
        self.layout.addWidget(self.label)
        self.layout.addLayout(input_layout)
        self.layout.addWidget(self.generate_random_btn)
        self.layout.addWidget(self.generate_manual_btn)
        self.layout.addWidget(self.speed_slider)
        self.layout.addWidget(self.speed_indicator)
        self.layout.addWidget(self.start_btn)
        self.layout.addWidget(self.reset_btn)
        self.layout.addWidget(self.back_btn)
        self.setLayout(self.layout)

        # ràng buộc giao diện
        self.reset_btn.setEnabled(False)

    def set_visualizer(self, visualizer_widget):
        if self.canvas:
            self.layout.removeWidget(self.canvas)
            self.canvas.deleteLater()
        self.canvas = visualizer_widget
        self.layout.insertWidget(1, self.canvas)  # Thêm dưới label
        self.canvas.reset()
        self.canvas.set_speed(70)  # mặc định = mức 2
        self.update_speed()  # # mặc định = mức 2

    def generate_random_array(self):
        # nhận N từ user
        try:
            num_elements = int(self.num_elements_input.text())
            if num_elements < 1:
                raise ValueError
            if self.canvas:
                self.canvas.array = [random.randint(10, 300) for _ in range(num_elements)]
                self.canvas.reset()
        except ValueError:
            self.show_error("Vui lòng nhập một số nguyên hợp lệ.")

    def generate_manual_array(self):
        # Nhận mảng từ user
        manual_input_text = self.manual_input.toPlainText()
        try:
            # chuỗi -> mảng số
            manual_array = list(map(int, manual_input_text.split()))
            if len(manual_array) < 1:
                raise ValueError
            if self.canvas:
                self.canvas.array = manual_array
                self.canvas.reset()
        except ValueError:
            self.show_error("Mảng nhập không hợp lệ. Vui lòng nhập các số nguyên cách nhau bằng dấu cách.")

    def show_error(self, message):
        # báo lỗi
        error_label = QLabel(message)
        self.layout.addWidget(error_label)

    def start_sort(self):
        if self.canvas:
            self.canvas.start()
            self.start_btn.setEnabled(False)  # ràng buộc giao diện
            self.reset_btn.setEnabled(True)  # 

    def reset_sort(self):
        if self.canvas:
            self.canvas.timer.stop()  # Dừng timer nếu đang chạy
            self.canvas.reset()
            self.start_btn.setEnabled(True) # ràng buộc giao diện
            self.reset_btn.setEnabled(False)  #

    def update_speed(self):
        if self.canvas:
            slider_value = self.speed_slider.value()
            speed = self.map_slider_to_speed(slider_value)
            self.canvas.set_speed(speed)
            self.update_speed_indicator(speed)

    def map_slider_to_speed(self, value):
        if value == 0:
            return 1100  # mù
        elif value == 1:
            return 240   # 
        elif value == 2:
            return 70   # dễ nhìn
        elif value == 3:
            return 20   # mờ mờ
        elif value == 4:
            return 10    # mù

    def update_speed_indicator(self, speed):
        """Cập nhật cột chỉ tốc độ"""
        self.speed_indicator.setText(f"{speed}ms")

