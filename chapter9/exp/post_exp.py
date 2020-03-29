import requests
import json

# 定义参数字典
data = {'key1': 'value1', 'key2': 'value2'}
# 将字典转换为JSON
data = json.dumps(data)

url = 'https://www.baidu.com/'
# 发送post请求
req = requests.post(url, data=data)
print(req.text)
