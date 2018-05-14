from PyQt5 import QtWidgets
import PyQt5.QtCore as C
import PyQt5.QtMultimedia as M
import os

class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.user_interface()

        def user_interface(self):
        self.all_song_button = QtWidgets.QPushButton("All songs")
        self.play_button = QtWidgets.QPushButton()
        self.play_button.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.next_button = QtWidgets.QPushButton()
        self.next_button.setIcon(self.style().standardIcon(QStyle.SP_MediaSeekForward))
        self.prev_button = QtWidgets.QPushButton()
        self.prev_button.setIcon(self.style().standardIcon(QStyle.SP_MediaSeekBackward))
        self.shuffle_button = QtWidgets.QPushButton("🔀")
        self.min_volumn = QtWidgets.QLabel("🔈")
        self.max_volumn = QtWidgets.QLabel("🔊")
        self.l_playlists = QtWidgets.QLabel("Playlists:")
        self.l_current_song = QtWidgets.QLabel("Current song:")

        self.songs = QtWidgets.QLabel("Songs:\n")

        self.all_songs = self.load_songs()

        self.set_playlist()

        self.line_edit = QtWidgets.QLineEdit()
        self.line_edit.setText("🔎")
        self.search_button = QtWidgets.QPushButton("search")

        #scroll are for list of songs
        self.songs_scroll_area = QtWidgets.QScrollArea()
        self.songs_scroll_area.setWidget(self.songs)
        self.songs_scroll_bar = QtWidgets.QScrollBar()
        self.songs_scroll_area.setVerticalScrollBar(self.songs_scroll_bar)
        self.songs_scroll_area.setVerticalScrollBarPolicy(C.Qt.ScrollBarAlwaysOn)
        self.songs_scroll_area.setWidgetResizable(True)
        self.songs_scroll_area.setAlignment(C.Qt.AlignTop)

        #scroll area for list of playlists
        self.playlists_scroll_area = QtWidgets.QScrollArea()
        self.playlists_scroll_area.setWidget(self.l_playlists)
        self.playlists_scroll_bar = QtWidgets.QScrollBar()
        self.playlists_scroll_area.setVerticalScrollBar(self.playlists_scroll_bar)
        self.playlists_scroll_area.setVerticalScrollBarPolicy(C.Qt.ScrollBarAlwaysOn)

        #set area for current song box
        self.current_song_area = QtWidgets.QScrollArea()
        self.current_song_area.setWidget(self.l_current_song)

        #set volumn slider
        self.volumn_slider = QtWidgets.QSlider(C.Qt.Horizontal)
        self.volumn_slider.setMaximum(100)
        self.volumn_slider.setMinimum(0)
        self.volumn_slider.setValue(50)
        self.volumn_slider.setTickPosition(QtWidgets.QSlider.TicksRight)
        self.volumn_slider.setTickInterval(10)

        #self.list_view = QtWidgets.QListView(self.all_songs)

        h_box = QtWidgets.QHBoxLayout()
        v_box = QtWidgets.QVBoxLayout()

        #h_box.addWidget(backGround)

        v_box.addWidget(self.all_song_button)
        v_box.addWidget(self.playlists_scroll_area)
        v_box.addWidget(self.current_song_area)

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

        h_box3 = QtWidgets.QHBoxLayout()
        h_box3.addWidget(self.min_volumn)
        h_box3.addWidget(self.volumn_slider)
        h_box3.addWidget(self.max_volumn)

        h_box2 = QtWidgets.QHBoxLayout()
        h_box2.addWidget(self.search_button)

        v_box1.addLayout(h_box2)
        v_box1.addLayout(v_box2)
        v_box1.addLayout(h_box1)
        v_box1.addLayout(h_box3)

        self.setLayout(h_box)

        self.setWindowTitle("Music Player")
        self.setGeometry(100, 100, 800, 600)
        self.show()

        self.play_button.setShortcut(' ')
        self.next_button.setShortcut('Alt+Right')
        self.prev_button.setShortcut('Alt+Left')
        self.play_button.clicked.connect(self.play)
        self.next_button.clicked.connect(self.next)
        self.prev_button.clicked.connect(self.back)
        self.shuffle_button.clicked.connect(self.shuffle)
        self.search_button.clicked.connect(self.search)
        self.volumn_slider.valueChanged.connect(self.volume_change)
        self.all_song_button.clicked.connect(self.load_songs)

        self.shuffled = False

    def change_duration(self):
        self.seekSlider.setRange(0, self.player.duration())
        print('fdsfffffgfgfgf')
        print(self.seekSlider.maximum())


    def seekPosition(self, position):
        pass


    def qmp_positionChanged(self, position):
        sliderLayout = self.h_box4.layout()
        sliderLayout.itemAt(0).widget().setText('%d:%02d' % (int(position / 60000), int((position / 1000) % 60)))
        self.seekSlider.setValue(position / 1000)
        print(self.player.duration())
        sliderLayout.itemAt(2).widget().setText('%d:%02d' % (int(position / 60000), int((position / 1000) % 60)))

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

    def display_song_list(self, list_of_songs):
        s='Songs:\n\n'
        for item in list_of_songs:
            i = item.replace("C:/Users/Nhu/Music/", "")
            s += (str(i[:-4]) + '\n')
        self.songs.setText(s)

    def search(self):
        s_term = self.line_edit.text()
        filtered_list_of_songs = []
        # search trhough each song in all_songs...if it matches add to filtered_list_of_songs
        for song in self.all_songs:
            if  song.lower().find(s_term.lower()) > -1:
                filtered_list_of_songs.append(song)
        self.display_song_list(filtered_list_of_songs)
