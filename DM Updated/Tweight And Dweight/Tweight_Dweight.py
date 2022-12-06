import numpy as np
import pandas as pd
import csv
########################################## DATA READING FROM CSV ############################################################
data = pd.read_csv('Tweight_Dweight_Input.csv')
Location = data['Class'].tolist()
A = data['First'].tolist()
B = data['Second'].tolist()    
#############################################################################################################################

######################################### T-Weight, D-weight calculation ####################################################
Total = []
for i in range(len(A)):
    tmp = A[i]+B[i]
    Total.append(tmp)

A_T_wt = []
B_T_wt = []
A_D_wt = []
B_D_wt = []
verify=[]
sum_total = sum(Total)
A_total=sum(A)
B_total=sum(B)
for i in range(len(A)):
    A_T_wt.append(A[i]/Total[i])
    B_T_wt.append(B[i]/Total[i])
    A_D_wt.append(A[i]/A_total)
    B_D_wt.append(B[i]/B_total)
    verify.append(A_T_wt[i]+B_T_wt[i])
###############################################################################################################################

############################################## Writing final output into CSV file #############################################
header = ['Company', 'Male', 'Female', 'Total' , 'Male_T_wt','Female_T_wt','verify t weight','Male_D_wt','Female_D_wt']

with open('Tweight_Dweight_Output.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data

    for i in range(len(A)):
        data = [Location[i],A[i],B[i],Total[i],A_T_wt[i],B_T_wt[i],verify[i],A_D_wt[i],B_D_wt[i]]
        writer.writerow(data)
    
    dValid=["Male d weight total",sum(A_D_wt)]
    writer.writerow(dValid)
    dValid=["Female d weight total",sum(B_D_wt)]
    writer.writerow(dValid)
################################################################################################################################
