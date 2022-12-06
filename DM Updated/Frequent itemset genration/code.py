import math
from itertools import combinations
import pandas as pd
from sklearn.preprocessing import LabelEncoder
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
        print(i,curSup)
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
    print(pre)


print("Frequent itemsets are")
for i in pre:
    liAns=[]
    for j in i:
        liAns.append(data['Items'][j])
    print(liAns)


        





