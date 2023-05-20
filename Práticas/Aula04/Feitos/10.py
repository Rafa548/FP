def main():
    isPrime()


def isPrime():
    primenumb = []
    for i in range(2, 100):
        j = 2
        templist = [1,i]
        while(j < i-1):
            if (i % j == 0):
                templist.append(j)
            j += 1
        if(len(templist) == 2):
            primenumb.append(i)

    for x in range(len(primenumb)):
        print("{} é primo".format(primenumb[x]))

if __name__ == "__main__":
    main()