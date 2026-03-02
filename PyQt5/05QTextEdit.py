"""   # TextEdit  是 PyQt 里用于显示和编辑文本的组件。支持普通文本、富文本及 HTML 文本的显示与编辑，
    # 能设置字体、颜色、样式、对齐方式等格式；支持文本选择，以及复制、剪切、粘贴等操作；
    # 具备撤销和重做功能；可进行文本搜索与替换；有自动换行功能，文本超出区域时自动换行 。

"""
from PyQt5.QtWidgets import QTextEdit, QApplication, QWidget
import sys




class myWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("文本编辑框使用")
        self.resize(900, 900)
        self.ui_init()

    def ui_init(self):
        # 创建文本编辑框
        textEdit1 = QTextEdit(self)

        textEdit1.resize(300, 300)
        textEdit1.move(50, 50)
        textEdit1.setText("Hello World")
        textEdit1.setPlaceholderText("输入要发送的消息")
        """样式设置"""
        # textEdit1.setStyleSheet("""
        #     QTextEdit:focus{    /*聚焦*/
        #         border:1px solid #C1DEF5;
        #         background-color:white;
        #     }
       #     QTextEdit:hover{
        #         border:1px solid #C1DEF5;
        #         background-color:#F5F5F5;
        #     }
        #
        # """)

        textEdit2 = QTextEdit(self)
        textEdit2.setStyleSheet("""
                    QTextEdit:focus{
                        border:1px solid #C1DEF5;
                        background-color:white;
                    }
                    QTextEdit:hover{
                        border:1px solid #C1DEF5;
                        background-color:#F5F5F5;
                    }

                """)
        textEdit2.resize(300, 300)
        textEdit2.move(400, 50)

        """三种文本的设置"""
        textEdit2.setPlainText("hi")  # 普通文本
        textEdit1.setText("<h1>我的第一个标题</h1>")  # QT富文本
        textEdit1.setHtml(
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

        """获取文本"""
        print("纯文本:", textEdit2.toPlainText())  # 获取纯文本
        print("HTML:", textEdit2.toHtml())  # 获取HTML代码


if __name__ == '__main__':
    # 创建app
    app = QApplication(sys.argv)
    window = myWidget()
    window.show()
    sys.exit(app.exec_())