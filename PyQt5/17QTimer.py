"""
    定时器  倒计时： 周期性执行任务    实时时间获取   动画效果

"""
import threading
import time
from PyQt5.QtCore import QTimer
"""
    实时获取时间
"""
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import sys

"""常用创建窗口的方式"""
# 继承QWidget类所有的属性和方法
class mainWidget(QMainWindow):
    def __init__(self):
        # 初始化父类的__init__方法 将self参数传进去
        super().__init__()  # QWidget.__init__(self)
        # 修改窗口标题
        self.setWindowTitle("定时器使用")
        # 修改窗口大小
        self.resize(700, 600)

        self.label = QLabel("定时器使用   ",self)
        self.label.move(100,100)
        self.label.resize(200,200)
        # 创建定时器
        self.timer = QTimer(self)
        # 设置超时时间
        self.timer.setInterval(1000)
        # 绑定定时器超时信号
        self.timer.timeout.connect(self.getTime)

        # 启动定时器
        self.timer.start()  # self.timer.stop()

    def getTime(self):
        ntime = time.time()  # 获取时间戳
        lotime = time.localtime(ntime)  # 转换为时间结构体
        str_time = time.strftime("%Y-%m-%d %H:%M:%S", lotime)
        self.label.setText(str_time)


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
    # 程序关闭之后自动释放资源
    sys.exit(app.exec_())



