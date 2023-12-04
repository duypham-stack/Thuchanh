import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk

class ImageFilterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Smoothing App")

        # Tạo biến lưu trữ ảnh gốc và ảnh được xử lý
        self.original_image = None
        self.processed_image = None

        # Tạo widgets
        self.create_widgets()

    def create_widgets(self):
        # Tạo các nút và các thành phần giao diện khác
        self.label = tk.Label(self.root, text="Select an image:")
        self.label.pack(pady=10)

        self.browse_button = tk.Button(self.root, text="Browse", command=self.load_image)
        self.browse_button.pack(pady=5)

        self.smooth_button = tk.Button(self.root, text="Smooth Image", command=self.smooth_image)
        self.smooth_button.pack(pady=5)

        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack(pady=10)

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
        if file_path:
            self.original_image = cv2.imread(file_path)
            self.display_image(self.original_image)

    def smooth_image(self):
        if self.original_image is not None:
            # Lọc làm mịn ảnh sử dụng Gaussian Blur
            blurred_image = cv2.GaussianBlur(self.original_image, (5, 5), 0)
            self.display_image(blurred_image)

    def display_image(self, image):
        # Chuyển đổi ảnh từ BGR sang RGB để hiển thị trên Canvas
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image_pil = Image.fromarray(image_rgb)
        image_tk = ImageTk.PhotoImage(image=image_pil)

        # Hiển thị ảnh trên Canvas
        self.canvas.config(width=image_tk.width(), height=image_tk.height())
        self.canvas.create_image(0, 0, anchor=tk.NW, image=image_tk)
        self.canvas.image = image_tk

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageFilterApp(root)
    root.mainloop()
