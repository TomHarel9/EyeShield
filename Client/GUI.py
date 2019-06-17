import os
import sys

os.environ['QT_API'] = "pyside2"
from PySide2.QtWidgets import QApplication, QMainWindow

from Client import UI


class GUI(QMainWindow):
    def __init__(self):
        super(GUI, self).__init__()
        self.dialog = UI.Ui_MainWindow()
        self.dialog.setupUi(self)
        self.dialog.activateQuery.clicked.connect(self.DBQueriesTab)
        self.dialog.EnterRecords.clicked.connect(self.RecordsTab)




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
