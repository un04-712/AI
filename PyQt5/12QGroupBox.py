
"""
    组合框： 提供一个带有标题的边框容器，将相关控件组合在一起，使界面结构更清晰

    支持设置一个可选的复选框或单选按钮作为组的开关，控制整个组内控件的启用状态
"""
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QGroupBox, QVBoxLayout, QCheckBox, QPushButton
import sys

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('带开关的QGroupBox')
        self.resize(700,700)
        mainLayout = QVBoxLayout(self)
        self.ui_init(mainLayout)
    def ui_init(self,layout):
        GruopBox = QGroupBox('权限设置')
        GruopBox.setCheckable(True)  #启用开关功能
        layout.addWidget(GruopBox)

        #创建垂直布局
        MainLay = QVBoxLayout()

        checkbox1 = QCheckBox('允许修改资料')
        checkbox2 = QCheckBox('允许查看历史')
        checkbox3 = QPushButton('只读权限')
        checkbox4 = QPushButton('编辑权限')
        MainLay.addWidget(checkbox1)
        MainLay.addWidget(checkbox2)
        MainLay.addWidget(checkbox3)
        MainLay.addWidget(checkbox4)

        GruopBox.setLayout(MainLay)
        layout.setAlignment(Qt.AlignTop)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWidget()
    window.show()
    sys.exit(app.exec_())