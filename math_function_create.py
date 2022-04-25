import math as m
# 1 abs or fabs

def modul(a):
    if a>0:
        return a
    elif a<0:
        return -1*a
    else:
        return 0

s = float(input(" sonni kiriting => "))
print(modul(s))
   
# 2 factorial
def faktorial(a):
    i=1
    faktr = 1
    while i <= a:
        faktr *= i
        i += 1
    return faktr
             
s = float(input(" sonni kiriting => "))
print(faktorial(s))
    
# 3 pow
def daraja(a,b):
    return a**b

print(daraja(16,0.5))

# 4 sqrt
def kv_ildiz(a):
    if a>=0:
        return a**0.5
    else:
        return "ValueError: math domain error"
print(kv_ildiz(5))

# 5 degrees

def daraja(a):
    return (a*180)/3.14159265358979323
print(daraja(-1))

# 6 radians
def radian(a):
    return (a*3.14159265358979323)/180
print(radian(57))

# 7 exp
def e_daraja(a):
    return 2.718281828459045**a
print(e_daraja(9))

# 8 ceil
def max_yaxlitla(a):
    if a > 0:
        if int(a) == a:
            return a
        else:
            return int(a)+1
    elif a < 0:
        return int(a)
    else:
        return 0
print(max_yaxlitla(6.2))
print(m.ceil(6.2))

# 9 floor
def min_yaxlitla(a):
        if a > 0:
            return int(a)
        elif a < 0:
            if int(a) == a:
                return a
            else:
                return int(a)-1
        else:
            return 0
print(min_yaxlitla(4))

# 10 fmod
def qoldiqni_top(a,b):
    
    if a>0 and b>0:
        while a>b:
            a-=b
        return float(a)
    
    elif a>0 and b<0:
        while a>0:
            a+=b
        return float(a-b)
    
    elif a<0 and b>0:
        a=-a
        while a>b:
            a-=b
        return float(-a)
    
    elif a == 0 or b == 0:
        if a == 0 and b != 0 :
            return 0
        elif a != 0 and b == 0:
            return"ValueError: math domain error"
        else:
            return"ValueError: math domain error"

print(qoldiqni_top(0, 0))
print (m.fmod(0, 0))
