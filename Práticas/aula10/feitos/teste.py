def f1(lst):
    fin = ["5","10","15","20"]
    s1 = 0
    s2 = 0
    for x in fin:
        lst.append(int(x))
        s1 += int(x)
        s2 += len(x)
    return s1,s2


L = []
k1,k2 = f1(L)
print (k1)
#print (k2)



price = {"olive": 2.15,"pineapple": 0.85,"pear": 1.49,"orange": 1.25}

price["apple"] = 0.75
item = "apple"
p = ""

for f in sorted(price.keys(), reverse=False):
    if item in f:
        p += "<{}:{}EUR>".format(f, price[f])
#print(p)


def pak(a, b):
    p = a*b
    return p, a

#print(pak(2,4))

pok = lambda a,b : (a*b, a)
#print(pok(2,4))