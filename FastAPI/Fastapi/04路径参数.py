"""
    路径参数(路径里面设置参数)
    http://ip:port/products/{product_id}  获取单个商品详情信息

"""

import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get('/user/1')
def get_user():
    return {'id_1':1}

@app.get('/user/{id}')
def get_user(id:int):
    return {'id_2':id}
