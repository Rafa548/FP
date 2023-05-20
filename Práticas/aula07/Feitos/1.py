#import sys

#idk = sys.argv[1]
dc = {}

#with open(idk, encoding="utf-8") as f:
with open("pg3333.txt", encoding="utf-8") as f:
    for line in f:
        for w in line.split():
            w = w.lower()
            for a in w:
                if (a.isalpha()) == True:
                    if a in dc:
                        dc[a] += 1
                    else:
                        dc[a] = 1

for pal, cont in sorted(dc.items()):
    print(pal, cont)

