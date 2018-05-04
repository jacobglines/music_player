import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QAction, QFileDialog
from music_player import Window
import os
from shutil import copy


class MenuBar(QtWidgets.QMainWindow):
    def __init__(self):
        super(MenuBar, self).__init__()
        self.setWindowTitle("Music Player")
        self.setGeometry(100, 100, 800, 600)

        extractAction = QAction("Open File", self)
        extractAction.setShortcut("Ctrl+F")
        extractAction.triggered.connect(self.open_file)

        self.window = Window()
        self.setCentralWidget(self.window)

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("File")
        fileMenu.addAction(extractAction)

        self.show()

    def open_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                "WAV Files (*.wav);;MP3 Files (*.mp3)", options=options)
        root = QtCore.QFileInfo(__file__).absolutePath()
        songs = (root + '/songs/')
        copy(fileName, songs)
        self.window.load_songs()
        self.window.set_playlist()
        print(self.window.playlist)
        self.update()





app = QtWidgets.QApplication(sys.argv)
window = MenuBar()
sys.exit(app.exec_())