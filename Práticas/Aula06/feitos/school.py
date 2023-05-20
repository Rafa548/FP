# a)
def loadFile(fname, lst):
    try:
        with open(fname, "r") as e:
            for line in e:
                if line[0].isnumeric():
                    value_list = line.strip().split("\t")
                    value_list[0] = int(value_list[0])
                    lst.append(tuple(value_list))
    except:
        print("Erro o documento não existe")
    
# b)
def notaFinal(idc):
    nota1 = float(idc[-1])
    nota2 = float(idc[-2])
    nota3 = float(idc[-3])
    return ((nota1 + nota2 + nota3) / 3)

# c)
def printPauta(lst):
    print("Numero{:^100}Nota".format("Nome"))
    for idc in lst:
        print("{:>6}{:^100}{:4.1f}".format(idc[0], idc[1], notaFinal(idc)))


# d)
def main():
    lst = []
    loadFile("school1.csv", lst)
    loadFile("school2.csv", lst)
    loadFile("school3.csv", lst)
    loadFile("naoexiste.csv", lst)

    lst.sort()
    printPauta(lst)

if __name__ == "__main__":
    main()


