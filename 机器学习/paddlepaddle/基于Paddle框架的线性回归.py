import numpy as np
import paddle

# 1、散点输入，定义输入数据
data = [[-0.5, 7.7], [1.8, 98.5], [0.9, 57.8], [0.4, 39.2], [-1.4, -15.7], [-1.4, -37.3], [-1.8, -49.1], [1.5, 75.6],
        [0.4, 34.0], [0.8, 62.3]]
data = np.array(data)
# 提取x和y
x_data = data[:, 0]
y_data = data[:, 1]

# 转换成paddle张量
x_train = paddle.to_tensor(x_data, dtype=paddle.float32)
y_train = paddle.to_tensor(y_data, dtype=paddle.float32)

# 2、定义前向模型
model = paddle.nn.Linear(1, 1)


# 3、定义损失函数和优化器
criterion = paddle.nn.MSELoss()
optimizer = paddle.optimizer.SGD(learning_rate=0.01, parameters=model.parameters())

# 4、开始迭代
epoches = 500
for epoch in range(1, 500 + 1):
    # 前向传播
    y_hat = model(x_train.unsqueeze(1))
    # 计算损失
    loss = criterion(y_hat.squeeze(1), y_train)
    # 清除之前计算的梯度
    optimizer.clear_grad()
    # 自动计算梯度
    loss.backward()
    # 更新参数
    optimizer.step()

    # 5、显示频率设置
    if epoch % 10 == 0 or epoch == 1:
        print(f"epoch:{epoch}, loss:{float(loss)}")

