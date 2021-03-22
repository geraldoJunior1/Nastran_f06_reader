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
import math
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
        self.checkBox.setGeometry(QtCore.QRect(250, 590, 70, 17))
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
        self.checkBox_2.setGeometry(QtCore.QRect(250, 610, 81, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.textEdit_45 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_45.setGeometry(QtCore.QRect(260, 650, 61, 25))
        self.textEdit_45.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_45.setObjectName("textEdit_45")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(250, 630, 91, 16))
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
        self.textEdit_46.setGeometry(QtCore.QRect(320, 560, 61, 25))
        self.textEdit_46.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_46.setObjectName("textEdit_46")
        self.textEdit_axismax_13 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_13.setGeometry(QtCore.QRect(1200, 190, 31, 25))
        self.textEdit_axismax_13.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_13.setObjectName("textEdit_axismax_13")
        self.textEdit_axismax_14 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_14.setGeometry(QtCore.QRect(1200, 220, 31, 25))
        self.textEdit_axismax_14.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_14.setObjectName("textEdit_axismax_14")
        self.textEdit_axismax_15 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_15.setGeometry(QtCore.QRect(1200, 250, 31, 25))
        self.textEdit_axismax_15.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_15.setObjectName("textEdit_axismax_15")
        self.textEdit_axismax_16 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_16.setGeometry(QtCore.QRect(1200, 280, 31, 25))
        self.textEdit_axismax_16.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_16.setObjectName("textEdit_axismax_16")
        self.textEdit_axismax_17 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_17.setGeometry(QtCore.QRect(1200, 310, 31, 25))
        self.textEdit_axismax_17.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_17.setObjectName("textEdit_axismax_17")
        self.textEdit_axismax_18 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_18.setGeometry(QtCore.QRect(1200, 340, 31, 25))
        self.textEdit_axismax_18.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_18.setObjectName("textEdit_axismax_18")
        self.textEdit_axismax_19 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_19.setGeometry(QtCore.QRect(1050, 340, 131, 25))
        self.textEdit_axismax_19.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_19.setObjectName("textEdit_axismax_19")
        self.textEdit_axismax_20 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_20.setGeometry(QtCore.QRect(1050, 310, 131, 25))
        self.textEdit_axismax_20.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_20.setObjectName("textEdit_axismax_20")
        self.textEdit_axismax_21 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_21.setGeometry(QtCore.QRect(1050, 280, 131, 25))
        self.textEdit_axismax_21.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_21.setObjectName("textEdit_axismax_21")
        self.textEdit_axismax_22 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_22.setGeometry(QtCore.QRect(1050, 250, 131, 25))
        self.textEdit_axismax_22.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_22.setObjectName("textEdit_axismax_22")
        self.textEdit_axismax_23 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_23.setGeometry(QtCore.QRect(1050, 220, 131, 25))
        self.textEdit_axismax_23.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_23.setObjectName("textEdit_axismax_23")
        self.textEdit_axismax_24 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_24.setGeometry(QtCore.QRect(1050, 190, 131, 25))
        self.textEdit_axismax_24.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_24.setObjectName("textEdit_axismax_24")
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setGeometry(QtCore.QRect(1070, 160, 111, 20))
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        self.label_31.setGeometry(QtCore.QRect(1190, 160, 51, 20))
        self.label_31.setObjectName("label_31")
        self.textEdit_axismax_25 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_25.setGeometry(QtCore.QRect(1070, 40, 161, 25))
        self.textEdit_axismax_25.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_25.setObjectName("textEdit_axismax_25")
        self.label_33 = QtWidgets.QLabel(self.centralwidget)
        self.label_33.setGeometry(QtCore.QRect(1100, 20, 111, 20))
        self.label_33.setObjectName("label_33")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(1090, 130, 121, 17))
        self.checkBox_3.setObjectName("checkBox_3")
        self.textEdit_axismax_26 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_26.setGeometry(QtCore.QRect(1050, 400, 131, 25))
        self.textEdit_axismax_26.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_26.setObjectName("textEdit_axismax_26")
        self.textEdit_axismax_27 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_27.setGeometry(QtCore.QRect(1200, 400, 31, 25))
        self.textEdit_axismax_27.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_27.setObjectName("textEdit_axismax_27")
        self.textEdit_axismax_28 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_28.setGeometry(QtCore.QRect(1200, 430, 31, 25))
        self.textEdit_axismax_28.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_28.setObjectName("textEdit_axismax_28")
        self.textEdit_axismax_29 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_29.setGeometry(QtCore.QRect(1050, 520, 131, 25))
        self.textEdit_axismax_29.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_29.setObjectName("textEdit_axismax_29")
        self.textEdit_axismax_30 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_30.setGeometry(QtCore.QRect(1050, 430, 131, 25))
        self.textEdit_axismax_30.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_30.setObjectName("textEdit_axismax_30")
        self.textEdit_axismax_31 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_31.setGeometry(QtCore.QRect(1050, 370, 131, 25))
        self.textEdit_axismax_31.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_31.setObjectName("textEdit_axismax_31")
        self.textEdit_axismax_32 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_32.setGeometry(QtCore.QRect(1050, 460, 131, 25))
        self.textEdit_axismax_32.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_32.setObjectName("textEdit_axismax_32")
        self.textEdit_axismax_33 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_33.setGeometry(QtCore.QRect(1050, 490, 131, 25))
        self.textEdit_axismax_33.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_33.setObjectName("textEdit_axismax_33")
        self.textEdit_axismax_34 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_34.setGeometry(QtCore.QRect(1200, 460, 31, 25))
        self.textEdit_axismax_34.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_34.setObjectName("textEdit_axismax_34")
        self.textEdit_axismax_35 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_35.setGeometry(QtCore.QRect(1200, 370, 31, 25))
        self.textEdit_axismax_35.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_35.setObjectName("textEdit_axismax_35")
        self.textEdit_axismax_36 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_36.setGeometry(QtCore.QRect(1200, 520, 31, 25))
        self.textEdit_axismax_36.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_36.setObjectName("textEdit_axismax_36")
        self.textEdit_axismax_37 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_37.setGeometry(QtCore.QRect(1200, 490, 31, 25))
        self.textEdit_axismax_37.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_37.setObjectName("textEdit_axismax_37")
        self.textEdit_47 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_47.setGeometry(QtCore.QRect(360, 650, 61, 25))
        self.textEdit_47.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_47.setObjectName("textEdit_47")
        self.label_32 = QtWidgets.QLabel(self.centralwidget)
        self.label_32.setGeometry(QtCore.QRect(350, 630, 91, 16))
        self.label_32.setObjectName("label_32")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(250, 560, 70, 17))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(350, 590, 70, 17))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_6.setGeometry(QtCore.QRect(350, 610, 121, 17))
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_8 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_8.setGeometry(QtCore.QRect(1090, 70, 141, 17))
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_9 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_9.setGeometry(QtCore.QRect(1030, 190, 21, 17))
        self.checkBox_9.setText("")
        self.checkBox_9.setChecked(True)
        self.checkBox_9.setObjectName("checkBox_9")
        self.checkBox_10 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_10.setGeometry(QtCore.QRect(1030, 220, 21, 17))
        self.checkBox_10.setText("")
        self.checkBox_10.setChecked(True)
        self.checkBox_10.setObjectName("checkBox_10")
        self.checkBox_11 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_11.setGeometry(QtCore.QRect(1030, 250, 21, 17))
        self.checkBox_11.setText("")
        self.checkBox_11.setChecked(True)
        self.checkBox_11.setObjectName("checkBox_11")
        self.checkBox_12 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_12.setGeometry(QtCore.QRect(1030, 280, 21, 17))
        self.checkBox_12.setText("")
        self.checkBox_12.setChecked(True)
        self.checkBox_12.setObjectName("checkBox_12")
        self.checkBox_13 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_13.setGeometry(QtCore.QRect(1030, 400, 21, 17))
        self.checkBox_13.setText("")
        self.checkBox_13.setChecked(True)
        self.checkBox_13.setObjectName("checkBox_13")
        self.checkBox_14 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_14.setGeometry(QtCore.QRect(1030, 310, 21, 17))
        self.checkBox_14.setText("")
        self.checkBox_14.setChecked(True)
        self.checkBox_14.setObjectName("checkBox_14")
        self.checkBox_15 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_15.setGeometry(QtCore.QRect(1030, 340, 21, 17))
        self.checkBox_15.setAutoFillBackground(False)
        self.checkBox_15.setText("")
        self.checkBox_15.setChecked(True)
        self.checkBox_15.setObjectName("checkBox_15")
        self.checkBox_16 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_16.setGeometry(QtCore.QRect(1030, 370, 21, 17))
        self.checkBox_16.setText("")
        self.checkBox_16.setChecked(True)
        self.checkBox_16.setObjectName("checkBox_16")
        self.checkBox_17 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_17.setGeometry(QtCore.QRect(1030, 520, 21, 17))
        self.checkBox_17.setText("")
        self.checkBox_17.setChecked(True)
        self.checkBox_17.setObjectName("checkBox_17")
        self.checkBox_18 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_18.setGeometry(QtCore.QRect(1030, 430, 21, 17))
        self.checkBox_18.setText("")
        self.checkBox_18.setChecked(True)
        self.checkBox_18.setObjectName("checkBox_18")
        self.checkBox_19 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_19.setGeometry(QtCore.QRect(1030, 460, 21, 17))
        self.checkBox_19.setText("")
        self.checkBox_19.setChecked(True)
        self.checkBox_19.setObjectName("checkBox_19")
        self.checkBox_20 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_20.setGeometry(QtCore.QRect(1030, 490, 21, 17))
        self.checkBox_20.setText("")
        self.checkBox_20.setChecked(True)
        self.checkBox_20.setObjectName("checkBox_20")
        self.checkBox_7 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_7.setGeometry(QtCore.QRect(1090, 90, 121, 17))
        self.checkBox_7.setObjectName("checkBox_7")
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setGeometry(QtCore.QRect(1030, 600, 221, 16))
        self.label_29.setObjectName("label_29")
        self.label_58 = QtWidgets.QLabel(self.centralwidget)
        self.label_58.setGeometry(QtCore.QRect(1030, 620, 201, 16))
        self.label_58.setObjectName("label_58")
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
        self.velo = 0
        self.bycases=0
        self.eff=0
        self.box1=2
        self.keas=0
        self.box2=2
        self.box3=2
        self.box4=2
        self.box5=2
        self.box6=2
        self.box7=2
        self.box8=2
        self.box9=2
        self.box10=2
        self.box11=2
        self.box12=2
        self.B = [None]*1
        self.checkBox.stateChanged.connect(lambda x:self.lig('legend',x))
        self.checkBox_2.stateChanged.connect(lambda x:self.lig('mark',x))
        self.checkBox_3.stateChanged.connect(lambda x:self.lig('diff',x))
        self.checkBox_4.stateChanged.connect(lambda x:self.lig('velo',x))
        #self.checkBox_4.stateChanged.connect(lambda x:self.lig('velo',x))
        self.checkBox_8.stateChanged.connect(lambda x:self.lig('eff',x))
        self.checkBox_9.stateChanged.connect(lambda x:self.lig('1',x))
        self.checkBox_10.stateChanged.connect(lambda x:self.lig('2',x))
        self.checkBox_11.stateChanged.connect(lambda x:self.lig('3',x))
        self.checkBox_12.stateChanged.connect(lambda x:self.lig('4',x))
        self.checkBox_13.stateChanged.connect(lambda x:self.lig('8',x))
        self.checkBox_14.stateChanged.connect(lambda x:self.lig('5',x))
        self.checkBox_15.stateChanged.connect(lambda x:self.lig('6',x))
        self.checkBox_16.stateChanged.connect(lambda x:self.lig('7',x))
        self.checkBox_17.stateChanged.connect(lambda x:self.lig('12',x))
        self.checkBox_18.stateChanged.connect(lambda x:self.lig('9',x))
        self.checkBox_19.stateChanged.connect(lambda x:self.lig('10',x))
        self.checkBox_20.stateChanged.connect(lambda x:self.lig('11',x))
        self.checkBox_6.stateChanged.connect(lambda x:self.lig('keas',x))
        
        self.checkBox_7.stateChanged.connect(lambda x:self.lig('bycases',x))        

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
        try:
            if a == 'legend':
                self.legend = x

            elif a == 'mark':
                self.mark = x

            elif a == 'velo':
                self.velo = x
            
            elif a == 'diff':
                self.mult=x
                return
            elif a == 'eff':
                self.eff=x
                return


            elif a == '1':
                self.box1=x
                return
            elif a == '2':
                self.box2 = x
                return
            elif a == '3':
                self.box3 = x
                return
            elif a == '4':
                self.box4=x
                return
            elif a == '5':
                self.box5=x
                return
            elif a == '6':
                self.box6=x
                return
            elif a == '7':
                self.box7=x
                return
            elif a == '8':
                self.box8 = x
                return
            elif a == '9':
                self.box9 = x
                return
            elif a == '10':
                self.box10=x
                return
            elif a == '11':
                self.box11=x
                return
            elif a == '12':
                self.box12=x
                return

            elif a == 'bycases':
                self.bycases=x
                return
            elif a == 'keas':
                self.keas=x
                return

            self.plot(0)
                
            return
        except:
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
        self.label_24.setText(_translate("MainWindow", "Freq ou vel - x"))
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
        self.checkBox_6.setText(_translate("MainWindow", "Velocidade em keas"))
        self.checkBox_8.setText(_translate("MainWindow", "Efetividade de comandos"))
        self.checkBox_7.setText(_translate("MainWindow", "f06 by cases"))
        self.label_29.setText(_translate("MainWindow", "Desenvolvido por: Geraldo Majella N. Junior"))
        self.label_58.setText(_translate("MainWindow", "Email de contato: thiacene@gmail.com"))



    def vec(self,to):
        try:
            self.A.append(int(to))
            self.n_mechs=self.n_mechs+1
        except:
            pass

        return
    def ploteff(self,a):

        try: self.fig.clf()
        except: pass
        self.fig_canvas = self.plot_static_canvas
        self.fig = self.fig_canvas.figure
        self.ax = self.fig.add_subplot(111)
        self.symbols = ['o', 's', 'd', '^', 'v', '*', 'P', 'h']
               
        if self.mult != 0:
            self.patchs=[]
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
            print(self.patchs)

            for i in range(len(self.patchs)):
                try:
                    
                    vel, eff = self.extracteff(self.patchs[i])
                    for j in range(len(eff)):
                        eff[j]=eff[j]*100
                    if self.mark == 0:
                        ssymbols = None
                        markk = None
                    else:
                        markk = self.ticknessMark
                        ssymbols = self.symbols[i]
                    self.ax.plot(vel, eff,marker=ssymbols, markersize=markk, linewidth=self.tickness)
                except:
                    pass

        else:

            vel, eff = self.extracteff(a)
            self.ax = self.fig.add_subplot(111)

            for i in range(len(eff)):
                eff[i]=eff[i]*100
            self.ax.plot(vel, eff, color ='black', marker='^')

        self.ax.set_title('Eficiência de comandos')
        self.ax.set_xlim(left=0,right=None)
        self.ax.set_ylim(0,100)
        self.ax.set_xlabel('Velocidade (m/s)')
        self.ax.set_ylabel('Eficiência (%)')
        self.ax.set_xlim(self.freqminX,self.freqmaxX)

        if self.velo != 0:
            self.ax.axvline(x=self.V_cert, linewidth=1.5, color='red')
        self.ax.grid()

        self.fig_canvas.draw()
        

    def extracteff(self,a):
        if True:
            path = a #./
            fileID = open(path,'r')
            tline = fileID.readline()

            l=10000000
            k=10000000
            m=10000000

            velo = []
            efetividade = []
            rigidsplined = []
            ailrigidsplined = []
            elasticunsrestrained = []
            ailelasticunsrestrained = []
            while  tline:

                a=tline

                design=a.find('    N O N - D I M E N S I O N A L   S T A B I L I T Y   A N D   C O N T R O L   D E R I V A T I V E   C O E F F I C I E N T S')
                design2=a.find('ROLL             CX')
                design3=a.find('AIL_R            CX')

                if design!=-1:
                    l=1
                else:
                    l=l+1

                if l==4:
                    point = float(a[81:95])
                    v = np.sqrt(2*point/1.08)
                    velo.append(v)

                if design2!=-1:
                    k=1
                else:
                    k=k+1

                if k==4:
                    rigido = float(a[47:60])
                    rigidsplined.append(rigido)
                    elastico = float(a[80:93])
                    elasticunsrestrained.append(elastico)

                if design3!=-1:
                    m=1
                else:
                    m=m+1

                if m==4:
                    ailrigidos = float(a[47:60])
                    ailrigidsplined.append(ailrigidos)
                    ailelastico = float(a[80:93])
                    ailelasticunsrestrained.append(ailelastico)
                    efft =  (ailelastico*rigido)/(ailrigidos*elastico)
                    efetividade.append(efft)

                tline = fileID.readline()

            fileID.close()       
            
            return velo, efetividade
            
        #except:
        #    return



    def plot(self,jj):

        try: 
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

            if self.eff !=0:
                self.ploteff(str(self.textEdit_axismax_25.toPlainText()))
                return

            if self.mult==0:
                if self.bycases==0:
                    self.vel, self.damp, self.freq, self.vel2 = self.extract(str(self.textEdit_axismax_25.toPlainText()))
                else:
                    self.vel, self.damp, self.freq, self.vel2 = self.extract2(str(self.textEdit_axismax_25.toPlainText()))
                    print('ola')

                self.n_mechs=0
                self.mode=1
                if jj ==0:
                    if self.B[0] == None:
                        self.B[0]=1
                        self.x = 1
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
                self.velao2 =[]
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
                    #for i in range(len(self.modes)):
                    if True:
                        if True:
                            try:
                                if self.box1 != 0:
                                    canolli = self.modes[0]
                                    self.modes[0] = canolli - 1
                            except:
                                pass
                            try:
                                if self.box2 != 0:
                                    canolli = self.modes[1]
                                    self.modes[1] = canolli - 1     
                            except:
                                pass
                            try:            
                                if self.box3 != 0:
                                    canolli = self.modes[2]
                                    self.modes[2] = canolli - 1
                            except:
                                pass
                            try:
                                if self.box4 != 0:
                                    canolli = self.modes[3]
                                    self.modes[3] = canolli - 1       
                            except:
                                pass
                            try:             
                                if self.box5 != 0:
                                    canolli = self.modes[4]
                                    self.modes[4] = canolli - 1
                            except:
                                pass
                            try:
                                if self.box6 != 0:
                                    canolli = self.modes[5]
                                    self.modes[5] = canolli - 1          
                            except:
                                pass
                            try:       
                                if self.box7 != 0:
                                    canolli = self.modes[6]
                                    self.modes[6] = canolli - 1
                            except:
                                pass
                            try:
                                if self.box8 != 0:
                                    canolli = self.modes[7]
                                    self.modes[7] = canolli - 1     
                            except:
                                pass
                            try:               
                                if self.box9 != 0:
                                    canolli = self.modes[8]
                                    self.modes[8] = canolli - 1
                            except:
                                pass
                            try:
                                if self.box10 != 0:
                                    canolli = self.modes[9]
                                    self.modes[9] = canolli - 1    
                            except:
                                pass
                            try:             
                                if self.box11 != 0:
                                    canolli = self.modes[10]
                                    self.modes[10] = canolli - 1
                            except:
                                pass
                            try:
                                if self.box12 != 0:
                                    canolli = self.modes[11]
                                    self.modes[11] = canolli - 1   
                            except:
                                pass               
                            else:
                                pass
                        #canolli = self.modes[i]
                        #self.modes[i] = canolli-1

                elif jj == 2:
                    if True:
                    #for i in range(len(self.modes)):
                            try:
                                if self.box1 != 0:
                                    canolli = self.modes[0]
                                    self.modes[0] = canolli + 1
                            except:
                                pass
                            try:
                                if self.box2 != 0:
                                    canolli = self.modes[1]
                                    self.modes[1] = canolli + 1          
                            except:
                                pass
                            try:       
                                if self.box3 != 0:
                                    canolli = self.modes[2]
                                    self.modes[2] = canolli + 1
                            except:
                                pass
                            try:
                                if self.box4 != 0:
                                    canolli = self.modes[3]
                                    self.modes[3] = canolli + 1      
                            except:
                                pass
                            try:              
                                if self.box5 != 0:
                                    canolli = self.modes[4]
                                    self.modes[4] = canolli + 1
                            except:
                                pass
                            try:
                                if self.box6 != 0:
                                    canolli = self.modes[5]
                                    self.modes[5] = canolli + 1    
                            except:
                                pass
                            try:             
                                if self.box7 != 0:
                                    canolli = self.modes[6]
                                    self.modes[6] = canolli + 1
                            except:
                                pass
                            try:
                                if self.box8 != 0:
                                    canolli = self.modes[7]
                                    self.modes[7] = canolli + 1        
                            except:
                                pass
                            try:            
                                if self.box9 != 0:
                                    canolli = self.modes[8]
                                    self.modes[8] = canolli + 1
                            except:
                                pass
                            try:
                                if self.box10 != 0:
                                    canolli = self.modes[9]
                                    self.modes[9] = canolli + 1      
                            except:
                                pass
                            try:           
                                if self.box11 != 0:
                                    canolli = self.modes[10]
                                    self.modes[10] = canolli + 1
                            except:
                                pass
                            try:
                                if self.box12 != 0:
                                    canolli = self.modes[11]
                                    self.modes[11] = canolli + 1                    
                            except:
                                pass
                        #canolli = self.modes[i]
                        #self.modes[i] = canolli+1
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

                ax = len(self.modes)
                self.patchs = self.patchs[:ax]
                for i in range (len(self.patchs)):
                    if self.bycases ==0:
                        self.vel, self.damp, self.freq, self.vel2 = self.extract(self.patchs[i])
                    else:
                        self.vel, self.damp, self.freq, self.vel2 = self.extract2(self.patchs[i])
                    
                    self.velao.append(self.vel)
                    self.velao2.append(self.vel2)
                    self.dampao.append(self.damp)
                    self.freqao.append(self.freq)
                    print('ooo')
            
                self.plote2()
        except:
            return

    def plote2(self):
        try:
            try: self.fig.clf()
            except: pass
            self.symbols = ['o', 's', 'd', '^', 'v', '*', 'P', 'h']
            self.frequin =[]
            self.velin = []
            self.velin2 = []
            self.sampin = []

            for i in range(len(self.patchs)):

                self.fig_canvas = self.plot_static_canvas
                self.fig = self.fig_canvas.figure
                
                self.ax = self.fig.add_subplot(211)
                self.ax2 = self.fig.add_subplot(212)
                self.velin = self.velao[i]
                self.velin2 = self.velao2[i]
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
                print(self.velin2)
                if self.keas==0:
                    self.ax.plot(self.velin[self.y+1],self.frequin[self.y+1],marker=ssymbols, markersize=markk, linewidth=self.tickness,label=(name[:-4]))
                else:
                    self.ax.plot(self.velin2[self.y+1],self.frequin[self.y+1],marker=ssymbols, markersize=markk, linewidth=self.tickness,label=(name[:-4]))

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
                self.ax2.axhline(y=0, color='black',linewidth=1)

                if self.velo != 0:
                    self.ax2.axvline(x=self.V_cert, linewidth=1.5, color='red')

                if self.keas==0:
                    self.ax2.plot(self.velin[self.y+1],self.dampin[self.y+1],marker=ssymbols, markersize=markk, linewidth=self.tickness)
                else:
                    self.ax2.plot(self.velin2[self.y+1],self.dampin[self.y+1],marker=ssymbols, markersize=markk, linewidth=self.tickness)
                self.ax2.set_xlim(self.amortminX,self.amortmaxX)
                self.ax2.set_ylim(self.amortminY,self.amortmaxY)
                if i<1:
                    self.ax2.set_position([box2.x0, box2.y0, box2.width * 0.93, box2.height])
                if self.keas==0:
                    self.ax2.set_xlabel('Velocidade (m/s)')
                else:
                    self.ax2.set_xlabel('Velocidade (keas)')
                self.ax2.set_ylabel('Amortecimento')
            self.fig_canvas.draw()
        except:
            return


    def plote(self,g):

        try:
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
            if self.bycases !=0:
                self.anao=2
            else:
                self.anao=0
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
                if self.keas == 0:
                    self.ax.plot(self.vel[self.x],self.freq[self.x],marker=ssymbols, markersize=markk, linewidth=self.tickness,label=('Mecanismo'+' '+str(self.x-1)))
                else:
                    self.ax.plot(self.vel2[self.x],self.freq[self.x],marker=ssymbols, markersize=markk, linewidth=self.tickness,label=('Mecanismo'+' '+str(self.x-1)))
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
                if self.keas == 0:
                    self.ax2.plot(self.vel[self.x],self.damp[self.x],marker=ssymbols, markersize=markk, linewidth=self.tickness)
                else:
                    self.ax2.plot(self.vel2[self.x],self.damp[self.x],marker=ssymbols, markersize=markk, linewidth=self.tickness)
                self.ax2.set_xlim(self.amortminX,self.amortmaxX)
                self.ax2.set_ylim(self.amortminY,self.amortmaxY)
                if i<1:
                    self.ax2.set_position([box2.x0, box2.y0, box2.width * 0.93, box2.height])

                if self.keas==0:
                    self.ax2.set_xlabel('Velocidade (m/s)')
                else:
                    self.ax2.set_xlabel('Velocidade (keas)')
                self.ax2.set_ylabel('Amortecimento')
                if g==1: self.x=self.x+1
                else: pass

            
            self.fig_canvas.draw()
            self.textBrowser.clear()
            if g==1: 
                self.textBrowser.append(str(self.x-2))
            else:
                self.textBrowser.append(str(self.x-1))
        except:
            return

    def extract2(self,a):

        try:
            path = a #./
            fileID = open(path,'r')
            tline = fileID.readline()
            l=10000000
            x=10000000
            alicate=1
            point=0

            vel = []
            vel2 = []
            damp = []
            freq = []

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
                    vel_point = (float(a[58:69]))
                    #vel_point = (float(a[39:52]))
                    vel_point2 = ((float(a[58:69]))*(math.sqrt(float(a[28:41])))*1.9438444924574)
                    #damp_point = (float(a[56:70]))
                    damp_point = (float(a[70:83]))
                    #freq_point = (float(a[75:90]))
                    freq_point = (float(a[86:97]))

                    try:
                        v1=vel[point-1]
                        v12=vel2[point-1]
                        d1=damp[point-1]
                        f1=freq[point-1]
                        v12.append(vel_point2)
                        v1.append(vel_point)
                        d1.append(damp_point)
                        f1.append(freq_point)
                        vel[point-1]=v1
                        vel2[point-1]=v12
                        damp[point-1]=d1
                        freq[point-1]=f1
                    except:
                        vel.append([vel_point])
                        vel2.append([vel_point2])
                        damp.append([damp_point])
                        freq.append([freq_point])

                alicate = point

                tline = fileID.readline()

            fileID.close()
            print(vel)
            print(damp)
            print(vel2)
            return vel, damp, freq, vel2

        except:
            return


    def extract(self,a):
        try:
            path = a #./
            fileID = open(path,'r')
            tline = fileID.readline()

            l=10000000
            x=10000000
            alicate=1
            point=0
            vel_point = np.zeros((36,1))
            vel_point2 = np.zeros((36,1))
            damp_point = np.zeros((36,1))
            freq_point = np.zeros((36,1))
            vel = []
            vel2=[]
            damp = []
            freq = []
            vel_point = []
            vel_point2 = []
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
                    vel_point2.append((float(a[58:69]))*math.sqrt(float(a[28:42]))*1.9438444924574)
                    damp_point.append(float(a[70:83]))
                    freq_point.append(float(a[86:97]))

                    x=x+1

                if point != alicate and x>36:

                    vel.append(vel_point)
                    vel2.append(vel_point2)
                    damp.append(damp_point)
                    freq.append(freq_point)

                    vel_point = []
                    vel_point2= []
                    damp_point = []
                    freq_point = []

                alicate = point

                tline = fileID.readline()

            fileID.close()

            return vel, damp, freq, vel2
        except:
            return

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())