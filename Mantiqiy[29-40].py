29
x,y=map(int,input('x va y ni kiriting=> ').split())
x1,y1=map(int,input('x1 va y1 ni kiriting=> ').split())
x2,y2=map(int,input('x2 va y2 ni kiriting=> ').split())
# if( (x1<x<x2) and (y1<y<y2)):
if( (x1<x<x2) and (y1<y) and (y<y2)):
    print('yotadi')
else:
    print('yotmaydi')

uchburchak
a=int(input('a=>'))
b=int(input('b=>'))
c=int(input('c=>'))
if((a+b>c) and (a+c>b) and (b+c>a)):
    if(a==b==c):
        print('teng tomonli uchburchak')
    elif((a==b) or (a==c) or (b==c)):
        print('teng yonli uchburchak')
    elif((a**2+c**2==b**2) or (a**2+b**2==c**2) or (b**2+c**2==a**2)):
        print('to\'g\'ri burchakli uchburchak')
    else:
        print("turli tomonli uchburchak")
else:
    print("bu o'lchamlar bilan uchburchak yasab bo'lmaydi")

# shaxmat
# 34
x,y=map(int,input('kordinatani kiriting [1,8] oralig\'i=> ').split())
a=x+y
if(a%2==0):
    print('black')
else:
    print('white')

# 35
x1,y1=map(int,input('1-kordinatani kiriting [1,8] oralig\'i=> ').split())
x2,y2=map(int,input('2-kordinatani kiriting [1,8] oralig\'i=> ').split())
a=x1+y1
b=x2+y2
if((a%2==0 and b%2==0) or (a%2!=0 and b%2!=0)):
    print('bir xil rangda')
else:
    print('bir xil rangda emas')

# 36 ruh

x1,y1=map(int,input('1-kordinatani kiriting [1,8] oralig\'i=> ').split())
x2,y2=map(int,input('2-kordinatani kiriting [1,8] oralig\'i=> ').split())

if(x1==x2 or y1==y2):
    print("ruh yura oladi")
else:
    print("ruh yura olmaydi")

# 37 shoh

x1,y1=map(int,input('1-kordinatani kiriting [1,8] oralig\'i=> ').split())
x2,y2=map(int,input('2-kordinatani kiriting [1,8] oralig\'i=> ').split())
a=(y2==y1+1) and ((x2==x1-1) or (x2==x1) or (x2==x1+1)) 
b=(y2==y1-1) and ((x2==x1-1) or (x2==x1) or (x2==x1+1))
c=(y2==y1) and ((x2==x1-1) or (x2==x1+1))  
if(a or b or c):
    print("shoh yura oladi");
else:
    print("shoh yura olmaydi")
    
# 38 fil

x1,y1=map(int,input('1-kordinatani kiriting [1,8] oralig\'i=> ').split())
x2,y2=map(int,input('2-kordinatani kiriting [1,8] oralig\'i=> ').split())

a=x1-x2
b=y1-y2
if(a==b):
    print("ruh yura oladi")
else:
    print("ruh yura olmaydi")
    
# 39 farzin

x1,y1=map(int,input('1-kordinatani kiriting [1,8] oralig\'i=> ').split())
x2,y2=map(int,input('2-kordinatani kiriting [1,8] oralig\'i=> ').split())

a=x1-x2
b=y1-y2
if((a==b) or (x1==x2) or (y1==y2)):
    print("farzin yura oladi")
else:
    print("farzin yura olmaydi")

# 40 ot

x1,y1=map(int,input('1-kordinatani kiriting [1,8] oralig\'i=> ').split())
x2,y2=map(int,input('2-kordinatani kiriting [1,8] oralig\'i=> ').split())

a=(x2==x1+1) and ((y2==y1+2) or (y2==y1-2))
b=(x2==x1-1) and ((y2==y1+2) or (y2==y1-2))

if(a or b):
    print("ot yura oladi")
else:
    print("ot yura olmaydi")
    
