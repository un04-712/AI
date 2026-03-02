from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap, QMovie
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit
import sys

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("购物管理系统")
        self.resize(650,550)
        self.move(30,30)
        self.ui_init()

    def ui_init(self):
        #图片
        image = QLabel(self)
        image.setPixmap(QPixmap('../images/购物.png'))
        image.resize(100,100)
        image.move(250,30)
        image.setScaledContents(True)
        text = QLabel(self)
        # 显示文本
        text.setText("购物管理系统")
        # 显示样式
        text.setStyleSheet("""
                  font-family:宋体;
                  font-size:30px;
                  font-weight:bold;   /* bold 加粗字体 */
              """)
        # 设置显示位置
        text.move(210,160)


        #用户名输入框
        UserNameEdit = QLineEdit(self)
        UserNameEdit.move(200,210)
        UserNameEdit.resize(200, 45)
        #密码输入框
        PassNameEdit = QLineEdit(self)
        PassNameEdit.move(200, 280)
        PassNameEdit.resize(200, 45)
        #用户名图标
        image_user = QLabel(self)
        image_user.setPixmap(QPixmap('../images/账号.png'))
        image_user.move(135, 215)
        image_user.resize(40, 40)
        image_user.setScaledContents(True)

        #密码图标
        image_pwd = QLabel(self)
        image_pwd.setPixmap(QPixmap('../images/密码.png'))
        image_pwd.move(135,285)
        image_pwd.resize(40, 40)
        image_pwd.setScaledContents(True)

        reBtn = QPushButton(self)
        reBtn.setText('登录')
        reBtn.resize(140,40)
        reBtn.move(135,360)
        reBtn.setStyleSheet("""
            QPushButton{
                    background-color: #4CAF50;
                    color: white;  
            }
        """)


        reBtn = QPushButton(self)
        reBtn.setText('注册')
        reBtn.resize(140, 40)
        reBtn.move(300, 360)
        reBtn.setStyleSheet("""
            QPushButton{
                 background-color:  #2196F3;
                color: white;  
            }
        """)







        """编辑框样式设置"""
        edit = """
            QLineEdit{
                border : 2px solid white;
                
            }
            QLineEdit:hover{
                border-color:white; 
            }
            QLineEdit:focus{
                border-color:white; 
                background-color:white;
            }
        """
        UserNameEdit.setStyleSheet(edit)
        PassNameEdit.setStyleSheet(edit)
        PassNameEdit.setPlaceholderText('请输入用户名或邮箱')
        UserNameEdit.setPlaceholderText('请输入密码')


        PassNameEdit.setEchoMode(QLineEdit.Password)




if __name__ == '__main__':
    # 创建qApplication类
    app = QApplication(sys.argv)

    # 创建窗口对象,QWidget为UI界面
    window = MainWidget()

    # 显示窗口
    window.show()

    # 程序关闭之后释放资源
    sys.exit(app.exec())
