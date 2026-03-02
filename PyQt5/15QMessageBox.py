from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QMessageBox
import sys




"""
    常用的窗口创建方式
"""
class mainWidget(QWidget):
    def __init__(self):
        super().__init__()  #QWidget.__init__(self)
        #修改窗口标题
        self.setWindowTitle("消息框的使用")
        #修改窗口大小
        self.resize(888,888)
        #设置窗口位置
        self.move(300,300)
        mainLayout = QVBoxLayout(self)

        self.button =[]#存储列表对象

        for text in ["关于对话框",'显示消息对话框','显示错误对话框','显示警告对话框','显示提问对话框']:
            self.button.append(QPushButton(text))
            mainLayout.addWidget(self.button[-1])

        #绑定槽函数
        for button in self.button:
            button.clicked.connect(self.dialog)

    def dialog(self):
        res = self.sender().text()
        if res in '关于对话框':
            QMessageBox.about(None,'关于对话框','这是关于对话框')
        elif res in '显示消息对话框':
            QMessageBox.information(None,'消息对话框','这是显示消息对话框')
        elif res in '显示错误对话框':
            QMessageBox.critical(None,'错误对话框','这是显示错误对话框')
        elif res in '显示警告对话框':
            result =  QMessageBox.warning(None,'警告对话框','这是警告对话框',QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
            if result == QMessageBox.Yes:
                print('用户选择了Yes')
            else:
                print('用户选择了No')
        elif res in '显示提问对话框':
            result = QMessageBox.question(None,'显示提问对话框','这是显示提问对话框',QMessageBox.Yes|QMessageBox.No,QMessageBox.No)

            if result == QMessageBox.Yes:
                print('用户选择了对的')
            else:
                print('用户选择了错的')




if __name__ == '__main__':
    #创建qApplication类
    app = QApplication(sys.argv)

    #创建窗口对象,QWidget为UI界面
    window = mainWidget()

    #显示窗口
    window.show()

    #程序关闭之后释放资源
    sys.exit(app.exec())
