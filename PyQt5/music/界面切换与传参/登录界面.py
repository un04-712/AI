import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit,
                             QPushButton, QCheckBox, QVBoxLayout, QHBoxLayout,
                             QFrame, QMessageBox)
from PyQt5.QtGui import QPixmap, QFont, QPalette, QBrush
from PyQt5.QtCore import Qt


class QQLoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口标题和大小
        self.setWindowTitle('QQ登录')
        self.setFixedSize(400, 500)

        # 设置窗口背景
        self.set_background()

        # 创建主布局
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(50, 30, 50, 30)
        main_layout.setSpacing(20)

        # 添加QQ图标
        self.add_qq_logo(main_layout)

        # 添加账号输入框
        self.account_input = self.create_input_field("账号", main_layout)

        # 添加密码输入框
        self.password_input = self.create_input_field("密码", main_layout, is_password=True)

        # 添加记住密码和自动登录选项
        self.add_checkboxes(main_layout)

        # 添加登录按钮
        self.add_login_button(main_layout)

        # 添加注册和忘记密码链接
        self.add_links(main_layout)

        # 设置主布局
        self.setLayout(main_layout)

        # 居中显示窗口
        self.center_window()

    def set_background(self):
        """设置窗口背景"""
        palette = QPalette()
        # 使用淡蓝色作为背景
        palette.setBrush(QPalette.Window, QBrush(Qt.lightGray))
        self.setPalette(palette)

    def add_qq_logo(self, layout):
        """添加QQ图标"""
        logo_label = QLabel()
        # 创建一个简单的QQ图标替代（实际使用时可以替换为真实的QQ图标）
        pixmap = QPixmap(100, 100)
        pixmap.fill(Qt.transparent)
        logo_label.setPixmap(pixmap.scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        logo_label.setAlignment(Qt.AlignCenter)

        # 添加QQ文字
        qq_text = QLabel("QQ")
        qq_text.setFont(QFont("SimHei", 24, QFont.Bold))
        qq_text.setAlignment(Qt.AlignCenter)

        # 创建垂直布局放置图标和文字
        logo_layout = QVBoxLayout()
        logo_layout.addWidget(logo_label)
        logo_layout.addWidget(qq_text)

        layout.addLayout(logo_layout)

    def create_input_field(self, placeholder, layout, is_password=False):
        """创建输入框，修复了边框设置错误"""
        frame = QFrame()
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 5px;
                border: 1px solid #CCCCCC;
            }
        """)

        input_layout = QHBoxLayout(frame)
        input_layout.setContentsMargins(10, 5, 10, 5)

        # 添加图标（使用QPixmap和QLabel正确显示图标）
        icon_label = QLabel()
        # 创建一个简单的图标替代（实际使用时可以加载真实图标）
        pixmap = QPixmap(20, 20)
        if placeholder == "账号":
            pixmap.fill(Qt.gray)  # 账号图标占位
        else:
            pixmap.fill(Qt.darkGray)  # 密码图标占位
        icon_label.setPixmap(pixmap)
        icon_label.setFixedSize(20, 20)

        # 添加输入框
        input_field = QLineEdit()
        input_field.setPlaceholderText(placeholder)
        # 使用样式表代替setBorder(0)
        input_field.setStyleSheet("border: none;")
        input_field.setFont(QFont("SimHei", 12))
        if is_password:
            input_field.setEchoMode(QLineEdit.Password)

        input_layout.addWidget(icon_label)
        input_layout.addWidget(input_field)

        layout.addWidget(frame)
        return input_field

    def add_checkboxes(self, layout):
        """添加复选框"""
        checkbox_layout = QHBoxLayout()

        # 记住密码
        self.remember_checkbox = QCheckBox("记住密码")
        self.remember_checkbox.setFont(QFont("SimHei", 10))

        # 自动登录
        self.auto_login_checkbox = QCheckBox("自动登录")
        self.auto_login_checkbox.setFont(QFont("SimHei", 10))

        checkbox_layout.addWidget(self.remember_checkbox)
        checkbox_layout.addStretch(1)
        checkbox_layout.addWidget(self.auto_login_checkbox)

        layout.addLayout(checkbox_layout)

    def add_login_button(self, layout):
        """添加登录按钮"""
        login_button = QPushButton("登录")
        login_button.setFont(QFont("SimHei", 14, QFont.Bold))
        login_button.setStyleSheet("""
            QPushButton {
                background-color: #2B79D9;
                color: white;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #3B89E9;
            }
            QPushButton:pressed {
                background-color: #1B69C9;
            }
        """)
        login_button.clicked.connect(self.login)

        layout.addWidget(login_button)

    def add_links(self, layout):
        """添加注册和忘记密码链接"""
        link_layout = QHBoxLayout()

        # 注册账号
        register_link = QLabel('<a href="#">注册账号</a>')
        register_link.setFont(QFont("SimHei", 10))
        register_link.setTextInteractionFlags(Qt.TextBrowserInteraction)
        register_link.setOpenExternalLinks(False)
        register_link.linkActivated.connect(self.register)

        # 忘记密码
        forget_link = QLabel('<a href="#">忘记密码</a>')
        forget_link.setFont(QFont("SimHei", 10))
        forget_link.setTextInteractionFlags(Qt.TextBrowserInteraction)
        forget_link.setOpenExternalLinks(False)
        forget_link.linkActivated.connect(self.forget_password)

        link_layout.addWidget(register_link)
        link_layout.addStretch(1)
        link_layout.addWidget(forget_link)

        layout.addLayout(link_layout)

        # 添加底部空白
        layout.addStretch(1)

    def center_window(self):
        """将窗口居中显示"""
        qr = self.frameGeometry()
        cp = QApplication.desktop().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def login(self):
        """处理登录逻辑"""
        account = self.account_input.text()
        password = self.password_input.text()

        if not account or not password:
            QMessageBox.warning(self, "提示", "请输入账号和密码")
            return

        # 这里可以添加实际的登录验证逻辑
        QMessageBox.information(self, "提示", f"账号: {account}\n登录成功!")

    def register(self):
        """处理注册逻辑"""
        QMessageBox.information(self, "提示", "跳转到注册页面")

    def forget_password(self):
        """处理忘记密码逻辑"""
        QMessageBox.information(self, "提示", "跳转到找回密码页面")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 确保中文正常显示
    font = QFont("SimHei")
    app.setFont(font)

    window = QQLoginWindow()
    window.show()
    sys.exit(app.exec_())
