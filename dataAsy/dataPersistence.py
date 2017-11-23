import sqlite3


## 数据持久化
class DataSave:
    def __init__(self):
        self.db = sqlite3.connect("data.db")
        pass

    def saveAliData(self, data):
        pass

    def saveJuheData(self, data):
        pass
