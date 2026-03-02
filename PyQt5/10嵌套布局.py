from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QFrame, QHBoxLayout, QLineEdit, QPushButton
import sys

"""常用创建窗口的方式"""


# 继承QWidget类所有的属性和方法
class mainWidget(QWidget):
    def __init__(self):
        # 初始化父类的__init__方法 将self参数传进去
        super().__init__()  # QWidget.__init__(self)
        # 修改窗口标题
        self.setWindowTitle("购物管理系统")
        # 修改窗口大小
        self.resize(800, 700)
        # 设置窗口图标
        icon = QIcon('../images/购物.png')
        self.setWindowIcon(icon)

        self.ui_init()

    def ui_init(self):
        # 创建主布局为垂直布局
        mainLayout = QVBoxLayout()

        self.create_Log_Title(mainLayout)
        self.create_formFrame(mainLayout)
        # 将垂直布局加入到主控件中
        self.setLayout(mainLayout)

    def create_Log_Title(self, layout):
        # 创建Logo
        logoLabel = QLabel()
        pixmap = QPixmap("../images/购物.png")
        pixmap_scaled = pixmap.scaled(150, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        logoLabel.setPixmap(pixmap_scaled)
        logoLabel.setAlignment(Qt.AlignHCenter)
        layout.addWidget(logoLabel)  # 将控件加入到布局中

        # 创建文字标题
        titleLabel = QLabel("购物管理系统")
        titleLabel.setStyleSheet("""
            font-size:60px;
            font-weight:bold;
        """)
        titleLabel.setAlignment(Qt.AlignCenter)
        layout.addWidget(titleLabel)  # 将控件加入到布局中

    def create_formFrame(self, layout):
        formContainer = QFrame()

        formContainer.setStyleSheet("""
            background-color:white;
            padding:20px;     /*设置内边距*/
        """)

        layout.addWidget(formContainer)

        # 创建垂直布局
        formLayout = QVBoxLayout()

        # 创建账号栏
        usernameLayout = QHBoxLayout()
        usernameIcon = QLabel()
        usernameIcon.setPixmap(QPixmap("../images/账号.png"))
        usernameIcon.setFixedSize(100, 100)
        usernameIcon.setScaledContents(True)

        Editstylesheet = """
         QLineEdit{
                border : 2px solid gray;   /*边框颜色是灰色 细宽为2px solid 实线  */
                border-radius: 5px;    /* 边框圆角弧度 ： 15px*/
                background-color: #F0F0F0;
                font-size:30px;
            }
            QLineEdit:hover{    /*鼠标悬停*/
                border-color:#44C1D6;  

            }
            QLineEdit:focus{   /*聚焦*/
               border-color:green;  
               background-color: white;;

            }"""
        # ctrl shift alt
        self.usernameEdit = QLineEdit()
        self.usernameEdit.setStyleSheet(Editstylesheet)

        self.usernameEdit.setPlaceholderText("用户名或邮箱")
        self.usernameEdit.setMinimumHeight(70)  # 设置输入框最小高度

        usernameLayout.addWidget(usernameIcon)
        usernameLayout.addWidget(self.usernameEdit)
        formLayout.addLayout(usernameLayout)

        # 创建密码栏
        passwordLayout = QHBoxLayout()
        passwordIcon = QLabel()
        passwordIcon.setPixmap(QPixmap("../images/密码.png"))
        passwordIcon.setFixedSize(100, 100)
        passwordIcon.setScaledContents(True)

        self.passwordEdit = QLineEdit()
        self.passwordEdit.setStyleSheet(Editstylesheet)

        self.passwordEdit.setPlaceholderText("用户名或邮箱")
        self.passwordEdit.setMinimumHeight(70)  # 设置输入框最小高度

        passwordLayout.addWidget(passwordIcon)
        passwordLayout.addWidget(self.passwordEdit)

        formLayout.addLayout(passwordLayout)

        # 创建按钮栏
        buttonLayout = QHBoxLayout()
        loginButton = QPushButton("登录")
        loginButton.setStyleSheet("""
            QPushButton{
                        background: #4EAF4E;  /*设置背景颜色*/
                        color : white;   /*设置文字颜色*/
                        font-size :20px;
                        font-weight : bold;
                        border-radius  : 15px ; /*设置边框圆角*/ 
                }

                QPushButton:pressed{
                        background: #387D38;  /*设置背景颜色*/
                        padding-left  : 30px;  /*按钮按下时微调内边距 实现文字下压效果*/
                        padding-top  : 25px;  
                }
        """)
        loginButton.setMinimumHeight(50)  # 设置输入框最小高度
        registerButton = QPushButton("注册")
        registerButton.setStyleSheet("""
                    QPushButton{
                                background: #2196F3;  /*设置背景颜色*/
                                color : white;   /*设置文字颜色*/
                                font-size :20px;
                                font-weight : bold;
                                border-radius  : 15px ; /*设置边框圆角*/ 
                        }

                        QPushButton:pressed{
                                background: #186BAD;  /*设置背景颜色*/
                                padding-left  : 30px;  /*按钮按下时微调内边距 实现文字下压效果*/
                                padding-top  : 25px;  
                        }
                """)
        registerButton.setMinimumHeight(50)  # 设置输入框最小高度
        buttonLayout.addWidget(loginButton)
        buttonLayout.addWidget(registerButton)
        formLayout.addLayout(buttonLayout)

        loginButton.clicked.connect(self.login)

        # 将布局加入到formContainer
        formContainer.setLayout(formLayout)

    def login(self):
        print("登录功能")
        # 获取账号编辑框内容
        print(self.usernameEdit.text())
        # 获取密码编辑框内容
        print(self.passwordEdit.text())


if __name__ == '__main__':
    """程序启动的基本流程"""
    # 创建qApplication类   sys.argv为了通过命令行传参，但是大部分场景已经不在需要
    # print(sys.argv)
    app = QApplication(sys.argv)
    # 创建窗口对象 QWidget为UI界面
    window = mainWidget()
    # 显示窗口
    window.show()
    # 程序关闭之后自动释放资源
    sys.exit(app.exec_())
