d = {}
l = list()
with open('5.txt') as f:
    r = f.read()
    for i in r:
        if i.islower():
            l.append(i)
    for i in sorted(l):
        d[i] = l.count(i)
          
print(sorted(l))
print(d)