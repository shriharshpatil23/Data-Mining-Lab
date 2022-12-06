import math
import numpy as np
import pandas as pd
import csv

################################################# Data reading from CSV ##########################################################
data=pd.read_csv('input.csv')
X = data['X'].tolist()
Y = data['Y'].tolist()
##################################################################################################################################


################################################ Function to calculate euclidan distance #########################################
def dist(x1,y1,x2,y2):
    a = (x2-x1)*(x2-x1)
    b = (y2-y1)*(y2-y1)
    ans = math.sqrt(a+b)
    return ans
##################################################################################################################################

############################################### Finding centroid #################################################################
n = len(X)
x_mid = sum(X)/n
y_mid = sum(Y)/n
x = []
y = []
minimum = 1e9
x.append(x_mid)
y.append(y_mid)
for i in range(n):
    x.append(X[i])
    y.append(Y[i])
##################################################################################################################################

############################################## Finding distance from centroid and putting it into upper triangular matrix ########
def findClustMat (a,b):
    N = len(x)
    matClust = [[0 for _ in range(N)] for _ in range(N)]
    minDist=1e9
    maxDist=-1e9
    nx=-1
    ny=-1
    x[0]=a
    y[0]=b
    for i in range(len(x)):
        for j in range(i+1,len(y)):
            matClust[i][j]=dist(x[i],y[i],x[j],y[j])
            if i==0 and dist(x[i],y[i],x[j],y[j])<minDist:
                minDist=dist(x[i],y[i],x[j],y[j])
                nx=x[j]
                ny=y[j]
            if i==0 and dist(x[i],y[i],x[j],y[j])>maxDist:
                maxDist=dist(x[i],y[i],x[j],y[j])
    for i in range(len(x)):
        print(matClust[i])   
    clstPnt=[nx,ny,minDist,maxDist]
    return clstPnt

def findClustMatrix(a,b):
    N = len(x)
    matClust = [[0 for _ in range(N)] for _ in range(N)]
    x[0]=a
    y[0]=b
    for i in range(len(x)):
        for j in range(i+1,len(y)):
            matClust[i][j]=dist(x[i],y[i],x[j],y[j])
    
    return matClust

curClstPnt=findClustMat(x_mid,y_mid)
finalAns=findClustMat(curClstPnt[0],curClstPnt[1])
print("Final center is {},{}".format(curClstPnt[0],curClstPnt[1]))
print("Final rad is {}".format(finalAns[3]))
centMat=findClustMatrix(x_mid,y_mid)
finalMat=findClustMatrix(curClstPnt[0],curClstPnt[1])


############################################# Writing output into CSV file #######################################################
with open('output.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    addRow=['Matrix from centroid',x_mid,y_mid]
    writer.writerow(addRow)

    for i in range(len(x)):
        writer.writerow(centMat[i])

    addRow=['Matrix from new center',curClstPnt[0],curClstPnt[1]]
    writer.writerow(addRow)

    for i in range(len(x)):
        writer.writerow(finalMat[i])
    
    addRow=['Final center',curClstPnt[0],curClstPnt[1]]
    writer.writerow(addRow)
    addRow=['Final radius',finalAns[3]]
    writer.writerow(addRow)
#################################################################################################################################