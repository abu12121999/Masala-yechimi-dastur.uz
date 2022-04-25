1
n = str(input("Satrni kiriting=> "))
k={}

for i in n:
    k[i] = ord(i)
print(k)  
    
2
n = int(input("ASCII kodi tartib raqamini kiriting=> "))
print(n,"- raqamli kod -> ",chr(n))

3
s = str(input('belgini kiriting=> '))
print(s," dan oldingi ", chr(ord(s)-1))
print(s," dan keyingi ",chr(ord(s)+1))

4
n = int(input("Sonni kiriting=> "))

if 1<=n<=26:
    for i in range(n):
        print(chr(65+i))
else:
    print("Bu son oraliqga tegishli emas!")

5
n = int(input("Sonni kiriting=> "))

if 1<=n<=26:
    for i in range(n):
        print(chr(122-i))
else:
    print("Bu son oraliqga tegishli emas!")

6
s = str(input('belgini kiriting=> '))

if s.isdigit():
    print("digit")
elif 65 <= ord(s) <= 90 or 97 <= ord(s) <= 122  :
    print("lotin")
else:
    print("0")
    
7
s = str(input('Satrni kiriting=> '))
print(ord(s[0])," va ",ord(s[-1]))

8
s = str(input('belgini kiriting=> '))
n = int(input("Sonni kiriting=> "))
print(s*n)

9
s1 = str(input('Satr 1ni kiriting=> '))
s2 = str(input('Satr 2ni kiriting=> '))
print(s1+s2)

10
s = str(input('Satrni kiriting=> '))
for i in range(len(s))[::-1]:
    print(s[i],end='')

11
s = str(input('Satrni kiriting=> '))
s1 = s.replace(" ", "")
print(" ".join(s1))

12
s = str(input('Satrni kiriting=> '))
n = int(input('Sonni kiritng=> '))
a = s.replace("", "*"*n)
print(a.strip("*"*n))

13
s = str(input('Satrni kiriting=> '))
sum = 0
for i in s:
    if i.isdigit():
        sum+=1
print(sum)

14
s = str(input('Satrni kiriting=> '))
sum = 0
for i in s:
    if 65 <= ord(i) <=90:
        sum+=1
print(sum)

