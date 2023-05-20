from os import read
k = {}
with open("names.txt", encoding="utf-8") as f:
        l = f.readlines()
        for i in l:
            h = i.split()
            if len(h)>1:
                if h[-1] in k:
                    k[h[-1]].add(h[0])
                else:
                    k[h[-1]] = {h[0]}

for i in k:       
    print("{} : {}".format(i, k[i]))


        
