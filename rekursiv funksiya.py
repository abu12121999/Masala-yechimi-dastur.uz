1
def fa(n):
    if n==1:
        return 1
    return fa(n-1)*n
print(fa(5))

2
def fa2(n):
    if n %2 == 0:
        if n == 2:
            return 2
        return n*fa2(n-2)
    else:
        if n == 1:
            return 1
        return n*fa2(n-2)

print(fa2(6))
print(fa2(5))

3
def powerN(x,n):
    if n > 0 and n %2 == 0:
        if n == 1:
            return x
        return (x**(n//2))**2 * powerN(x,n-1)
    elif n > 0 and n %2 != 0:
        if n == 1:
            return x
        return x * x**(n-1) * powerN(x,n-1)
    elif n < 0:
        if n == -1:
            return 1/x
        return 1/(x**(-n)) * powerN(x,n+1)
    else:
        return 1
    
print(powerN(5, 0))
print(powerN(5, -3))
print(powerN(5, 3))
print(powerN(5, 4))

print(5**5)

4
i = 0
def fib1(n):
    global i
    i+=1
    if n==1 or n==2:
        return 1
    return fib1(n-2)+fib1(n-1)
print(fib1(15),i)

5
a = [1]
def fib2(n):
    global a
    a.append(n)
    if n == 1 or n ==2:
        return 1
    fib2(n-2) + fib2(n-1)
    return 
print(fib2(2))

9
def Ekub(a,b):
    if a == 0 and b == 0:
        return a + b
    if a > b:
        a %= b
        Ekub(a, b)
    elif a < b:
        b %= a
        Ekub(a, b)

print(Ekub(12, 8))
