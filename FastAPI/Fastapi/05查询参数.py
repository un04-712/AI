"""
    查询参数:用于传递额外的参数
    通常出现在url路径后面,以？开头,格式为key=value,多个参数用&连接
    常用于过滤、排序或指定请求的附加条件，而不是直接表示资源本身

"""
import uvicorn
from fastapi import FastAPI

#用于在代码中说明变量或者函数参数的类型
from typing import Union,Optional

app = FastAPI()

@app.get('/jobs')
def get_jobs(zl:int,xl:Union[int,str]='本科',gz:Union[str,None]=None):
    return {
        'zl':zl,
        'xl':xl,
        'gz':gz
    }

if __name__ == '__main__':
    uvicorn.run(
        app,
        host='127.0.0.1',
        port=8080,
        log_level='debug'
    )