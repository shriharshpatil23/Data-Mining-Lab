import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import collections
import math
import csv
Le = LabelEncoder()

fire = pd.read_csv("fire.csv")


def find_entropy(x,y,t):
    if x!=0 and y!=0:
        return -((x/t)*(math.log2((x/t)))+(y/t)*(math.log2((y/t))))
    else:
        return 0.0




fire['day'] = Le.fit_transform(fire['day'])
fire['month'] = Le.fit_transform(fire['month'])
fire['Temperature'] = Le.fit_transform(fire['Temperature'])
fire['RH'] = Le.fit_transform(fire['RH'])
fire['Ws'] = Le.fit_transform(fire['Ws'])
fire['Rain'] = Le.fit_transform(fire['Rain'])
fire['FFMC'] = Le.fit_transform(fire['FFMC'])
fire['FWI'] = Le.fit_transform(fire['FWI'])
fire['Result'] = Le.fit_transform(fire['Result'])
frequencyFire = collections.Counter(fire.Result)
tot=fire.day.size


EntropyOfData=find_entropy(frequencyFire[0],frequencyFire[1],tot)
print("Total entropy is:"+str(EntropyOfData))

def infoGain(frequency,a,tot,cond):
    infogain = 0.0
    for i in frequency:
        cnt = 0
        for x in range(fire.day.size):
            if fire.day.get(x)==1 and a.get(x)==i:
                cnt=cnt+1
        infogain += (frequency[i]/tot)*find_entropy(frequency[i]-cnt,cnt,frequency[i])
    condition = cond
    infogain = EntropyOfData - infogain
    print("Information gain by {} is: {}" .format(condition,infogain))
    return infogain


header = ['Attribute', 'InfoGain']

with open('fire_output.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data

    frequencyDay = collections.Counter(fire.day)
    data=['Day',infoGain(frequencyDay,fire.day,tot,'day')]
    writer.writerow(data)
    data = ['Rain',infoGain(frequencyFire,fire.Rain,tot,'rain')]
    writer.writerow(data)
    data = ['RH',infoGain(frequencyFire,fire.RH,tot,'RH')]
    writer.writerow(data)


