"""
    gca:get current axis  获取当前子图对象

"""
import matplotlib.pyplot as plt

fig = plt.figure()

plt.plot([1,2],[3,4])

a = plt.gca()
a.set_title('line')
print(a)
plt.show()