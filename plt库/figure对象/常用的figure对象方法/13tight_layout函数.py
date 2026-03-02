"""
    自动调整子图布局，使子图与子图之间不会重叠

"""

from matplotlib import pyplot as plt
import numpy as np

# 创建数据
x = np.arange(0, 10, 0.01)
y1 = np.sin(x)

fig, axes = plt.subplots(2, 2, figsize=(10, 8), width_ratios=[1, 2], height_ratios=None)

# 第一个子图
axes[0][0].plot(x, y1)
axes[0][0].set_title('Sine Wave')
axes[0][0].set_xlabel('X-axis')
axes[0][0].set_ylabel('y-axis')

fig.tight_layout()
plt.show()
