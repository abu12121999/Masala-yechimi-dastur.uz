d = {}
with open('3.txt') as f:
    r = f.read()
    for i in r:
        if ( i not in d.values()):
            d[ord(i)] = i
s = str()
with open("newFile3.txt",'w') as file:
    for i in sorted(d):
        s += d[i]
    file.write(s)