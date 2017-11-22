from commonhttp import apihttp

data = apihttp.apicommonhttp("http://stock.market.alicloudapi.com/sz-sh-stock-history") \
    .addHeaders("Authorization", "APPCODE d831433e05c1404ea916b3062448d183") \
    .addBody("end", "2017-11-22") \
    .addBody("begin", "2017-11-01") \
    .addBody("code", "000050") \
    .get()

print(data)
