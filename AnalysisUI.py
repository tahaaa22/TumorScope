from pyqtgraph import ImageView
#import resources_rc
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox,  QPushButton
import sys

is_hidden = False

class Analysis(object):
    
    def toggle_menu(self):
        global is_hidden  
        is_hidden = not is_hidden 
        self.leftmenu.setHidden(is_hidden) 

    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1221, 659)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet("*{\n"
"color:#000;\n"
"border:none;\n"
"}\n"
"#process_button, #load_button {\n"
"    background-color: #3498db;  /* Default button color */\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"}\n"
"#load_button:hover {\n"
"    background-color: #2980b9;  /* Button color on hover */\n"
"}\n"
"#process_button:hover {\n"
"    background-color: #2980b9;  /* Button color on hover */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;  /* Button color on hover */\n"
"}\n"
"\n"
"#ProfileCont, #menu_button{\n"
"border-radius: 20px;\n"
"background-color:#eff9fe;\n"
"border-color: rgb(0, 255, 255);\n"
"}\n"
"#analysis_button, #compress_button,#process_button, #load_button, #decompress_button, #confirmButton{\n"
"padding:10px 5px;\n"
"text-align:left;\n"
"font: 18px;\n"
"}\n"
" #menu_button, #profileButton{\n"
"padding:10px 5px;\n"
"text-align:left;\n"
"font: 10pt;\n"
"}\n"
"#analysis_button{\n"
"background-color: #fefeff;\n"
"padding:10px 5px;\n"
"text-align:left;\n"
"color: rgb(0, 0, 0);\n"
"font: 18px;\n"
"border-top-left-radius: 20px;\n"
"}\n"
"\n"
"#card1,#card2{\n"
"border-radius: 20px;\n"
"background-color:#eff9fe;\n"
"}\n"
"\n"
"#label{\n"
"border-radius: 20px;\n"
"background: transparent;\n"
"}\n"
"\n"
"#appheader{\n"
"color:#2596be;\n"
"}\n"
"#vitalsign,#filterflex, #comboBox, #detect_label{\n"
"color:#2596be;\n"
"}\n"
"#EMGlabel{\n"
"color:#2596be;\n"
"}\n"
"\n"
"#leftmenu{\n"
"background-color: #2596be;\n"
"}\n"
"\n"
"#rightmenu{\n"
"background-color: #eff9fe;\n"
"}\n"
"\n"
"QLineEdit{\n"
"background: transparent;\n"
"color:#2596be;\n"
"}\n"
"\n"
"#SearchFrame, #process_button, #load_button, #menu_button{\n"
"border-radius: 10px;\n"
"border: 2px solid #2596be;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftmenu = QtWidgets.QWidget(self.centralwidget)
        self.leftmenu.setObjectName("leftmenu")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.leftmenu)
        self.verticalLayout_7.setContentsMargins(15, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_4 = QtWidgets.QFrame(self.leftmenu)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_8.setContentsMargins(44, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_10.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_4 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_10.addWidget(self.label_4)
        self.verticalLayout_8.addWidget(self.frame_5, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_7.addWidget(self.frame_4)
        self.frame_6 = QtWidgets.QFrame(self.leftmenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_10.setContentsMargins(18, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_7 = QtWidgets.QFrame(self.frame_6)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 18)
        self.verticalLayout_9.setSpacing(21)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.decompress_button = QtWidgets.QPushButton(self.frame_7)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/code.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.decompress_button.setIcon(icon)
        self.decompress_button.setObjectName("decompress_button")
        self.verticalLayout_9.addWidget(self.decompress_button)
        self.analysis_button = QtWidgets.QPushButton(self.frame_7)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/activity.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.analysis_button.setIcon(icon1)
        self.analysis_button.setIconSize(QtCore.QSize(24, 24))
        self.analysis_button.setObjectName("analysis_button")
        self.verticalLayout_9.addWidget(self.analysis_button)
        self.compress_button = QtWidgets.QPushButton(self.frame_7)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icons/check-square.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.compress_button.setIcon(icon2)
        self.compress_button.setIconSize(QtCore.QSize(24, 24))
        self.compress_button.setObjectName("compress_button")
        self.verticalLayout_9.addWidget(self.compress_button)
        self.verticalLayout_10.addWidget(self.frame_7, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_7.addWidget(self.frame_6)
        self.horizontalLayout.addWidget(self.leftmenu)
        self.rightmenu = QtWidgets.QWidget(self.centralwidget)
        self.rightmenu.setObjectName("rightmenu")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.rightmenu)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.headerframe = QtWidgets.QWidget(self.rightmenu)
        self.headerframe.setObjectName("headerframe")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.headerframe)
        self.horizontalLayout_2.setContentsMargins(8, 0, 0, 10)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.menu_button = QtWidgets.QPushButton(self.headerframe)
        self.menu_button.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.menu_button.setFont(font)
        self.menu_button.setStyleSheet("")
        self.menu_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Icons/menu.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_button.setIcon(icon3)
        self.menu_button.setIconSize(QtCore.QSize(24, 24))
        self.menu_button.setObjectName("menu_button")
        self.horizontalLayout_2.addWidget(self.menu_button, 0, QtCore.Qt.AlignLeft)
        self.appheader = QtWidgets.QLabel(self.headerframe)
        self.appheader.setMinimumSize(QtCore.QSize(630, 0))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.appheader.setFont(font)
        self.appheader.setObjectName("appheader")
        self.horizontalLayout_2.addWidget(self.appheader)
        self.verticalLayout.addWidget(self.headerframe, 0, QtCore.Qt.AlignTop)
        self.cardsframe = QtWidgets.QWidget(self.rightmenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cardsframe.sizePolicy().hasHeightForWidth())
        self.cardsframe.setSizePolicy(sizePolicy)
        self.cardsframe.setObjectName("cardsframe")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.cardsframe)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.widget_4 = QtWidgets.QWidget(self.cardsframe)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_2 = QtWidgets.QFrame(self.widget_4)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.EMGlabel = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.EMGlabel.setFont(font)
        self.EMGlabel.setObjectName("EMGlabel")
        self.horizontalLayout_12.addWidget(self.EMGlabel, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_4.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.widget_4)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.loaded_image = ImageView(self.frame_3)
        self.loaded_image.ui.roiBtn.hide()  
        self.loaded_image.ui.menuBtn.hide()  
        self.loaded_image.ui.histogram.hide()
        self.loaded_image.setMinimumSize(QtCore.QSize(400, 350))
        self.loaded_image.setObjectName("loaded_image")
        self.verticalLayout_6.addWidget(self.loaded_image)
        self.verticalLayout_4.addWidget(self.frame_3)
        self.horizontalLayout_11.addWidget(self.widget_4)
        self.widget_6 = QtWidgets.QWidget(self.cardsframe)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.frame_11 = QtWidgets.QFrame(self.widget_6)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.filterflex = QtWidgets.QLabel(self.frame_11)
        self.filterflex.setMinimumSize(QtCore.QSize(213, 0))
        self.filterflex.setMaximumSize(QtCore.QSize(213, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.filterflex.setFont(font)
        self.filterflex.setScaledContents(False)
        self.filterflex.setObjectName("filterflex")
        self.horizontalLayout_8.addWidget(self.filterflex, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_13.addWidget(self.frame_11)
        self.frame_12 = QtWidgets.QFrame(self.widget_6)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.segmented_image = ImageView(self.frame_12)
        self.segmented_image.ui.roiBtn.hide()  
        self.segmented_image.ui.menuBtn.hide()  
        self.segmented_image.ui.histogram.hide()
        self.segmented_image.setMinimumSize(QtCore.QSize(400, 350))
        self.segmented_image.setObjectName("segmented_image")
        self.verticalLayout_17.addWidget(self.segmented_image)
        self.verticalLayout_13.addWidget(self.frame_12)
        self.horizontalLayout_11.addWidget(self.widget_6)
        self.verticalLayout.addWidget(self.cardsframe)
        self.mainframe = QtWidgets.QWidget(self.rightmenu)
        self.mainframe.setObjectName("mainframe")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.mainframe)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.mainframe)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.detect_label = QtWidgets.QLabel(self.frame)
        self.detect_label.setMinimumSize(QtCore.QSize(188, 0))
        self.detect_label.setMaximumSize(QtCore.QSize(188, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.detect_label.setFont(font)
        self.detect_label.setObjectName("detect_label")
        self.horizontalLayout_7.addWidget(self.detect_label)
        self.verticalLayout_2.addWidget(self.frame)
        self.detected_image = ImageView(self.mainframe)
        self.detected_image.ui.roiBtn.hide()  
        self.detected_image.ui.menuBtn.hide() 
        self.detected_image.ui.histogram.hide() 
        self.detected_image.setMinimumSize(QtCore.QSize(400, 200))
        self.detected_image.setObjectName("detected_image")
        self.verticalLayout_2.addWidget(self.detected_image)
        self.widget = QtWidgets.QWidget(self.mainframe)
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.load_button = QtWidgets.QPushButton(self.widget) # clicked = lambda: manager.load_image()
        self.load_button.setObjectName("load_button")
        self.horizontalLayout_3.addWidget(self.load_button, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.process_button = QtWidgets.QPushButton(self.widget) # clicked = lambda: manager.process_image()
        self.process_button.setObjectName("process_button")
        self.horizontalLayout_3.addWidget(self.process_button, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_2.addWidget(self.widget)
        self.verticalLayout.addWidget(self.mainframe)
        self.horizontalLayout.addWidget(self.rightmenu)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        #hiding the menu button
        self.menu_button.clicked.connect(self.toggle_menu)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TumorScope"))
        self.label_4.setText(_translate("MainWindow", "Main Menu"))
        self.decompress_button.setText(_translate("MainWindow", "Decompress"))
        self.analysis_button.setText(_translate("MainWindow", "Analysis"))
        self.compress_button.setText(_translate("MainWindow", "Compress"))
        self.appheader.setText(_translate("MainWindow", "TumorScope"))
        self.EMGlabel.setText(_translate("MainWindow", "Loaded Image"))
        self.filterflex.setText(_translate("MainWindow", "Segmented Image"))
        self.detect_label.setText(_translate("MainWindow", "Detected Tumors"))
        self.load_button.setText(_translate("MainWindow", "Load image"))
        self.process_button.setText(_translate("MainWindow", "Process"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Analysis()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
