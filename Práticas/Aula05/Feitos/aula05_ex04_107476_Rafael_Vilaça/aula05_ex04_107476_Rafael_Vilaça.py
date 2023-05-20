
def telToName(tel, telList, nameList,):
    if tel in telList:
        name = (nameList[telList.index(tel)])
    else:
        name = tel
    return name

def nameToTels(partName, telList, nameList):   
    n = len(partName)
    tels = []
    for x in nameList:
        ver = True          #ver = Verificação
        for i in range(n):
            if x[i] != partName[i]:
                ver = False
        if ver == True:
            tels.append(telList[nameList.index(x)])
    return tels

def main():
    telList = ['975318642', '234000111', '777888333', '911911911']
    nameList = ['Angelina', 'Brad',      'Claudia',   'Bruna']

    tel = input("Tel number? ")
    print( telToName(tel, telList, nameList) )
    print( telToName('234000111', telList, nameList) == "Brad" )
    print( telToName('222333444', telList, nameList) == "222333444" )

    name = input("Name? ")
    print( nameToTels(name, telList, nameList) )
    print( nameToTels('Clau', telList, nameList) == ['777888333'] )
    print( nameToTels('Br', telList, nameList) == ['234000111', '911911911'] )


if __name__ == "__main__":
    main()
