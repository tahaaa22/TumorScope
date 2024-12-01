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
        target_widget.setImage(display_data, autoLevels=True) # autoLevels=True automatically adjusts the brightness and contrast of the image for optimal visualization. DOES NOT affect the image, just the UI

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

    def suppress_edges(self, image): # O(H * W * 25) = O(H * W)
        """
        Suppress strong edges (brain outline) using Gaussian blur and edge masking.
        """
        blurred = cv2.GaussianBlur(image, (5, 5), 0) # Smooth sharp edges to reduce noise and small details (kernel size = 5x5, std deviation = 0) O(H * W * 25)
        edges = cv2.Canny(blurred, 50, 150) #  identifies edges based on intensity gradients (low threshold = 50, high threshold = 150), result is a binary image where edges are highlighted in white (255) and everything else is black (0)
        edge_mask = cv2.bitwise_not(edges)
        suppressed_image = cv2.bitwise_and(image, image, mask=edge_mask) # O(H * W)
        return suppressed_image 

    def divide_and_conquer(self, image):
        """
        Apply Divide and Conquer to process the image recursively.
        """
        h, w = image.shape
        return self.process_region(image, 0, 0, h, w)

    def process_region(self, image, x, y, h, w): # O(H * W * log(H * W))
        """
        Recursively divide the image region and process each part.
        """
        if h <= 64 or w <= 64:  # Base case: Process small regions directly
            grid = image[y:y + h, x:x + w]
            return self.segment_and_refine_grid(grid) # O(H * W)

        # Divide the region into four quadrants
        mid_h, mid_w = h // 2, w // 2

        # Recursively process each quadrant
        top_left = self.process_region(image, x, y, mid_h, mid_w)
        top_right = self.process_region(image, x + mid_w, y, mid_h, w - mid_w)
        bottom_left = self.process_region(image, x, y + mid_h, h - mid_h, mid_w)
        bottom_right = self.process_region(image, x + mid_w, y + mid_h, h - mid_h, w - mid_w)

        # Combine results into a single image, takes O(H * W)
        combined = np.zeros((h, w), dtype=np.uint8)
        combined[0:mid_h, 0:mid_w] = top_left
        combined[0:mid_h, mid_w:w] = top_right
        combined[mid_h:h, 0:mid_w] = bottom_left
        combined[mid_h:h, mid_w:w] = bottom_right

        return combined


    def segment_and_refine_grid(self, grid): # O(H * W)
        """
        Segment and refine potential tumor regions within a grid.
        """
        # Threshold for segmentation, returns a tuple of 2 values: the first, T, is the threshold value which is trivial because we set it to 100, and the second is the image, O(H * W)
        _, binary = cv2.threshold(grid, 105, 255, cv2.THRESH_BINARY) # Convert the grayscale grid into a binary image to distinguish potential tumor regions (threshold = 100) Pixel intensities above 100 are set to 255 (white), while those below are set to 0 (black)

        # Morphological operations to clean up, O(H * W * 9)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
        cleaned = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel, iterations=3)

        # Filter regions based on properties (area, circularity), O(H * W)
        contours, _ = cv2.findContours(cleaned, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # Identify the boundaries of connected white regions (potential tumors) in the cleaned binary image
        refined_grid = np.zeros_like(grid, dtype=np.uint8)

        for contour in contours: # O(H * W)
            area = cv2.contourArea(contour)

            if 300 < area < 3000: # Filter out regions that are too small (<300) or too large (>3000) to be tumors
                perimeter = cv2.arcLength(contour, True)
                if perimeter > 0:
                    # Calculate circularity: 4π × (Area / Perimeter^2)
                    circularity = (4 * np.pi * area) / (perimeter ** 2)
                    if circularity > 0.6:  # Tumors are likely to have a circularity greater than 0.6 (roughly circular)
                        cv2.drawContours(refined_grid, [contour], -1, 255, thickness=cv2.FILLED) 

        return refined_grid # A binary image where only the regions that are likely to be tumors are white. All other regions are black.

    def highlight_tumor(self, original_image, segmented_image):
        """
        Highlight tumor regions on the original grayscale image with improved precision.
        """
        # Find contours in the segmented binary image, O(H * W)
        contours, _ = cv2.findContours(
            segmented_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )
        
        # Convert grayscale image to BGR for color highlighting, O(H * W)
        result = cv2.cvtColor(original_image, cv2.COLOR_GRAY2BGR)
        
        for contour in contours: # O(H * W)
            # Compute minimum enclosing circle
            (cx, cy), radius = cv2.minEnclosingCircle(contour)
            
            # Ensure the radius is large enough to draw
            if radius > 5:
                # Draw a circle around the tumor
                cv2.circle(result, (int(cx), int(cy)), int(radius + 2), (0, 255, 0), 2)
        
        return result

    def display_results(self, original, segmented, detected):
        """
        Display all processed results on the UI.
        """
        if self.UI:
            self.display_image(original, self.UI.loaded_image)
            self.display_image(segmented, self.UI.segmented_image)
            self.display_image(cv2.cvtColor(detected, cv2.COLOR_BGR2RGB), self.UI.detected_image)
