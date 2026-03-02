"""
    用于获取轴的背景颜色
    返回的是r g b a     属于0-1的范围
"""
import matplotlib.pyplot as plt



fig = plt.figure(figsize=(8,6),facecolor='g')

facecolor = fig. get_facecolor ()

print(facecolor)

plt.show()


