import json
import os

from fastapi import FastAPI

import uvicorn

app = FastAPI()

@app.get('/shoplist')
def get_info():
    with open('../db/products','r',encoding='utf-8') as f:
        text = f.readlines()
        res1 = json.loads(text[0])
        res2 = json.loads(text[1])
        return res1,res2

@app.get('/users')
def get_info():
    with open('../db/user', 'r', encoding='utf-8') as f:
        content = f.readlines()
        res = json.loads(content[0])
        return res


@app.get('/musiclist')
def get_info():
    res = os.listdir(r'C:\Users\86132\Desktop\FastAPI\music')
    musicList = [name for name in res if name.endswith(".mp3")]
    return  musicList


if __name__ == '__main__':
    uvicorn.run(
        app,
        host='127.0.0.1',
        port=8080,
        log_level='debug'
    )
