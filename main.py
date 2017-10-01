import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QListWidgetItem

import splitter as sp

def open_file():
    name, ext = QFileDialog.getOpenFileName(MainWindow,'Open File')
    file = open(name, 'r')

    with file:
        text = file.read()
        file.close()
        words = text.split()
        for word in words:
            item = QListWidgetItem(word)
            ui.listWidgetKnow.addItem(item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = sp.Ui_MainWindow()
    ui.setupUi(MainWindow)

    ui.actionOpen.triggered.connect(open_file)


    MainWindow.show()
    sys.exit(app.exec_())