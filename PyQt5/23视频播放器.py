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
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout,QFrame,QPushButton
import sys
import requests

"""错误日志重定向"""
import traceback
def except_hook(exc_type, exc_value, exc_tb):
    # 打印错误信息
    traceback.print_exception(exc_type, exc_value, exc_tb)
    # 也可以将错误写入日志文件
    # with open("error.log", "a") as f:
    #     traceback.print_exception(exc_type, exc_value, exc_tb, file=f)

# 重定向异常处理
sys.excepthook = except_hook


"""常用创建窗口的方式"""
# 继承QWidget类所有的属性和方法
class mainWidget(QWidget):
    def __init__(self):
        # 初始化父类的__init__方法 将self参数传进去
        super().__init__()  # QWidget.__init__(self)
        # 修改窗口标题
        self.setWindowTitle("创建pyqt窗口")
        # 修改窗口大小
        self.resize(1600, 1000)

        self.videoFrame = QFrame()

        self.videoFrame.setStyleSheet("""
            border:3px solid gray;
        """)

        # 创建视频播放控件
        self.videoWidget =  QVideoWidget(self)
        frameLayout = QVBoxLayout()
        frameLayout.addWidget(self.videoWidget)
        self.videoFrame.setLayout(frameLayout)


        # 创建按钮
        self.playBtn = QPushButton("播放")
        self.playBtn.clicked.connect(self.play_slot)

        # 创建垂直布局
        self.layout = QVBoxLayout(self)
        # 添加视频播放控件
        self.layout.addWidget(self.videoFrame)
        self.layout.addWidget(self.playBtn)


        # 设置布局
        self.setLayout(self.layout)
        self.VideoPlay_init()

    def play_slot(self):
        if self.playBtn.text() == "播放":
            self.playBtn.setText("暂停")
            self.VideoPlay.play()
        else:
            self.playBtn.setText("播放")
            self.VideoPlay.pause()

    def VideoPlay_init(self):
        # 创建播放器
        self.VideoPlay = QMediaPlayer(self)
        self.VideoPlay.setVideoOutput(self.videoWidget)

        # 设置本地播放内容
        # self.VideoPlay.setMedia(QMediaContent(QUrl.fromLocalFile('./video/1.mp4')))
        # 设置网络播放内容
        url = "https://upos-sz-estgcos.bilivideo.com/upgcxcode/53/08/30855990853/30855990853_da2-1-192.mp4?e=ig8euxZM2rNcNbRghWdVhwdlhWN1hwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&deadline=1754042858&nbs=1&uipk=5&og=cos&gen=playurlv3&os=upos&trid=29fb5a52867f4985ac0c2d55daba89dT&mid=3546831675984065&oi=2018263300&platform=html5&upsig=5316aea27913567324587ad81b4044e5&uparams=e,deadline,nbs,uipk,og,gen,os,trid,mid,oi,platform&bvc=vod&nettype=0&bw=972383&buvid=&build=0&dl=0&f=T_0_0&mobi_app=&agrr=1&orderid=0,1"
        self.VideoPlay.setMedia(QMediaContent(QUrl(url)))

        # self.VideoPlay.play()

        # 设置播放位置  单位为ms
        self.VideoPlay.setPosition(60000)
        """音量控制"""
        self.VideoPlay.setVolume(50)  # （0-100）

        """连接播放器的信号与槽函数（关键步骤）"""
        # 状态变化信号（播放/暂停/停止/加载）
        self.VideoPlay.stateChanged.connect(self.on_state_changed)
        # 错误信号（加载或播放失败时触发）
        self.VideoPlay.error.connect(self.on_error_occurred)
        # 播放结束时触发
        self.VideoPlay.mediaStatusChanged.connect(self.mediaStatusChanged)
        # 进度更新时触发
        self.VideoPlay.positionChanged.connect(self.positionChanged)
        # 媒体内容总时长发生变化时触发
        self.VideoPlay.durationChanged.connect(self.durationChanged)

        # 获取总时长  立马获取会为0
        duration = self.VideoPlay.duration()
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

    def on_state_changed(self, state):
        """处理媒体状态变化"""
        if state == QMediaPlayer.LoadingMedia:
            print("正在加载媒体...")
        elif state == QMediaPlayer.PlayingState:
            print("媒体加载成功，正在播放")
        elif state == QMediaPlayer.StoppedState:
            # 可能是播放结束，也可能是加载失败后停止
            print("播放已停止")

    def on_error_occurred(self):
        """处理错误信息"""
        error = self.VideoPlay.errorString()
        error_code = self.VideoPlay.error()

        print(f"加载失败: {error}")
        print(f"错误代码: {error_code}")

        # 常见错误代码含义：
        # QMediaPlayer.NoError: 无错误
        # QMediaPlayer.ResourceError: 资源无法访问（可能是URL无效、网络问题等）
        # QMediaPlayer.FormatError: 格式不支持
        # QMediaPlayer.NetworkError: 网络错误
        # QMediaPlayer.AccessDeniedError: 访问被拒绝




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

