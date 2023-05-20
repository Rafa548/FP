Un = 100 
x = 0
while Un > 0:
    print(x, Un)
    Un = 1.01*Un - 1.01     
    x += 1
print(x)