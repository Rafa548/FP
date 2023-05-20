

def main():
    n1 = float(input("Numero de litros?"))
    p = 1.40
    if n1 < 40:
        c = n1 * p
        print ("O preço é -> {:2f}$".format(c))
    if n1 > 40:
        p = p - (1.40 * 0.1)/100
        c = n1 * p
        print ("O preço é -> {:.2f}$".format(c))

main()