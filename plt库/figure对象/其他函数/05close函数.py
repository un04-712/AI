"""
    关闭一个或多个窗口
    matplotlib.pyplot.close(fig=None)
    fig:指定要关闭的图像窗口，如果是一个Figure则关闭该窗口，如果是一个整数
    则关闭与该编号对应的图形。如果为None，则关闭当前图形，'all'关闭所有图形
"""
import matplotlib.pyplot as plt

plt.figure()

plt.plot([1,2,3],[1,2,3])

plt.close()

plt.show()