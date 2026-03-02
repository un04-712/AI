import requests
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QButtonGroup, QRadioButton, QPushButton, QVBoxLayout, \
    QHBoxLayout, QMessageBox


class RegisterDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('用户注册')
        self.resize(400, 300)

        # 创建主布局
        main_layout = QVBoxLayout()
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(30, 30, 30, 30)

        # 标题
        title_label = QLabel('创建新账户')
        title_label.setStyleSheet('font-size: 20px; font-weight: bold;')
        title_label.setAlignment(Qt.AlignCenter)

        # 用户名
        username_layout = QHBoxLayout()
        username_label = QLabel('用户名:')
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText('请输入用户名')
        username_layout.addWidget(username_label)
        username_layout.addWidget(self.username_input)

        # 邮箱
        email_layout = QHBoxLayout()
        email_label = QLabel('邮  箱:')
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText('请输入邮箱')
        email_layout.addWidget(email_label)
        email_layout.addWidget(self.email_input)

        # 密码
        password_layout = QHBoxLayout()
        password_label = QLabel('密  码:')
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setPlaceholderText('请输入密码')
        password_layout.addWidget(password_label)
        password_layout.addWidget(self.password_input)

        # 确认密码
        confirm_layout = QHBoxLayout()
        confirm_label = QLabel('确认密码:')
        self.confirm_input = QLineEdit()
        self.confirm_input.setEchoMode(QLineEdit.Password)
        self.confirm_input.setPlaceholderText('请再次输入密码')
        confirm_layout.addWidget(confirm_label)
        confirm_layout.addWidget(self.confirm_input)

        # 按钮
        button_layout = QHBoxLayout()
        button_layout.setSpacing(20)

        self.register_btn = QPushButton('注册')
        self.register_btn.setStyleSheet('''
            QPushButton {
                padding: 8px 16px; 
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 4px;
            }
        ''')
        self.register_btn.clicked.connect(self.handle_register)

        self.cancel_btn = QPushButton('取消')
        self.cancel_btn.setStyleSheet('''
            QPushButton {
                padding: 8px 16px; 
                background-color: #f44336;
                color: white;
                border: none;
                border-radius: 4px;
            }
        ''')
        self.cancel_btn.clicked.connect(self.close)

        button_layout.addWidget(self.register_btn)
        button_layout.addWidget(self.cancel_btn)

        # 添加到主布局
        main_layout.addWidget(title_label)
        main_layout.addLayout(username_layout)
        main_layout.addLayout(email_layout)
        main_layout.addLayout(password_layout)
        main_layout.addLayout(confirm_layout)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def handle_register(self):
        username = self.username_input.text().strip()
        email = self.email_input.text().strip()
        password = self.password_input.text().strip()
        confirm_password = self.confirm_input.text().strip()

        # 本地验证
        if not username:
            QMessageBox.warning(self, '提示', '请输入用户名')
            return

        if not email:
            QMessageBox.warning(self, '提示', '请输入邮箱')
            return

        if not password:
            QMessageBox.warning(self, '提示', '请输入密码')
            return

        if password != confirm_password:
            QMessageBox.warning(self, '提示', '两次输入的密码不一致')
            return

        if len(password) < 6:
            QMessageBox.warning(self, '提示', '密码长度不能少于6位')
            return

        # 发送注册请求到后端
        try:
            url = 'http://127.0.0.1:8080/user/register'
            data = {
                'username': username,
                'password': password,
                'email': email
            }

            response = requests.post(url, json=data)

            if response.status_code == 200:
                QMessageBox.information(self, '成功', '注册成功，请登录')
                self.close()
            else:
                error_msg = response.json().get('detail', '注册失败')
                QMessageBox.warning(self, '失败', error_msg)

        except requests.exceptions.ConnectionError:
            QMessageBox.warning(self, '错误', '无法连接到服务器，请确保后端已启动')
        except Exception as e:
            QMessageBox.warning(self, '错误', f'注册失败: {str(e)}')