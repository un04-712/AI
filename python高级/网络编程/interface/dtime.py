
import time

def getTime():
    # 获取年月日时分秒
    ntime = time.time()
    lotime = time.localtime(ntime)  # 转换为时间结构体
    # 转换为字符串
    str_time = time.strftime("%Y-%m-%d %H:%M:%S", lotime)
    return str_time