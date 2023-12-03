import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class CalculusSoftware:
    def __init__(self, root):
        self.root = root
        self.root.title("Phần mềm Hỗ trợ Học tập Giải tích")

        self.create_widgets()

    def create_widgets(self):
        # Label và Entry cho nhập hàm số
        self.function_label = ttk.Label(self.root, text="Nhập hàm số f(x):")
        self.function_entry = ttk.Entry(self.root, width=50)

        # Button để tính đạo hàm
        self.derivative_button = ttk.Button(self.root, text="Tính đạo hàm", command=self.calculate_derivative)

        # Button để tính tích phân
        self.integral_button = ttk.Button(self.root, text="Tính tích phân", command=self.calculate_integral)

        # Button để vẽ đồ thị
        self.plot_button = ttk.Button(self.root, text="Vẽ đồ thị", command=self.plot_function)

        # Vùng hiển thị kết quả
        self.result_label = ttk.Label(self.root, text="Kết quả:")
        self.result_display = ttk.Label(self.root, text="")

        # Sắp xếp các thành phần trên giao diện sử dụng grid
        self.function_label.grid(row=0, column=0, padx=10, pady=10, sticky="W")
        self.function_entry.grid(row=0, column=1, columnspan=3, padx=10, pady=10, sticky="W")
        self.derivative_button.grid(row=1, column=0, padx=10, pady=10, sticky="W")
        self.integral_button.grid(row=1, column=1, padx=10, pady=10, sticky="W")
        self.plot_button.grid(row=1, column=2, padx=10, pady=10, sticky="W")
        self.result_label.grid(row=2, column=0, padx=10, pady=10, sticky="W")
        self.result_display.grid(row=2, column=1, columnspan=3, padx=10, pady=10, sticky="W")

    def calculate_derivative(self):
        try:
            # Lấy hàm số từ người dùng
            function_text = self.function_entry.get()

            # Chuyển đổi hàm số thành hàm Python sử dụng eval
            function = lambda x: eval(function_text)

            # Tính đạo hàm tại x = 0
            derivative_result = np.gradient([function(x) for x in np.linspace(-10, 10, 100)])

            # Hiển thị kết quả
            self.result_display.config(text=f"Đạo hàm: {derivative_result}")
        except Exception as e:
            self.result_display.config(text=f"Lỗi: {str(e)}")

    def calculate_integral(self):
        try:
            # Lấy hàm số từ người dùng
            function_text = self.function_entry.get()

            # Chuyển đổi hàm số thành hàm Python sử dụng eval
            function = lambda x: eval(function_text)

            # Tính tích phân từ -10 đến 10
            integral_result = np.trapz([function(x) for x in np.linspace(-10, 10, 100)])

            # Hiển thị kết quả
            self.result_display.config(text=f"Tích phân: {integral_result}")
        except Exception as e:
            self.result_display.config(text=f"Lỗi: {str(e)}")

    def plot_function(self):
        try:
            # Lấy hàm số từ người dùng
            function_text = self.function_entry.get()

            # Chuyển đổi hàm số thành hàm Python sử dụng eval
            function = lambda x: eval(function_text)

            # Vẽ đồ thị
            x_values = np.linspace(-10, 10, 100)
            y_values = [function(x) for x in x_values]

            fig, ax = plt.subplots()
            ax.plot(x_values, y_values, label=f"$f(x)={function_text}$")
            ax.legend()

            # Hiển thị đồ thị trên giao diện
            canvas = FigureCanvasTkAgg(fig, master=self.root)
            canvas_widget = canvas.get_tk_widget()
            canvas_widget.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky="W")

            # Hiển thị kết quả
            self.result_display.config(text="")
        except Exception as e:
            self.result_display.config(text=f"Lỗi: {str(e)}")

# Tạo cửa sổ
root = tk.Tk()
app = CalculusSoftware(root)

# Chạy ứng dụng
root.mainloop()
