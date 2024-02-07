# Form implementation generated from reading ui file 'pobrepy.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt, QTimer, QTime
import vlc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        self.instance = vlc.Instance("--no-xlib")
        self.player = self.instance.media_player_new()

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(902, 682)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(30, 30, 30, 255), stop:0.36 rgba(30, 30, 30, 240), stop:0.6 rgba(30, 30, 30, 225));")
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, -10, 941, 661))
        self.widget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 255));")
        self.widget.setObjectName("widget")
        self.widget_3 = QtWidgets.QWidget(parent=self.widget)
        self.widget_3.setGeometry(QtCore.QRect(20, 140, 861, 471))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 200), stop:0.5 rgba(0, 0, 0, 200));\n"
"border-top-left-radius: 30px;\n"
"border-top-right-radius: 30px;")
        self.widget_3.setObjectName("widget_3")
        self.label_6 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_6.setGeometry(QtCore.QRect(30, 30, 121, 41))
        self.label_6.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 0), stop:0.5 rgba(0, 0, 0, 0));\n"
"font: 700 24pt \"Trebuchet MS\";")
        self.label_6.setObjectName("label_6")
        self.line = QtWidgets.QFrame(parent=self.widget_3)
        self.line.setGeometry(QtCore.QRect(30, 80, 791, 1))
        self.line.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.widget_3)
        self.scrollArea.setGeometry(QtCore.QRect(20, 100, 811, 361))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 255));")
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 811, 378))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.widget_4 = QtWidgets.QWidget(parent=self.scrollAreaWidgetContents)
        self.widget_4.setMinimumSize(QtCore.QSize(0, 55))
        self.widget_4.setMaximumSize(QtCore.QSize(16777215, 55))
        self.widget_4.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.widget_4.setObjectName("widget_4")
        self.label_16 = QtWidgets.QLabel(parent=self.widget_4)
        self.label_16.setGeometry(QtCore.QRect(60, 0, 1000, 55))
        self.label_16.setMinimumSize(QtCore.QSize(0, 55))
        self.label_16.setMaximumSize(QtCore.QSize(16777215, 55))
        self.label_16.setStyleSheet("font: 16pt \"Trebuchet MS\";\n"
"background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.label_16.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.widget_4)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 10, 35, 35))
        self.pushButton_8.setStyleSheet("border-image: url(play.png);")
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_2.addWidget(self.widget_4)
        
        self.widget_5 = QtWidgets.QWidget(parent=self.scrollAreaWidgetContents)
        self.widget_5.setMinimumSize(QtCore.QSize(0, 55))
        self.widget_5.setMaximumSize(QtCore.QSize(16777215, 55))
        self.widget_5.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.widget_5.setObjectName("widget_5")
        self.label_17 = QtWidgets.QLabel(parent=self.widget_5)
        self.label_17.setGeometry(QtCore.QRect(60, 0, 1000, 55))
        self.label_17.setMinimumSize(QtCore.QSize(0, 55))
        self.label_17.setMaximumSize(QtCore.QSize(16777215, 55))
        self.label_17.setStyleSheet("font: 16pt \"Trebuchet MS\";\n"
"background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.label_17.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.pushButton_9 = QtWidgets.QPushButton(parent=self.widget_5)
        self.pushButton_9.setGeometry(QtCore.QRect(10, 10, 35, 35))
        self.pushButton_9.setStyleSheet("border-image: url(play.png);")
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_2.addWidget(self.widget_5)
        
        self.widget_6 = QtWidgets.QWidget(parent=self.scrollAreaWidgetContents)
        self.widget_6.setMinimumSize(QtCore.QSize(0, 55))
        self.widget_6.setMaximumSize(QtCore.QSize(16777215, 55))
        self.widget_6.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.widget_6.setObjectName("widget_6")
        self.label_18 = QtWidgets.QLabel(parent=self.widget_6)
        self.label_18.setGeometry(QtCore.QRect(60, 0, 1000, 55))
        self.label_18.setMinimumSize(QtCore.QSize(0, 55))
        self.label_18.setMaximumSize(QtCore.QSize(16777215, 55))
        self.label_18.setStyleSheet("font: 16pt \"Trebuchet MS\";\n"
"background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.label_18.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.pushButton_10 = QtWidgets.QPushButton(parent=self.widget_6)
        self.pushButton_10.setGeometry(QtCore.QRect(10, 10, 35, 35))
        self.pushButton_10.setStyleSheet("border-image: url(play.png);")
        self.pushButton_10.setText("")
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_2.addWidget(self.widget_6)

        self.widget_7 = QtWidgets.QWidget(parent=self.scrollAreaWidgetContents)
        self.widget_7.setMinimumSize(QtCore.QSize(0, 55))
        self.widget_7.setMaximumSize(QtCore.QSize(16777215, 55))
        self.widget_7.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.widget_7.setObjectName("widget_7")
        self.label_19 = QtWidgets.QLabel(parent=self.widget_7)
        self.label_19.setGeometry(QtCore.QRect(60, 0, 1000, 55))
        self.label_19.setMinimumSize(QtCore.QSize(0, 55))
        self.label_19.setMaximumSize(QtCore.QSize(16777215, 55))
        self.label_19.setStyleSheet("font: 16pt \"Trebuchet MS\";\n"
"background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.label_19.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_19.setObjectName("label_19")
        self.pushButton_11 = QtWidgets.QPushButton(parent=self.widget_7)
        self.pushButton_11.setGeometry(QtCore.QRect(10, 10, 35, 35))
        self.pushButton_11.setStyleSheet("border-image: url(play.png);")
        self.pushButton_11.setText("")
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout_2.addWidget(self.widget_7)

        self.widget_8 = QtWidgets.QWidget(parent=self.scrollAreaWidgetContents)
        self.widget_8.setMinimumSize(QtCore.QSize(0, 55))
        self.widget_8.setMaximumSize(QtCore.QSize(16777215, 55))
        self.widget_8.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.widget_8.setObjectName("widget_8")
        self.label_20 = QtWidgets.QLabel(parent=self.widget_8)
        self.label_20.setGeometry(QtCore.QRect(60, 0, 1000, 55))
        self.label_20.setMinimumSize(QtCore.QSize(0, 55))
        self.label_20.setMaximumSize(QtCore.QSize(16777215, 55))
        self.label_20.setStyleSheet("font: 16pt \"Trebuchet MS\";\n"
"background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.label_20.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.pushButton_12 = QtWidgets.QPushButton(parent=self.widget_8)
        self.pushButton_12.setGeometry(QtCore.QRect(10, 10, 35, 35))
        self.pushButton_12.setStyleSheet("border-image: url(play.png);")
        self.pushButton_12.setText("")
        self.pushButton_12.setObjectName("pushButton_12")
        self.verticalLayout_2.addWidget(self.widget_8)

        self.widget_9 = QtWidgets.QWidget(parent=self.scrollAreaWidgetContents)
        self.widget_9.setMinimumSize(QtCore.QSize(0, 55))
        self.widget_9.setMaximumSize(QtCore.QSize(16777215, 55))
        self.widget_9.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.widget_9.setObjectName("widget_9")
        self.label_21 = QtWidgets.QLabel(parent=self.widget_9)
        self.label_21.setGeometry(QtCore.QRect(60, 0, 1000, 55))
        self.label_21.setMinimumSize(QtCore.QSize(0, 55))
        self.label_21.setMaximumSize(QtCore.QSize(16777215, 55))
        self.label_21.setStyleSheet("font: 16pt \"Trebuchet MS\";\n"
"background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.label_21.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.pushButton_13 = QtWidgets.QPushButton(parent=self.widget_9)
        self.pushButton_13.setGeometry(QtCore.QRect(10, 10, 35, 35))
        self.pushButton_13.setStyleSheet("border-image: url(play.png);")
        self.pushButton_13.setText("")
        self.pushButton_13.setObjectName("pushButton_13")
        self.verticalLayout_2.addWidget(self.widget_9)

        self.widget_10 = QtWidgets.QWidget(parent=self.scrollAreaWidgetContents)
        self.widget_10.setMinimumSize(QtCore.QSize(0, 55))
        self.widget_10.setMaximumSize(QtCore.QSize(16777215, 55))
        self.widget_10.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.widget_10.setObjectName("widget_10")
        self.label_22 = QtWidgets.QLabel(parent=self.widget_10)
        self.label_22.setGeometry(QtCore.QRect(60, 0, 1000, 55))
        self.label_22.setMinimumSize(QtCore.QSize(0, 55))
        self.label_22.setMaximumSize(QtCore.QSize(16777215, 55))
        self.label_22.setStyleSheet("font: 16pt \"Trebuchet MS\";\n"
"background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.label_22.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_22.setObjectName("label_22")
        self.pushButton_14 = QtWidgets.QPushButton(parent=self.widget_10)
        self.pushButton_14.setGeometry(QtCore.QRect(10, 10, 35, 35))
        self.pushButton_14.setStyleSheet("border-image: url(play.png);")
        self.pushButton_14.setText("")
        self.pushButton_14.setObjectName("pushButton_14")
        self.verticalLayout_2.addWidget(self.widget_10)
        
        self.widget_11 = QtWidgets.QWidget(parent=self.scrollAreaWidgetContents)
        self.widget_11.setMinimumSize(QtCore.QSize(0, 55))
        self.widget_11.setMaximumSize(QtCore.QSize(16777215, 55))
        self.widget_11.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.widget_11.setObjectName("widget_11")
        self.label_23 = QtWidgets.QLabel(parent=self.widget_11)
        self.label_23.setGeometry(QtCore.QRect(60, 0, 1000, 55))
        self.label_23.setMinimumSize(QtCore.QSize(0, 55))
        self.label_23.setMaximumSize(QtCore.QSize(16777215, 55))
        self.label_23.setStyleSheet("font: 16pt \"Trebuchet MS\";\n"
"background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.label_23.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_23.setObjectName("label_23")
        self.pushButton_15 = QtWidgets.QPushButton(parent=self.widget_11)
        self.pushButton_15.setGeometry(QtCore.QRect(10, 10, 35, 35))
        self.pushButton_15.setStyleSheet("border-image: url(play.png);")
        self.pushButton_15.setText("")
        self.pushButton_15.setObjectName("pushButton_15")
        self.verticalLayout_2.addWidget(self.widget_11)

        self.widget_12 = QtWidgets.QWidget(parent=self.scrollAreaWidgetContents)
        self.widget_12.setMinimumSize(QtCore.QSize(0, 55))
        self.widget_12.setMaximumSize(QtCore.QSize(16777215, 55))
        self.widget_12.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.widget_12.setObjectName("widget_12")
        self.label_24 = QtWidgets.QLabel(parent=self.widget_12)
        self.label_24.setGeometry(QtCore.QRect(60, 0, 1000, 55))
        self.label_24.setMinimumSize(QtCore.QSize(0, 55))
        self.label_24.setMaximumSize(QtCore.QSize(16777215, 55))
        self.label_24.setStyleSheet("font: 16pt \"Trebuchet MS\";\n"
"background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.label_24.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_24.setObjectName("label_24")
        self.pushButton_16 = QtWidgets.QPushButton(parent=self.widget_12)
        self.pushButton_16.setGeometry(QtCore.QRect(10, 10, 35, 35))
        self.pushButton_16.setStyleSheet("border-image: url(play.png);")
        self.pushButton_16.setText("")
        self.pushButton_16.setObjectName("pushButton_16")
        self.verticalLayout_2.addWidget(self.widget_12)
        
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setEnabled(False)
        self.label.setGeometry(QtCore.QRect(260, 0, 380, 150))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(380, 150))
        self.label.setMaximumSize(QtCore.QSize(380, 150))
        self.label.setSizeIncrement(QtCore.QSize(0, 0))
        self.label.setStyleSheet("border-image: url(nome_edited.png);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 0), stop:0.5 rgba(0, 0, 0, 0));\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")


        self.player_widget = QtWidgets.QWidget(self.centralwidget)
        self.player_widget.setGeometry(QtCore.QRect(20, 590, 861, 80))
        self.player_widget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 200), stop:0.5 rgba(0, 0, 0, 200));\n"
                                        "border-top-left-radius: 15px;\n"
                                        "border-top-right-radius: 15px;")
        self.player_widget.setObjectName("player_widget")

        # Add the QLabel for song info
        self.song_info_label = QtWidgets.QLabel(self.player_widget)
        self.song_info_label.setGeometry(QtCore.QRect(20, 40, 821, 30))
        self.song_info_label.setStyleSheet("color: white; font-size: 14pt;")
        self.song_info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.song_info_label.setObjectName("song_info_label")

        self.play_pause_button = QtWidgets.QPushButton(self.player_widget)
        self.play_pause_button.setGeometry(QtCore.QRect(10, 10, 30, 30))
        self.play_pause_button.setStyleSheet("border-image: url(play.png);")
        self.play_pause_button.setText("")
        self.play_pause_button.setObjectName("play_pause_button")
        self.play_pause_button.clicked.connect(self.toggle_play_pause)

        self.progress_bar = QtWidgets.QSlider(self.player_widget)
        self.progress_bar.setGeometry(QtCore.QRect(50, 15, 700, 20))
        self.progress_bar.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.progress_bar.setObjectName("progress_bar")

        self.timer = QTimer(self.centralwidget)
        self.timer.timeout.connect(self.update_progress_bar)


        self.total_time_label = QtWidgets.QLabel(self.player_widget)
        self.total_time_label.setGeometry(QtCore.QRect(760, 20, 80, 20))
        self.total_time_label.setStyleSheet("color: white;")
        self.total_time_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.total_time_label.setObjectName("total_time_label")

        self.current_time_label = QtWidgets.QLabel(self.player_widget)
        self.current_time_label.setGeometry(QtCore.QRect(50, 55, 80, 20))  # Updated geometry to position below the progress bar
        self.current_time_label.setStyleSheet("color: white;")
        self.current_time_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.current_time_label.setObjectName("current_time_label")

        self.progress_bar.sliderPressed.connect(self.slider_pressed)
        self.progress_bar.sliderMoved.connect(self.slider_moved)
        self.progress_bar.sliderReleased.connect(self.slider_released)
        self.progress_bar.setStyleSheet("""
         QSlider::groove:horizontal {
        border: 1px solid #7A7A7A;
        background: #d1d1d1;
        height: 10px;
        border-radius: 5px;
    }

    QSlider::handle:horizontal {
        background: #8E7CC3;
        border: 1px solid #8E7CC3;
        width: 20px;
        margin: -5px 0;
        border-radius: 10px;
    }
        """)

        self.volume_slider = QtWidgets.QSlider(self.player_widget)
        self.volume_slider.setGeometry(QtCore.QRect(760, 50, 80, 20))
        self.volume_slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.volume_slider.setObjectName("volume_slider")
        self.volume_slider.setValue(100)  # Set default volume to maximum
        self.volume_slider.setStyleSheet("""
         QSlider::groove:horizontal {
        border: 1px solid #7A7A7A;
        background: #d1d1d1;
        height: 10px;
        border-radius: 5px;
    }

    QSlider::handle:horizontal {
        background: #8E7CC3;
        border: 1px solid #8E7CC3;
        width: 20px;
        margin: -5px 0;
        border-radius: 10px;
    }
""")

        self.volume_slider.valueChanged.connect(self.set_volume)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Músicas</span></p></body></html>"))

        self.label_16.setText(_translate("MainWindow", "Welcome to London (Welcome to London) - Charlie Sparks"))
        self.pushButton_8.clicked.connect(lambda: self.play_media("http://192.168.1.84:80/music/CSWL.m3u8", "Welcome to London", "Charlie Sparks"))
        
        self.label_17.setText(_translate("MainWindow", "Smoke Signals (Stranger in the Alps) - Phoebe Bridgers", ))
        self.pushButton_9.clicked.connect(lambda: self.play_media("http://192.168.1.84:80/music/PBSS.m3u8", "Smoke Signals", "Phoebe Bridgers"))
       
        self.label_18.setText(_translate("MainWindow", "LOWKEY TWERK (CANDY22) - Otta"))
        self.pushButton_10.clicked.connect(lambda: self.play_media("http://192.168.1.84:80/music/OTTA.m3u8", "LOWKEY TWERK", "Otta"))

        self.label_19.setText(_translate("MainWindow", "Deep Jungle Walk (He.art) - Astrix"))
        self.pushButton_11.clicked.connect(lambda: self.play_media("http://192.168.1.84:80/music/AstrixDJW.m3u8", "Deep Jungle Walk (He.art)", "Astrix"))

        self.label_20.setText(_translate("MainWindow", "Trepidation (Trepidation) - Stan Christ"))
        self.pushButton_12.clicked.connect(lambda: self.play_media("http://192.168.1.84:80/music/StanCT.m3u8", "Trepidation", "Stan Christ"))

        self.label_21.setText(_translate("MainWindow", "Souvenir (boygenius) - boygenius"))
        self.pushButton_13.clicked.connect(lambda: self.play_media("http://192.168.1.84:80/music/BGSouv.m3u8", "Souvenir", "boygenius"))

        self.label_22.setText(_translate("MainWindow", "Fake Plastic Trees (The Bends) - Radiohead"))
        self.pushButton_14.clicked.connect(lambda: self.play_media("http://192.168.1.84:80/music/RHFPT.m3u8", "Fake Plastic Trees", "Radiohead"))

        self.label_23.setText(_translate("MainWindow", "Oblivion (Visions) - Grimes"))
        self.pushButton_15.clicked.connect(lambda: self.play_media("http://192.168.1.84:80/music/Music2.m3u8", "Oblivion", "Grimes"))

        self.label_24.setText(_translate("MainWindow", "Harness Your Hopes (Brighten the Corners) - Pavement"))
        self.pushButton_16.clicked.connect(lambda: self.play_media("http://192.168.1.84:80/music/este.m3u8", "Harness Your Hopes", "Pavement"))

    def toggle_play_pause(self):
        if self.player.is_playing():
                self.player.pause()
                self.play_pause_button.setStyleSheet("border-image: url(play.png);")
                self.timer.stop()
        else:
                self.player.play()
                self.play_pause_button.setStyleSheet("border-image: url(pause.png);")
                self.timer.start(1000)  # Update every second   

    def play_media(self, media_path, song_name, artist_name):
        media = self.instance.media_new(media_path)
        self.player.set_media(media)

        # Set the initial volume (you can adjust this value as needed)
        initial_volume = 80
        self.player.audio_set_volume(initial_volume)
        self.volume_slider.setValue(initial_volume)

        self.player.play()

        def set_total_time():
                total_time = self.player.get_length()
                if total_time > 0:
                        self.total_time_label.setText(self.format_time(total_time))
                        self.timer.start(1000)  # Update every second

                # Set song name and artist
                self.song_info_label.setText(f"{song_name} - {artist_name}")

                # Update play/pause button
                self.play_pause_button.setStyleSheet("border-image: url(pause.png);")

        # Use a single shot timer to delay setting total time
        QTimer.singleShot(1000, set_total_time)

    def set_volume(self, value):
        volume = int(value)
        self.player.audio_set_volume(volume)

    def update_progress_bar(self):
        if self.player.get_length() > 0:
            position = self.player.get_time()
            duration = self.player.get_length()
            progress = int((position / duration) * 100)
            self.progress_bar.setValue(progress)

            # Update current time label
            self.current_time_label.setText(self.format_time(position))
    
    def format_time(self, milliseconds):
        time = QTime(0, 0)
        time = time.addMSecs(milliseconds)
        return time.toString("mm:ss")
   
    def slider_released(self):
        self.player.pause()
        self.timer.start(1000)

    def slider_moved(self):
        # Seek to the position corresponding to the slider value
        duration = self.player.get_length() #retrive percentage 
        position = int((self.progress_bar.value() / 100) * duration) #retrive position (dividir por 100 para dar o valor da percentagem de [0,1])
        self.player.set_time(position) 

        # Update current time label while moving the slider
        self.current_time_label.setText(self.format_time(position))

    def slider_pressed(self):
        # Pause playback when slider is pressed
        self.player.pause()
        self.timer.stop()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
