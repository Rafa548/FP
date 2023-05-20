n = int(input("Valor?"))
#x=2
#h=1
#while x <= n:
    #h *= x
    #x += 1
#print(h)
x = 1
n1 = 0
n2 = 1
while x < n:
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    x += 1
print(n3)
    
