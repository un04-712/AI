from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap, QMovie
from PyQt5.QtWidgets import QApplication,QWidget,QLabel
import sys

"""
        QLabel:显示文字、静态图片、动态图片
"""

class mainWidget(QWidget):
    def __init__(self):
        super().__init__()  # QWidget.__init__(self)
        # 修改窗口标题
        self.setWindowTitle("创建第一个PyQt窗口")
        # 修改窗口大小
        self.resize(888, 888)
        # 设置窗口位置
        self.move(200,200)
        # 设置窗口图标
        icon = QIcon('../images/1.png')
        self.setWindowIcon(icon)

        self.ui_init()  #界面初始化

    def ui_init(self):
        text = QLabel(self)
        #显示文本
        text.setText("购物管理系统")
        #显示样式
        text.setStyleSheet("""
            font-family:宋体;
            font-size:10px;
            font-weight:bold;   /* bold 加粗字体 */
        """)
        #设置显示位置
        text.move(0,0)
        #设置标签大小
        text.resize(100,100)

        """显示图片"""
        image = QLabel(self)
        image.setPixmap(QPixmap('../images/1.png'))
        image.move(400,400)

        #设置图片大小 方法一 图片大小和标签大小一样
        image.resize(100,100)
        # image.setScaledContents(True)

        #设置图片大小 图片大小和标签大小不一样
        pixmap = QPixmap('../images/1.png')

        pixmap_scled = pixmap.scaled(300,200,Qt.KeepAspectRatio)
        image.setPixmap(pixmap_scled)

        """显示gif动图"""
        movie = QMovie('../images/fan.gif')
        gifLabel = QLabel(self)
        gifLabel.setMovie(movie)
        gifLabel.move(278,456)
        gifLabel.setStyleSheet("""
            QLabel{
                border: 3px solid gray;
            }
            QLabel:hover{       /*hover 鼠标悬停 */
                border: 3px solid red;
                padding-top:    /*hover 上内边距 */
                padding-left:    /*hover 左内边距 */
            }
        """)

        movie.start() #播放动图
        movie.stop()




if __name__ == '__main__':
    # 创建qApplication类
    app = QApplication(sys.argv)

    # 创建窗口对象,QWidget为UI界面
    window = mainWidget()

    # 显示窗口
    window.show()

    # 程序关闭之后释放资源
    sys.exit(app.exec())
