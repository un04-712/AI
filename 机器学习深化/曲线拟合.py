import numpy as np
from IPython import display
import matplotlib.pyplot as plt

# 1、散点输入
data = np.array([[0.8, 0], [1.1, 0], [1.7, 0], [3.2, 1], [3.7, 1], [4.0, 1], [4.2, 1]])

# 提取 x_data 和 y_data
x_data = data[:, 0]
y_data = data[:, 1]


# 2、前向计算为了直观的观看与引入激活函数，代码无用
# 3、激活函数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# 4、超参数初始化
w = 2.8
b = -5.1
learning_rate = 0.05

# 5、损失函数只是为了展示公式，实际会直接求解导数，代码无用
# 数据个数，求平均用
l_x_data = x_data.size
# 显示子图
fig, (ax1, ax2) = plt.subplots(2, 1)
step_list = []
loss_list = []

# 6、开始迭代
num_iterations = 1000
for n in range(1, num_iterations + 1):
    # 7、反向传播，手动计算损失函数关于自变量(模型参数)的梯度
    z = w * x_data + b
    a = sigmoid(z)
    deda = -2 * (y_data - a)
    dadz = a * (1 - a)
    dzdw = x_data
    gradient_w = (deda * dadz * dzdw).sum() / l_x_data

    dzdb = 1
    gradient_b = (deda * dadz * dzdb).sum() / l_x_data
    # 更新参数
    w = float(w - learning_rate * gradient_w)
    b = float(b - learning_rate * gradient_b)

    # 计算当前步骤的损失函数值并添加到列表中
    z = w * x_data + b
    a = sigmoid(z)
    loss = np.mean((y_data - a) ** 2)

    step_list.append(n)
    loss_list.append(loss)

    # 8、显示频率设置
    frequence_display = 50
    if n % frequence_display == 0 or n == 1:
        # 9、梯度下降显示
        # 绘制拟合曲线
        # 清空Jupyter输出
        display.clear_output(wait=True)

        x_min, x_max = x_data.min(), x_data.max()
        x_values = np.linspace(x_min, x_max, int((x_max - x_min) * 10))
        y_values = np.round(sigmoid(w * x_values + b), 3)
        ax1.clear()
        ax1.scatter(x_data, y_data)
        ax1.plot(x_values, y_values, 'r-')
        ax1.set_title(f"Curve Regression: w={round(w, 3)}, b={round(b, 3)}")

        # 更新子图 2 数据并绘制
        ax2.clear()
        ax2.plot(step_list, loss_list, 'g-')
        ax2.set_xlabel("Step")
        ax2.set_ylabel("Loss")
        # 显示图形
        display.display(plt.gcf())
        # 清空Jupyter输出
        display.clear_output(wait=True)