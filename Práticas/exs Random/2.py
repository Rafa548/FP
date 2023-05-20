
def closertotarget(x, y, target):
    d1 = abs(target % x)
    d2 = abs(target % y)
    if d1 < d2:
        return x
    elif d1 > d2:
        return y
    else:
        if x < y:
            return x
        else:
            return y
def main():
    x = float(input("1"))
    y = float(input("2"))
    target = float(input("3"))
    print(closertotarget(x, y, target))    

main()