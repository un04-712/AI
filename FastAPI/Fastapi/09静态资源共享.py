import os

import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import  FileResponse

app = FastAPI()



"""
MIME（Multipurpose Internet Mail Extensions，多用途互联网邮件扩展）
        类型是一种标识文件格式的标准，用于告诉客户端（如浏览器、服务器）如何处理传输的数据。
        它由两部分组成：类型（type） 和子类型（subtype），格式为 type/subtype，中间用斜杠分隔。
一、文本类型（text）
用于表示文本数据，通常是人类可阅读的内容。
text/plain：纯文本文件（.txt）。
text/csv：CSV 表格文件（.csv）。
text/xml：XML 格式文件（.xml）。
二、图像类型（image）
用于表示各种图像文件。
image/jpeg：JPEG 格式图像（.jpg、.jpeg）。
image/png：PNG 格式图像（.png）。
image/gif：GIF 格式图像（.gif）。
image/bmp：BMP 格式图像（.bmp）。
三、音频类型（audio）
用于表示音频文件。
audio/mpeg：MP3 音频文件（.mp3）。
audio/wav：WAV 音频文件（.wav，无损格式）。
audio/flac：FLAC 音频文件（.flac，无损压缩格式）。
四、视频类型（video）
用于表示视频文件。
video/mpeg：MPEG 视频文件（.mpeg、.mpg）。
video/mp4：MP4 视频文件（.mp4，最常用的视频格式之一）。
video/x-msvideo：AVI 视频文件（.avi）。
五、应用程序类型（application）
用于表示二进制数据或特定应用程序格式的文件，涵盖范围较广。
application/octet-stream：通用二进制数据（未指定具体格式的文件，通常用于下载）。
application/json：JSON 格式数据（.json）。
application/xml：XML 格式数据（.xml，与 text/xml 类似，但更强调二进制或复杂结构）。
application/pdf：PDF 文档（.pdf）。
application/zip：ZIP 压缩文件（.zip）。
application/rar：RAR 压缩文件（.rar）。

"""
"""
    挂载文件目录
    第一个参数   url路径前缀 访问时需要加上该前缀
    第二个参数   为StaticFiles实例 指定本地目录
"""

app.mount("/staticImages",StaticFiles(directory='../images'))
app.mount("/staticMusic",StaticFiles(directory='../music'))
app.mount("/staticVideo",StaticFiles(directory='../video'))

@app.get('/musicUrl/{name}')
async def get_music_file(name:str):
    """提供指定文件的下载/流式传输"""
    file_path = rf"C:\Users\86132\Desktop\FastAPI\music\{name}"
    if os.path.isfile(file_path):
        return  FileResponse(file_path,media_type="audio/mpeg")
    return {"error":"文件不存在或格式输入不正确"}

# FileResponse 是一个用于返回文件的响应类，专门用于将服务器上的文件发送给客户端。它非常适合处理像音频、视频、图片、文档等二进制文件或大型文件的传输。
# 使用 FileResponse 比手动读取文件内容再返回更高效，尤其是对于大文件，因为它采用了流式传输的方式，不会占用过多内存。
@app.get('/music/')
async def get_music_info(name:str):
    file_path = rf"C:\Users\86132\Desktop\FastAPI\music\{name}"
    if os.path.isfile(file_path):
        music_name = name
        music_artist = "于冬然"
        return {
                "code":1,
                "message":"获取成功",
                "name" :    music_name,
                "music_artist" : music_artist,
              "music_url" : f"http://127.0.0.1:8080/musicUrl/{name}"
        }
    return {"error": "文件不存在或格式输入不正确"}

@app.get('/videoUrl/{name}')
async def get_video_file(name:str):
    """提供指定文件的下载/流式传输"""
    file_path = rf"C:\Users\86132\Desktop\FastAPI\video\{name}"
    if os.path.isfile(file_path):
        return  FileResponse(file_path,media_type="video/mp4")
    return {"error":"文件不存在或格式输入不正确"}

@app.get('/video/')
async def get_music_info(name:str):
    file_path = rf"C:\Users\86132\Desktop\FastAPI\video\{name}"
    if os.path.isfile(file_path):
        video_name = name
        return {
                "code":1,
                "message":"获取成功",
                "name" :    video_name,
              "video_url" : f"http://127.0.0.1:8080/videoUrl/{name}"
        }
    return {"error": "文件不存在或格式输入不正确"}


if __name__ == "__main__":
    uvicorn.run(
        app,   # 应用实例
        host='127.0.0.1', # 监听地址{"method":"get方法"}
        port=8080,   # 监听端口
        log_level="debug"  # 日志级别
    )


