# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testGUI.ui',
# licensing of 'testGUI.ui' applies.
#
# Created: Tue Jul 23 13:04:44 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1300, 948)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1300, 948))
        MainWindow.setMaximumSize(QtCore.QSize(1300, 948))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../Desktop/Software Engineering/4th Year/Final Project/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(40, 40))
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(1200, 900))
        self.tabWidget.setMaximumSize(QtCore.QSize(1200, 900))
        self.tabWidget.setIconSize(QtCore.QSize(12, 12))
        self.tabWidget.setObjectName("tabWidget")
        self.ProcessImage = QtWidgets.QWidget()
        self.ProcessImage.setObjectName("ProcessImage")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.ProcessImage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.ProcessImage)
        self.frame.setMinimumSize(QtCore.QSize(1150, 850))
        self.frame.setMaximumSize(QtCore.QSize(1150, 850))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.treeView = QtWidgets.QTreeView(self.frame)
        self.treeView.setGeometry(QtCore.QRect(-5, -9, 1150, 850))
        self.treeView.setMinimumSize(QtCore.QSize(1150, 850))
        self.treeView.setMaximumSize(QtCore.QSize(1150, 850))
        self.treeView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.treeView.setObjectName("treeView")
        self.verticalLayout.addWidget(self.frame)
        self.tabWidget.addTab(self.ProcessImage, "")
        self.AddNewCase = QtWidgets.QWidget()
        self.AddNewCase.setObjectName("AddNewCase")
        self.Choosequery = QtWidgets.QTextEdit(self.AddNewCase)
        self.Choosequery.setGeometry(QtCore.QRect(20, 20, 1161, 41))
        self.Choosequery.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Choosequery.setLineWidth(0)
        self.Choosequery.setObjectName("Choosequery")
        self.activateQuery = QtWidgets.QPushButton(self.AddNewCase)
        self.activateQuery.setEnabled(True)
        self.activateQuery.setGeometry(QtCore.QRect(850, 740, 161, 51))
        self.activateQuery.setMouseTracking(True)
        self.activateQuery.setObjectName("activateQuery")
        self.NameTextEdit = QtWidgets.QTextEdit(self.AddNewCase)
        self.NameTextEdit.setGeometry(QtCore.QRect(430, 90, 231, 31))
        self.NameTextEdit.setObjectName("NameTextEdit")
        self.CaseIDTextEdit = QtWidgets.QTextEdit(self.AddNewCase)
        self.CaseIDTextEdit.setGeometry(QtCore.QRect(430, 170, 231, 31))
        self.CaseIDTextEdit.setObjectName("CaseIDTextEdit")
        self.SusTextEdit = QtWidgets.QTextEdit(self.AddNewCase)
        self.SusTextEdit.setGeometry(QtCore.QRect(430, 250, 231, 31))
        self.SusTextEdit.setObjectName("SusTextEdit")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.AddNewCase)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 90, 301, 41))
        self.textBrowser_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.AddNewCase)
        self.textBrowser_3.setGeometry(QtCore.QRect(10, 170, 301, 41))
        self.textBrowser_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.AddNewCase)
        self.textBrowser_4.setGeometry(QtCore.QRect(10, 250, 301, 41))
        self.textBrowser_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.tabWidget.addTab(self.AddNewCase, "")
        self.Records = QtWidgets.QWidget()
        self.Records.setObjectName("Records")
        self.EnterRecords = QtWidgets.QPushButton(self.Records)
        self.EnterRecords.setGeometry(QtCore.QRect(780, 30, 56, 21))
        self.EnterRecords.setObjectName("EnterRecords")
        self.RecordsTextEdit = QtWidgets.QTextEdit(self.Records)
        self.RecordsTextEdit.setGeometry(QtCore.QRect(500, 20, 221, 41))
        self.RecordsTextEdit.setFrameShape(QtWidgets.QFrame.Box)
        self.RecordsTextEdit.setObjectName("RecordsTextEdit")
        self.textBrowser = QtWidgets.QTextBrowser(self.Records)
        self.textBrowser.setGeometry(QtCore.QRect(30, 30, 461, 31))
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setObjectName("textBrowser")
        self.caseDetails = QtWidgets.QTextBrowser(self.Records)
        self.caseDetails.setGeometry(QtCore.QRect(25, 110, 1141, 221))
        self.caseDetails.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.caseDetails.setObjectName("caseDetails")
        self.frame_2 = QtWidgets.QFrame(self.Records)
        self.frame_2.setGeometry(QtCore.QRect(-1, 329, 1201, 551))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.treeViewRecords = QtWidgets.QTreeView(self.frame_2)
        self.treeViewRecords.setGeometry(QtCore.QRect(25, 1, 1141, 541))
        self.treeViewRecords.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.treeViewRecords.setObjectName("treeViewRecords")
        self.tabWidget.addTab(self.Records, "")
        self.ForReview = QtWidgets.QWidget()
        self.ForReview.setObjectName("ForReview")
        self.refresh = QtWidgets.QPushButton(self.ForReview)
        self.refresh.setGeometry(QtCore.QRect(500, 10, 261, 41))
        self.refresh.setObjectName("refresh")
        self.frame_3 = QtWidgets.QFrame(self.ForReview)
        self.frame_3.setGeometry(QtCore.QRect(-1, 70, 1191, 811))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.treeViewForReview = QtWidgets.QTreeView(self.frame_3)
        self.treeViewForReview.setGeometry(QtCore.QRect(5, 0, 1191, 811))
        self.treeViewForReview.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.treeViewForReview.setObjectName("treeViewForReview")
        self.tabWidget.addTab(self.ForReview, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1300, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Eye Shield", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ProcessImage), QtWidgets.QApplication.translate("MainWindow", "Process Image", None, -1))
        self.Choosequery.setHtml(QtWidgets.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">Add new case:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt; font-weight:600;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None, -1))
        self.activateQuery.setText(QtWidgets.QApplication.translate("MainWindow", "Submit", None, -1))
        self.textBrowser_2.setHtml(QtWidgets.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Enter Case Name:</span></p></body></html>", None, -1))
        self.textBrowser_3.setHtml(QtWidgets.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Enter Case ID:</span></p></body></html>", None, -1))
        self.textBrowser_4.setHtml(QtWidgets.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Enter Suspects ID\'s:</span></p></body></html>", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.AddNewCase), QtWidgets.QApplication.translate("MainWindow", "Add New Case", None, -1))
        self.EnterRecords.setText(QtWidgets.QApplication.translate("MainWindow", "Enter", None, -1))
        self.textBrowser.setHtml(QtWidgets.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Please enter the case number you would like to review:</p></body></html>", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Records), QtWidgets.QApplication.translate("MainWindow", "Records", None, -1))
        self.refresh.setText(QtWidgets.QApplication.translate("MainWindow", "Refresh", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ForReview), QtWidgets.QApplication.translate("MainWindow", "For Review", None, -1))

