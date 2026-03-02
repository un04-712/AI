from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QVBoxLayout
import sys


class mainWidget(QWidget):
    def __init__(self):
        super().__init__()  #QWidget.__init__(self)
        #修改窗口标题
        self.setWindowTitle("滑块的使用")
        #修改窗口大小
        self.resize(888,888)
        #设置窗口位置
        self.move(666,666)

        self.slider = QSlider(Qt.Horizontal)#水平方向
        # slider = QSlider(Qt.Vertical)  #垂直方向

        """基本参数设置"""
        #设置最小值
        self.slider.setMinimum(7)
        # 设置最大值
        self.slider.setMaximum(29)
        #设置步长
        self.slider.setSingleStep(5)#键盘操作(左右方向键)才有效
        #设置当前值
        self.slider.setValue(24)
        #打印当前值
        print(self.slider.value())

        #发出值变化，连接槽函数
        # self.slider.valueChanged.connect(self.vlaue_change_slot)



        mainLayout = QVBoxLayout(self)

        mainLayout.addWidget(self.slider)


        """样式设置"""
        self.slider1.setStyleSheet("""
                     /*滑槽(轨道)样式*/
                     QSlider::groove:horizontal{
                         background: #7E7F80;
                         height:7px;
                         border-radius:3px;
                     }/*滑块前面的轨道样式*/
                     QSlider::sub-page:horizontal{
                         background: #0067C0;    /*蓝色 */
                     }
                     /*滑块样式*/
                     QSlider::handle:horizontal{
                         background: #0067C0;  /*蓝色 */
                         width:14px;
                         height:14px;
                         border-radius:7px;
                         margin:-4px 0;
                         border : 2px solid white ;
                     }
                     /*鼠标悬停样式*/
                     QSlider::handle:hover{
                         background: #00437D;
                     }
                     /*按下样式*/
                     QSlider::handle:pressed{
                         background: #0089FF;
                     }

             """)




if __name__ == '__main__':
    #创建qApplication类
    app = QApplication(sys.argv)

    #创建窗口对象,QWidget为UI界面
    window = mainWidget()

    #显示窗口
    window.show()

    #程序关闭之后释放资源
    sys.exit(app.exec())
