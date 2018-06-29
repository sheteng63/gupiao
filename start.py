

from commonUtil import apihttp
import json

http = apihttp.apicommonhttp("http://127.0.0.1:7980/user/login").addBody("username","sheteng").addBody("pwd","123456").post()
headers = http.headers
print(json.loads(http.text))
http2 = apihttp.apicommonhttp("http://127.0.0.1:7980/user/logout").addHeaders(headers).post()
print(json.loads(http2.text))


