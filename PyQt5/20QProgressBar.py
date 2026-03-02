import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QSpinBox, QApplication, QVBoxLayout,QProgressBar


class mainWidget(QWidget):
    def __init__(self):
        super().__init__()  #QWidget.__init__(self)
        #修改窗口标题
        self.setWindowTitle("进度条控件的使用")
        #修改窗口大小
        self.resize(888,888)
        #设置窗口位置
        self.move(666,666)
        mainLayout = QVBoxLayout(self)
        self.QProgress =QProgressBar()
        mainLayout.addWidget(self.QProgress)


        """基本参数设置"""
        #设置范围
        self.QProgress.setRange(0,100)
        # 设置初始值
        self.QProgress.setValue(29)
        #设置百分比文本是否可见
        self.QProgress.setVisible(True)






if __name__ == '__main__':
    #创建qApplication类
    app = QApplication(sys.argv)

    #创建窗口对象,QWidget为UI界面
    window = mainWidget()

    #显示窗口
    window.show()

    #程序关闭之后释放资源
    sys.exit(app.exec())
















