import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import collections
import math
import csv
Le = LabelEncoder()

PlayTennis = pd.read_csv("infogain_input.csv")


def find_entropy(x,y,t):
    if x!=0 and y!=0:
        return -((x/t)*(math.log2((x/t)))+(y/t)*(math.log2((y/t))))
    else:
        return 0.0




PlayTennis['outlook'] = Le.fit_transform(PlayTennis['outlook'])
PlayTennis['temp'] = Le.fit_transform(PlayTennis['temp'])
PlayTennis['humidity'] = Le.fit_transform(PlayTennis['humidity'])
PlayTennis['wind'] = Le.fit_transform(PlayTennis['wind'])
PlayTennis['play'] = Le.fit_transform(PlayTennis['play'])
frequencyPlay = collections.Counter(PlayTennis.play)
tot=PlayTennis.play.size


EntropyOfData=find_entropy(frequencyPlay[0],frequencyPlay[1],tot)
print("Total entropy is:"+str(EntropyOfData))

def infoGain(frequncy,a,tot,cond):
    infogain = 0.0
    for i in frequncy:
        cnt = 0
        for x in range(PlayTennis.play.size):
            if PlayTennis.play.get(x)==1 and a.get(x)==i:
                cnt=cnt+1
        infogain += (frequncy[i]/tot)*find_entropy(frequncy[i]-cnt,cnt,frequncy[i])
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

    frequncyoutlook = collections.Counter(PlayTennis.outlook)
    data=['Outlook',infoGain(frequncyoutlook,PlayTennis.outlook,tot,'outlook')]
    writer.writerow(data)
    frequencytemp = collections.Counter(PlayTennis.temp)
    data = ['Temperature', infoGain(frequencytemp,PlayTennis.temp,tot,'temp')]
    writer.writerow(data)
    frequencyHumidity = collections.Counter(PlayTennis.humidity)
    data = ['Hunidity',infoGain(frequencyHumidity,PlayTennis.humidity,tot,'humidity')]
    writer.writerow(data)
    frequencyWindy = collections.Counter(PlayTennis.wind)
    data = ['Wind',infoGain(frequencyWindy,PlayTennis.wind,tot,'wind')]
    writer.writerow(data)
    frequencyPlay = collections.Counter(PlayTennis.play)
    data = ['Play',infoGain(frequencyPlay,PlayTennis.play,tot,'play')]
    writer.writerow(data)


