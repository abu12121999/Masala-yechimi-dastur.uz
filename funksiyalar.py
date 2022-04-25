1
def PowerA3(a=0.0,b=0.0,c=0.0,d=0,e=0):
    # l = [a,b,c,d,e]
    # for i in range(len(l)):
    #     print( l[i]**3)
    return a**3, b**3, c**3, d**3, e**3
print(type(PowerA3(1,2,3,4,5)))
        
2
def PowerA234(a=0.0,b=0.0,c=0.0):
    l = [a,b,c]
    for i in range(len(l)):
        print( l[i]**2,l[i]**3,l[i]**4,)
    
PowerA234(2,3,4)
    
3
def MEAN(a,b,c,d):
    print(a,"va",b,"ning o'rta arifmetigi ",(a+b)/2 ," o'rta geometrigi ", ((a*b)**0.5))
    print(a,"va",c,"ning o'rta arifmetigi ",(a+c)/2 ," o'rta geometrigi ", ((a*c)**0.5))
    print(a,"va",d,"ning o'rta arifmetigi ",(a+d)/2 ," o'rta geometrigi ", ((a*d)**0.5))
    
MEAN(1, 2, 3, 4)

4
def Triangle(a=0):
    S=0
    P=0
    S = (a**2)/4*(3**0.5)
    P = 3*a
    return f"yuza = {S}\nperimetr = {P}"
print(Triangle(3))

5
def RectPS(x1,y1,x2,y2):

    a = abs(x1 - x2)
    b = abs(y1 - y2)
    S = 2*a*b
    P =4*(a + b)
    return f"2ta to'rtburchak \nyuzi = {S}\nperimetri = {P}"

print(RectPS(0, 0, 2, 2))

20
def TriangleP(a,b):
    c = (a**2 + b**2)**0.5
    P = a + b + c
    return f"uchburchak perimetri = {P}"
print(TriangleP(3, 4))



30
def DigitN(k,n):
    
    if k >= 0:
        if len(str(k)) < n:
            return -1
        else:
            return str(k)[n-1]
    else:
        return str(k)[n]
  
print(DigitN(-954, 1))










