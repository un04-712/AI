import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QRadioButton, QButtonGroup, QPushButton, QVBoxLayout, QHBoxLayout


class AccountCreation(QWidget):
    def __init__(self):
        super().__init__()
        self.ui_init()
        self.resize(550,650)

    def ui_init(self):
        # 设置窗口标题
        self.setWindowTitle('创建新账户')

        # 创建标签和输入框
        username_label = QLabel('用户名')
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText('请输入用户名')

        email_label = QLabel('邮箱')
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText('请输入邮箱地址')
        password_label = QLabel('密码')

        self.password_input = QLineEdit()
        self.password_input .setPlaceholderText('请输入密码')
        self.password_input.setEchoMode(QLineEdit.Password)

        confirm_password_label = QLabel('确认密码')
        self.confirm_password_input = QLineEdit()
        self.confirm_password_input.setPlaceholderText('请输入确认密码')
        self.confirm_password_input.setEchoMode(QLineEdit.Password)

        # 创建单选按钮
        self.account_type_group = QButtonGroup()
        self.user_radio = QRadioButton('普通用户')
        self.admin_radio = QRadioButton('管理员')
        self.account_type_group.addButton(self.user_radio)
        self.account_type_group.addButton(self.admin_radio)
        self.user_radio.setChecked(True)

        # 创建按钮
        self.create_button = QPushButton('创建账户')
        self.cancel_button = QPushButton('取消')

        # 创建布局
        layout = QVBoxLayout()
        layout.addWidget(username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(email_label)
        layout.addWidget(self.email_input)
        layout.addWidget(password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(confirm_password_label)
        layout.addWidget(self.confirm_password_input)

        radio_layout = QHBoxLayout()
        radio_layout.addWidget(self.user_radio)
        radio_layout.addWidget(self.admin_radio)
        layout.addLayout(radio_layout)

        button_layout = QVBoxLayout()
        button_layout.addWidget(self.create_button)
        button_layout.addWidget(self.cancel_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)

        # 设置窗口大小
        self.setGeometry(300, 300, 300, 200)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AccountCreation()
    ex.show()
    sys.exit(app.exec_())