
"""

    Qt Multimedia 是qt中专门用来处理多媒体功能的模块，主要负责提供音视频播放，录制，处理，
    以及相关设备交互功能
        QMediaPlayer 是一个高级媒体播放类，可用于播放歌曲，电影，网络电台。播放内容通过 QMediaContent对象指定(QURL),提供该对象就可以开始播放
            QMediaPlayer::setMedia  设置播放内容
            QMediaPlayer::play 播放内容
            QMediaPlayer::pause 暂停
            QMediaPlayer::stop  停止
            QMediaPlayer::setVolume  设置声音
"""
import time

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer,QMediaContent
from PyQt5.QtWidgets import QApplication,QWidget
import sys
import requests


"""常用创建窗口的方式"""
# 继承QWidget类所有的属性和方法
class mainWidget(QWidget):
    def __init__(self):
        # 初始化父类的__init__方法 将self参数传进去
        super().__init__()  # QWidget.__init__(self)
        # 修改窗口标题
        self.setWindowTitle("创建pyqt窗口")
        # 修改窗口大小
        self.resize(800, 800)

        self.data_dict = None

        # 请求地址
        url = "https://jkapi.com/api/music"
        # 请求参数
        params = {
            "plat":"qq" ,  # wy 和 qq
            "type":"json",
            "apiKey":"1d54ef8042552c4cdda5ccb18037bda6",
            "name" : "一程山路"
        }

        response =  requests.get(url,params=params)
        if response.status_code == 200:
            self.data_dict = response.json()  # 获取响应数据 字典数据类型
            print(self.data_dict)


        self.musicPlay_init()



    def musicPlay_init(self):
        """加载本地歌曲"""
        self.mp3Player = QMediaPlayer(self)
        # 设置本地播放内容
        # self.mp3Player.setMedia(QMediaContent(QUrl.fromLocalFile('./music/我终于等到你 - 任夏.mp3')))
        # 从网络加载歌曲
        url = self.data_dict.get('music_url',None)
        print( url)
        if url:
            self.mp3Player.setMedia(QMediaContent(QUrl(url)))
            self.mp3Player.play()  # 播放歌曲

            # 设置播放位置  单位为ms
            self.mp3Player.setPosition(60000)

            """音量控制"""
            self.mp3Player.setVolume(50)  # （0-100）

            # 播放结束时触发
            self.mp3Player.mediaStatusChanged.connect(self.mediaStatusChanged)
            # 进度更新时触发
            self.mp3Player.positionChanged.connect(self.positionChanged)
            # 媒体内容总时长发生变化时触发
            self.mp3Player.durationChanged.connect(self.durationChanged)

            # 获取总时长  立马获取会为0
            duration = self.mp3Player.duration()
            print("总时长：", duration)

    def mediaStatusChanged(self):
        """
        播放结束
        """
        print("播放结束")

    def positionChanged(self, position):
        """
        进度更新
        :param position:    1s进一次
        :return:
        """
        print("进度更新：", position)


    def durationChanged(self, duration):
        """
        媒体内容总时长发生变化时触发
        :param duration:
        :return:
        """
        print("媒体内容总时长发生变化时触发：", duration)




if __name__ == '__main__':
    """程序启动的基本流程"""
    # 创建qApplication类   sys.argv为了通过命令行传参，但是大部分场景已经不在需要
    # print(sys.argv)
    app = QApplication(sys.argv)
    # 创建窗口对象 QWidget为UI界面
    window =  mainWidget()
    # 显示窗口
    window.show()
    # 程序关闭之后自动释放资源
    sys.exit(app.exec_())



