def main():
     n = input("st?")
     long(n)

def long(n):
    lst = list(n.strip(""))
    for x in range(len(lst)):
        templst = lst[x-1] + lst[x]
        if len(lst) == 2:
            break
    print (lst)
    print(templst)
            

main()