"""
    restful 规范 增 POST 删 DELETE 改PUT 查 GET

"""

from fastapi import FastAPI

import uvicorn

#创建fastapi的实例
app = FastAPI()

#定义GET方法的路由,路径为/get,访问时返回json响应
@app.get('/get')
def get_text():
    pass


@app.post('/post')
def post_text():
    pass

@app.put('/put')
def put_text():
    pass

@app.delete('/delete')
def delete_text():
    pass


if __name__ == '__main__':
    pass

