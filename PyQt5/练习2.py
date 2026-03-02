import sys
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QTextEdit, QTextBrowser, QPushButton)

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("同步")
        self.setFixedSize(500, 400)


        self.textEdit = QTextEdit(self)
        self.textEdit.resize(200, 150)
        self.textEdit.move(20, 20)
        self.textEdit.setText("Hello World")
        self.textEdit.setPlaceholderText("输入要发送的消息")



        self.textBrowser = QTextBrowser(self)
        self.textBrowser.resize(200, 150)
        self.textBrowser.move(270, 20)


        self.pushButton = QPushButton("同步到 TextBrowser", self)
        self.pushButton.resize(200, 40)
        self.pushButton.move(150, 200)

        # 4) 绑定点击事件
        self.pushButton.clicked.connect(self.sync_text)

    # 同步函数
    def sync_text(self):
        self.textBrowser.setPlainText(self.textEdit.toPlainText())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWidget()
    window.show()
    sys.exit(app.exec_())