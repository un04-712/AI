import uvicorn
from fastapi import FastAPI
from api.product_api import router as product_router
from api.user_api import router as user_router

app = FastAPI()

# 注册API路由
app.include_router(product_router,tags={"产品管理接口"},prefix='/api')
app.include_router(user_router,tags={"用户账号接口"},prefix='/api')


if __name__ == "__main__":
    uvicorn.run(
        app,   # 应用实例
        host='0.0.0.0', # 监听地址{"method":"get方法"}
        port=8080,   # 监听端口
        log_level="debug"  # 日志级别
    )
