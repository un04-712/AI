import sys
import sqlite3
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit,
                             QPushButton, QVBoxLayout, QHBoxLayout,
                             QMessageBox, QDialog, QFrame)
from PyQt5.QtCore import Qt
import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from threading import Thread
import time

# 后端API部分
app = FastAPI()


# 数据模型
class UserRegister(BaseModel):
    username: str
    password: str
    email: str


class UserLogin(BaseModel):
    username: str
    password: str


# 数据库操作
def init_db():
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    # 创建用户表
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_info (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    conn.commit()
    conn.close()


# 初始化数据库
init_db()


# 注册接口
@app.post("/user/register")
def register(user: UserRegister):
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()

    try:
        # 检查用户名是否已存在
        cursor.execute("SELECT * FROM user_info WHERE username = ?", (user.username,))
        if cursor.fetchone():
            raise HTTPException(status_code=400, detail="用户名已存在")

        # 检查邮箱是否已存在
        cursor.execute("SELECT * FROM user_info WHERE email = ?", (user.email,))
        if cursor.fetchone():
            raise HTTPException(status_code=400, detail="邮箱已被注册")

        # 插入新用户
        cursor.execute(
            "INSERT INTO user_info (username, password, email) VALUES (?, ?, ?)",
            (user.username, user.password, user.email)
        )
        conn.commit()
        return {"message": "注册成功"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        conn.close()


# 登录接口
@app.post("/user/login")
def login(user: UserLogin):
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()

    try:
        cursor.execute(
            "SELECT * FROM user_info WHERE username = ? AND password = ?",
            (user.username, user.password)
        )
        user_data = cursor.fetchone()

        if not user_data:
            raise HTTPException(status_code=401, detail="用户名或密码错误")

        return {"message": "登录成功", "username": user.username}
    finally:
        conn.close()


# 启动后端服务的函数
def start_backend():
    uvicorn.run(app, host="127.0.0.1", port=8080)


# 注册对话框
class RegisterDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('登录管理系统')
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


# 首页界面
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


# 主函数
def main():
    # 启动后端服务线程
    backend_thread = Thread(target=start_backend, daemon=True)
    backend_thread.start()

    # 等待后端服务启动
    time.sleep(1)

    # 启动前端界面
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()