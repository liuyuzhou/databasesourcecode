import requests

# 不带参数的请求方式
req = requests.get('https://www.baidu.com')

# 带参数的请求方式
url_1 = 'https://www.baidu.com/s?wd=python'
req_1 = requests.get(url_1)

# 带参数的请求方式
url_2 = 'https://www.baidu.com/s'
params = {'wd': 'python'}
req_2 = requests.get(url_2, params=params)