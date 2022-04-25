rs = '0123456789'
shifr = str()
with open('7.txt') as f:
    rf = f.read()
    for i in range(len(rf)):
        if i == 0:
            shifr += chr(ord(rf[0]) + int(rs[0]))
        else:
            shifr += chr(ord(rf[i]) + int(rs[i%10]))
    print(rf)
    print(shifr)
        
