def inputTotal():
    tot = 0.0
    x = 0
    while True:
        s = input("valor? ")
        if s == "": break   # if empty line, stop repeating!
        x += 1
        v = float(s)
        tot = (tot + v)/x
    return tot

def main():
    n = inputTotal()
    print("A média é {:.2f}".format(n))

if __name__ == "__main__":
    main()