# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'animal.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


#from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import os
import sys
import matplotlib.pyplot as plt
from matplotlib.backends.qt_compat import QtCore, QtWidgets, is_pyqt5

if is_pyqt5():
    from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
else:
    from matplotlib.backends.backend_qt4agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1256, 717)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_input = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_input.setGeometry(QtCore.QRect(600, 550, 121, 31))
        self.pushButton_input.setObjectName("pushButton_input")
        self.pushButton_ana = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ana.setGeometry(QtCore.QRect(740, 550, 121, 31))
        self.pushButton_ana.setObjectName("pushButton_ana")
        self.pushButton_plot = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_plot.setGeometry(QtCore.QRect(890, 550, 121, 31))
        self.pushButton_plot.setObjectName("pushButton_plot")
        self.textEdit_31 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_31.setGeometry(QtCore.QRect(110, 560, 61, 25))
        self.textEdit_31.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_31.setObjectName("textEdit_31")
        self.textEdit_41 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_41.setGeometry(QtCore.QRect(180, 560, 61, 25))
        self.textEdit_41.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_41.setObjectName("textEdit_41")
        self.textEdit_32 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_32.setGeometry(QtCore.QRect(110, 590, 61, 25))
        self.textEdit_32.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_32.setObjectName("textEdit_32")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(10, 560, 91, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(10, 590, 91, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(130, 540, 61, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(200, 540, 61, 16))
        self.label_17.setObjectName("label_17")
        self.textEdit_axismax = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax.setGeometry(QtCore.QRect(540, 590, 61, 25))
        self.textEdit_axismax.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax.setObjectName("textEdit_axismax")
        self.textEdit_axismin = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismin.setGeometry(QtCore.QRect(470, 590, 61, 25))
        self.textEdit_axismin.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismin.setObjectName("textEdit_axismin")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(260, 590, 70, 17))
        self.checkBox.setObjectName("checkBox")
        self.textEdit_axismax_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_2.setGeometry(QtCore.QRect(680, 590, 61, 25))
        self.textEdit_axismax_2.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_2.setObjectName("textEdit_axismax_2")
        self.textEdit_axismin_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismin_2.setGeometry(QtCore.QRect(610, 590, 61, 25))
        self.textEdit_axismin_2.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismin_2.setObjectName("textEdit_axismin_2")
        self.textEdit_42 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_42.setGeometry(QtCore.QRect(180, 590, 61, 25))
        self.textEdit_42.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_42.setObjectName("textEdit_42")
        self.textEdit_33 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_33.setGeometry(QtCore.QRect(110, 650, 61, 25))
        self.textEdit_33.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_33.setObjectName("textEdit_33")
        self.textEdit_43 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_43.setGeometry(QtCore.QRect(180, 620, 61, 25))
        self.textEdit_43.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_43.setObjectName("textEdit_43")
        self.textEdit_44 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_44.setGeometry(QtCore.QRect(180, 650, 61, 25))
        self.textEdit_44.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_44.setObjectName("textEdit_44")
        self.textEdit_34 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_34.setGeometry(QtCore.QRect(110, 620, 61, 25))
        self.textEdit_34.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_34.setObjectName("textEdit_34")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(30, 620, 91, 16))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(30, 650, 91, 16))
        self.label_25.setObjectName("label_25")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 1001, 511))
        self.groupBox.setObjectName("groupBox")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(540, 550, 51, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.textEdit_axismax_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_3.setGeometry(QtCore.QRect(540, 620, 61, 25))
        self.textEdit_axismax_3.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_3.setObjectName("textEdit_axismax_3")
        self.textEdit_axismax_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_4.setGeometry(QtCore.QRect(680, 620, 61, 25))
        self.textEdit_axismax_4.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_4.setObjectName("textEdit_axismax_4")
        self.textEdit_axismin_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismin_3.setGeometry(QtCore.QRect(470, 620, 61, 25))
        self.textEdit_axismin_3.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismin_3.setObjectName("textEdit_axismin_3")
        self.textEdit_axismin_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismin_4.setGeometry(QtCore.QRect(610, 620, 61, 25))
        self.textEdit_axismin_4.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismin_4.setObjectName("textEdit_axismin_4")
        self.textEdit_axismax_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_5.setGeometry(QtCore.QRect(820, 590, 61, 25))
        self.textEdit_axismax_5.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_5.setObjectName("textEdit_axismax_5")
        self.textEdit_axismax_6 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_6.setGeometry(QtCore.QRect(960, 590, 61, 25))
        self.textEdit_axismax_6.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_6.setObjectName("textEdit_axismax_6")
        self.textEdit_axismax_7 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_7.setGeometry(QtCore.QRect(960, 620, 61, 25))
        self.textEdit_axismax_7.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_7.setObjectName("textEdit_axismax_7")
        self.textEdit_axismin_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismin_5.setGeometry(QtCore.QRect(750, 590, 61, 25))
        self.textEdit_axismin_5.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismin_5.setObjectName("textEdit_axismin_5")
        self.textEdit_axismin_6 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismin_6.setGeometry(QtCore.QRect(890, 620, 61, 25))
        self.textEdit_axismin_6.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismin_6.setObjectName("textEdit_axismin_6")
        self.textEdit_axismin_7 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismin_7.setGeometry(QtCore.QRect(890, 590, 61, 25))
        self.textEdit_axismin_7.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismin_7.setObjectName("textEdit_axismin_7")
        self.textEdit_axismin_8 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismin_8.setGeometry(QtCore.QRect(750, 620, 61, 25))
        self.textEdit_axismin_8.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismin_8.setObjectName("textEdit_axismin_8")
        self.textEdit_axismax_8 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_8.setGeometry(QtCore.QRect(820, 620, 61, 25))
        self.textEdit_axismax_8.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_8.setObjectName("textEdit_axismax_8")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(260, 610, 81, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.textEdit_45 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_45.setGeometry(QtCore.QRect(270, 650, 61, 25))
        self.textEdit_45.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_45.setObjectName("textEdit_45")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(260, 630, 91, 16))
        self.label_26.setObjectName("label_26")
        self.textEdit_axismax_9 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_9.setGeometry(QtCore.QRect(680, 650, 61, 25))
        self.textEdit_axismax_9.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_9.setObjectName("textEdit_axismax_9")
        self.textEdit_axismax_10 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_10.setGeometry(QtCore.QRect(820, 650, 61, 25))
        self.textEdit_axismax_10.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_10.setObjectName("textEdit_axismax_10")
        self.textEdit_axismin_9 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismin_9.setGeometry(QtCore.QRect(890, 650, 61, 25))
        self.textEdit_axismin_9.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismin_9.setObjectName("textEdit_axismin_9")
        self.textEdit_axismin_10 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismin_10.setGeometry(QtCore.QRect(610, 650, 61, 25))
        self.textEdit_axismin_10.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismin_10.setObjectName("textEdit_axismin_10")
        self.textEdit_axismin_11 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismin_11.setGeometry(QtCore.QRect(470, 650, 61, 25))
        self.textEdit_axismin_11.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismin_11.setObjectName("textEdit_axismin_11")
        self.textEdit_axismax_11 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_11.setGeometry(QtCore.QRect(960, 650, 61, 25))
        self.textEdit_axismax_11.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_11.setObjectName("textEdit_axismax_11")
        self.textEdit_axismax_12 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_12.setGeometry(QtCore.QRect(540, 650, 61, 25))
        self.textEdit_axismax_12.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_12.setObjectName("textEdit_axismax_12")
        self.textEdit_axismin_12 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismin_12.setGeometry(QtCore.QRect(750, 650, 61, 25))
        self.textEdit_axismin_12.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismin_12.setObjectName("textEdit_axismin_12")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(420, 550, 111, 20))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(130, 520, 91, 16))
        self.label_28.setObjectName("label_28")
        self.textEdit_46 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_46.setGeometry(QtCore.QRect(330, 560, 61, 25))
        self.textEdit_46.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_46.setObjectName("textEdit_46")
        self.textEdit_axismax_13 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_13.setGeometry(QtCore.QRect(1200, 170, 31, 25))
        self.textEdit_axismax_13.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_13.setObjectName("textEdit_axismax_13")
        self.textEdit_axismax_14 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_14.setGeometry(QtCore.QRect(1200, 200, 31, 25))
        self.textEdit_axismax_14.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_14.setObjectName("textEdit_axismax_14")
        self.textEdit_axismax_15 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_15.setGeometry(QtCore.QRect(1200, 230, 31, 25))
        self.textEdit_axismax_15.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_15.setObjectName("textEdit_axismax_15")
        self.textEdit_axismax_16 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_16.setGeometry(QtCore.QRect(1200, 260, 31, 25))
        self.textEdit_axismax_16.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_16.setObjectName("textEdit_axismax_16")
        self.textEdit_axismax_17 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_17.setGeometry(QtCore.QRect(1200, 290, 31, 25))
        self.textEdit_axismax_17.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_17.setObjectName("textEdit_axismax_17")
        self.textEdit_axismax_18 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_18.setGeometry(QtCore.QRect(1200, 320, 31, 25))
        self.textEdit_axismax_18.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_18.setObjectName("textEdit_axismax_18")
        self.textEdit_axismax_19 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_19.setGeometry(QtCore.QRect(1050, 320, 131, 25))
        self.textEdit_axismax_19.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_19.setObjectName("textEdit_axismax_19")
        self.textEdit_axismax_20 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_20.setGeometry(QtCore.QRect(1050, 290, 131, 25))
        self.textEdit_axismax_20.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_20.setObjectName("textEdit_axismax_20")
        self.textEdit_axismax_21 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_21.setGeometry(QtCore.QRect(1050, 260, 131, 25))
        self.textEdit_axismax_21.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_21.setObjectName("textEdit_axismax_21")
        self.textEdit_axismax_22 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_22.setGeometry(QtCore.QRect(1050, 230, 131, 25))
        self.textEdit_axismax_22.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_22.setObjectName("textEdit_axismax_22")
        self.textEdit_axismax_23 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_23.setGeometry(QtCore.QRect(1050, 200, 131, 25))
        self.textEdit_axismax_23.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_23.setObjectName("textEdit_axismax_23")
        self.textEdit_axismax_24 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_24.setGeometry(QtCore.QRect(1050, 170, 131, 25))
        self.textEdit_axismax_24.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_24.setObjectName("textEdit_axismax_24")
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setGeometry(QtCore.QRect(1070, 140, 111, 20))
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        self.label_31.setGeometry(QtCore.QRect(1190, 140, 51, 20))
        self.label_31.setObjectName("label_31")
        self.textEdit_axismax_25 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_25.setGeometry(QtCore.QRect(1070, 40, 161, 25))
        self.textEdit_axismax_25.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_25.setObjectName("textEdit_axismax_25")
        self.label_33 = QtWidgets.QLabel(self.centralwidget)
        self.label_33.setGeometry(QtCore.QRect(1100, 20, 111, 20))
        self.label_33.setObjectName("label_33")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(1090, 100, 121, 17))
        self.checkBox_3.setObjectName("checkBox_3")
        self.textEdit_axismax_26 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_26.setGeometry(QtCore.QRect(1050, 380, 131, 25))
        self.textEdit_axismax_26.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_26.setObjectName("textEdit_axismax_26")
        self.textEdit_axismax_27 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_27.setGeometry(QtCore.QRect(1200, 380, 31, 25))
        self.textEdit_axismax_27.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_27.setObjectName("textEdit_axismax_27")
        self.textEdit_axismax_28 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_28.setGeometry(QtCore.QRect(1200, 410, 31, 25))
        self.textEdit_axismax_28.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_28.setObjectName("textEdit_axismax_28")
        self.textEdit_axismax_29 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_29.setGeometry(QtCore.QRect(1050, 500, 131, 25))
        self.textEdit_axismax_29.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_29.setObjectName("textEdit_axismax_29")
        self.textEdit_axismax_30 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_30.setGeometry(QtCore.QRect(1050, 410, 131, 25))
        self.textEdit_axismax_30.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_30.setObjectName("textEdit_axismax_30")
        self.textEdit_axismax_31 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_31.setGeometry(QtCore.QRect(1050, 350, 131, 25))
        self.textEdit_axismax_31.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_31.setObjectName("textEdit_axismax_31")
        self.textEdit_axismax_32 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_32.setGeometry(QtCore.QRect(1050, 440, 131, 25))
        self.textEdit_axismax_32.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_32.setObjectName("textEdit_axismax_32")
        self.textEdit_axismax_33 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_33.setGeometry(QtCore.QRect(1050, 470, 131, 25))
        self.textEdit_axismax_33.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_33.setObjectName("textEdit_axismax_33")
        self.textEdit_axismax_34 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_34.setGeometry(QtCore.QRect(1200, 440, 31, 25))
        self.textEdit_axismax_34.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_34.setObjectName("textEdit_axismax_34")
        self.textEdit_axismax_35 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_35.setGeometry(QtCore.QRect(1200, 350, 31, 25))
        self.textEdit_axismax_35.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_35.setObjectName("textEdit_axismax_35")
        self.textEdit_axismax_36 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_36.setGeometry(QtCore.QRect(1200, 500, 31, 25))
        self.textEdit_axismax_36.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_36.setObjectName("textEdit_axismax_36")
        self.textEdit_axismax_37 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_37.setGeometry(QtCore.QRect(1200, 470, 31, 25))
        self.textEdit_axismax_37.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_37.setObjectName("textEdit_axismax_37")
        self.textEdit_47 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_47.setGeometry(QtCore.QRect(370, 650, 61, 25))
        self.textEdit_47.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_47.setObjectName("textEdit_47")
        self.label_32 = QtWidgets.QLabel(self.centralwidget)
        self.label_32.setGeometry(QtCore.QRect(360, 630, 91, 16))
        self.label_32.setObjectName("label_32")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(260, 560, 70, 17))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(360, 590, 70, 17))
        self.checkBox_5.setObjectName("checkBox_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1256, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.plotFigLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.plot_static_canvas = FigureCanvas(Figure(figsize=(2, 3)))
        self.plotFigLayout.addWidget(self.plot_static_canvas)

        self.fig_canvas = self.plot_static_canvas
        self.fig = self.fig_canvas.figure
        self.pushButton_input.clicked.connect(lambda:self.plot(0))
        self.pushButton_ana.clicked.connect(lambda:self.plot(1))
        self.pushButton_plot.clicked.connect(lambda:self.plot(2))
        self.legend = 0
        self.mark = 0
        self.mult = 0
        self.velo = 0
        self.B = [None]*1
        self.checkBox.stateChanged.connect(lambda x:self.lig('legend',x))
        self.checkBox_2.stateChanged.connect(lambda x:self.lig('mark',x))
        self.checkBox_3.stateChanged.connect(lambda x:self.lig('diff',x))
        self.checkBox_4.stateChanged.connect(lambda x:self.lig('velo',x))

        '''
        self.textEdit_31.textChanged.connect(lambda:self.plot(0))
        self.textEdit_41.textChanged.connect(lambda:self.plot(0))
        self.textEdit_32.textChanged.connect(lambda:self.plot(0))
        self.textEdit_42.textChanged.connect(lambda:self.plot(0))
        self.textEdit_34.textChanged.connect(lambda:self.plot(0))
        self.textEdit_43.textChanged.connect(lambda:self.plot(0))
        self.textEdit_33.textChanged.connect(lambda:self.plot(0))
        self.textEdit_44.textChanged.connect(lambda:self.plot(0))
        '''
    def lig(self,a,x):
        if a == 'legend':
            self.legend = x

        elif a == 'mark':
            self.mark = x

        elif a == 'velo':
            self.velo = x
        
        elif a == 'diff':
            self.mult=x
            return

        self.plot(0)
            
        return
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_input.setText(_translate("MainWindow", "Plot"))
        self.pushButton_ana.setText(_translate("MainWindow", "Anterior"))
        self.pushButton_plot.setText(_translate("MainWindow", "Próximo"))
        self.label_14.setText(_translate("MainWindow", "Amortecimento - x"))
        self.label_15.setText(_translate("MainWindow", "Amortecimento - y"))
        self.label_16.setText(_translate("MainWindow", "Min"))
        self.label_17.setText(_translate("MainWindow", "Max"))
        self.checkBox.setText(_translate("MainWindow", "Legenda"))
        self.label_24.setText(_translate("MainWindow", "Frequência - x"))
        self.label_25.setText(_translate("MainWindow", "Frequência - y"))
        self.groupBox.setTitle(_translate("MainWindow", "Plot"))
        self.checkBox_2.setText(_translate("MainWindow", "Marcadores"))
        self.label_26.setText(_translate("MainWindow", "Espessura da linha"))
        self.label_27.setText(_translate("MainWindow", "Mecanismo de número:"))
        self.label_28.setText(_translate("MainWindow", "Eixos"))
        self.label_30.setText(_translate("MainWindow", "Nome do arquivo f06"))
        self.label_31.setText(_translate("MainWindow", "Mecanismo"))
        self.label_33.setText(_translate("MainWindow", "Nome do arquivo f06"))
        self.checkBox_3.setText(_translate("MainWindow", "Diferentes arquivos"))
        self.label_32.setText(_translate("MainWindow", "Tamanho do mark"))
        self.checkBox_4.setText(_translate("MainWindow", "Vel cert."))
        self.checkBox_5.setText(_translate("MainWindow", "fit freqs."))


    def vec(self,to):
        try:
            self.A.append(int(to))
            self.n_mechs=self.n_mechs+1
        except:
            pass

        return

    def plot(self,jj):

        if True:
            try: 
                self.amortminX = float(self.textEdit_31.toPlainText())
            except : 
                self.amortminX =0 
                self.textEdit_31.insertPlainText(str(self.amortminX))
            try: 
                self.amortmaxX = float(self.textEdit_41.toPlainText())
            except : 
                self.amortmaxX = 32
                self.textEdit_41.insertPlainText(str(self.amortmaxX))
            try: 
                self.amortminY = float(self.textEdit_32.toPlainText())
            except : 
                self.amortminY = -0.2
                self.textEdit_32.insertPlainText(str(self.amortminY))
            try: 
                self.amortmaxY = float(self.textEdit_42.toPlainText())
            except : 
                self.amortmaxY = 0.2
                self.textEdit_42.insertPlainText(str(self.amortmaxY))
            try: 
                self.freqminX = float(self.textEdit_34.toPlainText())
            except : 
                self.freqminX = 0
                self.textEdit_34.insertPlainText(str(self.freqminX))

            try: 
                self.freqmaxX = float(self.textEdit_43.toPlainText())
            except : 
                self.freqmaxX = 32
                self.textEdit_43.insertPlainText(str(self.freqmaxX))

            try: 
                self.freqminY = float(self.textEdit_33.toPlainText())
            except : 
                self.freqminY = 0
                self.textEdit_33.insertPlainText(str(self.freqminY))

            try: 
                self.freqmaxY = float(self.textEdit_44.toPlainText())
            except : 
                self.freqmaxY = 50
                self.textEdit_44.insertPlainText(str(self.freqmaxY))

            try: 
                self.V_cert = float(self.textEdit_46.toPlainText())
            except : 
                self.V_cert=27
                self.textEdit_46.insertPlainText(str(self.V_cert))

            try: 
                self.tickness = float(self.textEdit_45.toPlainText())
            except : 
                self.tickness=1
                self.textEdit_45.insertPlainText(str(self.tickness))

            try: 
                self.ticknessMark = float(self.textEdit_47.toPlainText())
            except : 
                self.ticknessMark=4.5
                self.textEdit_47.insertPlainText(str(self.ticknessMark))

        if self.mult==0:
            self.vel, self.damp, self.freq = self.extract(str(self.textEdit_axismax_25.toPlainText()))

            self.n_mechs=0
            self.mode=1
            if jj ==0:
                if self.B[0] == None:
                    self.B[0]=7
                    self.x = 7
                self.A=[]

                self.vec(self.textEdit_axismin.toPlainText())
                self.vec(self.textEdit_axismin_3.toPlainText())
                self.vec(self.textEdit_axismin_11.toPlainText())
                self.vec(self.textEdit_axismax.toPlainText())
                self.vec(self.textEdit_axismax_3.toPlainText())
                self.vec(self.textEdit_axismax_12.toPlainText())
                self.vec(self.textEdit_axismin_2.toPlainText())
                self.vec(self.textEdit_axismin_4.toPlainText())
                self.vec(self.textEdit_axismin_10.toPlainText())
                self.vec(self.textEdit_axismax_4.toPlainText())
                self.vec(self.textEdit_axismax_9.toPlainText())
                self.vec(self.textEdit_axismin_5.toPlainText())
                self.vec(self.textEdit_axismin_8.toPlainText())
                self.vec(self.textEdit_axismin_12.toPlainText())
                self.vec(self.textEdit_axismin_7.toPlainText())
                self.vec(self.textEdit_axismax_5.toPlainText())
                self.vec(self.textEdit_axismax_8.toPlainText())
                self.vec(self.textEdit_axismax_10.toPlainText())
                self.vec(self.textEdit_axismin_6.toPlainText())
                self.vec(self.textEdit_axismax_7.toPlainText())
                self.vec(self.textEdit_axismax_6.toPlainText())
                self.vec(self.textEdit_axismax_11.toPlainText())
                self.vec(self.textEdit_axismax_2.toPlainText())
                self.vec(self.textEdit_axismin_9.toPlainText())

            elif jj == 1:
                self.x = self.x-1
                self.B[0]=self.x
                self.n_mechs=1
                try:
                    #self.x=self.A[-1]-1
                    #self.B[0]=self.x
                    pass
                except:
                    pass

            elif jj == 2:
                self.x = self.x+1
                self.B[0]=self.x
                self.n_mechs=1
                try:
                    #self.x=self.A[-1]+1
                    #self.B[0]=self.x
                    pass
                except:
                    pass
            else:
                pass


            try: 
                a= int(self.A[0])
                if jj ==0:
                    g=1
                else:
                    g=2
            except:
                if jj == 0:
                    g=0
                else:
                    g=2
            self.plote(g)
        else:

            self.velao =[]
            self.dampao =[]
            self.freqao =[]
            self.patchs = []
            self.modes = []
            
            try: self.patchs.append(str(self.textEdit_axismax_24.toPlainText()))
            except: pass
            try: self.patchs.append(str(self.textEdit_axismax_23.toPlainText()))
            except: pass
            try: self.patchs.append(str(self.textEdit_axismax_22.toPlainText()))
            except: pass
            try: self.patchs.append(str(self.textEdit_axismax_21.toPlainText()))
            except: pass
            try: self.patchs.append(str(self.textEdit_axismax_20.toPlainText()))
            except: pass
            try: self.patchs.append(str(self.textEdit_axismax_19.toPlainText()))
            except: pass
            try: self.patchs.append(str(self.textEdit_axismax_31.toPlainText()))
            except: pass
            try: self.patchs.append(str(self.textEdit_axismax_26.toPlainText()))
            except: pass
            try: self.patchs.append(str(self.textEdit_axismax_30.toPlainText()))
            except: pass
            try: self.patchs.append(str(self.textEdit_axismax_32.toPlainText()))
            except: pass
            try: self.patchs.append(str(self.textEdit_axismax_33.toPlainText()))
            except: pass
            try: self.patchs.append(str(self.textEdit_axismax_29.toPlainText()))
            except: pass


            try: self.modes.append(int(self.textEdit_axismax_13.toPlainText()))
            except: pass
            try: self.modes.append(int(self.textEdit_axismax_14.toPlainText()))
            except: pass
            try: self.modes.append(int(self.textEdit_axismax_15.toPlainText()))
            except: pass
            try: self.modes.append(int(self.textEdit_axismax_16.toPlainText()))
            except: pass
            try: self.modes.append(int(self.textEdit_axismax_17.toPlainText()))
            except: pass
            try: self.modes.append(int(self.textEdit_axismax_18.toPlainText()))
            except: pass
            try: self.modes.append(int(self.textEdit_axismax_35.toPlainText()))
            except: pass
            try: self.modes.append(int(self.textEdit_axismax_27.toPlainText()))
            except: pass
            try: self.modes.append(int(self.textEdit_axismax_28.toPlainText()))
            except: pass
            try: self.modes.append(int(self.textEdit_axismax_34.toPlainText()))
            except: pass
            try: self.modes.append(int(self.textEdit_axismax_37.toPlainText()))
            except: pass
            try: self.modes.append(int(self.textEdit_axismax_36.toPlainText()))
            except: pass

            if jj == 1:
                for i in range(len(self.modes)):
                    canolli = self.modes[i]
                    self.modes[i] = canolli-1

            elif jj == 2:
                for i in range(len(self.modes)):
                    canolli = self.modes[i]
                    self.modes[i] = canolli+1
            if jj != 0:
                try: 
                    self.textEdit_axismax_13.clear()
                    self.textEdit_axismax_13.insertPlainText(str(self.modes[0]))
                except: pass
                try: 
                    self.textEdit_axismax_14.clear()
                    self.textEdit_axismax_14.insertPlainText(str(self.modes[1]))
                except: pass
                try: 
                    self.textEdit_axismax_15.clear()
                    self.textEdit_axismax_15.insertPlainText(str(self.modes[2]))
                except: pass
                try: 
                    self.textEdit_axismax_16.clear()
                    self.textEdit_axismax_16.insertPlainText(str(self.modes[3]))
                except: pass
                try: 
                    self.textEdit_axismax_17.clear()
                    self.textEdit_axismax_17.insertPlainText(str(self.modes[4]))
                except: pass
                try: 
                    self.textEdit_axismax_18.clear()
                    self.textEdit_axismax_18.insertPlainText(str(self.modes[5]))
                except: pass
                try: 
                    self.textEdit_axismax_35.clear()
                    self.textEdit_axismax_35.insertPlainText(str(self.modes[6]))
                except: pass
                try: 
                    self.textEdit_axismax_27.clear()
                    self.textEdit_axismax_27.insertPlainText(str(self.modes[7]))
                except: pass
                try: 
                    self.textEdit_axismax_28.clear()
                    self.textEdit_axismax_28.insertPlainText(str(self.modes[8]))
                except: pass
                try: 
                    self.textEdit_axismax_34.clear()
                    self.textEdit_axismax_34.insertPlainText(str(self.modes[9]))
                except: pass
                try: 
                    self.textEdit_axismax_37.clear()
                    self.textEdit_axismax_37.insertPlainText(str(self.modes[10]))
                except: pass
                try: 
                    self.textEdit_axismax_36.clear()
                    self.textEdit_axismax_36.insertPlainText(str(self.modes[11]))
                except: pass

            print (self.patchs)
            print(self.modes)
            ax = len(self.modes)
            self.patchs = self.patchs[:ax]
            for i in range (len(self.patchs)):
                self.vel, self.damp, self.freq = self.extract(self.patchs[i])

                self.velao.append(self.vel)
                self.dampao.append(self.damp)
                self.freqao.append(self.freq)

            self.plote2()

    def plote2(self):
        try: self.fig.clf()
        except: pass
        self.symbols = ['o', 's', 'd', '^', 'v', '*', 'P', 'h']
        self.frequin =[]
        self.velin = []
        self.sampin = []

        for i in range(len(self.patchs)):

            self.fig_canvas = self.plot_static_canvas
            self.fig = self.fig_canvas.figure
            
            self.ax = self.fig.add_subplot(211)
            self.ax2 = self.fig.add_subplot(212)
            self.velin = self.velao[i]
            self.dampin = self.dampao[i]
            self.frequin = self.freqao[i]
            self.y = self.modes[i]

            #self.ax.subplot(211)
            box1 = self.ax.get_position()
            if self.mark == 0:
                ssymbols = None
                markk = None
            else:
                markk = self.ticknessMark
                ssymbols = self.symbols[i]
            name = self.patchs[i]
            self.ax.plot(self.velin[7],self.frequin[self.y+1],marker=ssymbols, markersize=markk, linewidth=self.tickness,label=(name[:-4]))
            self.ax.set_xlim(self.freqminX,self.freqmaxX)
            self.ax.set_ylim(self.freqminY,self.freqmaxY)
            if i<1:
                self.ax.set_position([box1.x0, box1.y0, box1.width * 0.93, box1.height])

            #self.ax.set_xlabel('Velocidade (m/s)')
            self.ax.set_ylabel('Frequência (Hz)')
            self.ax.set_title('Diagrama v-g-f')
            
            if self.legend != 0:
                self.ax.legend(loc='upper left',fontsize = 'small', framealpha =1, bbox_to_anchor=(1.014, 1),fancybox=True)

            box2 = self.ax2.get_position()

            #self.ax.subplot(212)
            self.ax2.axhline(y=0, color='black')

            if self.velo != 0:
                self.ax2.axvline(x=self.V_cert, linewidth=1.5, color='red')

            
            self.ax2.plot(self.velin[7],self.dampin[self.y+1],marker=ssymbols, markersize=markk, linewidth=self.tickness)
            self.ax2.set_xlim(self.amortminX,self.amortmaxX)
            self.ax2.set_ylim(self.amortminY,self.amortmaxY)
            if i<1:
                self.ax2.set_position([box2.x0, box2.y0, box2.width * 0.93, box2.height])

            self.ax2.set_xlabel('Velocidade (m/s)')
            self.ax2.set_ylabel('Amortecimento')

        
        self.fig_canvas.draw()





    def plote(self,g):
        try: self.fig.clf()
        except: pass
        self.symbols = ['o', 's', 'd', '^', 'v', '*', 'P', 'h']
        if g==1: 
            self.x=self.A[0]
        elif g==0: 
            self.x = self.B[0]+1
            self.n_mechs=1
        elif g==2:
            self.n_mechs=1

        for i in range(self.n_mechs):
            if g==1: 
                self.x=self.A[i]+1
            elif g==0: self.x = self.B[0]+1
            self.fig_canvas = self.plot_static_canvas
            self.fig = self.fig_canvas.figure
            
            self.ax = self.fig.add_subplot(211)
            self.ax2 = self.fig.add_subplot(212)

            #self.ax.subplot(211)
            box1 = self.ax.get_position()
            if self.mark == 0:
                ssymbols = None
                markk = None
            else:
                markk = self.ticknessMark
                ssymbols = self.symbols[i]
            
            self.ax.plot(self.vel[7],self.freq[self.x],marker=ssymbols, markersize=markk, linewidth=self.tickness,label=('Mecanismo'+' '+str(self.x-1)))
            self.ax.set_xlim(self.freqminX,self.freqmaxX)
            self.ax.set_ylim(self.freqminY,self.freqmaxY)
            if i<1:
                self.ax.set_position([box1.x0, box1.y0, box1.width * 0.93, box1.height])

            #self.ax.set_xlabel('Velocidade (m/s)')
            self.ax.set_ylabel('Frequência (Hz)')
            self.ax.set_title('Diagrama v-g-f')
            
            if self.legend != 0:
                self.ax.legend(loc='upper left',fontsize = 'small', framealpha =1, bbox_to_anchor=(1.014, 1),fancybox=True)

            box2 = self.ax2.get_position()

            #self.ax.subplot(212)
            self.ax2.axhline(y=0, lw=0.8, color='black')

            if self.velo != 0:
                self.ax2.axvline(x=self.V_cert, linewidth=1.5, color='red')
            
            self.ax2.plot(self.vel[7],self.damp[self.x],marker=ssymbols, markersize=markk, linewidth=self.tickness)
            self.ax2.set_xlim(self.amortminX,self.amortmaxX)
            self.ax2.set_ylim(self.amortminY,self.amortmaxY)
            if i<1:
                self.ax2.set_position([box2.x0, box2.y0, box2.width * 0.93, box2.height])

            self.ax2.set_xlabel('Velocidade (m/s)')
            self.ax2.set_ylabel('Amortecimento')
            if g==1: self.x=self.x+1
            else: pass

        
        self.fig_canvas.draw()
        self.textBrowser.clear()
        if g==1: 
            self.textBrowser.append(str(self.x-2))
        else:
            self.textBrowser.append(str(self.x-1))


    def extract(self,a):
            
        path = a #./
        fileID = open(path,'r')
        tline = fileID.readline()

        l=10000000
        x=10000000
        alicate=1
        point=0
        vel_point = np.zeros((36,1))
        damp_point = np.zeros((36,1))
        freq_point = np.zeros((36,1))
        vel = []
        damp = []
        freq = []
        vel_point = []
        damp_point = []
        freq_point = []
        while  tline:

            a=tline

            design=a.find('FLUTTER  SUMMARY')

            if design!=-1:
                l=1
            else:
                l=l+1

            if l==3:
                point = int(a[17:20])

            if l==7:
                x=1

            if x<=36:
                vel_point.append(float(a[58:69]))
                damp_point.append(float(a[70:83]))
                freq_point.append(float(a[86:97]))

                x=x+1

            if point != alicate and x>36:

                vel.append(vel_point)
                damp.append(damp_point)
                freq.append(freq_point)

                vel_point = []
                damp_point = []
                freq_point = []

            alicate = point

            tline = fileID.readline()

        fileID.close()
        return vel, damp, freq

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())