"""
    fig.add_subplot(nrows,ncols,plot_number)

"""

import matplotlib.pyplot as plt

fig = plt.figure()

a = fig.add_subplot(1,2,1)
a.plot([1,5],[6,12])

a = fig.add_subplot(1,2,2)
a.plot([-3,1],[4,-2])

plt.show()