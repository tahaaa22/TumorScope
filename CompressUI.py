from pyqtgraph import ImageView
#import resources_rc
from PyQt5 import QtCore, QtGui, QtWidgets



is_hidden = False


class Compression(object):
    
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
"#load_button, #compression_button, #reconstruction_button {\n"
"    background-color: #3498db;  /* Default button color */\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"}\n"
"#process_button:hover {\n"
"    background-color: #2980b9;  /* Button color on hover */\n"
"}\n"
"#load_button:hover {\n"
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
"#analysis_button, #compress_button,#load_button, #compression_button, #reconstruction_button, #decompress_button, #confirmButton{\n"
"padding:10px 5px;\n"
"text-align:left;\n"
"font: 18px;\n"
"}\n"
" #menu_button, #profileButton{\n"
"padding:10px 5px;\n"
"text-align:left;\n"
"font: 10pt;\n"
"}\n"
"#compress_button{\n"
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
"#vitalsign,#filterflex, #comboBox, #detect_label, #EMGlabel{\n"
"color:#2596be;\n"
"}\n"
"\n"
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
"#SearchFrame, #load_button, #compression_button, #reconstruction_button, #menu_button{\n"
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
        self.leftmenu.setMinimumSize(QtCore.QSize(302, 0))
        self.leftmenu.setMaximumSize(QtCore.QSize(302, 16777215))
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
        # Add spacer to center the label
        self.left_spacer = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(self.left_spacer)

        # App header label
        self.appheader = QtWidgets.QLabel(self.headerframe)
        self.appheader.setMinimumSize(QtCore.QSize(630, 0))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.appheader.setFont(font)
        self.appheader.setText("App Header")
        self.appheader.setAlignment(QtCore.Qt.AlignCenter)
        self.appheader.setObjectName("appheader")
        self.horizontalLayout_2.addWidget(self.appheader)

        # Add another spacer for symmetry
        self.right_spacer = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(self.right_spacer)
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
        self.frame_3 = QtWidgets.QFrame(self.widget_4)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.normal_image = ImageView(self.frame_3)
        self.normal_image.setMinimumSize(QtCore.QSize(400, 400)) 
        self.normal_image.setObjectName("normal_image")
        self.normal_image.ui.roiBtn.hide()  
        self.normal_image.ui.menuBtn.hide() 
        self.normal_image.ui.histogram.hide()
        self.verticalLayout_6.addWidget(self.normal_image)
        self.frame_2 = QtWidgets.QFrame(self.frame_3)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.EMGlabel = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.EMGlabel.setFont(font)
        self.EMGlabel.setObjectName("EMGlabel")
        self.verticalLayout_3.addWidget(self.EMGlabel, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.normal_size = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.normal_size.setFont(font)
        self.normal_size.setObjectName("normal_size")
        self.horizontalLayout_4.addWidget(self.normal_size)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.normal_extension = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.normal_extension.setFont(font)
        self.normal_extension.setObjectName("normal_extension")
        self.horizontalLayout_5.addWidget(self.normal_extension)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.verticalLayout_6.addWidget(self.frame_2)
        self.verticalLayout_4.addWidget(self.frame_3)
        self.horizontalLayout_11.addWidget(self.widget_4)
        self.widget_6 = QtWidgets.QWidget(self.cardsframe)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.frame_12 = QtWidgets.QFrame(self.widget_6)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.compressed_image = ImageView(self.frame_12)
        self.compressed_image.ui.roiBtn.hide()
        self.compressed_image.ui.menuBtn.hide()
        self.compressed_image.ui.histogram.hide()
        self.compressed_image.setMinimumSize(QtCore.QSize(400, 400))
        self.compressed_image.setObjectName("compressed_image")
        self.verticalLayout_17.addWidget(self.compressed_image)
        self.frame_11 = QtWidgets.QFrame(self.frame_12)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
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
        self.verticalLayout_5.addWidget(self.filterflex, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.frame_11)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.compressed_size = QtWidgets.QLabel(self.frame_11)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.compressed_size.setFont(font)
        self.compressed_size.setObjectName("compressed_size")
        self.horizontalLayout_6.addWidget(self.compressed_size)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.frame_11)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        self.compressed_extension = QtWidgets.QLabel(self.frame_11)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.compressed_extension.setFont(font)
        self.compressed_extension.setObjectName("compressed_extension")
        self.horizontalLayout_7.addWidget(self.compressed_extension)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.verticalLayout_17.addWidget(self.frame_11)
        self.verticalLayout_13.addWidget(self.frame_12)
        self.horizontalLayout_11.addWidget(self.widget_6)
        self.verticalLayout.addWidget(self.cardsframe)
        self.mainframe = QtWidgets.QWidget(self.rightmenu)
        self.mainframe.setObjectName("mainframe")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.mainframe)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(self.mainframe)
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.load_button = QtWidgets.QPushButton(self.widget)
        self.load_button.setObjectName("load_button")
        self.horizontalLayout_3.addWidget(self.load_button, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.compression_button = QtWidgets.QPushButton(self.widget)
        self.compression_button.setMinimumSize(QtCore.QSize(0, 0))
        self.compression_button.setObjectName("compression_button")
        self.horizontalLayout_3.addWidget(self.compression_button, 0, QtCore.Qt.AlignHCenter)

        self.reconstruction_button = QtWidgets.QPushButton(self.widget)
        self.reconstruction_button.setMinimumSize(QtCore.QSize(0, 0))
        self.reconstruction_button.setObjectName("reconstruction_button")
        self.horizontalLayout_3.addWidget(self.reconstruction_button, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addWidget(self.widget)
        self.verticalLayout.addWidget(self.mainframe)
        self.horizontalLayout.addWidget(self.rightmenu)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.menu_button.clicked.connect(self.toggle_menu)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TumorScope"))
        self.label_4.setText(_translate("MainWindow", "Main Menu"))
        self.analysis_button.setText(_translate("MainWindow", "Analysis"))
        self.compress_button.setText(_translate("MainWindow", "Compress"))
        self.appheader.setText(_translate("MainWindow", "TumorScope"))
        self.EMGlabel.setText(_translate("MainWindow", "Normal Image"))
        self.label.setText(_translate("MainWindow", "Original Size:"))
        self.label_2.setText(_translate("MainWindow", "Extension:"))
        self.normal_extension.setText(_translate("MainWindow", "PNG"))
        self.filterflex.setText(_translate("MainWindow", "Compressed Image"))
        self.label_3.setText(_translate("MainWindow", "Compressed Size:"))
        self.label_5.setText(_translate("MainWindow", "Extension:"))
        self.compressed_extension.setText(_translate("MainWindow", "Zlib"))
        self.load_button.setText(_translate("MainWindow", "Load Image"))
        self.compression_button.setText(_translate("MainWindow", "Compress"))
        self.reconstruction_button.setText(_translate("MainWindow", "Reconstruct"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Compression()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
