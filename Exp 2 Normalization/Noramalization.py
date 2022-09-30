from cmath import sqrt
import pandas
import csv  
from scipy import stats
 
# reading the CSV file
csvFile = pandas.read_csv('Noramalization_Input.csv')
 
#Storing all elements in Array
arr = csvFile['Array'].tolist()
n = len(arr)                #length of Array
sum_array = sum(arr)        #Sum of all elements in Array
mean_array = sum_array/n    #Mean of Array
max_array = max(arr)        #Max of all elements in Array
min_array = min(arr)        #Min of all elements in Array
new_min = 0
new_max = 1
MinMaxNorm = []

if min_array == max_array:
    for i in range(n):
        MinMaxNorm.append(new_max-new_min)
else:
    for i in arr:
        tmp = ((i-min_array)*(new_max-new_min))/(max_array-min_array)           #Min Max Normalization Formula
        MinMaxNorm.append(tmp)

sum_of_square = 0

for i in arr:
    sum_of_square += (i-mean_array)*(i-mean_array)  #finding sum of Square of all elements in Array

standardDeviation = sqrt(sum_of_square/n)           #calculating Standard Deviation

ZscoreNorm = []
if standardDeviation==0:
    for i in range(n):
        ZscoreNorm.append(0)
else:
    for i in arr:
        tmp = (i-mean_array)/standardDeviation
        ZscoreNorm.append(tmp)

print(ZscoreNorm)

# newZscore = arr
# print(stats.zscore(newZscore))

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