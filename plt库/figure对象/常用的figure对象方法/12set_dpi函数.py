"""
        设置分辨率
"""

from matplotlib import pyplot as plt

fig = plt.figure(figsize=(8,6),dpi=120,facecolor='g')

fig.set_dpi(200)

plt.plot(  [1,2,3,4], [1,4,9,16])

plt. show()

print(fig.get_size_inches())