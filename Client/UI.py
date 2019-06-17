# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testGUI.ui',
# licensing of 'testGUI.ui' applies.
#
# Created: Sun Jun 16 23:52:22 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(888, 684)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../Desktop/Software Engineering/4th Year/Final Project/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(40, 40))
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 891, 661))
        self.tabWidget.setIconSize(QtCore.QSize(12, 12))
        self.tabWidget.setObjectName("tabWidget")
        self.ProcessImage = QtWidgets.QWidget()
        self.ProcessImage.setObjectName("ProcessImage")
        self.tabWidget.addTab(self.ProcessImage, "")
        self.DBQueries = QtWidgets.QWidget()
        self.DBQueries.setObjectName("DBQueries")
        self.Choosequery = QtWidgets.QTextEdit(self.DBQueries)
        self.Choosequery.setGeometry(QtCore.QRect(20, 20, 621, 31))
        self.Choosequery.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Choosequery.setLineWidth(0)
        self.Choosequery.setObjectName("Choosequery")
        self.queriesComboBox = QtWidgets.QComboBox(self.DBQueries)
        self.queriesComboBox.setGeometry(QtCore.QRect(650, 20, 91, 22))
        self.queriesComboBox.setObjectName("queriesComboBox")
        self.queriesComboBox.addItem("")
        self.queriesComboBox.addItem("")
        self.queriesComboBox.addItem("")
        self.activateQuery = QtWidgets.QPushButton(self.DBQueries)
        self.activateQuery.setEnabled(True)
        self.activateQuery.setGeometry(QtCore.QRect(770, 20, 56, 21))
        self.activateQuery.setMouseTracking(True)
        self.activateQuery.setObjectName("activateQuery")
        self.tabWidget.addTab(self.DBQueries, "")
        self.Records = QtWidgets.QWidget()
        self.Records.setObjectName("Records")
        self.EnterRecords = QtWidgets.QPushButton(self.Records)
        self.EnterRecords.setGeometry(QtCore.QRect(760, 30, 56, 21))
        self.EnterRecords.setObjectName("EnterRecords")
        self.RecordsTextEdit = QtWidgets.QTextEdit(self.Records)
        self.RecordsTextEdit.setGeometry(QtCore.QRect(500, 20, 221, 41))
        self.RecordsTextEdit.setFrameShape(QtWidgets.QFrame.Box)
        self.RecordsTextEdit.setObjectName("RecordsTextEdit")
        self.textBrowser = QtWidgets.QTextBrowser(self.Records)
        self.textBrowser.setGeometry(QtCore.QRect(30, 30, 461, 31))
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setObjectName("textBrowser")
        self.tabWidget.addTab(self.Records, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 888, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Eye Shield", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ProcessImage), QtWidgets.QApplication.translate("MainWindow", "Process Image", None, -1))
        self.Choosequery.setHtml(QtWidgets.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Please choose the query you would like to preform from the list:</p></body></html>", None, -1))
        self.queriesComboBox.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "Query 1", None, -1))
        self.queriesComboBox.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "Query 2", None, -1))
        self.queriesComboBox.setItemText(2, QtWidgets.QApplication.translate("MainWindow", "Query 3", None, -1))
        self.activateQuery.setText(QtWidgets.QApplication.translate("MainWindow", "Find", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DBQueries), QtWidgets.QApplication.translate("MainWindow", "DB Queries", None, -1))
        self.EnterRecords.setText(QtWidgets.QApplication.translate("MainWindow", "Enter", None, -1))
        self.textBrowser.setHtml(QtWidgets.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Please enter the case number you would like to review:</p></body></html>", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Records), QtWidgets.QApplication.translate("MainWindow", "Records", None, -1))

