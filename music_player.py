from PyQt5 import QtWidgets
import PyQt5.QtCore as C
import PyQt5.QtMultimedia as M
import os

class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.user_interface()

    def user_interface(self):
        self.shuffled = False
        self.all_song_button = QtWidgets.QPushButton("All songs")
        self.play_button = QtWidgets.QPushButton("\u25B6")
        self.next_button = QtWidgets.QPushButton("\u23E9")
        self.prev_button = QtWidgets.QPushButton("\u23EA")
        self.shuffle_button = QtWidgets.QPushButton("🔀")
        self.min_volumn = QtWidgets.QLabel("🔈")
        self.max_volumn = QtWidgets.QLabel("🔊")
        self.l_playlists = QtWidgets.QLabel("Playlists")
        self.l_current_song = QtWidgets.QLabel("Current song")
        self.songs = QtWidgets.QLabel("Songs:\n")
        self.all_songs = self.load_songs()
        self.set_playlist()
        self.line_edit = QtWidgets.QLineEdit()
        self.line_edit.setText("🔎")
        self.search_button = QtWidgets.QPushButton("search")
        # backGround = QImage("music-player-bg.png")

        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_area.setWidget(self.songs)
        self.scroll_bar = QtWidgets.QScrollBar()
        self.scroll_area.setVerticalScrollBar(self.scroll_bar)
        self.scroll_area.setVerticalScrollBarPolicy(C.Qt.ScrollBarAlwaysOn)

        # scroll area for list of songs
        self.songs_scroll_area = QtWidgets.QScrollArea()
        self.songs_scroll_area.setWidget(self.songs)
        self.songs_scroll_bar = QtWidgets.QScrollBar()
        self.songs_scroll_area.setVerticalScrollBar(self.songs_scroll_bar)
        self.songs_scroll_area.setVerticalScrollBarPolicy(C.Qt.ScrollBarAlwaysOn)

        # scroll area for list of playlists
        self.playlists_scroll_area = QtWidgets.QScrollArea()
        self.playlists_scroll_area.setWidget(self.l_playlists)
        self.playlists_scroll_bar = QtWidgets.QScrollBar()
        self.playlists_scroll_area.setVerticalScrollBar(self.playlists_scroll_bar)
        self.playlists_scroll_area.setVerticalScrollBarPolicy(C.Qt.ScrollBarAlwaysOn)

        # set are for current song box
        self.current_song_area = QtWidgets.QScrollArea()
        self.current_song_area.setWidget(self.l_current_song)

        self.slider = QtWidgets.QSlider()
        self.slider.windowHandle()
        self.slider.setFixedSize(20, 70)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setValue(50)
        self.slider.setTickInterval(5)

        self.seekSlider = QtWidgets.QSlider()
        self.seekSlider.setMinimum(0)
        self.seekSlider.setMaximum(100)
        #self.seekSlider.setRange(-10, self.player.duration() / 1000)
        max = self.seekSlider.maximum()
        print(max)
        self.seekSlider.setOrientation(C.Qt.Horizontal)
        self.seekSlider.setTracking(False)
        seekSliderLabel1 = QtWidgets.QLabel('0.00')
        seekSliderLabel2 = QtWidgets.QLabel('0.00')

        self.set_playlist()
        self.volume_change()

        h_box = QtWidgets.QHBoxLayout()
        v_box = QtWidgets.QVBoxLayout()
        self.h_box4 = QtWidgets.QHBoxLayout()

        #h_box.addWidget(backGround)

        v_box.addWidget(self.all_song_button)
        v_box.addWidget(self.playlists_scroll_area)
        v_box.addWidget(self.current_song_area)

        self.h_box4.addWidget(seekSliderLabel1)
        self.h_box4.addWidget(self.seekSlider)
        self.h_box4.addWidget(seekSliderLabel2)

        h_box.addLayout(v_box)

        v_box1 = QtWidgets.QVBoxLayout()
        v_box1.addWidget(self.line_edit)

        v_box2 = QtWidgets.QVBoxLayout()
        v_box2.addWidget(self.songs_scroll_area)

        h_box.addLayout(v_box1)

        h_box1 = QtWidgets.QHBoxLayout()
        h_box1.addWidget(self.shuffle_button)
        h_box1.addWidget(self.prev_button)
        h_box1.addWidget(self.play_button)
        h_box1.addWidget(self.next_button)

        v_box3 = QtWidgets.QVBoxLayout()
        v_box3.addWidget(self.min_volumn)
        v_box3.addWidget(self.slider)
        v_box3.addWidget(self.max_volumn)
        h_box1.addLayout(v_box3)

        h_box2 = QtWidgets.QHBoxLayout()
        h_box2.addWidget(self.search_button)

        v_box1.addLayout(h_box2)
        v_box1.addLayout(v_box2)
        v_box1.addLayout(self.h_box4)
        v_box1.addLayout(h_box1)

        self.setLayout(h_box)

        self.setWindowTitle("Music Player")
        self.setGeometry(100, 100, 800, 600)
        self.show()
        self.play_button.setShortcut(' ')
        self.next_button.setShortcut('Ctrl+Right')
        self.prev_button.setShortcut('Ctrl+Left')
        self.play_button.clicked.connect(self.play)
        self.next_button.clicked.connect(self.next)
        self.prev_button.clicked.connect(self.back)
        self.shuffle_button.clicked.connect(self.shuffle)
        self.search_button.clicked.connect(self.search)
        self.slider.valueChanged.connect(self.volume_change)

    def load_songs(self):
        songList = []
        s = 'Songs:\n\n'
        root = C.QFileInfo(__file__).absolutePath()
        songs = os.listdir(root + "/songs")
        for item in songs:
            print(item)
            s += (str(item[:-4]) + '\n')
            song = (root + '/songs/' + item + '\n')
            songList.append(song)
        self.songs.setText(s)
        return songList

    def set_playlist(self):
        self.player = M.QMediaPlayer(self)
        self.player2 = M.QMediaPlayer(self)
        self.playlist = M.QMediaPlaylist(self.player)
        self.playlist2 = M.QMediaPlaylist(self.player2)
        for song in self.all_songs:
            url = C.QUrl.fromLocalFile(song[:-1])
            content = M.QMediaContent(url)
            self.playlist.addMedia(content)
            self.playlist2.addMedia(content)
        self.playlist.setCurrentIndex(0)
        self.playlist2.shuffle()
        self.playlist2.setCurrentIndex(0)
        self.player.setPlaylist(self.playlist)
        self.player2.setPlaylist(self.playlist2)

    def play(self):
        if self.shuffled == False:
            if self.player.state() == 0 or self.player.state() == 2:
                self.player.play()
            else:
                self.player.pause()
        else:
            if self.player2.state() == 0 or self.player2.state() == 2:
                self.player2.play()
            else:
                self.player2.pause()

    def next(self):
        if self.shuffled == False:
            numb = self.playlist.currentIndex()
            self.playlist.setCurrentIndex(numb + 1)
            self.player.play()
        else:
            numb = self.playlist2.currentIndex()
            self.playlist2.setCurrentIndex(numb + 1)
            self.player2.play()

    def back(self):
        if self.shuffled == False:
            numb = self.playlist.currentIndex()
            self.playlist.setCurrentIndex(numb - 1)
            self.player.play()
        else:
            numb = self.playlist2.currentIndex()
            self.playlist2.setCurrentIndex(numb - 1)
            self.player2.play()

    def shuffle(self):
        if self.shuffled == False:
            self.player.stop()
            self.playlist2.shuffle()
            self.playlist2.setCurrentIndex(0)
            self.player2.play()
            self.shuffled = True
        elif self.shuffled == True:
            print('hello')
            self.player2.stop()
            self.playlist.setCurrentIndex(0)
            self.player.play()
            self.shuffled = False

    def volume_change(self):
        numb = self.slider.value()
        self.player.setVolume(numb)
        self.player2.setVolume(numb)

    def search(self):
        pass
