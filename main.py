from music_player_1 import MenuBar
from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = MenuBar()
sys.exit(app.exec_())
