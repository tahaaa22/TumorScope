import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from DecompressUI import Decompression
from CompressUI import Compression
from AnalysisUI import Analysis
from TumorFinder import TumorFinder
from CompressionsOperations import CompressionOperations
from DecompressionsOperations import DecompressionOperations


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.fullscreen = False
        self.current_layout = None  
        decompress = Decompression()
        compress = Compression()
        analysis = Analysis()
        self.arr = [decompress, compress, analysis]
        self.setupUi("Analysis")   
        self.tumor_finder = None
        self.compression_operations = None    
        self.decompression_operations = None  
        
        

    def setupUi(self, layout_name):
        if layout_name == "Decompression":
            self.current_layout = self.arr[0]
        elif layout_name == "Compression":
            self.current_layout = self.arr[1]
        elif layout_name == "Analysis":
            self.current_layout = self.arr[2]

        self.current_layout.setupUi(self)
        if layout_name == "Decompression":
            self.current_layout.analysis_button.clicked.connect(lambda: self.switch_layout("Analysis"))
            self.current_layout.compress_button.clicked.connect(lambda: self.switch_layout("Compression"))
            self.decompression_operations = DecompressionOperations(self.current_layout)
            self.current_layout.decompress_button.clicked.connect(lambda: self.decompression_operations.decompress())
            self.current_layout.load_button.clicked.connect(lambda: self.decompression_operations.load())
            
        elif layout_name == "Compression":
            self.current_layout.decompress_button.clicked.connect(lambda: self.switch_layout("Decompression"))
            self.current_layout.analysis_button.clicked.connect(lambda: self.switch_layout("Analysis"))
            self.compression_operations = CompressionOperations(self.current_layout)  #object of CompressionOperations, user it to connect functions
            self.current_layout.compress_button.clicked.connect(lambda: self.compression_operations.compress())
            self.current_layout.load_button.clicked.connect(lambda: self.compression_operations.load())
            
        elif layout_name == "Analysis":
            self.current_layout.compress_button.clicked.connect(lambda: self.switch_layout("Compression"))
            self.current_layout.decompress_button.clicked.connect(lambda: self.switch_layout("Decompression"))
            self.tumor_finder = TumorFinder(self.current_layout) #object of tumor finder, user it to connect functions
            self.current_layout.load_button.clicked.connect(lambda: self.tumor_finder.load_image())
            self.current_layout.process_button.clicked.connect(lambda: self.tumor_finder.process_image())
            
            
            

    def switch_layout(self, layout_name):
        self.current_layout = layout_name
        self.centralWidget().deleteLater()
        self.setupUi(layout_name)
        
    def toggle_full_screen(self):
        if self.fullscreen is True:
            self.showFullScreen() 
        else:
            self.show()  
        self.fullscreen = not self.fullscreen

   
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
   