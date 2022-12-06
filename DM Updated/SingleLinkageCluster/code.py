import pandas as pd
import math 
data=pd.read_csv('data1.csv')
listOfCol=data.columns
points=[]
for i in data[listOfCol[0]]:
    points.append([i])

n=data['X'].size

def findDistMat(points):
    
    dist_mat=[]
    for i in range(0,n):
        add=[]
        for j in range(0,n):
            add.append(0)
        dist_mat.append(add)
    for i in range(0,n):
        for j in range(0,n):
            curDist=((data['X'][i]-data['X'][j])*(data['X'][i]-data['X'][j]))+((data['Y'][i]-data['Y'][j])*(data['Y'][i]-data['Y'][j]))
            dist_mat[i][j]=curDist
    return dist_mat


dist_mat=findDistMat(points)
print(dist_mat)
cnt=n
for itr in range(0,n-1):
    print("current points ->",points)
    print(dist_mat)
    dist=1e10
    curR=-1
    curC=-1
    newMat=[]
    for i in range(0,cnt):
        for j in range(0,cnt):
            if i!=j and dist>dist_mat[i][j]:
                dist=dist_mat[i][j]
                curR=i
                curC=j
    finalAdd=[]
    
    for i in range(0,cnt):
        add=[]
        m=1e10
        for j in range(0,cnt):
            if i!=curR and i!=curC:
                #print(i,curR,curC)
                m=min(dist_mat[i][curR],dist_mat[i][curC])
                if j!=curR and j!=curC:
                    add.append(dist_mat[i][j])
        if m!=1e10:
            finalAdd.append(m)
            add.append(m)
        if len(add)!=0:
            newMat.append(add)
    finalAdd.append(0)
    newMat.append(finalAdd)
    #print(points[curR],points[curC])
    rem1=points[curR]
    rem2=points[curC]
    points.remove(rem1)
    points.remove(rem2)
    #print(points)
    points.append([rem1,rem2])
    dist_mat=newMat
    cnt=cnt-1


    

print("current points ->",points)
print(dist_mat)