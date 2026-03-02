"""
    网格布局    QGridLayout:控件从上到下排,默认情况为等间距
              addWidget 将控件加入到布局中
              addLayout 将子布局加入到布局中
              addSpacing 为布局添加空隙
              setContentsMargins 设置内边距

"""
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QGridLayout
import sys

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()  #QWidget.__init__(self)
        #修改窗口标题
        self.setWindowTitle("网格布局")
        #修改窗口大小
        self.resize(800,800)
        #设置窗口位置
        self.move(300,300)
        self.ui_init()
    def ui_init(self):
        #创建水平布局
        MainLayout = QGridLayout()
        #创建按钮
        btn1 = QPushButton(text='按钮1')
        btn2 = QPushButton(text='按钮2')
        btn3 = QPushButton(text='按钮3')
        #将空间加入布局
        MainLayout.addWidget(btn1,0,0)
        MainLayout.addWidget(btn2,3,1)
        MainLayout.addWidget(btn3,1,0)
        #添加空隙
        MainLayout.setSpacing(100)
        #设置内边距  参数 左 上 右 下
        MainLayout.setContentsMargins(300,400,50,50)



        #设置对齐方式
        # MainLayout.setAlignment(Qt.AlignTop)
        #将布局加入到主控件
        self.setLayout(MainLayout)



if __name__ == '__main__':
    #创建qApplication类
    app = QApplication(sys.argv)

    #创建窗口对象,QWidget为UI界面
    window = MainWidget()

    #显示窗口
    window.show()

    #程序关闭之后释放资源
    sys.exit(app.exec())