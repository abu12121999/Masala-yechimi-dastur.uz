s = str()
with open('2.txt') as f:
    r = f.read()
    for i in r:
        if ( i not in s):
            s += i
with open("newFile2.txt",'w') as file:
    file.write(s)