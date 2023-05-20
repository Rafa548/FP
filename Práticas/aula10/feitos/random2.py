t = [['coal', 30], ['rice', 50], ['iron', 5], ['rice', 42], ['coal', 45]]

M, Q = 0, 1

def unload(t,m,q):
    for vagao in t[-1::-1]:
        if vagao[M] == m:
            if q >= vagao[Q]:
                t.remove(vagao)
                return 0
            else:
                vagao[Q] -= q
                return vagao[Q]


def main():
    print('t:', t)
    q = unload(t, 'rice', 40)
    print("unload(t, 'rice', 40) ->", q)
    print('t:', t)
    q = unload(t, 'coal', 50)
    print("unload(t, 'coal', 50) ->", q)
    print('t:', t)
    q = unload(t, 'iron', 20)
    print("unload(t, 'iron', 20) ->", q)
    print('t:', t)

main()