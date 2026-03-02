"""
    单选按钮控件
"""
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication,QWidget,QHBoxLayout,QRadioButton
import sys

"""常用创建窗口的方式"""
# 继承QWidget类所有的属性和方法
class mainWidget(QWidget):
    def __init__(self):
        # 初始化父类的__init__方法 将self参数传进去
        super().__init__()  # QWidget.__init__(self)
        # 修改窗口标题
        self.setWindowTitle("创建pyqt窗口")
        # 修改窗口大小
        self.resize(500, 300)
        layout = QHBoxLayout(self)

        radionBtn1 = QRadioButton("单选按钮1")
        radionBtn2 = QRadioButton("单选按钮2")

        radionBtn1.setChecked(True)

        layout.addWidget(radionBtn1)
        layout.addWidget(radionBtn2)

        radionBtn2.toggled.connect(self.buttonState)
        radionBtn1.toggled.connect(self.buttonState)
    def buttonState(self):
        radioButton =  self.sender()  # 获取发送信号的对象 即触发的槽函数控件
        print(f"{radioButton.text()}: {radioButton.isChecked()}")



if __name__ == '__main__':
    """程序启动的基本流程"""
    # 创建qApplication类   sys.argv为了通过命令行传参，但是大部分场景已经不在需要
    # print(sys.argv)
    app = QApplication(sys.argv)
    # 创建窗口对象 QWidget为UI界面
    window =  mainWidget()
    # 显示窗口
    window.show()
    # 程序关闭之后自动释放资源
    sys.exit(app.exec_())
