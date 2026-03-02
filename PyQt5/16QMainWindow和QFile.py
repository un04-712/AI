from PIL.ImageColor import getcolor
from PyQt5.QtGui import QIcon, QKeySequence, QColor
from PyQt5.QtWidgets import QApplication, QMenuBar, QMenu, QMainWindow, QAction, QToolBar, QPushButton, QToolButton, \
    QFontDialog, QColorDialog, QTextEdit, QMessageBox, QFileDialog
import sys

"""常用创建窗口的方式"""
# 继承QWidget类所有的属性和方法
class mainWidget(QMainWindow):
    def __init__(self):
        # 初始化父类的__init__方法 将self参数传进去
        super().__init__()  # QWidget.__init__(self)
        # 修改窗口标题
        self.setWindowTitle("无标题-记事本")
        # 修改窗口大小
        self.resize(700, 600)

        # 设置窗口图标
        icon =  QIcon('../images/icon/1.png')
        self.setWindowIcon(icon)

        self.ui_init()
    def ui_init(self):
        """创建菜单栏"""
        self.create_menu_bar()
        """创建工具栏"""
        self.create_tool_bar()

        self.textEdit = QTextEdit(self)
        #文本修改时触发信号
        self.textEdit.textChanged.connect(self.update_title)

        self.setCentralWidget(self.textEdit)


    def create_menu_bar(self):
        # 添加菜单栏类
        menubar =  QMenuBar(self)
        self.setMenuBar(menubar)

        # 在菜单中添加文件菜单 QMenu
        file_menu =  QMenu("文件(F)",self)
        menubar.addMenu(file_menu)

        # 在菜单中添加编辑菜单 QMenu
        edit_menu = QMenu("编辑(E)", self)
        menubar.addMenu(edit_menu)

        # 在文件栏中添加动作  QAction 并设计图标
        # 新建
        self.new_action =  QAction(QIcon('../images/icon/new.png'),"新建(N)",self)
        self.new_action.setShortcut(QKeySequence.New)
        self.new_action.triggered.connect(self.new_create)
        file_menu.addAction(self.new_action)

        # 打开self.
        open_action = QAction(QIcon('../images/icon/open.png'), "打开(O)", self)
        open_action.setShortcut(QKeySequence.Open)
        file_menu.addAction(open_action)

        # 保存
        self.save_action = QAction(QIcon('../images/icon/save.png'), "保存(S)", self)
        self.save_action.setShortcut(QKeySequence.Save)
        file_menu.addAction(self.save_action)

        # 另存
        saveAs_action = QAction(QIcon('../images/icon/save.png'), "另存为(A)", self)
        saveAs_action.setShortcut(QKeySequence.SaveAs)
        file_menu.addAction(saveAs_action)

        # 复制
        copy_action = QAction(QIcon('../images/icon/copy.png'), "复制(C)", self)
        copy_action.setShortcut(QKeySequence.Copy)
        edit_menu.addAction(copy_action)

        # 粘贴
        paste_action = QAction(QIcon('../images/icon/paste.png'), "粘贴(P)", self)
        paste_action.setShortcut(QKeySequence.Paste)
        edit_menu.addAction(paste_action)

        # 剪切
        cut_action = QAction(QIcon('../images/icon/cut.png'), "剪切(T)", self)
        cut_action.setShortcut(QKeySequence.Cut)
        edit_menu.addAction(cut_action)

        # 撤销
        undo_action = QAction(QIcon('../images/icon/undo.png'), "撤销(U)", self)
        undo_action.setShortcut(QKeySequence.Undo)
        edit_menu.addAction(undo_action)

        # 恢复
        redo_action = QAction(QIcon('../images/icon/redo.png'), "恢复(R)", self)
        redo_action.setShortcut(QKeySequence.Redo)
        edit_menu.addAction(redo_action)




    def create_tool_bar(self):
        #添加工具栏
        tool_bar = QToolBar(self)
        #将工具栏添加到主窗口
        self.addToolBar(tool_bar)

        tool_bar.addAction(self.new_action)
        tool_bar.addAction(self.save_action)

        font_btn = QToolButton(self)
        font_btn.setIcon(QIcon('../images/icon/font.png'))
        #绑定槽函数
        font_btn.clicked.connect(self.open_font)

        tool_bar.addWidget(font_btn)


        color_btn = QToolButton(self)
        color_btn.setIcon(QIcon('../images/icon/color.png'))
        # 绑定槽函数
        color_btn.clicked.connect(self.open_color)

        tool_bar.addWidget(color_btn)

    def update_title(self):
        self.setWindowTitle('*'+'无标题')

    def open_font(self):
        # 获取用户用户选择的字体属性 (元组  ： 字体 + 是否确认)
        font,is_ok = QFontDialog.getFont(self)
        if is_ok:
            # self.textEdit.setFont(font)   #应用所有的文本
            self.textEdit.setCurrentFont(font)  # 应用选中的文本
        else:
            print("用户取消了字体选择")
    def open_color(self):
        color = QColorDialog.getColor(QColor(),self)
        self.textEdit.setTextColor(color)

    def new_create(self):
        print('new_create')
        result = self.textEdit.document().isModified()
        if result == False:
            self.textEdit.clear()
            self.setWindowTitle('无标题记事本')
        else:
            res = QMessageBox.question(None,'提示','是否保存当前修改内容',QMessageBox.Yes|QMessageBox.No)
            if res ==  QMessageBox.Yes:
                file_path = QFileDialog.getSaveFileName(self,'../','记事本')
                print(file_path)

                text = self.textEdit.toPlainText()
                with open(file_path[0],'w') as f:
                    f.write(text)











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


