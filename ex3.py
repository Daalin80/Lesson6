l = ['a', 'b', 'c', 'd', 'e']
indexes = []
for i in l:
       indexes.append(l.index(i))
s = dict(zip(indexes, l))
print(s)