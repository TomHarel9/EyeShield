import os
import sys

os.environ['QT_API'] = "pyside2"
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2 import QtGui, QtWidgets, QtCore

from Client import UI
from VideoLayer import faceRecognition


class GUI(UI.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(GUI, self).__init__()
        self.dialog = UI.Ui_MainWindow()
        self.dialog.setupUi(self)
        self.dialog.activateQuery.clicked.connect(self.DBQueriesTab)
        self.dialog.EnterRecords.clicked.connect(self.RecordsTab)
        self.dialog.treeView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.dialog.treeView.customContextMenuRequested.connect(self.context_menu)
        self.populate()


    def populate(self):
        path = "C:\\Users\\tomharel\\Documents\\GitHub\\EyeShield\images"
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

    def activateFaceRecognition(self):
        index = self.dialog.treeView.currentIndex()
        file_path = self.model.filePath(index)
        faceRecognition.find_match(file_path)

    def DBQueriesTab(self):
        comboBox = self.dialog.queriesComboBox
        if comboBox.currentIndex() == 0:
            print("activate query 1")
        elif comboBox.currentIndex() == 1:
            print("activate query 2")
        elif comboBox.currentIndex() == 2:
            print("activate query 3")

    def simulateCaseQuery(self, caseID):
        print(caseID)

    def RecordsTab(self):
        editText = self.dialog.RecordsTextEdit
        self.simulateCaseQuery(editText.toPlainText())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GUI()
    window.show()
    sys.exit(app.exec_())
