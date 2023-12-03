import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class SignalProcessingSoftware:
    def __init__(self, root):
        self.root = root
        self.root.title("Phần mềm Hỗ trợ Học tập Xử lý Tín hiệu Số")

        self.create_widgets()

    def create_widgets(self):
        # Label và Entry cho nhập tín hiệu
        self.signal_label = ttk.Label(self.root, text="Nhập tín hiệu:")
        self.signal_entry = ttk.Entry(self.root, width=50)

        # Button để vẽ đồ thị tín hiệu
        self.plot_button = ttk.Button(self.root, text="Vẽ đồ thị tín hiệu", command=self.plot_signal)

        # Button để tính biên độ tối đa của tín hiệu
        self.amplitude_button = ttk.Button(self.root, text="Tính biên độ tối đa", command=self.calculate_amplitude)

        # Vùng hiển thị kết quả
        self.result_label = ttk.Label(self.root, text="Kết quả:")
        self.result_display = ttk.Label(self.root, text="")

        # Sắp xếp các thành phần trên giao diện sử dụng grid
        self.signal_label.grid(row=0, column=0, padx=10, pady=10, sticky="W")
        self.signal_entry.grid(row=0, column=1, columnspan=3, padx=10, pady=10, sticky="W")
        self.plot_button.grid(row=1, column=0, padx=10, pady=10, sticky="W")
        self.amplitude_button.grid(row=1, column=1, padx=10, pady=10, sticky="W")
        self.result_label.grid(row=2, column=0, padx=10, pady=10, sticky="W")
        self.result_display.grid(row=2, column=1, columnspan=3, padx=10, pady=10, sticky="W")

    def plot_signal(self):
        try:
            # Lấy tín hiệu từ người dùng
            signal_text = self.signal_entry.get()

            # Chuyển đổi tín hiệu thành mảng NumPy
            signal = np.array([float(x) for x in signal_text.split(",")])

            # Vẽ đồ thị tín hiệu
            fig, ax = plt.subplots()
            ax.plot(signal, label="Tín hiệu")
            ax.legend()

            # Hiển thị đồ thị trên giao diện
            canvas = FigureCanvasTkAgg(fig, master=self.root)
            canvas_widget = canvas.get_tk_widget()
            canvas_widget.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky="W")

            # Hiển thị kết quả
            self.result_display.config(text="")
        except ValueError:
            self.result_display.config(text="Lỗi! Hãy nhập tín hiệu hợp lệ.")

    def calculate_amplitude(self):
        try:
            # Lấy tín hiệu từ người dùng
            signal_text = self.signal_entry.get()

            # Chuyển đổi tín hiệu thành mảng NumPy
            signal = np.array([float(x) for x in signal_text.split(",")])

            # Tính biên độ tối đa của tín hiệu
            max_amplitude = np.max(np.abs(signal))

            # Hiển thị kết quả
            self.result_display.config(text=f"Biên độ tối đa: {max_amplitude:.2f}")
        except ValueError:
            self.result_display.config(text="Lỗi! Hãy nhập tín hiệu hợp lệ.")

# Tạo cửa sổ
root = tk.Tk()
app = SignalProcessingSoftware(root)

# Chạy ứng dụng
root.mainloop()
