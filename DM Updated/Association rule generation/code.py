import math
from itertools import combinations
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import collections
import csv
from functools import reduce
from operator import concat
data = pd.read_csv('data.csv')
k=1
list_of_column_names = list(data.columns) 
colLen=len(list_of_column_names)
curItems=[]
cnt=0
for i in data[list_of_column_names[0]]:
    curItems.append(cnt)
    cnt=cnt+1

lev=1

pre=[]
minSup=40
tot=colLen-1

def findFreq(col,comb):
    cnt=0
    for i in comb:
        if col[i]==1:
            cnt=cnt+1
    return cnt==len(comb)
while 1:
    #print(curItems)
    if len(curItems)<lev:
        break
    comb=combinations(curItems,lev)
    comb=list(comb)
    ans=[]
    #print(comb)
    for i in comb:
        curFre=0
        for j in range(1,colLen):
            #print(data[list_of_column_names[j]])
            curFre=curFre+findFreq(data[list_of_column_names[j]],list(i))
        
        
        curSup=((curFre/tot)*100)
        #print(i,curFre,tot,curSup)
        if curSup>=minSup :
            ans.append(list(i))
        
    # if len(ans)==0 :
    #     break
    pre=ans
    curItems=reduce(concat,ans)
    uniItem=set()
    for i in curItems:
        uniItem.add(i)
    curItems=[]
    for i in uniItem:
        curItems.append(i)
    #print(curItems)
    lev=lev+1

allComb=[]


for i in pre:
    #print(i)
    for j in range(1,len(i)):
        combl=list(combinations(i,j))
        for k in combl:
            allComb.append(list(k))

threShouldConf=50
totLen=len(allComb)
print("Association rules are as follows:")
def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))
for i in range (0,totLen):
    for j in range (0,totLen):
        curFre=0
        curFre1=0
        inter=intersection(allComb[i], allComb[j])
        #print(inter)
        if i!=j and len(inter)==0:
            for k in range(1,colLen):
                curFre=curFre+findFreq(data[list_of_column_names[k]],allComb[j])
            for k in range(1,colLen):
                #print(inter)
                curFre1=curFre1+findFreq(data[list_of_column_names[k]],inter)
            #print(allComb[i],curFre)
            if (curFre/curFre1)*100>=threShouldConf:
                print(allComb[i],"=>",allComb[j],(curFre/curFre1)*100)
            
            




        





