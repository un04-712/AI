#练习 ： 创建商品信息   在products路径下通过请求体参数将商品信息写入到文件

import uvicorn
from fastapi import FastAPI,HTTPException
from typing import Union,Optional
from pydantic import BaseModel,Field  # BaseModel主要用于数据验证 Field用于定义额外的验证规则


app = FastAPI()


# 定义数据模型 用于表示商品信息
class Goods(BaseModel):
    id: int
    name: Union[str,int]
    description:Union[str,int]
    price:int = Field(default=0,gt=0)
    quantity:int = Field(default=0,gt=0)
    category_id:int = Field(default=0,gt=0)

#商品添加
@app.post("/Goods/add")
def Add(Add:Goods):
    print(Add.model_dump())

    Good =Add.model_dump()
    if Good.get('name') == "iphone 15":
        raise HTTPException(status_code=400,detail="商品已存在")
    else:
        with open(r'C:\Users\86132\Desktop\FastAPI\db\products','a',encoding='utf-8') as f:
            f.write('\n'+str(Good))



if __name__ == "__main__":
    uvicorn.run(
        app,   # 应用实例
        host='0.0.0.0', # 监听地址{"method":"get方法"}
        port=8080,   # 监听端口
        log_level="debug"  # 日志级别
    )
