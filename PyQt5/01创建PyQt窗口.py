import PyQt5
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication,QWidget
import sys




"""
    常用的窗口创建方式
"""
class mainWidget(QWidget):
    def __init__(self):
        super().__init__()  #QWidget.__init__(self)
        #修改窗口标题
        self.setWindowTitle("创建第一个PyQt窗口")
        #修改窗口大小
        self.resize(888,888)
        #设置窗口位置
        self.move(666,666)
        #设置窗口图标
        icon = QIcon('./images/1.png')
        self.setWindowIcon(icon)



if __name__ == '__main__':
    #创建qApplication类
    app = QApplication(sys.argv)

    #创建窗口对象,QWidget为UI界面
    window = mainWidget()

    #显示窗口
    window.show()

    #程序关闭之后释放资源
    sys.exit(app.exec())
