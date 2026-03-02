import sys
from PyQt5.QtCore import Qt, QFileInfo, QUrl, QTimer, QTime
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QWidget, QApplication, QListWidget, QLabel, QHBoxLayout, QVBoxLayout,
                             QSlider, QPushButton, QComboBox, QFileDialog, QListWidgetItem)
import requests

class Video_Player(QWidget):
    def __init__(self):
        super().__init__()
        self.songname_index = 0
        self.ui_init()
        self.slot_init()


    def ui_init(self):
        """
        界面创建
        :return:
        """
        self.setWindowTitle("视频播放器")
        # 创建歌曲列表
        self.song_list = QListWidget(self)
        self.song_list.setMaximumWidth((150))
        #创建视频播放的窗口
        self.video_widget = QVideoWidget(self)

        #准备一个水平布局
        self.video_hbox = QHBoxLayout()
        self.video_hbox.addWidget(self.song_list)
        self.video_hbox.addWidget(self.video_widget)

        # 显示歌曲名称
        self.name_lab = QLabel("视频名称", self)
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

        # 设置下拉框
        self.play_combox = QComboBox(self)
        item_value = ["单曲循环", "顺序播放", "随机播放"]
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
        # 按顺序将控件放到垂直布局中
        self.vbox.addLayout(self.video_hbox)
        self.vbox.addLayout(self.label_layout)
        self.vbox.addWidget(self.player_slider)
        self.vbox.addLayout(self.btn_layout)

        # 把垂直布局设置到整个界面中
        self.setLayout(self.vbox)

        # 创建媒体播放器的对象
        self.MP3_Player = QMediaPlayer(self)

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


        # 更新播放时间显示的定时器
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_showtime_slot)

        # # 请求地址
        # url = "https://jkapi.com/api/music"
        # #请求参数
        # params = {
        #     "plat":"wy" ,  # wy 和 qq
        #     "type":"json",
        #     "apiKey":"1d54ef8042552c4cdda5ccb18037bda6",
        #     "name" : "一程山路"
        # }
        #
        # response =  requests.get(url,params=params)
        # if response.status_code == 200:
        #     self.data_dict = response.json()  # 获取响应数据 字典数据类型
        #     print(self.data_dict)

    def choose_btn_slot(self):
        # """加载本地歌曲"""
        # self.mp3Player = QMediaPlayer(self)
        # # 设置本地播放内容
        # # self.mp3Player.setMedia(QMediaContent(QUrl.fromLocalFile('./music/我终于等到你 - 任夏.mp3')))
        # # 从网络加载歌曲
        # url = self.data_dict.get('music_url',None)
        # if url:
        #     # 获取歌曲名称
        #     self.music_name = self.data_dict.get('name')
        #     # 歌曲名称添加到列表中
        #     self.song_list.addItem(QListWidgetItem(self.music_name))
        #     self.name_lab.setText(self.music_name)
        #     # 音乐播放器加载歌曲
        #     self.mp3Player.setMedia(QMediaContent(QUrl(url)))
        #     # self.mp3Player.play()  # 播放歌曲
        #     # 设置播放位置  单位为ms
        #     self.mp3Player.setPosition(60000)
        #
        # # 启动歌曲名称滚动显示的定时器功能
        # self.startTimer(1000)


        # 弹出文件对话框
        self.music_path = QFileDialog.getOpenFileName(self, "选择视频", "./", "ship(*.avi)")[0]
        print(self.music_path)
        # 获取视频名称
        self.music_name = QFileInfo(self.music_path).fileName()
        print( self.music_name)
        # 视频名称添加到列表中
        self.song_list.addItem(QListWidgetItem(self.music_name))
        self.name_lab.setText(self.music_name)
        # 视频播放器加载视频
        self.MP3_Player.setMedia(QMediaContent(QUrl(self.music_path)))
        #视频画面的显示
        self.MP3_Player.setVideoOutput(self.video_widget)

        # 启动视频名称滚动显示的定时器功能
        self.startTimer(1000)


    def play_btn_slot(self):
        if self.play_btn.text() == "播放":
            self.timer.start(1000)
            self.MP3_Player.play()
            self.play_btn.setText("暂停")
        else:
            self.timer.stop()
            self.MP3_Player.pause()
            self.play_btn.setText("播放")

    def pre_btn_slot(self):
        pass

    def next_btn_slot(self):
        pass




    def timerEvent(self, a0):

        if self.songname_index == len(self.music_name):
            self.songname_index = 0
        else:
            self.songname_index += 1
            self.name_lab.setText(self.music_name[self.songname_index:])

    def update_showtime_slot(self):
        """
        更新音乐播放时间
        :return:
        """
        # 获取歌曲当前播放时长, 返回 int 类型的时长，单位是ms
        cur_playtime = self.MP3_Player.position()

        # 总时长
        music_time = self.MP3_Player.duration()

        # 时间格式转换 将 int 类型转化为（分钟：秒）的格式
        cur_playtime_str = QTime(0,0,0,0).addMSecs(cur_playtime).toString("mm:ss")
        music_time_str = QTime(0,0,0,0).addMSecs(music_time).toString("mm:ss")

        self.time_lab.setText(cur_playtime_str + "/" + music_time_str)

    def update_playslider_value(self, position):

        self.player_slider.setValue(position)

    def update_playslider_range(self, duration):

        self.player_slider.setRange(0, duration)

    def update_player_position(self, position):

        self.MP3_Player.setPosition(position)

    def update_player_volume(self, position):

        self.MP3_Player.setVolume(position)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Video_Player()
    w.show()
    sys.exit(app.exec_())