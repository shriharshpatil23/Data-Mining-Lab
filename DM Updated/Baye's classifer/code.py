import pandas as pd
from sklearn.preprocessing import LabelEncoder
import collections
import math
import csv
data = pd.read_csv("data.csv")
mamClass=data['Class Label']
n=mamClass.size
for i in range(0,n):
    if mamClass[i]!='mammal':
        mamClass[i]='NonMammal'

def findFreqPerCol(col):
    uniVal=set()
    for i in range(0,n):
        uniVal.add(col[i])
    ans={}
    for i in uniVal:
        y=0
        no=0
        for j in range(0,n):
            if col[j]==i and mamClass[j]=='mammal':
                y=y+1
            if col[j]==i and mamClass[j]=='NonMammal':
                no=no+1
        #print(i,y,no)
        ans.update({i:[y,no]})
    return ans

list_of_column_names = list(data.columns) 
colLen=len(list_of_column_names)
freqTab={}
for i in range (1,colLen):
    freqTab.update({list_of_column_names[i]:findFreqPerCol(data[list_of_column_names[i]])})


print(freqTab[list_of_column_names[1]])

def findProb(ty1,ty2,ty3,ty4,className):
    curClass=0
    if className=='mammal':
        curClass=0
    elif className=='NonMammal':
        curClass=1
    totClass=freqTab[list_of_column_names[colLen-1]][className][curClass]
    curFre=0
    for i in freqTab[list_of_column_names[1]]:
        curFre=curFre+freqTab[list_of_column_names[1]][i][curClass]
    ty1Prob=freqTab[list_of_column_names[1]][ty1][curClass]/curFre
    curFre=0
    for i in freqTab[list_of_column_names[2]]:
        curFre=curFre+freqTab[list_of_column_names[2]][i][curClass]
    ty2Prob=freqTab[list_of_column_names[2]][ty2][curClass]/curFre
    curFre=0
    for i in freqTab[list_of_column_names[3]]:
        curFre=curFre+freqTab[list_of_column_names[3]][i][curClass]
    ty3Prob=freqTab[list_of_column_names[3]][ty3][curClass]/curFre
    curFre=0
    for i in freqTab[list_of_column_names[4]]:
        curFre=curFre+freqTab[list_of_column_names[4]][i][curClass]
    ty4Prob=freqTab[list_of_column_names[4]][ty4][curClass]/curFre
    return ty1Prob*ty2Prob*ty3Prob*ty4Prob*(totClass/n)

ty1=input('Enter Type of Body Temperature\n') 
ty2=input('Enter does it gives Birth\n')
ty3=input('Enter is it Aerial Creature\n')
ty4=input('Enter is it Aquatic Creature\n')
print("For given condition probabilty for it to be mammel is",findProb(ty1,ty2,ty3,ty4,'mammal'))
print("For given condition probabilty for it to be Non mammel is",findProb(ty1,ty2,ty3,ty4,'NonMammal'))


