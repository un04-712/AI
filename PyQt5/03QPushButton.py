"""
        信号与槽
            在QT中,信号与槽机制是一种给非常强大的通信机制,这是一个重要概念,特别是对于初学者来说,理解它对于编写Qt程序至关重要
            信号（signals)  是由对象在特定事件发生时发出的消息，例如，QPushButton有一个c1icked()信号，当用户点击按钮时发出。
            槽(Slots) : 是用来响应信号的方法。一个槽可以是任何函数，当其关联的信号被发出时，该槽函数将被调用。
            连接信号和槽:  使用Qobject::connect方法将信号连接到槽函数。当信号发出时，关联的槽函数会自动执行，

"""




import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600,600)
        self.ui_init()
    def ui_init(self):
        reBtn = QPushButton(self)
        reBtn.setText('注册')
        reBtn.resize(150,40)
        reBtn.move(70,200)

        reBtn = QPushButton(self)
        reBtn.setText('登录')
        reBtn.resize(150, 40)
        reBtn.move(320, 200)


        #
        # """设置样式"""
        # reBtn.setStyleSheet("""
        #     QPushButton{
        #         background:#59B7FD; /* 设置背景颜色 */
        #         color:white;    /* 设置字体颜色 */
        #         font-size:20px  /* 设置字体大小 */
        #         font-weight: bold /* bold 加粗字体 */
        #         border-radius:15px /*设置边框圆角 */
        #     }
        #     QPushButton:hover{
        #         background:#2DACEB;
        #     }
        #     QPushButton:press{
        #         background:#299BD4;
        #         padding-left :50px;
        #         padding-top : 120px;
        #     }
        #      QPushButton:disabled{
        #         background:gray;
        #
        #     }
        # """)

        # reBtn.clicked.connect(self.register)  # 将 clicked信号和register槽函数绑定在一起
        # reBtn.setEnabled(False)#启用或禁用按钮状态

    #
    # def register(self):
    #         int("注册功能")





if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWidget()

    window.show()

    sys.exit(app.exec())