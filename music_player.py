import sys
from PyQt5 import QtWidgets
import PyQt5.QtCore as C
import PyQt5.QtMultimedia as M
import os

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
        self.songs = QtWidgets.QLabel("Songs:\n")
        self.all_songs = self.load_songs()
        self.line_edit = QtWidgets.QLineEdit()
        self.line_edit.setText("Search")
        self.search_button = QtWidgets.QPushButton("search")

        self.player = M.QMediaPlayer(self)
        self.playlist = M.QMediaPlaylist(self.player)
        print(self.all_songs)
        for song in self.all_songs:
            url = C.QUrl.fromLocalFile(song[:-1])
            print(url)
            content = M.QMediaContent(url)
            self.playlist.addMedia(content)
        self.playlist.setCurrentIndex(0)
        self.player.setPlaylist(self.playlist)

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
        self.next_button.clicked.connect(self.next)
        self.prev_button.clicked.connect(self.back)

    def load_songs(self):
        songList = []
        s = 'Songs:\n'
        songs = os.listdir("/Users/jacobglines/Desktop/Programming/music_player/songs")
        for item in songs:
            s += (str(item[:-4]) + '\n')
            song = ('/Users/jacobglines/Desktop/Programming/music_player/songs/' + item + '\n')
            songList.append(song)
        self.songs.setText(s)
        return songList

    def play(self):
        self.player.play()

    def next(self):
        numb = self.playlist.currentIndex()
        self.playlist.setCurrentIndex(numb + 1)
        self.player.play()

    def back(self):
        numb = self.playlist.currentIndex()
        self.playlist.setCurrentIndex(numb - 1)
        self.player.play()

app = QtWidgets.QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
