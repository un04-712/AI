"""
   进度条 ：
"""
from PyQt5.QtCore import QTimer, Qt, QDir, QProcess
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, \
    QPushButton, QLineEdit, QListWidgetItem
import sys
"""常用创建窗口的方式  模拟资源"""


# 继承QWidget类所有的属性和方法
class mainWidget(QWidget):
    def __init__(self):
        # 初始化父类的__init__方法 将self参数传进去
        super().__init__()  # QWidget.__init__(self)
        # 修改窗口标题
        self.setWindowTitle("文件资源管理器")
        # 修改窗口大小
        self.resize(800, 500)
        self.filePath = './'  # 存储文件路径
        # 创建目录类对象
        self.dir = QDir('./')

        mainLayout = QVBoxLayout(self)

        pathlayout = QHBoxLayout()
        # 返回按钮
        backBtn = QPushButton("<-")
        backBtn.setMinimumHeight(50)
        pathlayout.addWidget(backBtn)
        backBtn.clicked.connect(self.back_btn_slot)


        # 路径输入框
        self.filepahtInput =  QLineEdit()
        self.filepahtInput.setMinimumHeight(50)
        self.filepahtInput.setText(self.filePath)
        pathlayout.addWidget(self.filepahtInput)

        mainLayout.addLayout(pathlayout)

        # 创建列表控件
        self.fileList =  QListWidget()
        mainLayout.addWidget(self.fileList)
        self.fileList.itemDoubleClicked.connect(self.updataFile)

        # 获取目录内容
        self.show_dir()


    def back_btn_slot(self):
        print("back_btn_slot")
        # 返回上一级目录  返回是否执行成功的状态
        result = self.dir.cdUp()
        if result:
            # 获取当前目录路径
           path =  self.dir.absolutePath()
           self.filepahtInput.setText(path)
           self.show_dir()
    def updataFile(self,item):
        print(item.text())

        result = self.dir.cd(item.text())
        if result:  # 目录
            # 获取当前目录路径
            path = self.dir.absolutePath()
            self.filepahtInput.setText(path)
            self.show_dir()
        else:   # 文件  python .\16QMainWindow与QFile.py .\temp\1.txt
            argv = []
            argv.append(r'C:\Users\86132\Desktop\PyQt5\16QMainWindow和QFile.py')
            argv.append(self.dir.absolutePath()+'/'+item.text())
            print(self.dir.absolutePath()+'/'+item.text())

            # 创建进程
            self.process =   QProcess(self)
            self.process.start('python',argv)  # python .\16QMainWindow与QFile.py .\temp\1.txt
    # 显示目录内容
    def show_dir(self):

        self.fileList.clear()
        # 获取当前目录里面的内容   os.path.listdir()
        # 设置目录路径
        self.dir.setPath(self.filepahtInput.text())

        # 文件过滤器  包含所有类型的文件和目录 排除. 和 .. 表示当前目录和上一级目录
        Dir_fitter = QDir.AllEntries | QDir.NoDotAndDotDot

        # 排序过滤器  先排文件夹 再排文件
        sort_fitter = QDir.DirsFirst

        # 获取目录内容 返回的是文件对象
        self.fileinfo_list =  self.dir.entryInfoList(Dir_fitter,sort_fitter)
        print(self.fileinfo_list)

        for  file in self.fileinfo_list:  # 遍历文件对象
            # 创建列表项
            item = QListWidgetItem()
            if file.isDir():  # 判断是否是目录
                item.setIcon(QIcon('../images/icon/dir.png'))
            else:
                item.setIcon(QIcon('../images/icon/file.png'))
            item.setText(file.fileName())
            self.fileList.addItem(item)




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


