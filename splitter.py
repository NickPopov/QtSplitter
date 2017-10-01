# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'splitter.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(545, 337)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(545, 337))
        MainWindow.setMaximumSize(QtCore.QSize(545, 337))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.listWidgetKnow = QtWidgets.QListWidget(self.centralwidget)
        self.listWidgetKnow.setGeometry(QtCore.QRect(30, 50, 161, 192))
        self.listWidgetKnow.setObjectName("listWidgetKnow")

        self.listWidgetLearn = QtWidgets.QListWidget(self.centralwidget)
        self.listWidgetLearn.setGeometry(QtCore.QRect(350, 50, 161, 192))
        self.listWidgetLearn.setObjectName("listWidgetLearn")

        self.btnLern = QtWidgets.QPushButton(self.centralwidget)
        self.btnLern.setGeometry(QtCore.QRect(230, 80, 75, 23))
        self.btnLern.setObjectName("btnLern")

        self.btnKnow = QtWidgets.QPushButton(self.centralwidget)
        self.btnKnow.setGeometry(QtCore.QRect(230, 140, 75, 23))
        self.btnKnow.setObjectName("btnKnow")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 545, 21))
        self.menubar.setObjectName("menubar")
        self.menuOpen = QtWidgets.QMenu(self.menubar)
        self.menuOpen.setObjectName("menuOpen")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")

        self.menuOpen.addAction(self.actionOpen)
        self.menubar.addAction(self.menuOpen.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Splitter"))
        self.btnLern.setText(_translate("MainWindow", "--->"))
        self.btnKnow.setText(_translate("MainWindow", "<---"))
        self.menuOpen.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setStatusTip(_translate("MainWindow", "Open file"))

