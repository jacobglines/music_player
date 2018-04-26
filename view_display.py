import sys
from PyQt5 import QtWidgets


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.user_interface()

    def user_interface(self):
        self.all_song_button = QtWidgets.QPushButton("All songs")
        self.play_button = QtWidgets.QPushButton("\u25B6")
        self.next_button = QtWidgets.QPushButton("\u23E9")
        self.prev_button = QtWidgets.QPushButton("\u23EA")
        self.shuffle_button = QtWidgets.QPushButton("🔀")
        self.l_playlists = QtWidgets.QLabel("Playlists")
        self.l_current_song = QtWidgets.QLabel("Current song")
        #self.songs = QtWidgets.QLabel("Songs: \n1. \n2. \n3. \n4. \n5.")

        self.l_playlists.setGeometry(50,50,100,10)

        h_box = QtWidgets.QHBoxLayout()
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.all_song_button)
        v_box.addWidget(self.l_playlists)
        v_box.addWidget(self.l_current_song)
        #v_box.addWidget(self.songs)

        h_box.addLayout(v_box)

        h_box.addWidget(self.shuffle_button)

        h_box.addWidget(self.prev_button)
        h_box.addWidget(self.play_button)
        h_box.addWidget(self.next_button)

        self.setLayout(h_box)

        self.setWindowTitle("Music Player")
        self.setGeometry(100, 100, 800, 600)
        self.show()

app = QtWidgets.QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())