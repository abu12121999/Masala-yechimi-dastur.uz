1
k,n=map(int,input().split())
for i in range(n):
    print(k,end=' ')

2
s=0
a,b = map(int,input().split())
for i in range(a,b+1):
    s+=1
    print(i,end=' ')
print('soni=>',s,'ta')

3
s=0
a,b = map(int,input().split())
for i in range(a+1,b)[::-1]:
    s+=1
    print(i,end=' ')
print('soni=>',s,'ta')

4
narx=float(input())
for i in range(1,11):
    print(narx*i)

5
narx=float(input())
for i in range(1,11):
    print(int(narx*i/10))
    
6
narx=float(input())
for i in range(12,21,2):
    print(narx*i/10)


7
s=0
a,b = map(int,input().split())
for i in range(a,b):
    s+=i
print(s)

8
s=1
a,b = map(int,input().split())
for i in range(a,b):
    s*=i
print(s)

9
s=0
a,b = map(int,input().split())
for i in range(a,b):
    s+=i**2
print(s)

10
n=int(input())
s=0
for i in range(1,n+1):
    s+=1/i
print(s)


11
n=int(input())
s=0
for i in range(n+1):
    s+=(n+i)**2
print(s)

12
s=1
n=int(input())
for i in range(11,n+11):
    s*=i/10
print(s)
    
13
s=0
n=int(input())
for i in range(11,n+11):
    s+=(-1)**(i+1)*i/10
print(s)

14
s=0
n=int(input())
for i in range(1,n+1):
    s+=2*i-1
    print(s)

15
s=1
a=float(input('sonni kirit=> '))
n=int(input('darajani kirit=> '))
for i in range(1,n+1):
    s*=a
print(s)

16
s=1
a=float(input('sonni kirit=> '))
n=int(input('darajani kirit=> '))
for i in range(1,n+1):
    s*=a
    print(s)

17
s=1
S=1
a=float(input('sonni kirit=> '))
n=int(input('darajani kirit=> '))
for i in range(1,n+1):
    s*=a
    S+=s
    print(s)
print(S)


18
s=1
S=1
a=float(input('sonni kirit=> '))
n=int(input('darajani kirit=> '))
for i in range(1,n+1):
    s*=a
    S+=s*(-1)**i
    print(s)
print(S)

19
n=int(input())
s=1
for i in range(1,n+1):
    s*=i
print(s)

20
sum=0
n=int(input())
s=1
for i in range(1,n+1):
    s*=i
    sum+=s
print(sum)

36
n,k = map(int,input('n va k => ').split())
sum=0
for i in range(1,n+1):
    sum+=i**k
print(sum)

37
n = int(input('n=> '))
sum=0
for i in range(1,n+1):
    sum+=i**i
print(sum)


38
n = int(input('n=> '))
sum=0
for i in range(1,n+1):
    sum+=i**n
    n-=1
print(sum)


39
a,b = map(int,input(' a va b => ').split())
for i in range(a+1,b):
    print(str(i)*i)

40
n=1
a,b = map(int,input(' a va b => ').split())
for i in range(a+1,b):
    print(str(i)*n)
    n+=1


