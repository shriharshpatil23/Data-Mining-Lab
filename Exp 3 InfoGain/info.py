import pandas as pd
from sklearn.preprocessing import LabelEncoder
import collections
import math
import csv
data = pd.read_csv("infogain_input.csv")
play=data['play']

rec=play.size
def helpGini(y,n):
    if y==0 or n==0 :
        return 0
    tot=y+n
    return (1-((y/tot)*(y/tot))-((n/tot)*(n/tot)))*(tot/rec)

def helpGain(y,n):
    if y==0 or n==0 :
        return 0
    tot=y+n
    entro=-(((y/tot)*math.log2(y/tot))+((n/tot)*math.log2(n/tot)))
    return (entro*tot)/rec

def findGini(arr):
    uniVal=set()
    for i in range(0,rec):
        uniVal.add(arr[i])
    ans=0
    for i in uniVal :
        y=0
        n=0
        for j in range(0,rec):
            if arr[j]==i and play[j]=='Yes':
                y=y+1
            elif arr[j]==i and play[j]=='No':
                n=n+1
        #print(y,n)
        ans=ans+helpGini(y,n)
    return ans
list_of_column_names = list(data.columns) 
finalY=0
finalN=0
colLen=len(list_of_column_names)
for i in list_of_column_names[colLen-1]:
    if i=='Yes':
        finalY=finalY+1
    else:
        finalN=finalN+1

finalEntro=helpGain(finalY,finalN)
def findGain(arr):
    uniVal=set()
    for i in range(0,rec):
        uniVal.add(arr[i])
    ans=0
    for i in uniVal :
        y=0
        n=0
        for j in range(0,rec):
            if arr[j]==i and play[j]=='Yes':
                y=y+1
            elif arr[j]==i and play[j]=='No':
                n=n+1
        #print(y,n)
        ans=ans+helpGain(y,n)
    return helpGain(9,5)-ans



for i in range (1,colLen-1):
    print("Gain by",list_of_column_names[i],findGain(data[list_of_column_names[i]]))
