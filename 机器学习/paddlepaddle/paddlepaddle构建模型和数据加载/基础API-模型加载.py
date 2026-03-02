import numpy as np
import paddle
from paddle.io import TensorDataset, Dataset, DataLoader


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

# 3、定义损失函数和优化器
criterion = paddle.nn.MSELoss()
optimizer = paddle.optimizer.SGD(learning_rate=0.01, parameters=model.parameters())


"""加载模型"""
model_state_dict = paddle.load("./基础API模型/model.params")
optimizer_state_dict = paddle.load("./基础API模型/optimizer.pdopt")
final_checkpoint_state_dict = paddle.load("./基础API模型/checkpoint.pkl")

print(final_checkpoint_state_dict)

model.set_state_dict(model_state_dict)


# 验证模式
model.eval()

dataloader_test = DataLoader(TensorDataset([paddle.to_tensor([1.5],dtype=paddle.float32)]))

for x_test in dataloader_test:
    predict = model(x_test[0])
    print(predict)



