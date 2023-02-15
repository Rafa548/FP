temp = int(input("Tempo em segundos?"))

h = temp//3600
m = temp%3600//60
s= temp%60


print("{:02d}:{:02d}:{:02d}".format(h,m,s))