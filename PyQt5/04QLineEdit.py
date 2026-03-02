
import sys

from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator
from PyQt5.QtWidgets import QApplication, QWidget,QLineEdit


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('单行编辑框使用')
        self.resize(700,700)
        self.ui_init()

    def ui_init(self):
        UserNameEdit = QLineEdit(self)
        PassNameEdit = QLineEdit(self)
        UserNameEdit.move(100,100)
        PassNameEdit.move(100,300)
        UserNameEdit.resize(200, 45)
        PassNameEdit.resize(200, 45)
        """编辑框样式设置"""
        edit = """
            QLineEdit{
                border : 2px solid gray;
                border-radius : 15px;
            }
            QLineEdit:hover{
                border-color:white; 
            }
            QLineEdit:focus{
                border-color:#DEEBDC; 
                background-color:#DEEBDC;
            }
        """
        UserNameEdit.setStyleSheet(edit)
        PassNameEdit.setStyleSheet(edit)

        """占位符文本设置"""
        UserNameEdit.setPlaceholderText('请输入用户名或邮箱')
        PassNameEdit.setPlaceholderText('请输入密码')

        """回显模式"""
        # PassNameEdit.setEchoMode(QLineEdit.NoEcho)  #不显示任何输入内容
        PassNameEdit.setEchoMode(QLineEdit.Password)    #以密文形式显示输入内容
        # PassNameEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)    #编辑时显示明文，失去焦点时显示密文

        """设置验证器"""
        # PassNameEdit.setValidator(QIntValidator())  #整数验证器,只允许输入数字
        # PassNameEdit.setValidator(QDoubleValidator())  #小数验证器,只允许输入小数
        PassNameEdit.setValidator(QRegExpValidator(QRegExp('[0-9a-z]+')))  #正则验证器，只允许数字和小写字母

        """得到输入框里面的内容"""


if __name__ == '__main__':

    app = QApplication(sys.argv)

    window = MainWidget()

    window.show()

    sys.exit(app.exec())