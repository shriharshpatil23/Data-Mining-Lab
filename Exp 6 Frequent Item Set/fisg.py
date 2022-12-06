import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
import csv
  
data = []
with open('csvData.csv') as file_obj:
      
    # Create reader object by passing the file 
    # object to reader method
    reader_obj = csv.reader(file_obj)
      
    # Iterate over each row in the csv 
    # file using reader object
    for row in reader_obj:
        data.append(row)

print(data)

tr = TransactionEncoder()
tr_arr = tr.fit(data).transform(data)
df = pd.DataFrame(tr_arr, columns=tr.columns_)
print(df)
colNames = list(df.columns)
n = len(df[colNames[0]])
for i in range(0,n):
    df[colNames[0]][i] = False

print(df)

from mlxtend.frequent_patterns import apriori
frequent_itemsets = apriori(df, min_support = 0.5, use_colnames = True)
print(frequent_itemsets)