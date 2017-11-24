import time

from dataAsy import dataAcquire
import json

# data = dataAcquire.AliApiData("sz000050").getData("2017-11-23", "2017-11-22")

while 1:
    data = dataAcquire.JuheApiData("sz000050").getNowData()
    print(data['result'][0]['dapandata']['dot'])
    time.sleep(10)
