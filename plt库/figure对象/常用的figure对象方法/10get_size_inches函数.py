"""
    获取图形大小，单位为英寸

"""

from matplotlib import pyplot as plt

fig = plt.figure(figsize=(8,6),dpi=120,facecolor='g')

plt.plot( [1,2,3,4], [1,4,9,16])

plt. show()

print(fig.get_size_inches())