d = {}
with open('4.txt') as f:
    r = f.read()
    for i in r:
        if ( i not in d.values()):
            d[ord(i)] = i
s = str()
with open("newFile4.txt",'w') as file:
    for i in sorted(d)[::-1]:
        s += d[i]
    file.write(s)