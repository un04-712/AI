# 导入FastAPI
from fastapi import FastAPI

# 创建fastapi对象
app = FastAPI()

# 定义路由
@app.get('/musicList') #路径操作装饰器
async def musicList():  # 路径操作函数
    return {'musicList':["abc.mp3","def.mp3"]}

@app.get('/')
async def musicList():
    return "hello world"

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("01FastApi的基本使用:app",host="127.0.0.1",port=8080)

