import sys
import random
from PyQt5.QtCore import Qt, QFileInfo, QUrl, QTimer, QTime
from PyQt5.QtGui import QIcon
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import (QWidget, QApplication, QListWidget, QLabel, QHBoxLayout, QVBoxLayout,
                             QSlider, QPushButton, QComboBox, QFileDialog, QListWidgetItem, QMessageBox)


class MP3_Player(QWidget):
    def __init__(self):
        super().__init__()
        self.songname_index = 0
        self.current_index = -1  # 当前播放歌曲的索引
        self.song_paths = []  # 存储所有歌曲的路径
        self.ui_init()
        self.slot_init()

    def ui_init(self):
        """界面创建"""
        self.setWindowTitle("MP3音乐播放器")
        # 设置窗口图标
        icon = QIcon('../images/音乐.png')
        self.setWindowIcon(icon)
        # 创建歌曲列表
        self.song_list = QListWidget(self)
        self.song_list.doubleClicked.connect(self.on_list_item_clicked)  # 双击列表项播放歌曲

        # 显示歌曲名称
        self.name_lab = QLabel("歌曲名称", self)
        # 显示播放时间
        self.time_lab = QLabel("00:00/00:00", self)

        # 创建水平布局
        self.label_layout = QHBoxLayout()
        self.label_layout.addWidget(self.name_lab)
        self.label_layout.addWidget(self.time_lab)

        # 创建播放滑块
        self.player_slider = QSlider(self)
        self.player_slider.setValue(0)
        # 设置滑块的方向为水平
        self.player_slider.setOrientation(Qt.Horizontal)

        # 设置按键
        self.play_btn = QPushButton("播放", self)
        self.choose_btn = QPushButton("选择文件", self)
        self.pre_btn = QPushButton("<-", self)
        self.next_btn = QPushButton("->", self)

        # 设置下拉框 - 增加了"列表循环"选项
        self.play_combox = QComboBox(self)
        item_value = ["单曲循环", "顺序播放", "列表循环", "随机播放"]
        self.play_combox.addItems(item_value)

        # 音量滑块
        self.volume_slider = QSlider(self)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(30)
        self.volume_slider.setOrientation(Qt.Horizontal)

        # 设置按钮的水平布局
        self.btn_layout = QHBoxLayout()
        self.btn_layout.addWidget(self.play_btn)
        self.btn_layout.addWidget(self.choose_btn)
        self.btn_layout.addWidget(self.pre_btn)
        self.btn_layout.addWidget(self.next_btn)
        self.btn_layout.addWidget(self.play_combox)
        self.btn_layout.addWidget(self.volume_slider)

        # 设置垂直布局
        self.vbox = QVBoxLayout()
        # 按顺序将控件放到放到垂直布局中
        self.vbox.addWidget(self.song_list)
        self.vbox.addLayout(self.label_layout)
        self.vbox.addWidget(self.player_slider)
        self.vbox.addLayout(self.btn_layout)

        # 把垂直布局设置到整个界面中
        self.setLayout(self.vbox)

        # 设置音乐播放器
        self.MP3_Player = QMediaPlayer(self)
        # 当歌曲播放结束时自动切换到下一首
        self.MP3_Player.stateChanged.connect(self.on_state_changed)

    def slot_init(self):
        self.play_btn.clicked.connect(self.play_btn_slot)
        self.choose_btn.clicked.connect(self.choose_btn_slot)
        self.pre_btn.clicked.connect(self.pre_btn_slot)
        self.next_btn.clicked.connect(self.next_btn_slot)

        # 滑块功能关联
        self.MP3_Player.positionChanged.connect(self.update_playslider_value)
        self.MP3_Player.durationChanged.connect(self.update_playslider_range)

        # 依据滑块的位置，更新歌曲播放的位置
        self.player_slider.sliderMoved.connect(self.update_player_position)

        # 依据音量滑块的位置，更新音量大小
        self.volume_slider.sliderMoved.connect(self.update_player_volume)
        # 初始设置音量
        self.MP3_Player.setVolume(self.volume_slider.value())

        # 更新播放时间显示的定时器
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_showtime_slot)

    def choose_btn_slot(self):
        """加载本地歌曲，可以选择多个文件"""
        music_paths, _ = QFileDialog.getOpenFileNames(self, "选择歌曲", "./", "MP3(*.mp3)")

        if music_paths:
            for path in music_paths:
                # 避免添加重复的歌曲
                if path not in self.song_paths:
                    self.song_paths.append(path)
                    music_name = QFileInfo(path).fileName()
                    self.song_list.addItem(QListWidgetItem(music_name))
                    for i in range(self.song_list.count()):
                        print(self.song_list.item(i).text())  # 输出列表中显示的歌曲名称

            # 如果是第一次添加歌曲，自动选中第一首
            if self.current_index == -1 and self.song_paths:
                self.current_index = 0
                self.load_music_by_index(self.current_index)

    def play_btn_slot(self):
        if self.MP3_Player.mediaStatus() == QMediaPlayer.NoMedia:
            # 如果没有加载媒体，尝试加载第一首
            if self.song_paths:
                self.current_index = 0
                self.load_music_by_index(self.current_index)
                self.MP3_Player.play()
                self.play_btn.setText("暂停")
                self.timer.start(1000)
        elif self.MP3_Player.state() == QMediaPlayer.PlayingState:
            self.timer.stop()
            self.MP3_Player.pause()
            self.play_btn.setText("播放")
        else:
            self.timer.start(1000)
            self.MP3_Player.play()
            self.play_btn.setText("暂停")

    def pre_btn_slot(self):
        """上一首功能"""
        if not self.song_paths:
            return
        # 根据播放模式处理上一首
        play_mode = self.play_combox.currentIndex()
        if play_mode == 3:  # 随机播放模式
            # 随机选择不同于当前的歌曲
            if len(self.song_paths) > 1:
                old_index = self.current_index
                while self.current_index == old_index:
                    self.current_index = random.randint(0, len(self.song_paths) - 1)
        else:  # 其他模式
            self.current_index = (self.current_index - 1) % len(self.song_paths)

        self.load_music_by_index(self.current_index)
        # 如果当前是播放状态，切换后继续播放
        if self.play_btn.text() == "暂停" or self.MP3_Player.state() == QMediaPlayer.PlayingState:
            self.MP3_Player.play()
            self.timer.start(1000)

    def next_btn_slot(self):
        """下一首功能"""
        if not self.song_paths:
            return
        # 根据播放模式处理下一首
        self.play_next_by_mode()

        self.load_music_by_index(self.current_index)
        # 如果当前是播放状态，切换后继续播放
        if self.play_btn.text() == "暂停" or self.MP3_Player.state() == QMediaPlayer.PlayingState:
            self.MP3_Player.play()
            self.timer.start(1000)

    def play_next_by_mode(self):

        play_mode = self.play_combox.currentIndex()

        if play_mode == 0:  # 单曲循环
            pass

        elif play_mode == 1:  # 顺序播放
            if self.current_index < len(self.song_paths) - 1:
                self.current_index += 1
            else:
                self.current_index = 0

        elif play_mode == 2:  # 列表循环
            self.current_index = (self.current_index + 1) % len(self.song_paths)

        elif play_mode == 3:  # 随机播放
            if len(self.song_paths) > 1:
                old_index = self.current_index
                while self.current_index == old_index:
                    self.current_index = random.randint(0, len(self.song_paths) - 1)
            else:
                self.current_index = 0

    def on_list_item_clicked(self):
        """双击列表项播放对应的歌曲"""
        self.current_index = self.song_list.currentRow()
        self.load_music_by_index(self.current_index)
        self.MP3_Player.play()
        self.play_btn.setText("暂停")
        self.timer.start(1000)

    def on_state_changed(self, state):

        # 如果歌曲播放结束，根据播放模式切换到下一首
        if state == QMediaPlayer.StoppedState and self.song_paths:
            self.play_next_by_mode()
            self.load_music_by_index(self.current_index)
            self.MP3_Player.play()

    def load_music_by_index(self, index):
        """根据索引加载并显示歌曲"""
        if 0 <= index < len(self.song_paths):
            music_path = self.song_paths[index]
            music_name = QFileInfo(music_path).fileName()
            self.MP3_Player.setMedia(QMediaContent(QUrl.fromLocalFile(music_path)))
            self.name_lab.setText(music_name)
            self.music_name = music_name  # 用于滚动显示
            self.songname_index = 0  # 重置滚动索引
            # 高亮显示当前播放的歌曲
            self.song_list.setCurrentRow(index)

    def timerEvent(self, a0):
        """歌曲名称滚动显示"""
        if hasattr(self, 'music_name') and self.music_name:
            if self.songname_index >= len(self.music_name):
                self.songname_index = 0
            else:
                self.songname_index += 1
                self.name_lab.setText(self.music_name[self.songname_index:])

    def update_showtime_slot(self):
        """更新音乐播放时间"""
        # 获取歌曲当前播放时长, 返回 int 类型的时长，单位是ms
        cur_playtime = self.MP3_Player.position()

        # 总时长
        music_time = self.MP3_Player.duration()

        # 时间格式转换 将 int 类型转化为（分钟：秒）的格式
        cur_playtime_str = QTime(0, 0, 0, 0).addMSecs(cur_playtime).toString("mm:ss")
        music_time_str = QTime(0, 0, 0, 0).addMSecs(music_time).toString("mm:ss")

        self.time_lab.setText(cur_playtime_str + "/" + music_time_str)

    def update_playslider_value(self, position):
        self.player_slider.setValue(position)

    def update_playslider_range(self, duration):
        self.player_slider.setRange(0, duration)

    def update_player_position(self, position):
        self.MP3_Player.setPosition(position)

    def update_player_volume(self, position):
        self.MP3_Player.setVolume(position)
    def closeEvent(self, event):

        reply = QMessageBox.question(
            self,
            "确认退出",
            "确定要退出MP3播放器吗？",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            event.accept()  # 接受关闭事件
        else:
            event.ignore()  # 忽略关闭事件


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MP3_Player()
    w.resize(600, 400)  # 设置窗口大小
    w.show()
    sys.exit(app.exec_())