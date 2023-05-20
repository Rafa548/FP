import random

def main():
    secret = random.randrange(1, 101)
    n = int(input("Can you guess my secret?"))  
    if n < 1 or n > 101:
        print("Please choose a number between 1-101")
        n = int(input("Can you guess my secret?"))
    while n != secret:
        if n < 1 or n > 101:
            print("Please choose a number between 1-101")
            n = int(input("Can you guess my secret?"))
        elif n > secret:
            print("High")
            n = int(input("Can you guess my secret?")) 
        else:
            print("Low")
            n = int(input("Can you guess my secret?")) 
    if n == secret:
        print("U Won")    

main()
