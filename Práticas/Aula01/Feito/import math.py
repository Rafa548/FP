import math;

c1 = int(input("Qual é o valor do primeiro cateto?"))
c2 = int(input("Qual é o valor do segundo cateto?"))

h = math.sqrt((c1**2) + (c2**2))
a = math.degrees(math.acos(math.acos(c1/h))) 

print("A hipotenusa é :{}".format(h))
print("O angulo é :{}".format(a))