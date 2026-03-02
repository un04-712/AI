import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QPainter, QColor


class AnimationWindow(QWidget):
    def __init__(self):
        super().__init__()
        # 初始化窗口
        self.setWindowTitle('PyQt 定时器动画示例')
        self.setGeometry(100, 100, 800, 600)

        # 方块属性
        self.rect_size = 50
        self.x = 50  # 初始x坐标
        self.y = 50  # 初始y坐标
        self.dx = 3  # x方向速度
        self.dy = 2  # y方向速度

        # 创建定时器
        self.timer = QTimer(self)
        # 每30毫秒触发一次timeout信号
        self.timer.timeout.connect(self.update_position)
        self.timer.start(30)  # 启动定时器

    def update_position(self):
        # 更新方块位置
        self.x += self.dx
        self.y += self.dy

        # 检测边界碰撞，碰到边界则反弹
        if self.x <= 0 or self.x + self.rect_size >= self.width():
            self.dx = -self.dx
        if self.y <= 0 or self.y + self.rect_size >= self.height():
            self.dy = -self.dy

        # 重绘窗口
        self.update()

    def paintEvent(self, event):
        # 绘制方块
        painter = QPainter(self)
        painter.setBrush(QColor(0, 120, 215))  # 设置蓝色
        painter.drawRect(self.x, self.y, self.rect_size, self.rect_size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AnimationWindow()
    window.show()
    sys.exit(app.exec_())
