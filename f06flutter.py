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
        MainWindow.resize(926, 729)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_input = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_input.setGeometry(QtCore.QRect(490, 550, 121, 31))
        self.pushButton_input.setObjectName("pushButton_input")
        self.pushButton_ana = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ana.setGeometry(QtCore.QRect(630, 550, 121, 31))
        self.pushButton_ana.setObjectName("pushButton_ana")
        self.pushButton_plot = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_plot.setGeometry(QtCore.QRect(780, 550, 121, 31))
        self.pushButton_plot.setObjectName("pushButton_plot")
        self.textEdit_31 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_31.setGeometry(QtCore.QRect(110, 570, 61, 25))
        self.textEdit_31.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_31.setObjectName("textEdit_31")
        self.textEdit_41 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_41.setGeometry(QtCore.QRect(180, 570, 61, 25))
        self.textEdit_41.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_41.setObjectName("textEdit_41")
        self.textEdit_32 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_32.setGeometry(QtCore.QRect(110, 600, 61, 25))
        self.textEdit_32.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_32.setObjectName("textEdit_32")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(10, 570, 91, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(10, 600, 91, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(130, 550, 61, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(200, 550, 61, 16))
        self.label_17.setObjectName("label_17")
        self.textEdit_axismax = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax.setGeometry(QtCore.QRect(430, 590, 61, 25))
        self.textEdit_axismax.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax.setObjectName("textEdit_axismax")
        self.textEdit_axismin = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismin.setGeometry(QtCore.QRect(360, 590, 61, 25))
        self.textEdit_axismin.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismin.setObjectName("textEdit_axismin")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(260, 590, 70, 17))
        self.checkBox.setObjectName("checkBox")
        self.textEdit_axismax_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_2.setGeometry(QtCore.QRect(570, 590, 61, 25))
        self.textEdit_axismax_2.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_2.setObjectName("textEdit_axismax_2")
        self.textEdit_axismin_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismin_2.setGeometry(QtCore.QRect(500, 590, 61, 25))
        self.textEdit_axismin_2.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismin_2.setObjectName("textEdit_axismin_2")
        self.textEdit_42 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_42.setGeometry(QtCore.QRect(180, 600, 61, 25))
        self.textEdit_42.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_42.setObjectName("textEdit_42")
        self.textEdit_33 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_33.setGeometry(QtCore.QRect(110, 660, 61, 25))
        self.textEdit_33.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_33.setObjectName("textEdit_33")
        self.textEdit_43 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_43.setGeometry(QtCore.QRect(180, 630, 61, 25))
        self.textEdit_43.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_43.setObjectName("textEdit_43")
        self.textEdit_44 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_44.setGeometry(QtCore.QRect(180, 660, 61, 25))
        self.textEdit_44.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_44.setObjectName("textEdit_44")
        self.textEdit_34 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_34.setGeometry(QtCore.QRect(110, 630, 61, 25))
        self.textEdit_34.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_34.setObjectName("textEdit_34")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(30, 630, 91, 16))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(30, 660, 91, 16))
        self.label_25.setObjectName("label_25")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 891, 511))
        self.groupBox.setObjectName("groupBox")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(430, 550, 51, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.textEdit_axismax_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_3.setGeometry(QtCore.QRect(430, 620, 61, 25))
        self.textEdit_axismax_3.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_3.setObjectName("textEdit_axismax_3")
        self.textEdit_axismax_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_4.setGeometry(QtCore.QRect(570, 620, 61, 25))
        self.textEdit_axismax_4.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_4.setObjectName("textEdit_axismax_4")
        self.textEdit_axismin_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismin_3.setGeometry(QtCore.QRect(360, 620, 61, 25))
        self.textEdit_axismin_3.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismin_3.setObjectName("textEdit_axismin_3")
        self.textEdit_axismin_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismin_4.setGeometry(QtCore.QRect(500, 620, 61, 25))
        self.textEdit_axismin_4.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismin_4.setObjectName("textEdit_axismin_4")
        self.textEdit_axismax_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_5.setGeometry(QtCore.QRect(710, 590, 61, 25))
        self.textEdit_axismax_5.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_5.setObjectName("textEdit_axismax_5")
        self.textEdit_axismax_6 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_6.setGeometry(QtCore.QRect(850, 590, 61, 25))
        self.textEdit_axismax_6.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_6.setObjectName("textEdit_axismax_6")
        self.textEdit_axismax_7 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_7.setGeometry(QtCore.QRect(850, 620, 61, 25))
        self.textEdit_axismax_7.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_7.setObjectName("textEdit_axismax_7")
        self.textEdit_axismin_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismin_5.setGeometry(QtCore.QRect(640, 590, 61, 25))
        self.textEdit_axismin_5.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismin_5.setObjectName("textEdit_axismin_5")
        self.textEdit_axismin_6 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismin_6.setGeometry(QtCore.QRect(780, 620, 61, 25))
        self.textEdit_axismin_6.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismin_6.setObjectName("textEdit_axismin_6")
        self.textEdit_axismin_7 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismin_7.setGeometry(QtCore.QRect(780, 590, 61, 25))
        self.textEdit_axismin_7.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismin_7.setObjectName("textEdit_axismin_7")
        self.textEdit_axismin_8 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismin_8.setGeometry(QtCore.QRect(640, 620, 61, 25))
        self.textEdit_axismin_8.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismin_8.setObjectName("textEdit_axismin_8")
        self.textEdit_axismax_8 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_8.setGeometry(QtCore.QRect(710, 620, 61, 25))
        self.textEdit_axismax_8.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_8.setObjectName("textEdit_axismax_8")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(260, 610, 81, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.textEdit_45 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_45.setGeometry(QtCore.QRect(270, 660, 61, 25))
        self.textEdit_45.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_45.setObjectName("textEdit_45")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(260, 640, 91, 16))
        self.label_26.setObjectName("label_26")
        self.textEdit_axismax_9 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_9.setGeometry(QtCore.QRect(570, 650, 61, 25))
        self.textEdit_axismax_9.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_9.setObjectName("textEdit_axismax_9")
        self.textEdit_axismax_10 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_10.setGeometry(QtCore.QRect(710, 650, 61, 25))
        self.textEdit_axismax_10.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_10.setObjectName("textEdit_axismax_10")
        self.textEdit_axismin_9 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismin_9.setGeometry(QtCore.QRect(780, 650, 61, 25))
        self.textEdit_axismin_9.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismin_9.setObjectName("textEdit_axismin_9")
        self.textEdit_axismin_10 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismin_10.setGeometry(QtCore.QRect(500, 650, 61, 25))
        self.textEdit_axismin_10.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismin_10.setObjectName("textEdit_axismin_10")
        self.textEdit_axismin_11 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismin_11.setGeometry(QtCore.QRect(360, 650, 61, 25))
        self.textEdit_axismin_11.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismin_11.setObjectName("textEdit_axismin_11")
        self.textEdit_axismax_11 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_11.setGeometry(QtCore.QRect(850, 650, 61, 25))
        self.textEdit_axismax_11.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_11.setObjectName("textEdit_axismax_11")
        self.textEdit_axismax_12 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_12.setGeometry(QtCore.QRect(430, 650, 61, 25))
        self.textEdit_axismax_12.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_12.setObjectName("textEdit_axismax_12")
        self.textEdit_axismin_12 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismin_12.setGeometry(QtCore.QRect(640, 650, 61, 25))
        self.textEdit_axismin_12.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismin_12.setObjectName("textEdit_axismin_12")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(340, 560, 91, 16))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(130, 530, 91, 16))
        self.label_28.setObjectName("label_28")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 926, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.plotFigLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.plot_static_canvas = FigureCanvas(Figure(figsize=(2, 2)))
        self.plotFigLayout.addWidget(self.plot_static_canvas)

        self.vel, self.damp, self.freq = self.extract('1')

        self.fig_canvas = self.plot_static_canvas
        self.fig = self.fig_canvas.figure
        self.pushButton_input.clicked.connect(lambda:self.plot())
        self.pushButton_ana.clicked.connect(lambda:self.plot())
        self.pushButton_plot.clicked.connect(lambda:self.plot())

        self.checkBox.stateChanged.connect(lambda:self.plot())
        self.checkBox.stateChanged.connect(lambda:self.plot())

        self.textEdit_31.textChanged.connect(lambda:self.plot())
        self.textEdit_41.textChanged.connect(lambda:self.plot())
        self.textEdit_32.textChanged.connect(lambda:self.plot())
        self.textEdit_42.textChanged.connect(lambda:self.plot())
        self.textEdit_34.textChanged.connect(lambda:self.plot())
        self.textEdit_43.textChanged.connect(lambda:self.plot())
        self.textEdit_33.textChanged.connect(lambda:self.plot())
        self.textEdit_44.textChanged.connect(lambda:self.plot())


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
        self.label_27.setText(_translate("MainWindow", "Modo de número:"))
        self.label_28.setText(_translate("MainWindow", "Eixos"))


    def vec(self,to):
        try:
            self.A.append(int(to))
            self.n_mechs=self.n_mechs+1
        except:
            pass

        return

    def plot(self):
        self.n_mechs=0
        self.A=[]
        self.mode=1
        
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


        print(self.A)
        print(self.n_mechs)
        if self.A[2]
            self.plote(1)
        else
            self.plote(0)


    def plote(self,g):
        try: self.fig.clf()
        except: pass
        for i in range(self.n_mechs):
            if g==1: self.A[i]
            else: pass
            self.fig_canvas = self.plot_static_canvas
            self.fig = self.fig_canvas.figure
            
            self.ax = self.fig.add_subplot(111)

            self.ax.subplot(211)
            self.ax.plot(self.vel[7],self.freq[x],marker=self.symbols[i], markersize=4.5, linewidth=1)
            self.ax.set_xlim(0,40)
            #self.ax.set_ylim(-0.5,0.5)

            self.ax.set_xlabel('Velocidade (m/s)')
            self.ax.set_ylabel('Frequência (Hz)')


            self.ax.subplot(212)
            self.ax.axhline(y=0, color='black')
            self.ax.axvline(x=32, linewidth=1.5, color='red')
            self.ax.plot(self.vel[7],self.damp[x],marker=self.symbols[i], markersize=4.5, linewidth=1)
            self.ax.set_xlim(0,40)
            self.ax.set_ylim(-0.5,0.5)
            
            self.ax.set_xlabel('Velocidade (m/s)')
            self.ax.set_ylabel('Amortecimento')
            if g==1: x=x+1
            else: pass
        self.fig_canvas.draw()
        self.textBrowser.append(x)

    def extract(self,a):
            
        path =  'teste.f06' #./
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