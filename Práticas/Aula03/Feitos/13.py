
def main():
    n1 = int(input("1º numero->"))
    n2 = int(input("2º numero->"))
    print(mdc(n1,n2))
        

def mdc(n1,n2):
    r = n1 % n2
    if (r == 0):
        return (n2)
    else:
        return (mdc(n2,r))

if __name__ == "__main__":
    main()