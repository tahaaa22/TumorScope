import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from DecompressUI import Decompression
from CompressUI import Compression
from AnalysisUI import Analysis


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.current_layout = None
        self.setupUi("Decompression")
        

    def setupUi(self, layout_name):
        if layout_name == "Decompression":
            self.current_layout = Decompression()
        elif layout_name == "Compression":
            self.current_layout = Compression()
        elif layout_name == "Analysis":
            self.current_layout = Analysis()

        self.current_layout.setupUi(self)
        if layout_name == "Decompression":
            self.current_layout.analysis_button.clicked.connect(lambda: self.switch_layout("Analysis"))
            self.current_layout.compress_button.clicked.connect(lambda: self.switch_layout("Compression"))
        elif layout_name == "Compression":
            self.current_layout.decompress_button.clicked.connect(lambda: self.switch_layout("Decompression"))
            self.current_layout.analysis_button.clicked.connect(lambda: self.switch_layout("Analysis"))
        elif layout_name == "Analysis":
            self.current_layout.compress_button.clicked.connect(lambda: self.switch_layout("Compression"))
            self.current_layout.decompress_button.clicked.connect(lambda: self.switch_layout("Decompression"))

    def switch_layout(self, layout_name):
        self.current_layout = layout_name
        self.centralWidget().deleteLater() 
        self.setupUi(layout_name)
        self.adjustSize()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
   