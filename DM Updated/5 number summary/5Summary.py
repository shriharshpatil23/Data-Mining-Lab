import pandas
import csv
import math

############################################ Data reading from CSV file ##############################################################
data = pandas.read_csv("5noInput.csv")
arr = data['Marks'].tolist()
arr.sort()
######################################################################################################################################

########################################### Function to calculate median #############################################################
def median(array,start,end):
    n = end - start +1
    if n%2==0:
        return (array[start + (n//2) -1]+array[start + (n//2) ])/2
    else:
        return array[start+ n//2]
######################################################################################################################################

########################################### Finding 5 number summary #################################################################
n= len(arr)
Min_val = min(arr)
Max_val = max(arr)
Median_val = median(arr,0,n-1)
quartile_1 = median(arr,0,n//2-1)
quartile_3 = median(arr,n//2+1,n-1)
IQR = quartile_3-quartile_1
upper_outlinear = quartile_3 + 1.5*(IQR)
lower_outlinear = quartile_1 - 1.5*(IQR)
#######################################################################################################################################

########################################### Writing output into CSV ###################################################################
header = ['Min Value', 'Max Value', 'Median','Quartile 1','Quartile 3','Upper Quartile','Lower Outliner']

with open("5noOutput.csv", 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data

    data = [Min_val,Max_val,Median_val,quartile_1,quartile_3,upper_outlinear,lower_outlinear]
    writer.writerow(data)
#######################################################################################################################################