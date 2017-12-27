# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'botgui.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!
import FarmBot
from FarmBot import Bot
import webbrowser
import sys
import shutil
import os
import subprocess
from time import sleep
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5 import QtCore, QtGui
from os import _exit, startfile
from psutil import process_iter
import threading




bot = Bot()
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(478, 372)
        Dialog.setMaximumSize(QtCore.QSize(480, 372))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pubg2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setAutoFillBackground(False)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(-10, 0, 491, 381))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("background-color: rgb(138, 138, 138);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.Start = QtWidgets.QPushButton(self.tab)
        self.Start.setGeometry(QtCore.QRect(130, 260, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.Start.setFont(font)
        self.Start.setIconSize(QtCore.QSize(16, 16))
        self.Start.setObjectName("Start")
        self.Start.clicked.connect(self.start_bot)
        self.stop = QtWidgets.QPushButton(self.tab)
        self.stop.setEnabled(True)
        self.stop.setGeometry(QtCore.QRect(350, 270, 101, 31))
        self.stop.setObjectName("stop")
        self.stop.clicked.connect(self.closeIt)
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setGeometry(QtCore.QRect(90, 130, 291, 101))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.teneighty = QtWidgets.QRadioButton(self.frame)
        self.teneighty.setGeometry(QtCore.QRect(30, 20, 101, 17))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(10)
        self.teneighty.setFont(font)
        self.teneighty.setObjectName("teneighty")
        self.teneighty.clicked.connect(lambda: self.set_res('1080'))
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_2.setGeometry(QtCore.QRect(170, 20, 111, 17))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(10)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.clicked.connect(lambda: self.set_res('1440'))
        self.radioButton_3 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_3.setGeometry(QtCore.QRect(30, 70, 91, 17))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(10)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_3.clicked.connect(lambda: self.set_res('720'))
        self.radioButton_4 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_4.setGeometry(QtCore.QRect(170, 70, 111, 17))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(10)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_4.setEnabled(True)
        self.radioButton_4.clicked.connect(lambda: self.set_res('w1440'))
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(50, 70, 391, 41))
        font = QtGui.QFont()
        font.setFamily("Lithos Pro Regular")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(210, 10, 61, 61))
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.joindiscord = QtWidgets.QPushButton(self.tab_2)
        self.joindiscord.setGeometry(QtCore.QRect(70, 260, 331, 61))
        self.joindiscord.setObjectName("joindiscord")
        self.joindiscord.clicked.connect(lambda: webbrowser.open("https://discord.gg/vQxmu8S"))        
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 441, 231))
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setGeometry(QtCore.QRect(10, 0, 471, 341))
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.tabWidget.addTab(self.tab_3, "")
        self.PROCNAME = "TslGame.exe"        

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def start_bot(self):
        thr = threading.Thread(target=bot.run)
        thr.start()
        #bot.run()
    
    def closeIt(self):
        for proc in process_iter():
            # check whether the process name matches
            if proc.name() == self.PROCNAME:
                proc.kill()
                _exit(1)
        QCoreApplication.instance().quit
    
    
    def set_res(self, res):
        if res.strip() is '1440':
            bot.setConfig(res.strip())
        elif res.strip() is '1080':
            bot.setConfig(res.strip())
        elif res.strip() is '720':
            bot.setConfig(res.strip())
        elif res.strip() is 'w1440':
            bot.setConfig(res.strip())
        else:
            bot.setConfig('1080')

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "PUBG BP Farmer"))
        self.Start.setText(_translate("Dialog", "Start!"))
        self.stop.setText(_translate("Dialog", "Stop"))
        self.teneighty.setText(_translate("Dialog", "1920x1080p"))
        self.radioButton_2.setText(_translate("Dialog", "2560x1440p"))
        self.radioButton_3.setText(_translate("Dialog", "1366x768p"))
        self.radioButton_4.setText(_translate("Dialog", "1680x1050"))
        self.label.setText(_translate("Dialog", "PUBG Battlepoint Farmer"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><img src=\"pubg2.png\"/></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Bot"))
        self.joindiscord.setText(_translate("Dialog", "Need Help/updates? Join the Discord!"))
        self.label_3.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:13pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:16px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji,Segoe UI Symbol\'; font-size:10pt; font-weight:400; color:#24292e;\">if the bot is not doing anything try:</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji,Segoe UI Symbol\'; font-size:10pt; font-weight:400; color:#24292e;\" style=\" margin-top:16px; margin-bottom:16px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Making sure reshade or any other color changers is turned off</li>\n"
"<li style=\" font-family:\'-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji,Segoe UI Symbol\'; font-size:10pt; font-weight:400; color:#24292e;\" style=\" margin-top:16px; margin-bottom:16px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Making sure your screen and game resolution matches the resolution you selected</li>\n"
"<li style=\" font-family:\'-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji,Segoe UI Symbol\'; font-size:10pt; font-weight:400; color:#24292e;\" style=\" margin-top:16px; margin-bottom:16px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Making sure you are running the game in fullscreen windowed</li>\n"
"<li style=\" font-family:\'-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji,Segoe UI Symbol\'; font-size:10pt; font-weight:400; color:#24292e;\" style=\" margin-top:16px; margin-bottom:16px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">if its crashing, make sure to close the game before starting the bot, the bot will open the game for you!</li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:16px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji,Segoe UI Symbol\'; font-size:10pt; font-weight:400; color:#24292e;\">if you need more assistance ping me in the discord</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Help"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:9pt;\">* Auto Jumps at random point</span></p><p><span style=\" font-size:9pt;\">*Auto runs </span></p><p><span style=\" font-size:9pt;\">* Lays down and prevents drowning</span></p><p><span style=\" font-size:9pt;\">*Exit game when it passes AFK Timer</span></p><p>Future: </p><p><span style=\" font-size:9pt;\">Auto fighting afk players so you can leave earlier(I have an idea of how to do it but it will be more long term)</span></p><p><span style=\" font-size:9pt;\">Selecting the server </span></p><p><span style=\" font-size:9pt;\">Selecting the random jump time</span></p><p><br/><span style=\" font-size:9pt;\">Getting the quit button to work again(lol I swear it used to work)</span></p><p><span style=\" font-size:9pt;\">Donate:</span></p><p><span style=\" font-size:9pt;\">Bitcoin address : 16mCfoqBuvymgVVktCAPp1W6HNL3zoMiFq</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Features"))

#import pubgimage_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

