26
n = int(input('n=> '))
S = str(input('satr=> '))
s = list()
if len(S) < n:
    s.extend(['.']*(n-len(S)))
    s.extend(list(S))
    print(''.join(s))
if len(S) > n:
    S = S[(len(S)-n):]
    print(S)
else:
    print(S)

27
n1,n2 = map(int,input('n1 va n2 => ').split())
s1,s2 = map(str,input('s1 va s2 => ').split())
s3 = s1[:n1] + s2[(len(s2) - n2):]
print(s3)


28
a = str(input("belgini kiriting=> "))
b = str(input("So'zni kiriting=> "))
c = list()
for i in b:
    c.append(i)
    if a==i:
        c.append(i)
print("".join(c))

29
c = str(input('c=> '))
s1,s2 = map(str,input('s1 va s2 => ').split())
a = list()
for i in s1:
    if i==c:
        a.extend(list(s2))
    a.append(i)
print(''.join(a))

30
c = str(input('c=> '))
s1,s2 = map(str,input('s1 va s2 => ').split())
a = list()
for i in s1:
    a.append(i)
    if i==c:
        a.extend(list(s2))
print(''.join(a))

31
s1,s2 = map(str,input('s1 va s2 => ').split())
print(True) if s2 in s1 else print(False)

32
s1,s2 = map(str,input('s1 va s2 => ').split())
print(s1.count(s2))

33
s1 = str(input('s1 satrni kiriting=> '))
s2 = str(input('s2 satrni kiriting=> '))
print(s1.replace(s2, "",1))
34

s1 = str(input('s1 satrni kiriting=> '))
s2 = str(input('s2 satrni kiriting=> '))

x = list(s1)
x.reverse()
x1 = "".join(x)

x = list(s2)
x.reverse()
x2 = "".join(x)

y = x1.replace(x2, "",1)

x = list(y)
x.reverse()
s = "".join(x)

print(s)

35
s1 = str(input('s1 satrni kiriting=> '))
s2 = str(input('s2 satrni kiriting=> '))
print(s1.replace(s2, ""))

36
s1 = str(input('s1 satrni kiriting=> '))
s2 = str(input('s2 satrni kiriting=> '))
s3 = str(input('s3 satrni kiriting=> '))

print(s1.replace(s2, s3,1))

37

s1 = str(input('s1 satrni kiriting=> '))
s2 = str(input('s2 satrni kiriting=> '))
s3 = str(input('s3 satrni kiriting=> '))

x = list(s1)
x.reverse()
x1 = "".join(x)

x = list(s2)
x.reverse()
x2 = "".join(x)

x = list(s3)
x.reverse()
x3 = "".join(x)

y = x1.replace(x2, x3,1)

x = list(y)
x.reverse()

s = "".join(x)
print(s)

38
s1 = str(input('s1 satrni kiriting=> '))
s2 = str(input('s2 satrni kiriting=> '))
s3 = str(input('s3 satrni kiriting=> '))

print(s1.replace(s2, s3))

39
s = str(input('satrni kiriting=> '))

if s.count(" ")>1:
    x = s.split()
    print(x[1])
else:
    print(str())
    
40
s = str(input('satrni kiriting=> '))

if s.count(" ")>1:
    if s.endswith(" "):
        x = s.split()
        x.pop(0)
        print(" ".join(x))
    else:
        x = s.split()
        x.pop(0)
        x.pop(-1)
        print(" ".join(x))
else:
    print(str())

41

s = str(input('satrni kiriting=> '))

# 1-usul
x = s.split()
print(len(x))

# 2-usul
print(s.count(" ") + 1)


42
s = str(input('satrni kiriting=> '))
x = s.split()
summ = 0

for i in x:
    if i[0] == i[-1]:
        summ += 1
print(summ)

43
s = str(input('satrni kiriting=> '))
x = s.split()
summ = 0

for i in x:
    if "A" in i.upper():
        summ += 1
print(summ)

44
s = str(input('satrni kiriting=> '))
x = s.split()
summ = 0

for i in range(len(x)):
    if x[i].count("A") >2:
        summ += 1
print(summ)

45
s = str(input('satrni kiriting=> '))
x = s.split()
minum = len(x[0])

for i in range(len(x)):
    if minum >= len(x[i]):
        minum = len(x[i])
print(minum)
    

46
s = str(input('satrni kiriting=> '))
x = s.split()
maxim = len(x[0])

for i in range(len(x)):
    if maxim <= len(x[i]):
        maxim = len(x[i])
print(maxim)

47
s = str(input('satrni kiriting=> '))
x = s.split()
y = ".".join(x)
print(y)

48
s = str(input('satrni kiriting=> '))
s1 = s[0]
k = s.count(s1)
y = s.replace(s1, ".")
z = y.replace(".",s1,1)
print(z)

49
s = str(input('satrni kiriting=> '))
s1 = s[-1]
k = s.count(s1)
print(s.replace(s1, ".",k-1))

50
s = str(input('satrni kiriting=> '))
x = s.split()
y = " ".join(x)
for i in range(len(y))[::-1]:
    print(y[i],end='')

51
s = str(input('satrni kiriting=> '))
x = s.split()
y = sorted(x)
z = " ".join(y)
print(z)

52
s = str(input('satrni kiriting=> '))
print(s.title())

53
s = str(input('satrni kiriting=> '))
x = list()

for i in range(len(s)):
    if not s[i].isalnum():
        x.append(s[i])
print(" ".join(x))

54
s = str(input('satrni kiriting=> '))
summa = 0
for i in range(len(s)):
    if s[i].isupper():
        summa +=1
print(summa)

55
s = str(input('satrni kiriting=> '))
x = s.split()

m = x[0]

for i in range(len(x)):
    if len(x[i]) >= len(m):
        m = x[i]
print(m)

56       
s = str(input('satrni kiriting=> '))
x = s.split()

m = x[0]

for i in range(len(x)):
    if len(x[i]) <= len(m):
        m = x[i]
        print(m)
        

57
s = str(input('satrni kiriting=> '))
x = s.split()
y = " ".join(x)
print(y)

58
s = str(input('satrni kiriting=> '))
x = s.split("\\")
fayl_nomi = x[-1]
fayl = fayl_nomi.split(".")
fayl_nomi = fayl[0]
print(fayl_nomi)

59
s = str(input('satrni kiriting=> '))
x = s.split("\\")
fayl_nomi = x[-1]
fayl = fayl_nomi.split(".")
fayl_kengaytmasi = fayl[1]
print(fayl_kengaytmasi)

60
s = str(input('satrni kiriting=> '))
x = s.split("\\")

if len(x) ==2:
    print('\\')
else:
    print(x[1])

61
s = str(input('satrni kiriting=> '))
x = s.split("\\")

if len(x) ==2:
    print('\\')
else:
    print(x[-2])

62
s = str(input('satrni kiriting=> '))
k = list()
for i in range(len(s)):
    if s[i].isalpha() and s[i] != "z" and s[i] != "Z":
        k.append(chr(ord(s[i]) + 1))
    elif s[i] == "z":
        k.append("a")
    elif s[i] == "Z":
        k.append("A")
    else:
        k.append(s[i])
print(''.join(k))



66
s = str(input('satrni kiriting=> '))
j = list()
t = list()

for i in range(len(s)):
    if i%2 == 0:
        j.append(s[i])
    elif i%2 == 1:
        t.append(s[i])
x = "".join(j)
y = reversed(t)
z = "".join(y)
print(x + z)

67
s = str(input('satrni kiriting=> '))
t = list()
s1= list()
if len(s) %2 ==0:
   st = reversed(s)
   t = list(st)
   for i in range(len(s)//2):
       s1.append(s[i])
       s1.append(t[i])
   print("".join(s1))
else:
    st = reversed(s)
    t = list(st)
    s1.append(s[0])
    for i in range(len(s)//2):
        s1.append(t[i])
        s1.append(s[i+1])
    print("".join(s1))
    
       

    