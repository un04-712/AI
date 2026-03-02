"""
    只有get方法没有请求体参数，其余都有该参数
    请求体参数 ： 传递结构化 大容量 或复杂的数据
    pydantic  一般用于请求体参数

     练习 ： 创建商品信息   在products路径下通过请求体参数将商品信息写入到文件
"""
import uvicorn
from fastapi import FastAPI,HTTPException
from typing import Union,Optional
from pydantic import BaseModel,Field  # BaseModel主要用于数据验证 Field用于定义额外的验证规则


app = FastAPI()

# 定义数据模型 用于表示地址信息
class Addr(BaseModel):
    province: str = "湖南"
    city: str = "长沙"

# 定义数据模型 用于表示用户信息
class User(BaseModel):
    name:str =Field(pattern="^a+")
    age:int = Field(default=18,gt=18,lt=100)  # 年龄必须大于18小于100
    sex:Optional[str]  # 等价于sex:Union[str,None]
    addr:Addr

# 当接收到的数据类型和规定的不一致时 pydantic会尝试自动转换
@app.post("/data")
def data(data:User):
    print(data,type(data))
    print(data.name)
    print(data.age)
    print(data.sex)
    print(data.addr.province)
    print(data.addr.city)
    print(data.model_dump()) # 转换为字典

    return data   # 自动转换为json


class RegisterRquest(BaseModel):
    username:str
    email:str =Field(pattern="^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$")
    password:str
    is_admin:bool

# 用户注册
@app.post("/auth/register")
def register(request:RegisterRquest):
    if request.username == "pg":
       raise   HTTPException(status_code=400,detail="用户名已存在")
    if request.email == "33122@qq.com":
       raise   HTTPException(status_code=400,detail="邮箱已注册")
    print(request.model_dump())
    return request


if __name__ == "__main__":
    uvicorn.run(
        app,   # 应用实例
        host='0.0.0.0', # 监听地址{"method":"get方法"}
        port=8080,   # 监听端口
        log_level="debug"  # 日志级别
    )
