'''
s = 0
for m in range(4, -1, -1):
    x = (-1)**(m) * (2**m)
    s += x
    if m%2 != 1:
        print(x, end='')
    else:
        print(x, end='+')
else:       
    print("=", s, sep='')
print("Value x:", x)
print("Value m:", m)
print("Value s:", s)'''

def f1(a, b):
    print(a)
    print(b)
    c = a + b
    return c

def f2(k):
    s = 0
    for i in range(k):
        s += i
    return s

x = int(input())
y = int(input())
z = f1(x, y)
print(z)
print(f2(z))