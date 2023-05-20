
def main():
    n1 = float(input("N-1?"))
    n2 = float(input("N-2?"))
    n3 = float(input("N-3?"))
    if n1 > n2 and n1 > n3:
        print("O maior numero é -> {}".format(n1))
    elif n3 > n2 and n3 > n1:
        print("O maior numero é -> {}".format(n3))
    else:
        print("O maior numero é -> {}".format(n2))

main()