#导入网络请求库
import requests

#发送get请求
response = requests.get('https://www.baidu.com?key1=1&key2=2&key3=3')


#输出状态码
print(response.status_code)
#输出响应头
print(response.headers)
#输出html文本
print(response.text)


#发送post请求
d = {"key1": "value1", "key2": "value2", "key3": "value3"}
res = requests.post('http://httpbin.org/post',data=d)

print(res.status_code)

print(res.text)
