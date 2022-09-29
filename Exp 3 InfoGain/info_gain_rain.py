import pandas as pd
from sklearn.preprocessing import LabelEncoder
import collections
import math
import csv
Le = LabelEncoder()

Rain_data = pd.read_csv('info_gain_rain_input.csv')


def find_entropy(x,y,t):
    if x!=0 and y!=0:
        return -((x/t)*(math.log2((x/t)))+(y/t)*(math.log2((y/t))))
    else:
        return 0.0




Rain_data['Temperature'] = Le.fit_transform(Rain_data['Temperature'])
Rain_data['Humidity'] = Le.fit_transform(Rain_data['Humidity'])
Rain_data['Clouds'] = Le.fit_transform(Rain_data['Clouds'])
Rain_data['Rain'] = Le.fit_transform(Rain_data['Rain'])
frequencyRain = collections.Counter(Rain_data.Rain)
tot=Rain_data.Rain.size


EntropyOfData=find_entropy(frequencyRain[0],frequencyRain[1],tot)
print("Total entropy is:"+str(EntropyOfData))

def infoGain(frequency,a,tot,cond):
    infogain = 0.0
    for i in frequency:
        cnt = 0
        for x in range(Rain_data.Rain.size):
            if Rain_data.Rain.get(x)==1 and a.get(x)==i:
                cnt=cnt+1
        infogain += (frequency[i]/tot)*find_entropy(frequency[i]-cnt,cnt,frequency[i])
    condition = cond
    infogain = EntropyOfData - infogain
    print("Information gain by {} is: {}" .format(condition,infogain))
    return infogain



header = ['Attribute', 'InfoGain']

with open('infogain_Output.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data

    frequencyTemp = collections.Counter(Rain_data.Temperature)
    data=['Temperature',infoGain(frequencyTemp,Rain_data.Temperature,tot,'Temperature')]
    writer.writerow(data)
    frequencyHumidity = collections.Counter(Rain_data.Humidity)
    data = ['Humidity', infoGain(frequencyHumidity,Rain_data.Humidity,tot,'Humidity')]
    writer.writerow(data)
    frequencyClouds = collections.Counter(Rain_data.Clouds)
    data = ['Clouds',infoGain(frequencyClouds,Rain_data.Clouds,tot,'Clouds')]
    writer.writerow(data)



