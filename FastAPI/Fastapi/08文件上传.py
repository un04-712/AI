from typing import List

import uvicorn
from fastapi import FastAPI, File, UploadFile

app = FastAPI()
#单个小文件传输
@app.post('/file')
def upload_single_small_file(file:bytes = File()):
    print("接收到的文件字节数:",len(file))

    return{
        'message' : '小文件上传成功',
        'file-size' : f"{len(file)}bytes"
    }
#多个小文件传输
@app.post('/files')
def files(files:List[bytes] = File()):
    return{
        'message' : '小文件上传成功',
        'file-size' : f"{len(files)}个文件"
    }
#单个大文件传输
@app.post('/uploadfile')
def upload_single_big_file(file:UploadFile):
    # UploadFile适合大文件上传，因为它使用流式处理
    # 可以获取文件的相关属性
    print("接收到文件名:", file.filename, "文件类型:", file.content_type, "文件大小:", file.size)
    # 流式写入文件，避免一次性加载大文件到内存
    print(type(file.size))

    with open(f"./file", "wb") as f:
        pass
        # 逐行读取上传的文件并写入本地文件  file.file为文件句柄

    return {
        "message": "大文件上传成功",
        "file_name": file.filename,
        "save_path": f"./images/{file.filename}"
    }


if __name__ =='__main__':
    uvicorn.run(
        app,
        host='127.0.0.1',
        port=8080,
        log_level='debug'
    )