"""
    获取当前活动的图形(figure)对象

"""

import matplotlib.pyplot as plt

fig,a = plt.subplots()

a.plot([1,2,3],[1,2,3])

current_fig = plt.gcf()
current_fig.suptitle('Title Test')

plt.show()

