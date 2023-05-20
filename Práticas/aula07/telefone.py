
def listContacts(dic):
    print("{:>12s} : {}".format("Numero", "Nome"))
    for num in dic:
        print("{:>12s} : {}".format(num, dic[num]))

def filterPartName(contacts, partName):
    a = {}
    for i in contacts:
        if partName.lower() in contacts[i].lower():
            a[i] = contacts[i]
    return a        


def menu():
    print()
    print("(L)istar contactos")
    print("(A)dicionar contacto")
    print("(R)emover contacto")
    print("Procurar (N)úmero")
    print("Procurar (P)arte do nome")
    print("(T)erminar")
    op = input("opção? ").upper()
    return op

def adicionarContacto(contactos):
    a = input("Numero?")
    b = input("Nome?")
    contactos[a] = b
    return contactos

def removerContacto(contactos):
    a = input("Numero?")
    contactos.pop(a)
    return   

def procNumero(contactos):
    a = input("Numero?")
    if a in contactos:
        b = contactos.get(a)
    else:
        b = a    
    return b

def main():
    contactos = {"234370200": "Universidade de Aveiro",
        "727392822": "Cristiano Aveiro",
        "387719992": "Maria Matos",
        "887555987": "Marta Maia",
        "876111333": "Carlos Martins",
        "433162999": "Ana Bacalhau"
        }

    op = ""
    while op != "T":
        op = menu()
        if op == "T":
            print("Fim")
        elif op == "L":
            print("Contactos:")
            listContacts(contactos)
        elif op == "A":
            adicionarContacto(contactos)
        elif op == "R":
            removerContacto(contactos)
        elif op == "N":
            print(procNumero(contactos))
        elif op == "P":
            partName = input("Nome?")
            print(filterPartName(contactos, partName))
        else:
            print("Não implementado!")


if __name__ == "__main__":
    main()

