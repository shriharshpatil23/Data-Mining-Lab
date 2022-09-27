import pandas
import csv
import math

data = pandas.read_csv("BoxPlot_Input.csv")

arr = data['A'].tolist()
#sort the Array
arr.sort()

n= len(arr)
Min_val = min(arr)
Max_val = max(arr)
Median_val = arr[(n+1)//2-1]
quartile_1 = arr[(n+1)//4-1]
quartile_3 = arr[3*(n+1)//4-1]

header = ['Min Value', 'Max Value', 'Median','Quartile 1','Quartile 3']

with open('BoxPlot_Output.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data

    data = [Min_val,Max_val,Median_val,quartile_1,quartile_3]
    writer.writerow(data)