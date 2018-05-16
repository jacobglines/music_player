from PyQt5 import QtWidgets
import PyQt5.QtCore as C
import PyQt5.QtMultimedia as M
import os
from PyQt5.QtWidgets import QStyle, QListWidget, QAction, QInputDialog, QLineEdit


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.user_interface()

    def item_click(self, item):
        number = self.view.currentRow()
        if self.shuffled == False:
            self.playlist.setCurrentIndex(number)
            self.player.play()
        elif self.shuffled == True:
            pass

    def item_doubleclick(self, item):
        self.current_item = item
        menu = QtWidgets.QMenu()
        createPlaylist = QAction('Create New Playlist')
        createPlaylist.triggered.connect(self.create_playlist)
        menu.addAction(createPlaylist)
        addToPlaylist = QAction('Add To Playlist')
        addToPlaylist.triggered.connect(self.add_to_playlist)
        menu.addAction(addToPlaylist)
        menu.exec_()

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

        self.view = QListWidget()
        self.viewPlaylists = QListWidget()
        self.all_songs = self.load_songs()
        self.all_playlists = self.load_playlists()
        self.viewPlaylists.adjustSize()

        self.view.adjustSize()
        self.view.itemClicked.connect(self.item_click)
        self.view.itemDoubleClicked.connect(self.item_doubleclick)

        self.view.installEventFilter(self)

        self.set_playlist()

        self.line_edit = QtWidgets.QLineEdit()
        self.line_edit.setText("")
        self.search_button = QtWidgets.QPushButton("search")

        # scroll are for list of songs
        self.songs_scroll_area = QtWidgets.QScrollArea()
        self.songs_scroll_area.setWidget(self.view)
        self.songs_scroll_area.setWidgetResizable(True)

        # scroll area for list of playlists
        self.playlists_scroll_area = QtWidgets.QScrollArea()
        self.playlists_scroll_area.setWidget(self.viewPlaylists)
        self.playlists_scroll_area.setWidgetResizable(True)
        # self.playlists_scroll_bar = QtWidgets.QScrollBar()
        # self.playlists_scroll_area.setVerticalScrollBar(self.playlists_scroll_bar)
        # self.playlists_scroll_area.setVerticalScrollBarPolicy(C.Qt.ScrollBarAlwaysOn)

        # set area for current song box
        self.current_song_area = QtWidgets.QScrollArea()
        self.current_song_area.setWidget(self.l_current_song)

        # set volumn slider
        self.volumn_slider = QtWidgets.QSlider(C.Qt.Horizontal)
        self.volumn_slider.setMaximum(100)
        self.volumn_slider.setMinimum(0)
        self.volumn_slider.setValue(50)
        self.volumn_slider.setTickPosition(QtWidgets.QSlider.TicksRight)
        self.volumn_slider.setTickInterval(10)

        self.seekSlider = QtWidgets.QSlider()
        self.seekSlider.setMinimum(0)
        self.seekSlider.setMaximum(100)
        self.seekSlider.setRange(0, self.player.duration() / 1000)
        self.seekSlider.setOrientation(C.Qt.Horizontal)
        self.seekSlider.setTracking(False)
        seekSliderLabel1 = QtWidgets.QLabel('0.00')
        seekSliderLabel2 = QtWidgets.QLabel('0.00')

        self.set_playlist()
        self.volume_change()

        # self.list_view = QtWidgets.QListView(self.all_songs)

        h_box = QtWidgets.QHBoxLayout()
        v_box = QtWidgets.QVBoxLayout()
        self.h_box4 = QtWidgets.QHBoxLayout()

        # h_box.addWidget(backGround)

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

        h_box3 = QtWidgets.QHBoxLayout()
        h_box3.addWidget(self.min_volumn)
        h_box3.addWidget(self.volumn_slider)
        h_box3.addWidget(self.max_volumn)

        h_box2 = QtWidgets.QHBoxLayout()
        h_box2.addWidget(self.search_button)

        v_box1.addLayout(h_box2)
        v_box1.addLayout(v_box2)
        v_box1.addLayout(self.h_box4)
        v_box1.addLayout(h_box1)
        v_box1.addLayout(h_box3)

        self.setLayout(h_box)

        self.setWindowTitle("Music Player")
        self.setGeometry(100, 100, 800, 600)
        self.show()

        self.play_button.setShortcut(' ')
        self.next_button.setShortcut('Alt+Right')
        self.prev_button.setShortcut('Alt+Left')
        self.search_button.setShortcut('Return')
        self.play_button.clicked.connect(self.play)
        self.next_button.clicked.connect(self.next)
        self.prev_button.clicked.connect(self.back)
        self.shuffle_button.clicked.connect(self.shuffle)
        self.search_button.clicked.connect(self.search)
        self.volumn_slider.valueChanged.connect(self.volume_change)
        self.all_song_button.clicked.connect(self.load_songs)
        self.player.currentMediaChanged.connect(self.current_song)
        self.player.positionChanged.connect(self.qmp_positionChanged)
        self.player.durationChanged.connect(self.change_duration)
        # self.all_song_button.clicked.connect(self.show_all_songs)

        self.shuffled = False


    def add_to_playlist(self):
        menu = QtWidgets.QMenu()
        

    def create_playlist(self):
        root = C.QFileInfo(__file__).absolutePath()
        spot = (root + '/songs/')
        playlistName = self.getText()
        completeName = os.path.join(spot, f'{playlistName}.m3u')
        file = open(completeName, 'w')
        file.close()
        self.all_playlists.clear()
        self.playlists_scroll_area.update()
        self.all_playlists = self.load_playlists()
        self.playlists_scroll_area.update()

    def getText(self):
        text, okPressed = QInputDialog.getText(self, "New Playlist", "Playlist Name:", QLineEdit.Normal, "")
        if okPressed and text != '':
            return text

    def load_playlists(self):
        playlists = []
        root = C.QFileInfo(__file__).absolutePath()
        songs = os.listdir(root + "/songs")
        for item in songs:
            if str(item[-4:]) == '.m3u':
                self.viewPlaylists.addItem(item[:-4])
                print(root + "/songs" + item)
                playlists.append(root + "/songs" + item)
        return playlists


    def show_all_songs(self):
        root = C.QFileInfo(__file__).absolutePath()
        songs = os.listdir(root + "/songs")
        for item in songs:
            if item[-4:] != '.m3u':
                self.view.addItem(str(item[:-4]))

    def current_song(self, media):
        name = media.canonicalUrl()
        name = name.toString()
        name = name.split('/')
        url = name[-1]
        url = url[:-4]
        self.l_current_song.setText('Current Song:\n\n' + url)
        self.l_current_song.adjustSize()

    def change_duration(self):
        self.seekSlider.setRange(0, self.player.duration() / 1000)

    def qmp_positionChanged(self, position):
        if self.shuffled == False:
            sliderLayout = self.h_box4.layout()
            sliderLayout.itemAt(0).widget().setText('%d:%02d' % (int(position / 60000), int((position / 1000) % 60)))
            self.seekSlider.setValue(position / 1000)
            sliderLayout.itemAt(2).widget().setText(
                '%d:%02d' % (int(self.player.duration() / 60000), int((self.player.duration() / 1000) % 60)))
        elif self.shuffled == True:
            sliderLayout = self.h_box4.layout()
            sliderLayout.itemAt(0).widget().setText('%d:%02d' % (int(position / 60000), int((position / 1000) % 60)))
            self.seekSlider.setValue(position / 1000)
            sliderLayout.itemAt(2).widget().setText(
                '%d:%02d' % (int(self.player.duration() / 60000), int((self.player.duration() / 1000) % 60)))

    def load_songs(self):
        songList = []
        s = 'Songs:\n\n'
        root = C.QFileInfo(__file__).absolutePath()
        songs = os.listdir(root + "/songs")
        for item in songs:
            if item[-4:] != '.m3u':
                s += (str(item[:-4]) + '\n')
                self.view.addItem(str(item[:-4]))
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
                self.play_button.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
                self.player.play()
            else:
                self.player.pause()
                self.play_button.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        else:
            if self.player2.state() == 0 or self.player2.state() == 2:
                self.play_button.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
                self.player2.play()
            else:
                self.player2.pause()
                self.play_button.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

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
            self.player2.stop()
            self.playlist.setCurrentIndex(0)
            self.player.play()
            self.shuffled = False

    def volume_change(self):
        numb = self.volumn_slider.value()
        self.player.setVolume(numb)
        self.player2.setVolume(numb)

    def display_song_list(self, list_of_songs):
        s = 'Songs:\n\n'
        for item in list_of_songs:
            s += (str(item[:-4]) + '\n')
        self.songs.setText(s)

    def search(self):
        s_term = self.line_edit.text()
        filtered_list_of_songs = []
        root = C.QFileInfo(__file__).absolutePath()
        songs = os.listdir(root + "/songs")
        # search through each song in all_songs...if it matches add to filtered_list_of_songs
        for song in songs:
            if song.lower().find(s_term.lower()) > -1:
                filtered_list_of_songs.append(song)
        self.display_song_list(filtered_list_of_songs)
