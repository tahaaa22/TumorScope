import cv2
import numpy as np
import zlib
import os
from PyQt5.QtWidgets import QFileDialog, QMessageBox

class CompressionOperations:
    def __init__(self, GUI) -> None:
        self.ui = GUI
        self.original_image = None
        self.image_name = None
        self.compressed_image = None


    def load_image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            None, "Open Image", "", "Image Files (*.png *.jpg *.jpeg)"
        )
        if file_path:
            self.clear()
            self.original_image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
            self.image_name = os.path.basename(file_path).split('.')[0]
            self.ui.normal_image.setImage(np.float32(self.original_image.T), autoLevels=True)
            image_size = self.original_image.nbytes
            self.ui.normal_size.setText(f"{image_size//1024} Kbytes")
            
        else:
            QMessageBox.warning(None, "Load Error", "No image selected.")


    def clear(self):
        self.ui.normal_image.clear()
        self.ui.compressed_image.clear()
        self.ui.compressed_size.setText("0 Kbytes")
        self.image_name = None


    def display_image_with_divisions(self):
        image_with_lines = self.original_image.copy() # O(H * W)
        height, width = image_with_lines.shape
        h_split = height // 3
        w_split = width // 3

        color = (0,255,0) 
        thickness = 3
        
        for i in range(1, 4): # O 3*(H + W)
            cv2.line(image_with_lines, (0, i * h_split), (width, i * h_split), color, thickness)
            cv2.line(image_with_lines, (i * w_split, 0), (i * w_split, height), color, thickness)

        self.ui.normal_image.setImage(np.float32(image_with_lines.T)) # O(H * W)


    def compress_image(self):
        if self.original_image is None:
            QMessageBox.warning(None, "Compression Error", "No image loaded.")
            return
        self.display_image_with_divisions() # O(H * W)

        height, width = self.original_image.shape
        h_split = height // 3
        w_split = width // 3
        self.compressed_data = []
        self.sub_image_shapes = []
        
        for i in range(3): # O (H/3 * W/3) = O(H * W)
            for j in range(3):
                sub_image = self.original_image[i * h_split:(i + 1) * h_split, j * w_split:(j + 1) * w_split]
                compressed_sub_image = zlib.compress(sub_image.tobytes())
                self.compressed_data.append(compressed_sub_image)
                self.sub_image_shapes.append(sub_image.shape)
        
        total_compressed_size = sum(len(data) for data in self.compressed_data) # O(9) = O(1), because compressed data is always 9 parts
        self.ui.compressed_size.setText(f"{total_compressed_size//1024} Kbytes")
        self.save_compressed_image()
        
        
    def save_compressed_image(self): # O(C), where C is the total compressed size
        dir = os.path.join(os.getcwd(), "Compressed_Images")
        
        compressed_file_path = os.path.join(dir, f"{self.image_name}_compressed.zlib")
        with open(compressed_file_path, 'wb') as f:
            for data in self.compressed_data:
                f.write(data + b'###')

    def reconstruct_image(self): # O(C + H * W)
        if not self.compressed_data:
            QMessageBox.warning(None, "Reconstruction Error", "No compressed data found.")
            return
        
        height, width = self.original_image.shape
        h_split = height // 3
        w_split = width // 3
        reconstructed_image = np.zeros((height, width), dtype=np.uint8) # O(H * W)
        
        for i in range(3):
            for j in range(3):
                index = i * 3 + j
                decompressed_data = np.frombuffer(zlib.decompress(self.compressed_data[index]), dtype=np.uint8) # O(C), where C is the total compressed size
                sub_image_shape = self.sub_image_shapes[index]
                decompressed_image = decompressed_data.reshape(sub_image_shape) # O(1), because it only modifies metadata without actual data copying
                reconstructed_image[i * h_split:(i + 1) * h_split, j * w_split:(j + 1) * w_split] = decompressed_image # O(H/3 * W/3) = O(H * W)
        
        self.ui.compressed_image.setImage(np.float32(reconstructed_image.T))   