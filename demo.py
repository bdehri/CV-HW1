# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import random
import cv2
import numpy as np

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(949, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(540, 50, 501, 1101))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.figure4 = Figure()
        self.figure4.clear()
        self.canvas4 = FigureCanvas(self.figure4)
        self.canvas4.setParent(self.centralwidget)
        self.canvas4.setGeometry(QtCore.QRect(540, 500, 501,200))

        self.figure5 = Figure()
        self.figure5.clear()
        self.canvas5 = FigureCanvas(self.figure5)
        self.canvas5.setParent(self.centralwidget)
        self.canvas5.setGeometry(QtCore.QRect(540, 700, 501,200))

        self.figure6 = Figure()
        self.figure6.clear()
        self.canvas6 = FigureCanvas(self.figure6)
        self.canvas6.setParent(self.centralwidget)
        self.canvas6.setGeometry(QtCore.QRect(540, 900, 501,200))

        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(40, 50, 501, 1101))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        self.figure = Figure()
        self.figure.clear()
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setParent(self.centralwidget)
        self.canvas.setGeometry(QtCore.QRect(40, 500, 501,200))

        self.figure2 = Figure()
        self.figure2.clear()
        self.canvas2 = FigureCanvas(self.figure2)
        self.canvas2.setParent(self.centralwidget)
        self.canvas2.setGeometry(QtCore.QRect(40, 700, 501,200))

        self.figure3 = Figure()
        self.figure3.clear()
        self.canvas3 = FigureCanvas(self.figure3)
        self.canvas3.setParent(self.centralwidget)
        self.canvas3.setGeometry(QtCore.QRect(40, 900, 501,200))

        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(1041, 50, 501, 1101))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 0, 151, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.handleplot)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 949, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.actionOpen_Input = QtWidgets.QAction(MainWindow)
        self.actionOpen_Input.setObjectName("actionOpen_Input")
        self.actionOpen_Input.triggered.connect(self.handleopeninput)

        self.actionOpen_Target = QtWidgets.QAction(MainWindow)
        self.actionOpen_Target.setObjectName("actionOpen_Target")
        self.actionOpen_Target.triggered.connect(self.handleopentarget)
        self.menuFile.addAction(self.actionOpen_Input)
        self.menuFile.addAction(self.actionOpen_Target)
        self.menubar.addAction(self.menuFile.menuAction())
        self.retranslateUi(MainWindow)


        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Execute Histogram"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_Input.setText(_translate("MainWindow", "Open Input"))
        self.actionOpen_Target.setText(_translate("MainWindow", "Open Target"))

    def handleopeninput(self):
        picinput = QtWidgets.QLabel(self.frame_2)
        picinput.setPixmap(QtGui.QPixmap("color2.png"))
        picinput.show()
        self.img = cv2.imread("color2.png")
        self.x_pos = [i for i in range(256)]

        self.histograminput = self.histogram(self.img)

        self.axes = self.figure.add_subplot(111)
        self.axes.bar(self.x_pos, self.histograminput[..., 0, 0], color='b')
        self.canvas.draw()

        self.axes2 = self.figure2.add_subplot(111)
        self.axes2.bar(self.x_pos, self.histograminput[..., 0, 1], color='g')
        self.canvas2.draw()

        self.axes3 = self.figure3.add_subplot(111)
        self.axes3.bar(self.x_pos, self.histograminput[..., 0, 2], color='r')
        self.canvas3.draw()
        print("click")

    def handleopentarget(self):
        pictarget = QtWidgets.QLabel(self.frame)
        pictarget.setPixmap(QtGui.QPixmap("color1.png"))
        pictarget.show()
        self.img2 = cv2.imread("color1.png")
        self.x_pos2 = [i for i in range(256)]

        self.histogramtarget = self.histogram(self.img2)

        self.axes4 = self.figure4.add_subplot(111)
        self.axes4.bar(self.x_pos2, self.histogramtarget[..., 0, 0], color='b')
        self.canvas4.draw()

        self.axes5 = self.figure5.add_subplot(111)
        self.axes5.bar(self.x_pos2, self.histogramtarget[..., 0, 1], color='g')
        self.canvas5.draw()

        self.axes6 = self.figure6.add_subplot(111)
        self.axes6.bar(self.x_pos2, self.histogramtarget[..., 0, 2], color='r')
        self.canvas6.draw()


    def histogram(self,i):
        R, C, B = i.shape
        hist = np.zeros((256, 1, B), dtype=np.uint32)

        for g in range(256):
            hist[g, 0, ...] = np.sum(np.sum(i == g, 0), 0)

        return hist


    def probdensityfunc(self,histogram, shape):
        probdensity = np.zeros((256, 1, 3), dtype=np.float32)
        probdensity = histogram / shape
        return probdensity


    def cumulativedistfuncrgb(self,probdensity):
        return np.cumsum(probdensity[..., 0, 0]), np.cumsum(probdensity[..., 0, 1]), np.cumsum(probdensity[..., 0, 2])


    def createlookuptable(self,cdfinput, cdftarget):
        lut = np.zeros((256, 1, 3), dtype=np.float32)
        gj = np.zeros(3, dtype=np.uint32)
        for gi in range(256):
            while (cdftarget[gj[0], 0, 0] < cdfinput[gi, 0, 0]) and (gj[0] < 255):
                gj[0] = gj[0] + 1
            lut[gi, 0, 0] = gj[0]

            while (cdftarget[gj[1], 0, 1] < cdfinput[gi, 0, 1]) and (gj[1] < 255):
                gj[1] = gj[1] + 1
            lut[gi, 0, 1] = gj[0]

            while (cdftarget[gj[2], 0, 2] < cdfinput[gi, 0, 2]) and (gj[2] < 255):
                gj[2] = gj[2] + 1
            lut[gi, 0, 2] = gj[2]

        return lut


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

