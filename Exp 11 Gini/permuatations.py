from itertools import combinations

features = ['A', 'B', 'C']
tmp = []
for i in range(len(features)):
    oc = combinations(features, i + 1)
    for c in oc:
        tmp.append(list(c))

print(tmp)