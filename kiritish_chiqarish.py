  #1 va 2
a=float(input('kvadrat tomoni= '))
print('P= ',4*a,'  S= ',a**2)


# 3
a,b=map(float,input('a va b ni kiriting=> ').split())
print('P= ',2*(a+b),'  S= ',a*b)

# 4
import  math as m
d=float(input('d='))
print('L=',m.pi*d)

# 5
a=float(input('kub tomoni= '))
print('V= ',a**3,'  S= ',6*a**2)

# 6
s=0
v=1
a=list(map(float,input('tomonlarni kiriting=').split()))
k=len(a)
for i in range(k):
    s+=a[i-1]*a[i]
    v*=a[i]
S=s*2
V=v
print('V=',V,'\tS=',S)

# 7
import  math as m
r=float(input('r='))
print('L=',2*m.pi*r,'\tS=',m.pi*r**2)

# 8
a,b=map(float,input('a va b ni kiriting=> ').split())
print('average=> ',0.5*(a+b))

# 9
a,b=map(float,input('a va b ni kiriting=> ').split())
print('av.geom=> ',(a*b)**0.5)

#10 va 11
a,b=map(float,input('a va b ni kiriting=> ').split())
print(a+b,a*b,a**2,b**2,abs(a),abs(b),sep='\n')

# 12
a,b=map(float,input('katetlarni kiriting=> ').split())
c=(a**2+b**2)**0.5
p=a+b+c
print(c,p,sep='\n')

# 13
import math as m
r1,r2=map(float,input('r1 va r2 ni kiriting=> ').split())
S1=m.pi*r1**2
S2=m.pi*r2**2
if(r1<r2):
    r1,r2=r2,r1
S3=m.pi*(r1**2-r2**2)
print(S1,S2,S3,sep='\n')

# 14
import  math as m
L=float(input('L='))
print('r=',L/(2*m.pi),'\tS=',m.pi*(L/(2*m.pi))**2)

# 15
S=float(input('S='))
print('r=',(S/3.14)**0.5,'\td=',2*(S/3.14)**0.5)

# 16
x1,x2=map(int,input('x1 va x2 nuqtani kiriting=> ').split())
print('nuqtalar orasidagi masofa=',abs(x1-x2))

#17 va 18
A=float(input('A nuqtani kiriting: '))
B=float(input('B nuqtani kiriting: '))
C=float(input('C nuqtani kiriting: '))
print('AC kesma uzunligi=',abs(A-C))
print('BC kesma uzunligi=',abs(B-C))
print('AC va BC kesma yig\'indisi=',abs(A-C)+abs(B-C))
print('AC va BC kesma ko\'paytmasi=',abs(A-C)*abs(B-C),C)

# 19
x1,y1=map(float,input('x1 va y1 kiriting=> ').split())
x2,y2=map(float,input('x2 va y2 kiriting=> ').split())
a=abs(x1-x2)
b=abs(y1-y2)
print('P=',2*(a+b),'  S=',a*b)

# 20
x1,y1=map(float,input('x1 va y1 kiriting=> ').split())
x2,y2=map(float,input('x2 va y2 kiriting=> ').split())
a=abs(x1-x2)
b=abs(y1-y2)
print('masofa=',(a**2+b**2)**0.5)