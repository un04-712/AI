"""
    表单参数是通过 HTTP 请求体（Request Body）传递的键值对数据，application/x-www-form-urlencoded：默认的表单格式
    数据以 key1=value1&key2=value2 的形式编码

    网页表单是最典型的应用场景，用户在页面中输入的信息（如登录表单的用户名 / 密码、注册表单的个人信息、
    搜索表单的关键词等），会通过表单参数提交给服务器处理。

"""
import uvicorn
from fastapi import FastAPI,Form

app = FastAPI()

# 表单参数
@app.post("/regin")
def data(username:str=Form(default="admin",description="用户名"),password:str=Form()):
    print(username,password)
    return username,password


if __name__ == "__main__":
    uvicorn.run(
        app,   # 应用实例
        host='127.0.0.1', # 监听地址{"method":"get方法"}
        port=8080,   # 监听端口
        log_level="debug"  # 日志级别
    )
