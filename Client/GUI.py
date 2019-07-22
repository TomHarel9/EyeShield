import os
import sys

import cv2
from BI.Case import Case
from BI.Suspect import Suspect
from DAL.MongoHelper import DbHelper

os.environ['QT_API'] = "pyside2"
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2 import QtGui, QtWidgets, QtCore

from Client import UI
from VideoLayer import FaceRecognitionTester


class GUI(UI.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        self.DHL = DbHelper()
        super(GUI, self).__init__()
        self.dialog = UI.Ui_MainWindow()
        self.dialog.setupUi(self)
        self.dialog.activateQuery.clicked.connect(self.addNewCase)
        self.dialog.EnterRecords.clicked.connect(self.RecordsTab)
        self.dialog.refresh.clicked.connect(self.forReview)
        self.dialog.treeView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.dialog.treeView.customContextMenuRequested.connect(self.context_menu)
        self.populateProcessImage()
        self.dialog.treeViewRecords.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.dialog.treeViewRecords.customContextMenuRequested.connect(self.context_menu2)


    def populateProcessImage(self):
        path = "//C"
        self.model = QtWidgets.QFileSystemModel()
        self.model.setRootPath((QtCore.QDir.rootPath()))
        self.dialog.treeView.setModel(self.model)
        self.dialog.treeView.setRootIndex(self.model.index(path))
        self.dialog.treeView.setSortingEnabled(True)

    def context_menu(self):
        menu = QtWidgets.QMenu()
        open = menu.addAction("Open")
        #open.triggered.connect(self.open_file)
        process = menu.addAction("Process Image")
        #process.triggered.connect(self.activateFaceRecognition())
        cursor = QtGui.QCursor()
        action = menu.exec_(cursor.pos())
        if action == open:
            self.open_file()
        elif action == process:
            self.activateFaceRecognition()

    def open_file(self):
        index = self.dialog.treeView.currentIndex()
        file_path = self.model.filePath(index)
        os.startfile(file_path)

    def populateRecords(self, path):
        self.model = QtWidgets.QFileSystemModel()
        self.model.setRootPath((QtCore.QDir.rootPath()))
        self.dialog.treeViewRecords.setModel(self.model)
        self.dialog.treeViewRecords.setRootIndex(self.model.index(path))
        self.dialog.treeViewRecords.setSortingEnabled(True)

    def context_menu2(self):
        menu = QtWidgets.QMenu()
        open = menu.addAction("Open")
        cursor = QtGui.QCursor()
        action = menu.exec_(cursor.pos())
        if action == open:
            self.open_file2()


    def open_file2(self):
        index = self.dialog.treeViewRecords.currentIndex()
        file_path = self.model.filePath(index)
        os.startfile(file_path)

    def activateFaceRecognition(self):
        index = self.dialog.treeView.currentIndex()
        file_path = self.model.filePath(index)
        FaceRecognitionTester.find_match(file_path)

    def addNewCase(self):
        flag = 1
        caseName = self.dialog.NameTextEdit.toPlainText()
        caseID = self.dialog.CaseIDTextEdit.toPlainText()
        susID = self.dialog.SusTextEdit.toPlainText()
        susIDArr = susID.split(",")

        newCase = Case(caseID, caseName, susIDArr)
        allSuspect = self.DHL.get_all_suspects_names()

        for sus in susIDArr:
            if sus in allSuspect:
                pass
            else:
                QtWidgets.QMessageBox.information(self,"Invalid Data"
                                , "The suspect: " + sus + " does not exist in our DB", QtWidgets.QMessageBox.Ok)
                flag = 0

        if flag:
            self.DHL.add_case(newCase)
            QtWidgets.QMessageBox.information(self, "Successful Action"
                                              , "The new case has been added",
                                              QtWidgets.QMessageBox.Ok)



    def RecordsTab(self):
        caseNumber = self.dialog.RecordsTextEdit.toPlainText()
        case = self.DHL.get_case_by_id(caseNumber)
        self.dialog.caseDetails.append("Case ID:\t\t" + case.get_ID() + "\n\n")
        self.dialog.caseDetails.append("Case Name:\t" + case.get_name() + "\n\n")
        self.dialog.caseDetails.append("Suspects List:      " )
        for sus in case.suspects:
            self.dialog.caseDetails.append("\t\t" + sus)
        self.dialog.caseDetails.append("Images:      ")
        sus = self.DHL.get_suspect_by_tz(203973797)
        images = self.DHL.get_images(sus.images)
        dirPath = "..//images//case" + str(case.number_id)
        os.makedirs(dirPath)
        for i in range(len(images)):
            path = "..//images//case" + str(case.number_id) + "//" + str(i) + ".jpg"
            cv2.imwrite(path, images[i].data)
        self.populateRecords("..//images//case" + str(case.number_id))



    def forReview(self):
        return




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GUI()
    window.show()
    sys.exit(app.exec_())
