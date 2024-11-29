import cv2
import numpy as np
from PyQt5.QtWidgets import QFileDialog, QMessageBox

class TumorFinder:
    def __init__(self, ui):
        self.UI = ui
        self.original_image = None
        self.segmented_image = None

    def load_image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            None, "Open Image", "", "Image Files (*.png *.jpg *.jpeg)"
        )
        if file_path:
            self.clear_images()
            self.original_image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
            self.display_image(self.original_image, self.UI.loaded_image)
        else:
            QMessageBox.warning(None, "Load Error", "No image selected.")

    def clear_images(self):
        self.segmented_image = None
        if self.UI:
            self.UI.loaded_image.clear()
            self.UI.segmented_image.clear()
            self.UI.detected_image.clear()

    def display_image(self, image, target_widget):
        if image.ndim == 2:
            display_data = np.float32(image.T)
        elif image.ndim == 3:
            display_data = np.float32(image.transpose(1, 0, 2))
        else:
            QMessageBox.warning(None, "Display Error", "Invalid image format.")
            return
        target_widget.setImage(display_data, autoLevels=True)

    def process_image(self):
        if self.original_image is None:
            QMessageBox.warning(None, "Process Error", "Please load an image first.")
            return

        # Step 1: Preprocessing to suppress brain outlines
        preprocessed_image = self.suppress_edges(self.original_image)

        # Step 2: Process image using Divide and Conquer
        segmented_image = self.divide_and_conquer(preprocessed_image)

        # Step 3: Highlight tumor regions
        highlighted_tumor = self.highlight_tumor(self.original_image, segmented_image)

        # Step 4: Display results
        self.display_results(self.original_image, segmented_image, highlighted_tumor)

    def suppress_edges(self, image):
        """
        Suppress strong edges (e.g., brain outline) using Gaussian blur and edge masking.
        """
        blurred = cv2.GaussianBlur(image, (5, 5), 0)
        edges = cv2.Canny(blurred, 50, 150)
        edge_mask = cv2.bitwise_not(edges)
        suppressed_image = cv2.bitwise_and(image, image, mask=edge_mask)
        return suppressed_image

    def divide_and_conquer(self, image):
        """
        Apply Divide and Conquer to process the image recursively.
        """
        h, w = image.shape
        return self.process_region(image, 0, 0, h, w)

    def process_region(self, image, x, y, h, w):
     """
     Recursively divide the image region and process each part.
     """
     if h <= 64 or w <= 64:  # Base case: Process small regions directly
        grid = image[y:y + h, x:x + w]
        return self.segment_and_refine_grid(grid)

     # Divide the region into four quadrants
     mid_h, mid_w = h // 2, w // 2
    
     # Recursively process each quadrant
     top_left = self.process_region(image, x, y, mid_h, mid_w)
     top_right = self.process_region(image, x + mid_w, y, mid_h, w - mid_w)
     bottom_left = self.process_region(image, x, y + mid_h, h - mid_h, mid_w)
     bottom_right = self.process_region(image, x + mid_w, y + mid_h, h - mid_h, w - mid_w)

    # Combine results into a single image
     combined = np.zeros((h, w), dtype=np.uint8)
     combined[0:mid_h, 0:mid_w] = top_left
     combined[0:mid_h, mid_w:w] = top_right
     combined[mid_h:h, 0:mid_w] = bottom_left
     combined[mid_h:h, mid_w:w] = bottom_right

     return combined


    def segment_and_refine_grid(self, grid):
        """
        Segment and refine potential tumor regions within a grid.
        """
        # Threshold for segmentation
        _, binary = cv2.threshold(grid, 100, 255, cv2.THRESH_BINARY)

        # Morphological operations to clean up
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
        cleaned = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel, iterations=1)

        # Filter regions based on properties (area, circularity)
        contours, _ = cv2.findContours(cleaned, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        refined_grid = np.zeros_like(grid, dtype=np.uint8)

        for contour in contours:
            area = cv2.contourArea(contour)

            # Filter based on area
            if 200 < area < 3000:
                perimeter = cv2.arcLength(contour, True)
                if perimeter > 0:
                    # Calculate circularity: 4π × (Area / Perimeter^2)
                    circularity = (4 * np.pi * area) / (perimeter ** 2)
                    if circularity > 0.5:  # Tumor regions tend to be circular
                        cv2.drawContours(refined_grid, [contour], -1, 255, thickness=cv2.FILLED)

        return refined_grid

    def highlight_tumor(self, original_image, segmented_image):
        """
        Highlight tumor regions on the original grayscale image.
        """
        contours, _ = cv2.findContours(
            segmented_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )
        result = cv2.cvtColor(original_image, cv2.COLOR_GRAY2BGR)
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(result, (x, y), (x + w, y + h), (0, 255, 0), 2)
        return result

    def display_results(self, original, segmented, detected):
        """
        Display all processed results on the UI.
        """
        if self.UI:
            self.display_image(original, self.UI.loaded_image)
            self.display_image(segmented, self.UI.segmented_image)
            self.display_image(cv2.cvtColor(detected, cv2.COLOR_BGR2RGB), self.UI.detected_image)
