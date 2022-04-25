1
a,b = map(int,input().split())
while a>b:
    a-=b
print(a)


2
s=0
a,b = map(int,input().split())
while a>b:
    a-=b
    s+=1
print(s)

3
s=0
a,b = map(int,input().split())
while a>b:
    a-=b
    s+=1
print('qoldiq: ',a)
print('bo\'linma: ', s)

4
s=0
a=int(input())
while a>=3:
    a-=3
if(a==0):
    print("3 ning darajasi")
else:
    print("3 ning darajasi emas")

5
s=0
a=int(input())
while a>=2:
  a/=2
  s+=1
print(s)

6
s=1
n=int(input())
while n>0:
    s*=n
    n-=2
    if n==0 or n==-1:
        break
print(s)

7
n=int(input())
k=n
while k**2>n:
    k-=1
print(k+1)

8
n=int(input())
k=1
while k**2<=n:
    k+=1
print(k-1)

9
n=int(input())
k=n
while 3**k>n:
    k-=1
print(k+1)

10
n=int(input())
k=0
while 3**k<=n:
    k+=1
print(k-1)


12
s=0
n=int(input())
k=0
while s<=n:
    k+=1
    s+=k
print(k-1,s-k)


14
s=0
n=int(input())
k=0
while s<=n:
    k+=1
    s+=1/k
print(k-1,s-1/k)

15
S=float(input("summa=> "))
p=int(input('foiz=> '))
s=p*S/100+S
k=1
while s/S<=2:
    k+=1
    s+=s*(p/100)
print(k,s)

16
s=10
S=s
k=0
p=int(input('foiz=> '))
while S<=200:
    s=s*(1+p/100)
    k+=1
    S+=s
print(k,S)

17
s=0
n,m = map(int,input().split())
while n>m:
    n-=m
    s+=1
print('qoldiq: ',n)
print('bo\'linma: ', s)


