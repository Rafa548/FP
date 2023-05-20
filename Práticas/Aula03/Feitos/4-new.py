def main():
    print(poli(0))
    print(poli(1))
    print(poli(2))
    print(poli(poli(1)))


def poli(x):
    y = x**2+2*x+3
    return (y)


main()