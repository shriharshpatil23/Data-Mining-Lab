import numpy as np
import pandas as pd
import csv
data = pd.read_csv('Tweight_Dweight_Input.csv')

Location = data['Location'].tolist()
A = data['A'].tolist()
B = data['B'].tolist()    
Total = []

for i in range(len(A)):
    tmp = A[i]+B[i]
    Total.append(tmp)


A_T_wt = []
B_T_wt = []
A_D_wt = []
B_D_wt = []
sum_total = sum(Total)

for i in range(len(A)):
    A_T_wt.append(A[i]/Total[i])
    B_T_wt.append(B[i]/Total[i])
    A_D_wt.append(A[i]/sum_total)
    B_D_wt.append(B[i]/sum_total)

header = ['Location', 'A', 'B', 'Total' , 'A_T_wt','B_T_wt','A_D_wt','B_D_wt']



with open('Tweight_Dweight_Output.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data
    #writer.writerow(data)

    for i in range(len(A)):
        data = [Location[i],A[i],B[i],Total[i],A_T_wt[i],B_T_wt[i],A_D_wt[i],B_D_wt[i]]
        writer.writerow(data)