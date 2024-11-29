import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon  
from CompressUI import Compression
from AnalysisUI import Analysis
from TumorFinder import TumorFinder
from CompressionsOperations import CompressionOperations


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.fullscreen = False
        self.current_layout = None  
        compress = Compression()
        analysis = Analysis()
        self.arr = [compress, analysis]
        self.setupUi("Analysis")   
        self.tumor_finder = TumorFinder(analysis)
        self.compression_operations = None     
        self.setWindowIcon(QIcon("Icons/brain.png")) 
        
        

    def setupUi(self, layout_name):
        if layout_name == "Compression":
            self.current_layout = self.arr[0]
        elif layout_name == "Analysis":
            self.current_layout = self.arr[1]

        self.current_layout.setupUi(self)
        
            
        if layout_name == "Compression":
            self.current_layout.analysis_button.clicked.connect(lambda: self.switch_layout("Analysis"))
            self.compression_operations = CompressionOperations(self.current_layout)
            self.current_layout.load_button.clicked.connect(lambda: self.compression_operations.load_image())
            self.current_layout.compression_button.clicked.connect(lambda: self.compression_operations.compress_image())
            self.current_layout.reconstruction_button.clicked.connect(lambda: self.compression_operations.reconstruct_image())
            
        elif layout_name == "Analysis":
            self.current_layout.compress_button.clicked.connect(lambda: self.switch_layout("Compression"))
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
   