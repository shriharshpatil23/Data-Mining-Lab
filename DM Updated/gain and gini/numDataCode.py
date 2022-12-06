import pandas as pd
from sklearn.preprocessing import LabelEncoder
import collections
import math
import csv
data = pd.read_csv("DataNum.csv")
print(data)
finalClass=data['Class']
n=finalClass.size
def helpGiniFun(num,col):
    greaterYes=0
    greaterNo=0
    lowYes=0
    lowNo=0
    for i in range(0,n):
        if int(col[i])>=int(num) and finalClass[i]=='A':
            greaterYes=greaterYes+1
        elif int(col[i])>=int(num) and finalClass[i]=='B':
            greaterNo=greaterNo+1
        elif int(col[i])<int(num) and finalClass[i]=='A':
            lowYes=lowYes+1
        elif int(col[i])<int(num) and finalClass[i]=='B':
            lowNo=lowNo+1
    
    #print(greaterYes,greaterNo,lowYes,lowNo)
    greaterProb=0
    lowProb=0
    if greaterYes+greaterNo==0 :
        greaterProb=0
    else:
        gretYProb=greaterYes/(greaterYes+greaterNo)
        gretNProb=greaterNo/(greaterYes+greaterNo)
        greaterProb=(((greaterYes+greaterNo)/n)*(1-(gretYProb*gretYProb)-(gretNProb*gretNProb)))
    if lowYes+lowNo==0 :
        lowProb=0
    else:
        lowYProb=lowYes/(lowYes+lowNo)
        lowNProb=lowNo/(lowYes+lowNo)
        lowProb=(((lowYes+lowNo)/n)*(1-(lowYProb*lowYProb)-(lowNProb*lowNProb)))
    
    #print(greaterProb+lowProb,num)
    return greaterProb+lowProb

     
def findGini(col):
    uniVal=set()
    for i in col:
        uniVal.add(i)
    minGini=1.0
    spiltingVal=-1
    low=col[0]
    high=col[0]
    for i in range(0,n):
        if col[i]<low :
            low=col[i]
        if col[i]>high :
            high=col[i]
    

    #print(helpGiniFun(32,col))
    for i in range(low,high):
        curGiniVal=helpGiniFun(i,col)
        print(curGiniVal)
        if curGiniVal<minGini :
            minGini=curGiniVal
            spiltingVal=i
    
    #print(minGini)
    return {minGini,spiltingVal}

print(findGini(data['Var']))