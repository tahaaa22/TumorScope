class TumorFinder:
    def __init__(self, ui = None):
        self.UI = ui
        print("TumorFinder initialized")

    
    def load_image(self):
    #  file_path, _ = QFileDialog.getOpenFileName(
    #     None, "Open Image", "", "Image Files (*.png *.jpg *.jpeg )"
    # )
    #  if file_path:
    #     # Load the image as grayscale
    #     self.image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    #     if self.image is not None:
    #         QMessageBox.information(None, "Image Loaded", "Image successfully loaded.")
    #         # Display the image in the ImageView widget
    #         self.display_image(self.image, self.loaded_image)
    #     else:
    #         QMessageBox.warning(None, "Load Error", "Failed to read the image.")
    #  else:
    #     QMessageBox.warning(None, "Load Error", "No image selected.")
        print("Image loaded")

    # def display_image(self, image, image_view):
     
    #  if image_view is not None:
    #     # Ensure the image is displayed correctly by using ImageView's setImage method
    #     image_view.setImage(image.T)  # Transpose if necessary for correct orientation
    #  else:
    #     QMessageBox.warning(None, "Display Error", "ImageView widget is not initialized.")

    def process_image(self):
    #     if self.image is None:
    #         QMessageBox.warning(None, "Process Error", "Please load an image first.")
    #         return

    #     grid_size = 64
    #     threshold_value = 150

    #     grids = self.divide_image(self.image, grid_size)
    #     processed_grids = [
    #         (i, j, self.process_grid(grid, threshold_value)) for i, j, grid in grids
    #     ]
    #     segmented_image = self.combine_grids(processed_grids, self.image.shape, grid_size)
    #     result = self.highlight_tumor(self.image, segmented_image)

    #     # Display the results
    #     self.display_results(self.image, segmented_image, result)
        print("Image processed")

    # def divide_image(self, image, grid_size):
    #     h, w = image.shape
    #     grids = []
    #     for i in range(0, h, grid_size):
    #         for j in range(0, w, grid_size):
    #             grid = image[i : i + grid_size, j : j + grid_size]
    #             grids.append((i, j, grid))
    #     return grids

    # def process_grid(self, grid, threshold_value):
    #     _, binary = cv2.threshold(grid, threshold_value, 255, cv2.THRESH_BINARY)
    #     return binary

    # def combine_grids(self, grids, original_shape, grid_size):
    #     h, w = original_shape
    #     segmented_image = np.zeros((h, w), dtype=np.uint8)
    #     for i, j, processed_grid in grids:
    #         segmented_image[i : i + grid_size, j : j + grid_size] = processed_grid
    #     return segmented_image

    # def highlight_tumor(self, original_image, segmented_image):
    #     contours, _ = cv2.findContours(segmented_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #     result = cv2.cvtColor(original_image, cv2.COLOR_GRAY2BGR)
    #     for contour in contours:
    #         if cv2.contourArea(contour) > 100:
    #             x, y, w, h = cv2.boundingRect(contour)
    #             cv2.rectangle(result, (x, y), (x + w, y + h), (0, 255, 0), 2)
    #     return result

    # def display_results(self, original, segmented, detected):
           
    #  if self.loaded_image is not None:
    #     # Display the original image in the 'loaded_image' widget
    #     self.loaded_image.setImage(original.T)  # Transpose if needed

    #  if self.segmented_image is not None:
    #     # Display the segmented image in the 'segmented_image' widget
    #     self.segmented_image.setImage(segmented.T)  # Transpose if needed

    #  if self.detected_image is not None:
    #     # Display the detected tumors in the 'detected_image' widget
    #     self.detected_image.setImage(cv2.cvtColor(detected, cv2.COLOR_BGR2RGB).transpose(1, 0, 2))
