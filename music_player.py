import sys
from PyQt5 import QtWidgets
import PyQt5.QtCore as C
import PyQt5.QtMultimedia as M


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
        self.line_edit = QtWidgets.QLineEdit()
        self.line_edit.setText("Search")
        self.search_button = QtWidgets.QPushButton("search")

        h_box = QtWidgets.QHBoxLayout()
        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.all_song_button)
        v_box.addWidget(self.l_playlists)
        v_box.addWidget(self.l_current_song)

        h_box.addLayout(v_box)

        v_box1 = QtWidgets.QVBoxLayout()
        v_box1.addWidget(self.line_edit)

        v_box2 = QtWidgets.QVBoxLayout()
        v_box2.addWidget(self.songs)

        h_box.addLayout(v_box1)

        h_box1 = QtWidgets.QHBoxLayout()
        h_box1.addWidget(self.shuffle_button)
        h_box1.addWidget(self.prev_button)
        h_box1.addWidget(self.play_button)
        h_box1.addWidget(self.next_button)

        h_box2 = QtWidgets.QHBoxLayout()
        h_box2.addWidget(self.search_button)

        v_box1.addLayout(h_box2)
        v_box1.addLayout(v_box2)
        v_box1.addLayout(h_box1)


        self.setLayout(h_box)

        self.setWindowTitle("Music Player")
        self.setGeometry(100, 100, 800, 600)
        self.show()
        self.play_button.clicked.connect(self.play)

    def play(self):
        #
        # Currently doesn't work
        #
        url = C.QUrl.fromLocalFile("/Users/jacobglines/Desktop/Programming/music_player/songs/Maroon 5 - She Will Be Loved.mp3")
        content = M.QMediaContent(url)
        player = M.QMediaPlayer()
        player.setVolume(75)
        player.setMedia(content)
        player.play()
        #
        # Only works for .wav files
        #
        M.QSound.play("/Users/jacobglines/Desktop/dog_growl3.wav")

app = QtWidgets.QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())