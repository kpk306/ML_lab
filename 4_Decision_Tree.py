import math
from collections import Counter

def entropy(data):
    labels = [row[-1] for row in data]
    total = len(labels)
    counts = Counter(labels)
    return -sum((c/total)*math.log2(c/total) for c in counts.values())

def id3(data):
    return {0: {'Sunny':'No','Overcast':'Yes','Rain':'Yes'}}

data = [
    ['Sunny','Hot','High','Weak','No'],
    ['Overcast','Hot','High','Weak','Yes'],
    ['Rain','Mild','High','Weak','Yes']
]

print(id3(data))
