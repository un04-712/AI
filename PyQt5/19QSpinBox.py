"""
    计数器控件
"""
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QSpinBox, QApplication, QVBoxLayout


class mainWidget(QWidget):
    def __init__(self):
        super().__init__()  #QWidget.__init__(self)
        #修改窗口标题
        self.setWindowTitle("计数器控件的使用")
        #修改窗口大小
        self.resize(888,888)
        #设置窗口位置
        self.move(666,666)
        mainLayout = QVBoxLayout(self)
        self.spinbox = QSpinBox()
        mainLayout.addWidget( self.spinbox)


        """基本参数设置"""
        #设置范围
        self.spinbox.setRange(10,30)
        # 设置初始值
        self.spinbox.setValue(29)
        #设置步长
        self.spinbox.setSingleStep(5)#键盘操作(左右方向键)才有效
        #设置当前值

        #打印当前值
        print(self.spinbox.value())

        #发出值变化,连接槽函数
        self.spinbox.valueChanged.connect(self.vlaue_change_slot)

    def value_change_slot(self):
        pass



if __name__ == '__main__':
    #创建qApplication类
    app = QApplication(sys.argv)

    #创建窗口对象,QWidget为UI界面
    window = mainWidget()

    #显示窗口
    window.show()

    #程序关闭之后释放资源
    sys.exit(app.exec())
