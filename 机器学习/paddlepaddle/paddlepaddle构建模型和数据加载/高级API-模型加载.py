import numpy as np
import paddle
from paddle.io import TensorDataset, DataLoader


# 1、散点输入，定义输入数据
data = [[-0.5, 7.7], [1.8, 98.5], [0.9, 57.8], [0.4, 39.2], [-1.4, -15.7], [-1.4, -37.3], [-1.8, -49.1], [1.5, 75.6],
        [0.4, 34.0], [0.8, 62.3]]
data = np.array(data)
# 提取x和y
x_data = data[:, 0]
y_data = data[:, 1]

x_data = x_data.reshape(-1, 1)  # 现在形状是 (10, 1) 而不是 (10,)

# 转换成paddle张量
x_train = paddle.to_tensor(x_data, dtype=paddle.float32)
y_train = paddle.to_tensor(y_data, dtype=paddle.float32)

dataset = TensorDataset([x_train,y_train])
dataloader = DataLoader(dataset,batch_size=10,shuffle=True)

# 2、定义前向模型

# 单独定义
class LinearModel(paddle.nn.Layer):
    def __init__(self):
        super(LinearModel,self).__init__()
        self.Linear = paddle.nn.Linear(1,1)
    def forward(self,x):
        x = self.Linear(x)
        return x
model = LinearModel()

# 使用paddle的高级API
model = paddle.Model(model)

model.prepare(optimizer=paddle.optimizer.SGD(learning_rate=0.01,parameters=model.parameters()),
              loss=paddle.nn.MSELoss(),metrics=paddle.metric.Accuracy())

model.load("./高级API模型1/final")

dataset = TensorDataset([paddle.to_tensor([1.5,82], dtype=paddle.float32)])

dataloader_eval = DataLoader(dataset)

eval_predict = model.evaluate(dataloader_eval,verbose=1)

print(eval_predict)

# # 预测
# dataset_test = TensorDataset([paddle.to_tensor([1.5],dtype=paddle.float32)])
#
# dataloader_test = DataLoader(dataset_test)
#
# pre_result = model.predict(dataloader_test)
# print(pre_result)







