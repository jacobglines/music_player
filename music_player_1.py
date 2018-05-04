import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QAction
from example import Interface


class MenuBar(QtWidgets.QMainWindow):
    def __init__(self):
        super(MenuBar, self).__init__()
        self.setWindowTitle("Music Player")
        self.setGeometry(100, 100, 800, 600)

        extractAction = QAction("Open File", self)
        extractAction.setShortcut("Ctrl+F")
        extractAction.triggered.connect(self.open_file)

        window = Interface()
        self.setCentralWidget(window)

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("File")
        fileMenu.addAction(extractAction)

        self.show()

    def open_file(self):
        pass
