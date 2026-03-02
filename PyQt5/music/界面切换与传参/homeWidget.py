import requests
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QMessageBox, QHBoxLayout, QLabel, QFrame

from music.界面切换与传参.RegisterDialog import RegisterDialog

"""常用创建窗口的方式"""
# 继承QWidget类所有的属性和方法
class HomeWidget(QWidget):
    def __init__(self, parent=None, username=None):
        super().__init__(parent)
        self.parent = parent
        self.username = username
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('首页')
        self.resize(600, 400)

        layout = QVBoxLayout()

        welcome_label = QLabel(f'欢迎回来，{self.username}！')
        welcome_label.setStyleSheet('font-size: 24px; margin: 20px;')
        welcome_label.setAlignment(Qt.AlignCenter)

        logout_btn = QPushButton('退出登录')
        logout_btn.setStyleSheet('''
            QPushButton {
                padding: 10px 20px; 
                font-size: 14px;
                background-color: #f44336;
                color: white;
                border: none;
                border-radius: 4px;
                margin: 20px;
            }
        ''')
        logout_btn.clicked.connect(self.logout)

        layout.addWidget(welcome_label)
        layout.addWidget(logout_btn)

        self.setLayout(layout)

    def logout(self):
        self.close()
        if self.parent:
            self.parent.show()


# 登录窗口
class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('用户登录')
        self.resize(500, 400)

        # 创建主布局
        main_layout = QVBoxLayout()
        main_layout.setSpacing(20)
        main_layout.setContentsMargins(50, 50, 50, 50)

        # 标题
        title_label = QLabel('用户登录')
        title_label.setStyleSheet('font-size: 28px; font-weight: bold;')
        title_label.setAlignment(Qt.AlignCenter)

        # 用户名
        username_layout = QHBoxLayout()
        username_label = QLabel('用户名:')
        username_label.setStyleSheet('font-size: 14px;')
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText('请输入用户名')
        self.username_input.setStyleSheet('padding: 8px;')
        username_layout.addWidget(username_label)
        username_layout.addWidget(self.username_input)

        # 密码
        password_layout = QHBoxLayout()
        password_label = QLabel('密  码:')
        password_label.setStyleSheet('font-size: 14px;')
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setPlaceholderText('请输入密码')
        self.password_input.setStyleSheet('padding: 8px;')
        password_layout.addWidget(password_label)
        password_layout.addWidget(self.password_input)
        # 分隔线
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        # 按钮
        button_layout = QHBoxLayout()
        button_layout.setSpacing(20)

        self.login_btn = QPushButton('登录')
        self.login_btn.setStyleSheet('''
            QPushButton {
                padding: 10px 20px; 
                font-size: 14px;
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        ''')
        self.login_btn.clicked.connect(self.handle_login)

        self.register_btn = QPushButton('注册')
        self.register_btn.setStyleSheet('''
            QPushButton {
                padding: 10px 20px; 
                font-size: 14px;
                background-color: #2196F3;
                color: white;
                border: none;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #0b7dda;
            }
        ''')
        self.register_btn.clicked.connect(self.show_register_dialog)

        button_layout.addWidget(self.login_btn)
        button_layout.addWidget(self.register_btn)

        # 添加到主布局
        main_layout.addWidget(title_label)
        main_layout.addLayout(username_layout)
        main_layout.addLayout(password_layout)
        main_layout.addWidget(line)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def handle_login(self):
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()

        # 本地验证
        if not username:
            QMessageBox.warning(self, '提示', '请输入用户名')
            return

        if not password:
            QMessageBox.warning(self, '提示', '请输入密码')
            return

        # 发送登录请求到后端
        try:
            url = 'http://127.0.0.1:8080/user/login'
            data = {
                'username': username,
                'password': password
            }
            response = requests.post(url, json=data)
            if response.status_code == 200:
                # 登录成功，显示首页
                self.hide()
                self.home_widget = HomeWidget(self, username)
                self.home_widget.show()
            else:
                error_msg = response.json().get('detail', '登录失败')
                QMessageBox.warning(self, '失败', error_msg)

        except requests.exceptions.ConnectionError:
            QMessageBox.warning(self, '错误', '无法连接到服务器，请确保后端已启动')
        except Exception as e:
            QMessageBox.warning(self, '错误', f'登录失败: {str(e)}')

    def show_register_dialog(self):
        # 显示注册对话框
        self.register_dialog = RegisterDialog(self)
        self.register_dialog.exec_()