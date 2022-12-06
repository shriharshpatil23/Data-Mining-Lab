import pandas as pd

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
        ans.update({i:[y,no]})
    return ans

list_of_column_names = list(data.columns) 
colLen=len(list_of_column_names)
freqTab={}
for i in range (1,colLen):
    freqTab.update({list_of_column_names[i]:findFreqPerCol(data[list_of_column_names[i]])})

print(freqTab)

def findProb(ty1,ty2,ty3,ty4,className):
    curClass=0
    if className=='mammal':
        curClass=0
    elif className=='NonMammal':
        curClass=1
    totClass=freqTab[list_of_column_names[colLen-1]][className][curClass]
    ty1Prob=freqTab[list_of_column_names[1]][ty1][curClass]/totClass
    ty2Prob=freqTab[list_of_column_names[2]][ty2][curClass]/totClass
    ty3Prob=freqTab[list_of_column_names[3]][ty3][curClass]/totClass
    ty4Prob=freqTab[list_of_column_names[4]][ty4][curClass]/totClass
    return ty1Prob*ty2Prob*ty3Prob*ty4Prob*(totClass/n)

ty1=input('Enter Type of Body Temperature\n') 
ty2=input('Enter does it gives Birth\n')
ty3=input('Enter is it Aerial Creature\n')
ty4=input('Enter is it Aquatic Creature\n')
print("For given condition probabilty for it to be mammel is",findProb(ty1,ty2,ty3,ty4,'mammal'))
print("For given condition probabilty for it to be Non mammel is",findProb(ty1,ty2,ty3,ty4,'NonMammal'))
