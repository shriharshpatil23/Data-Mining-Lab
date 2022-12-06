import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
 
## Use this to read data directly from github
df = pd.read_csv('csvData.csv')
print(df)
 
items = set()
# for col in df:
#     items.update(df[col].unique())
# print(items)
colNames = list(df.columns)
print(colNames)
for col in colNames:
    for x in df[col]:
        items.add(x)

print(items)
itemset = set(items)
encoded_vals = []
for index, row in df.iterrows():
    rowset = set(row)
    labels = {}
    uncommons = list(itemset - rowset)
    commons = list(itemset.intersection(rowset))
    for uc in uncommons:
        labels[uc] = 0
    for com in commons:
        labels[com] = 1
    encoded_vals.append(labels)
encoded_vals[0]
ohe_df = pd.DataFrame(encoded_vals)
freq_items = apriori(ohe_df, min_support=0.5, use_colnames=True, verbose=1)
n = len(freq_items)
print(freq_items)   
# rules = association_rules(freq_items, metric="confidence", min_threshold=0.5)
 
# print(rules.head(4)[["antecedents", "consequents", "support", "confidence"]])
 

