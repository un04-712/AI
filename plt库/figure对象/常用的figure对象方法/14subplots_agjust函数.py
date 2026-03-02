"""
    手动调节子图布局


"""

from matplotlib import pyplot as plt
import numpy as np

# 创建数据
x = np.arange(0,10,0.01)
y1 = np.sin(x)

fig, axes = plt. subplots ( 2,  2, figsize=(10,8),width_ratios=[1,2],height_ratios=None)

fig.subplots_adjust(left=0.5, right=0.95, top=0.95, bottom=0.5)
fig.tight_layout ()
plt. show()