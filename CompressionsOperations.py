


class CompressionOperations:
    def __init__(self, GUI) -> None:
        self.ui = GUI
        
    def compress():
        print("testing compression function")
        
    def load():
        print("testing loading function")

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel, QPushButton

class FullScreenApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt Full-Screen Tab Example")
        self.setGeometry(100, 100, 800, 600)  # Initial window size

        # Create the tab widget
        self.tab_widget = QTabWidget(self)
        self.setCentralWidget(self.tab_widget)

        # Add tabs
        self.add_tab("Tab 1", "Content of Tab 1")
        self.add_tab("Tab 2", "Content of Tab 2")
        self.add_tab("Tab 3", "Content of Tab 3")

        # Add a button to toggle full-screen mode
        self.fullscreen_button = QPushButton("Toggle Full Screen", self)
        self.fullscreen_button.clicked.connect(self.toggle_full_screen)
        self.statusBar().addPermanentWidget(self.fullscreen_button)

        self.fullscreen = False  # Track full-screen state

    def add_tab(self, title, content):
        tab = QWidget()
        layout = QVBoxLayout()
        label = QLabel(content)
        layout.addWidget(label)
        tab.setLayout(layout)
        self.tab_widget.addTab(tab, title)

    def toggle_full_screen(self):
        if self.fullscreen:
            self.showNormal()  # Return to normal windowed mode
        else:
            self.showFullScreen()  # Enter full-screen mode
        self.fullscreen = not self.fullscreen

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FullScreenApp()
    window.show()
    sys.exit(app.exec_())
