import requests

base_url = "http://127.0.0.1:8080"


# get 请求
"""路径参数方式请求 """
# response =  requests.get(f"{base_url}/user/1")
# print("请求 /user/1 的结果：")
# print("状态码：", response.status_code)
# print("响应内容：", response.json())
#
# response =  requests.get(f"{base_url}/user/a")
# print("请求 /user/a 的结果：")
# print("状态码：", response.status_code)
# print("响应内容：", response.json())

"""查询参数方式请求 """
param1 = {
    "zl":1,
    "xl":"本科",
    "gz":"软件开发工程师"
}
# 通过params封装成查询参数
response =  requests.get(f"{base_url}/jobs",params=param1)
print("查询参数的结果：")
print("状态码：", response.status_code)
print("请求地址：", response.url)  # 打印请求地址
print("响应内容：", response.json())
