from dataAsy import dataAcquire

data = dataAcquire.AliApiData("SZ000050").getData("2017-11-23", "2017-11-22")

# data = dataAcquire.JuheApiData("SZ000050",1).getNowData()

print(data)
