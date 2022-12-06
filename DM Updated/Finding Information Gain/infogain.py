import pandas as pd
from sklearn.preprocessing import LabelEncoder
import collections
import math
import csv
Le = LabelEncoder()
######################################## DATA READING FROM CSV ################################################################
buysComp = pd.read_csv("infogain_input.csv")

buysComp['Income'] = Le.fit_transform(buysComp['Income'])
buysComp['Student'] = Le.fit_transform(buysComp['Student'])
buysComp['creditRat'] = Le.fit_transform(buysComp['creditRat'])
buysComp['buys'] = Le.fit_transform(buysComp['buys'])
frequencyBuys = collections.Counter(buysComp.buys)
tot=buysComp.buys.size
###############################################################################################################################

######################################## FUNCTION TO CALCULATE ENTROPY ########################################################
def find_entropy(x,y,t):
    if x!=0 and y!=0:
        return -((x/t)*(math.log2((x/t)))+(y/t)*(math.log2((y/t))))
    else:
        return 0.0
###############################################################################################################################

######################################## FUNCTION TO CALCULATE INFORMATION GAIN ###############################################
def infoGain(frequncy,a,tot,cond):
    infogain = 0.0
    for i in frequncy:
        cnt = 0
        for x in range(buysComp.buys.size):
            if buysComp.buys.get(x)==1 and a.get(x)==i:
                cnt=cnt+1
        infogain += (frequncy[i]/tot)*find_entropy(frequncy[i]-cnt,cnt,frequncy[i])
    condition = cond
    infogain = EntropyOfData - infogain
    print("Information gain by {} is: {}" .format(condition,infogain))
    return infogain
###############################################################################################################################


######################################## FINDING INFORMATION GAIN FOR EACH ATTRIBUTE AND WRITING OUTPUT INTO CSV###############
EntropyOfData=find_entropy(frequencyBuys[0],frequencyBuys[1],tot)
print("Total entropy is:"+str(EntropyOfData))
header = ['Attribute', 'InfoGain']
with open('infogain_Output.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data

    frequncyincome = collections.Counter(buysComp.Income)
    data=['Income',infoGain(frequncyincome,buysComp.Income,tot,'Income')]
    writer.writerow(data)
    frequencyStudent = collections.Counter(buysComp.Student)
    data = ['Student', infoGain(frequencyStudent,buysComp.Student,tot,'Student')]
    writer.writerow(data)
    frequencycreditRat = collections.Counter(buysComp.creditRat)
    data = ['creditRat',infoGain(frequencycreditRat,buysComp.creditRat,tot,'creditRat')]
    writer.writerow(data)
################################################################################################################################
