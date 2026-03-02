import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QVBoxLayout


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('复选框的使用')
        self.resize(800,800)
        MainLayout = QVBoxLayout(self)
        self.ui_init(MainLayout)

    def ui_init(self,layout):

        checkboxsetsheet ="""
            QCheckBox{
                background-color: #2D5A78;
                color:white;
                font-weight:bold;
                font-size:24px;
                border-radius:5px;
                padding:10px;
            }
            QCheckBox:hover{
                background-color: orange;
            }
            QCheckBox:checked{
                background-color: green;
            }
            QCheckBox:indeterminate{
                background-color: #DBD652;
            }
        """
        self.checkbox1 = QCheckBox('摔倒检测', self)
        self.checkbox1.setStyleSheet(checkboxsetsheet)

        checkbox2 = QCheckBox('风水检测', self)
        checkbox2.setStyleSheet(checkboxsetsheet)

        self.checkbox3 = QCheckBox('目标跟踪', self)
        self.checkbox3.setStyleSheet(checkboxsetsheet)

        layout.addWidget(self.checkbox1)
        layout.addWidget(checkbox2)
        layout.addWidget(self.checkbox3)

        """设置默认方法"""
        self.checkbox1.setChecked(True)
        checkbox2.setChecked(False)

        """设置三态模式"""
        self.checkbox3.setTristate(True) #启用三态模式
        self.checkbox3.setCheckState(Qt.PartiallyChecked)


        self.checkbox1.stateChanged.connect(self.CheckBoxState)
        self.checkbox3.stateChanged.connect(self.CheckBoxState)
    def CheckBoxState(self):
        print('checkbox')
        """
             3种状态
                 未选中：0
                 半选中：1
                 选中：2
             QCheckBox1.text() ：获取控件文本内容
             QCheckBox1.isChecked() ： 获取被勾选的状态布尔值
             QCheckBox1.checkState()： 获取状态编号
        """

        print(f"{self.checkbox1.text()}:{self.checkbox1.isChecked()}:{self.checkbox1.checkState()}")
        print(f"{self.checkbox3.text()}:{self.checkbox3.isChecked()}:{self.checkbox3.checkState()}")


if __name__ == '__main__':

    app = QApplication(sys.argv)

    window = MainWidget()

    window.show()

    sys.exit(app.exec())

"""
    复选框
"""


# from PyQt5.QtGui import QIcon
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QVBoxLayout
# import sys
#
#
# """常用创建窗口的方式"""
# # 继承QWidget类所有的属性和方法
# class mainWidget(QWidget):
#     def __init__(self):
#         # 初始化父类的__init__方法 将self参数传进去
#         super().__init__()  # QWidget.__init__(self)
#         # 修改窗口标题
#         self.setWindowTitle("复选框使用")
#         # 修改窗口大小
#         self.resize(400, 300)
#         mainLayout = QVBoxLayout(self)
#         self.ui_init(mainLayout)
#
#     def ui_init(self,layout):
#
#        checkBoxStysheet ="""
#         QCheckBox{
#                     background-color: #2D5A7B;
#                     color:white;
#                     font-size:20px;
#                     font-weight:bold;
#                     border-radius:10px;
#                     padding:10px;
#                     }
#         QCheckBox:hover{
#                     border:2px solid #4D9BD4;
#                     }
#         QCheckBox:checked{
#                     background-color: #4CB051;
#                     }
#         QCheckBox:indeterminate{ /*半选中状态*/
#                     background-color: orange;
#                     }
#        """
#        self.checkbox1 =  QCheckBox("摔倒检测",self)
#        self.checkbox1.setStyleSheet(checkBoxStysheet)
#
#        checkbox2 = QCheckBox("风水检测", self)
#        checkbox2.setStyleSheet(checkBoxStysheet)
#
#        self.checkbox3 = QCheckBox("目标跟踪", self)
#        self.checkbox3.setStyleSheet(checkBoxStysheet)
#
#        layout.addWidget(self.checkbox1)
#        layout.addWidget(checkbox2)
#        layout.addWidget(self.checkbox3)
#
#
#        """基本设置"""
#        self.checkbox1.setChecked(True)
#        checkbox2.setChecked(False)
#
#        # 设置三态模式
#        self.checkbox3.setTristate(True)  #启用三态模式
#        self.checkbox3.setCheckState(Qt.PartiallyChecked)  # 设置为半选中状态
#
#        self.checkbox1.stateChanged.connect(self.checkBoxState)  # 状态改变时触发
#        self.checkbox3.stateChanged.connect(self.checkBoxState)  # 状态改变时触发
#
#
#     def checkBoxState(self):
#         # print("checkBoxState")
#         """
#                 3种状态
#                     未选中：0
#                     半选中：1
#                     选中：2
#                 QCheckBox1.text() ：获取控件文本内容
#                 QCheckBox1.isChecked() ： 获取被勾选的状态布尔值
#                 QCheckBox1.checkState()： 获取状态编号
#          """
#         print(f"{self.checkbox1.text()}:{self.checkbox1.isChecked()}:{self.checkbox1.checkState()}")
#         print(f"{self.checkbox3.text()}:{self.checkbox3.isChecked()}:{self.checkbox3.checkState()}")
#
#
#
#
# if __name__ == '__main__':
#     """程序启动的基本流程"""
#     # 创建qApplication类   sys.argv为了通过命令行传参，但是大部分场景已经不在需要
#     # print(sys.argv)
#     app = QApplication(sys.argv)
#     # 创建窗口对象 QWidget为UI界面
#     window =  mainWidget()
#     # 显示窗口
#     window.show()
#     # 程序关闭之后自动释放资源
#     sys.exit(app.exec_())
