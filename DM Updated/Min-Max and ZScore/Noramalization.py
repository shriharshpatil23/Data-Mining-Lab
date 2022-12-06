from cmath import sqrt
import pandas
import math
import csv  

############################################## DATA READING FROM CSV ########################################################
data = pandas.read_csv('Normalization_Input.csv')
arr = data['Marks'].tolist()
############################################################################################################################

############################################# Initialization ###############################################################
n = len(arr)                
sum_array = sum(arr)        
mean_array = sum_array/n  
max_array = max(arr)        
min_array = min(arr)        
############################################################################################################################


############################################# Min-Max normalization ########################################################
MinMaxNorm = []
newMax=1
newMin=0
for i in arr:
    if max_array-min_array==0 :
        MinMaxNorm.append(0)
    else:
        tmp = ((i-min_array)/(max_array-min_array))*(newMax-newMin)           
        MinMaxNorm.append(tmp)
############################################################################################################################


############################################# Z-score normalization ########################################################
sum_of_square = 0

for i in arr:
    sum_of_square += (i-mean_array)*(i-mean_array)  

standardDeviation = sqrt(sum_of_square/n)           

ZscoreNorm = []

for i in arr:
    if standardDeviation==0 :
        ZscoreNorm.append(0)
    else :
        tmp = (i-mean_array)/standardDeviation
        ZscoreNorm.append(tmp)
############################################################################################################################


####################################### Writing output in CSV ##############################################################
header = ['Input', 'Min-Max Normalized Array', 'Zscore Normalized Array']

with open('Normalization_Output.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data
    #writer.writerow(data)

    for i in range(len(ZscoreNorm)):
        data = [arr[i],MinMaxNorm[i],ZscoreNorm[i]]
        writer.writerow(data)
############################################################################################################################