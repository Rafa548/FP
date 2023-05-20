n = float(input("Numero de litros?"))
n_2 = n*1.4
if (n > 40) :
    n_3 = (n_2*10)/100
    n_4 = n_2 - n_3

print("O preço a pagar é {}".format(n_4))