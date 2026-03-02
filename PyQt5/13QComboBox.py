from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QComboBox, QLabel
import sys




"""
    常用的窗口创建方式
"""
class mainWidget(QWidget):
    def __init__(self):
        super().__init__()  #QWidget.__init__(self)
        #修改窗口标题
        self.setWindowTitle("下拉框的使用")
        #修改窗口大小
        self.resize(300,300)
        #设置窗口位置
        self.move(666,666)
        mainLayout = QHBoxLayout(self)
        self.ui_init(mainLayout)
    def ui_init(self,layout):
        layout.addWidget(QLabel('模型:'))
        Combo = QComboBox()
        layout.addWidget(Combo)
        Combo.addItem('YOLOv5')
        Combo.addItem('YOLOv6')
        Combo.addItem('YOLOv7')
        Combo.addItem('YOLOv8')





if __name__ == '__main__':
    #创建qApplication类
    app = QApplication(sys.argv)

    #创建窗口对象,QWidget为UI界面
    window = mainWidget()

    #显示窗口
    window.show()

    #程序关闭之后释放资源
    sys.exit(app.exec())
