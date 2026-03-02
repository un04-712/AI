import json

import uvicorn
from fastapi import FastAPI,HTTPException
from typing import Union,Optional

from matplotlib.font_manager import json_dump
from pydantic import BaseModel,Field  # BaseModel主要用于数据验证 Field用于定义额外的验证规则


app = FastAPI()


# 定义数据模型 用于表示商品信息
class Goods(BaseModel):
    id: int
    name: Union[str,int]
    description:Union[str,int]
    price:int = Field(default=0,gt=0)
    quantity:int = Field(default=0,gt=0)
    category_id:int = Field(default=0,gt=0
)

def read_goods():
    with open(r'C:\Users\86132\Desktop\FastAPI\db\products', 'r', encoding='utf-8') as f:
        goods = []
        for line in f.readlines():
            res = line.strip()
            # 跳过空行
            if res:
                # 将字符串转换为字典
                good = json.loads(res)
                goods.append(good)
        # 返回解析后的商品列表
        return goods

def save_products(products):
    with open(r'C:\Users\86132\Desktop\FastAPI\db\products', 'w', encoding='utf-8') as f:
        for product in products:
            f.write(json.dumps(product) + '\n')


#商品添加
@app.post("/Goods/add")
def Add_goods(Add_goods:Goods):
    print(Add_goods.model_dump())
    Goods =Add_goods.model_dump()

    product = read_goods()
    # 判断商品编号是否已存在
    if any(p['id'] == Goods.get('id') for p in product):
        raise HTTPException(status_code=400, detail=f"商品编号 {Goods.get('id')} 已存在")
    product.append(Goods)
    #存入数据
    save_products(product)

    return {"message": "商品添加成功", "data": Goods}

#商品删除
@app.delete("/good/del/{id}")
def del_goods():
    products = read_goods()
    original_count = len(products)

    # 过滤掉要删除的商品
    products = [p for p in products if p['id'] != Goods.get('id')]

    if len(products) == original_count:
        raise HTTPException(status_code=404, detail=f"商品编号 {Goods.get('id')} 不存在")

    save_products(products)
    return {"message": f"商品编号 {Goods.get('id')} 已成功删除"}



if __name__ == "__main__":
    uvicorn.run(
        app,   # 应用实例
        host='0.0.0.0', # 监听地址{"method":"get方法"}
        port=8080,   # 监听端口
        log_level="debug"  # 日志级别
    )
