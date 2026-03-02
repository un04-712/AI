"""
在 PyQt5 中， QTextBrowser 是一个用于显示富文本（Rich Text）的控件。
它是 QTextEdit 的只读版本。专门用于显示带有格式的文本内容，如 HTML、超链接、图片等。
与 QTextEdit 不同的是，QTextBrowser 不允许用户直接编辑其中的内容。
"""
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication,QWidget,QTextBrowser
import sys
# 继承QWidget类所有的属性和方法
class MainWidget(QWidget):
    def __init__(self):
        # 初始化父类的__init__方法 将self参数传进去
        super().__init__()  # QWidget.__init__(self)
        # 修改窗口标题
        self.setWindowTitle("文本浏览器控件使用")
        # 修改窗口大小
        self.resize(900, 900)
        self.ui_init()



    def ui_init(self):
        textBrowser = QTextBrowser(self)
        textBrowser.resize(300, 300)

        """三种文本的设置"""
        textBrowser.setPlainText("文本")  # 普通文本
        textBrowser.append("<h1>文本</h1>")  # 追加富文本
        textBrowser.append(
            """
                <!DOCTYPE html>
                <html>
                <head>
                <meta charset="utf-8">
                <title>菜鸟教程(runoob.com)</title>
                </head>
                <body>

                <h1>我的第一个标题</h1>
                <p>我的第一个段落。</p>

                </body>
                </html>
        """)  # /*HTML*/

        textBrowser.append('<a href="https://www.baidu.com">百度</a>')  # 追加富文本
        textBrowser.setOpenExternalLinks(True)

        """获取文本"""
        print("纯文本:", textBrowser.toPlainText())  # 获取纯文本
        print("HTML:", textBrowser.toHtml())  # 获取HTML代码


if __name__ == '__main__':
    """程序启动的基本流程"""
    # 创建qApplication类   sys.argv为了通过命令行传参，但是大部分场景已经不在需要
    # print(sys.argv)
    app = QApplication(sys.argv)
    # 创建窗口对象 QWidget为UI界面
    window =  MainWidget()
    # 显示窗口
    window.show()
    # 程序关闭之后自动释放资源
    sys.exit(app.exec_())
