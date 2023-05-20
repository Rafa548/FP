dc = {}

with open("wordlist.txt", encoding="utf-8") as f:
    for line in f:
        for w in line.split():
            w = w.lower()
            for a in w:
                if (a.isalpha()) == True:
                    if a in dc:
                        dc[a] += 1
                    else:
                        dc[a] = 1

for pal, cont in sorted(dc.items(), key = lambda d:(d[1]), reverse=True ):
    print(pal, cont)