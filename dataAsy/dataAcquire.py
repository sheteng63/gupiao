from commonUtil import apihttp


## 获取数据
class AliApiData:
    def __init__(self, code):
        self.http = apihttp.apicommonhttp("http://stock.market.alicloudapi.com/sz-sh-stock-history") \
            .addHeaders("Authorization", "APPCODE d831433e05c1404ea916b3062448d183")
        self.code = str(code)[2:8]

    def getData(self, endDay, BeginDay):
        return self.http.addBody("end", endDay) \
            .addBody("begin", BeginDay) \
            .addBody("code", self.code) \
            .get()

    def getDayData(self, day):
        return self.getData(day, day)


class JuheApiData:
    def __init__(self, code, type = 1):
        self.http = apihttp.apicommonhttp("http://web.juhe.cn:8080/finance/stock/hs") \
            .addBody("key", "0d2246a147ea4b8c676a18763b2bce0c")
        self.code = code
        self.type = type

    def getNowData(self):
        return self.http.addBody("gid", self.code).addBody("type", self.type).get()
