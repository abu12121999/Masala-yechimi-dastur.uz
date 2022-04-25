s = str()
with open('1.txt') as f:
    r = f.read()
    for i in r:
        if not i.isalnum():
            s += i
with open("newFile.txt",'w') as file:
    file.write(s)
