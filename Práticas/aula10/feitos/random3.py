t = [['coal', 30], ['rice', 50], ['iron', 5], ['rice', 42], ['coal', 45]]

M, Q = 0, 1

def merchandise(t):
    dic = {}
    for i in t:
        if i[0] not in dic:
            dic[i[0]] = i[1]
        else:
            dic[i[0]] += i[1]
    return dic

def main():
    print('t:', t)
    d = merchandise(t)
    print("merchandise(t) ->\n", d)
    print('t:', t)

main()