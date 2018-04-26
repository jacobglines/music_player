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
        self.songs = QtWidgets.QLabel("Songs: \n1. \n2. \n3. \n4. \n5.")

        h_box1 = QtWidgets.QHBoxLayout()
        v_box1 = QtWidgets.QVBoxLayout()

        v_box1.addWidget(self.all_song_button)
        v_box1.addWidget(self.l_playlists)
        v_box1.addWidget(self.l_current_song)

        h_box1.addLayout(v_box1)

        v_box2 = QtWidgets.QVBoxLayout()
        v_box2.addWidget(self.songs)

        h_box1.addLayout(v_box2)

        h_box2 = QtWidgets.QHBoxLayout()
        h_box2.addWidget(self.shuffle_button)

        h_box3 = QtWidgets.QHBoxLayout()
        h_box3.addWidget(self.prev_button)

        h_box4 = QtWidgets.QHBoxLayout()
        h_box4.addWidget(self.play_button)

        h_box5 = QtWidgets.QHBoxLayout()
        h_box5.addWidget(self.next_button)

        v_box2.addLayout(h_box2)
        v_box2.addLayout(h_box3)
        v_box2.addLayout(h_box4)
        v_box2.addLayout(h_box5)

        self.setLayout(h_box1)

        self.setWindowTitle("Music Player")
        self.setGeometry(100, 100, 800, 600)
        self.show()

app = QtWidgets.QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())

