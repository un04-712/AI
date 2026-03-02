import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QFormLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class LoginWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("购物管理系统")
        self.resize(400, 300)
        self.move(300, 150)
        self.setupUi()

    def setupUi(self):
        # 设置窗口布局
        mainLayout = QVBoxLayout()

        # 添加标题
        title = QLabel('购物管理系统')
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 24px;")
        mainLayout.addWidget(title)

        # 添加图标
        icon = QLabel()
        icon.setPixmap(QPixmap('../images/lock.png').scaled(50, 50, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        icon.setAlignment(Qt.AlignCenter)
        mainLayout.addWidget(icon)

        # 创建表单布局
        formLayout = QFormLayout()

        # 用户名输入框
        self.usernameEdit = QLineEdit()
        self.usernameEdit.setPlaceholderText('用户名或邮箱')
        formLayout.addRow(QLabel(''), self.usernameEdit)

        # 密码输入框
        self.passwordEdit = QLineEdit()
        self.passwordEdit.setEchoMode(QLineEdit.Password)
        self.passwordEdit.setPlaceholderText('密码')
        formLayout.addRow(QLabel(''), self.passwordEdit)

        # 添加表单布局到主布局
        mainLayout.addLayout(formLayout)

        # 创建按钮布局
        buttonLayout = QHBoxLayout()

        # 登录按钮
        self.loginBtn = QPushButton('登录')
        self.loginBtn.setStyleSheet("background-color: #4CAF50; color: white;")
        buttonLayout.addWidget(self.loginBtn)

        # 注册按钮
        self.registerBtn = QPushButton('注册')
        self.registerBtn.setStyleSheet("background-color: #2196F3; color: white;")
        buttonLayout.addWidget(self.registerBtn)

        # 添加按钮布局到主布局
        mainLayout.addLayout(buttonLayout)

        # 设置主布局
        self.setLayout(mainLayout)

        # 连接信号和槽
        self.loginBtn.clicked.connect(self.onLoginClicked)
        self.registerBtn.clicked.connect(self.onRegisterClicked)

    def onLoginClicked(self):
        username = self.usernameEdit.text()
        password = self.passwordEdit.text()
        print(f"登录: 用户名={username}, 密码={password}")

    def onRegisterClicked(self):
        print("注册按钮被点击")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWidget()
    window.show()
    sys.exit(app.exec_())




