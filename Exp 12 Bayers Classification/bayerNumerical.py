import pandas as pd

data = pd.read_csv("data.csv")

mammal = data['Class Label']
n = len(mammal)

for i in range(0,n):
    if mammal[i]!='mammal':
        mammal[i] = 'NO'
    else:
        mammal[i] = 'YES'

def FindFrequencyInColumn(col):
    ans = {}
    st = set()
    for x in col:
        st.add(x)
    for x in st:
        yes = 0
        no = 0
        for i in range(0,n):
            if col[i]==x and mammal[i]=='YES':
                yes += 1
            elif col[i]==x and mammal[i] == 'NO':
                no += 1
        ans.update({x:[yes,no]})
    return ans

colNames = list(data.columns)
colLen = len(colNames)
dict = {}
for i in range(0,colLen):
    dict.update({colNames[i] : FindFrequencyInColumn(data[colNames[i]])})

def findProbability(a,b,c,d,name):
    currClass = 0
    if name=='YES':
        currClass = 0
    else:
        currClass = 1
    total = dict[colNames[colLen-1]][name][currClass]
    prob1 = dict[colNames[1]][a][currClass]/total
    prob2 = dict[colNames[2]][b][currClass]/total
    prob3 = dict[colNames[3]][c][currClass]/total
    prob4 = dict[colNames[4]][d][currClass]/total
    return prob1*prob2*prob3*prob4*(total/n)


print("For Mammal :", findProbability('warm-blooded','yes','yes','no','YES'))
print("For Non-Mammal :", findProbability('warm-blooded','yes','yes','no','NO'))