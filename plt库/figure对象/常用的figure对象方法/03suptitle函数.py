"""
    往figure添加标题(居中对齐)

"""
import matplotlib.pyplot as plt

fig = plt.figure()

a = fig.add_subplot(1, 2, 1)
a.plot([1, 5], [6, 12])

a = fig.add_subplot(1, 2, 2)
a.plot([-3, 1], [4, -2])

fig.suptitle('line', fontsize=23, color='r')
plt.show()
