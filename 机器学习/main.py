from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import matplotlib.pyplot as plt

# 定义三个点集
point1 = [[7.7, 6.1], [3.1, 5.9], [8.6, 8.8], [9.5, 7.3], [3.9, 7.4], [5.0, 5.3], [1.0, 7.3]]
point2 = [[0.2, 2.2], [4.5, 4.1], [0.5, 1.1], [2.7, 3.0], [4.7, 0.2], [2.9, 3.3], [7.3, 7.9]]
point3 = [[9.2, 0.7], [9.2, 2.1], [7.3, 4.5], [8.9, 2.9], [9.5, 3.7], [7.7, 3.7], [9.4, 2.4]]

# 合并输入特征
np_train_data = np.concatenate((point1, point2, point3))

# 根据输入特征创建标签
np_train_label = np.array([0] * len(point1) + [1] * len(point2) + [2] * len(point3))

# 初始化K近邻分类器
knn_clf = KNeighborsClassifier(3)

# 对分类器进行训练
knn_clf.fit(np_train_data, np_train_label)

# 定义坐标轴范围
axis = [0, 10, 0, 10]
# 生成坐标点网格
x0, x1 = np.meshgrid(
    np.linspace(axis[0], axis[1], int((axis[1] - axis[0]) * 10)).reshape(-1, 1),  # 在 x 轴上生成一系列均匀分布的点
    np.linspace(axis[2], axis[3], int((axis[3] - axis[2]) * 10)).reshape(-1, 1)  # 在 y 轴上生成一系列均匀分布的点
)
X_new = np.c_[x0.ravel(), x1.ravel()]  # 将坐标点网格展平并合并为一个新的特征矩阵
y_predict = knn_clf.predict(X_new)  # 使用训练好的 KNN 模型进行预测
zz = y_predict.reshape(x0.shape)  # 将预测结果转换为与坐标点网格相同的形状

# 绘制等高线图和散点图
cn = plt.contour(x0, x1, zz)  # 绘制等高线图
plt.scatter(np_train_data[np_train_label == 0, 0], np_train_data[np_train_label == 0, 1], marker='*')  # 绘制第一类样本散点图
plt.scatter(np_train_data[np_train_label == 1, 0], np_train_data[np_train_label == 1, 1], marker='^')  # 绘制第二类样本散点图
plt.scatter(np_train_data[np_train_label == 2, 0], np_train_data[np_train_label == 2, 1], marker='s')  # 绘制第三类样本散点图
plt.show()
